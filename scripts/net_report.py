"""Single authorized host only. DNS by default; TCP/ping/route are explicit opt-ins."""
import argparse
import datetime
import ipaddress
import json
import platform
import re
import shutil
import socket
import subprocess

def validate_host(value):
    try:
        return str(ipaddress.ip_address(value))
    except ValueError:
        labels=value.rstrip('.').split('.')
        if len(value)>253 or not all(re.fullmatch(r'[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?', p) for p in labels):
            raise argparse.ArgumentTypeError('Provide a hostname or IP address, not a URL or command option')
        return value

def parse_ports(value):
    try: ports=list(dict.fromkeys(int(p.strip()) for p in value.split(',')))
    except ValueError: raise argparse.ArgumentTypeError('Ports must be comma-separated integers')
    if not ports or len(ports)>8 or any(p<1 or p>65535 for p in ports):
        raise argparse.ArgumentTypeError('Choose one to eight ports in 1..65535')
    return ports

def command_check(tool, args, timeout):
    executable=shutil.which(tool)
    if not executable: return {'status':'unavailable'}
    try:
        result=subprocess.run([executable]+args, capture_output=True, text=True, errors='replace', timeout=timeout, check=False)
        return {'status':'completed','returncode':result.returncode,'output':(result.stdout+result.stderr)[:12000]}
    except subprocess.TimeoutExpired: return {'status':'timeout'}
    except OSError: return {'status':'unavailable'}

def collect(host, ports, probe=False, ping=False, route=False):
    # Enforce the same limits for callers importing this function as for the CLI.
    host = validate_host(host)
    ports = parse_ports(','.join(str(port) for port in ports))
    report={'schema_version':1,'timestamp_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
            'host':host,'dns':{'status':'unavailable'},'tcp':[],'ping':{'status':'not-requested'},'route':{'status':'not-requested'}}
    # OS resolver timeout behavior is platform-specific; getaddrinfo has no portable timeout.
    try:
        addresses=sorted({item[4][0] for item in socket.getaddrinfo(host, None, type=socket.SOCK_STREAM)})
        report['dns']={'status':'resolved','addresses':addresses} if addresses else {'status':'failed'}
    except OSError: report['dns']={'status':'failed'}
    if probe:
        for port in ports:
            try:
                with socket.create_connection((host,port),timeout=3): pass
                state='connected'
            except OSError: state='failed'
            report['tcp'].append({'port':port,'status':state})
    windows=platform.system()=='Windows'
    if ping: report['ping']=command_check('ping',(['-n','2'] if windows else ['-c','2'])+[host],12)
    if route: report['route']=command_check('tracert' if windows else 'traceroute',(['-d','-h','8','-w','500'] if windows else ['-n','-m','8','-w','1'])+[host],20)
    return report

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--host',required=True,type=validate_host)
    parser.add_argument('--ports',type=parse_ports,default=[443])
    parser.add_argument('--probe',action='store_true')
    parser.add_argument('--ping',action='store_true')
    parser.add_argument('--route',action='store_true')
    args=parser.parse_args()
    print(json.dumps(collect(args.host,args.ports,args.probe,args.ping,args.route),indent=2))
if __name__=='__main__': main()
