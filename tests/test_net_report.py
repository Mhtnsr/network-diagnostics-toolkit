import argparse
from pathlib import Path
import socket
import sys
import unittest
from unittest.mock import patch
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from net_report import validate_host,parse_ports,collect,command_check
class NetworkTests(unittest.TestCase):
    def test_hosts(self):
        for host in ['localhost','host.lab.invalid','127.0.0.1','::1']: self.assertTrue(validate_host(host))
        for host in ['-bad','https://host','host;whoami','a..b']:
            with self.assertRaises(argparse.ArgumentTypeError): validate_host(host)
    def test_ports(self):
        self.assertEqual(parse_ports('443,53,443'),[443,53])
        for value in ['0','65536','x','1,2,3,4,5,6,7,8,9']:
            with self.assertRaises(argparse.ArgumentTypeError): parse_ports(value)
    @patch('net_report.socket.getaddrinfo',side_effect=socket.gaierror())
    @patch('net_report.socket.create_connection')
    def test_no_implicit_probes(self,connect,dns):
        result=collect('host.lab.invalid',[443])
        self.assertEqual(result['dns']['status'],'failed'); connect.assert_not_called()
        self.assertEqual(result['ping']['status'],'not-requested')
    @patch('net_report.socket.getaddrinfo',return_value=[])
    @patch('net_report.socket.create_connection',side_effect=TimeoutError())
    def test_failed_probe(self,connect,dns):
        self.assertEqual(collect('localhost',[443],probe=True)['tcp'][0]['status'],'failed')
    @patch('net_report.shutil.which',return_value=None)
    def test_missing_tool(self,which): self.assertEqual(command_check('ping',[],1)['status'],'unavailable')
if __name__=='__main__': unittest.main()
