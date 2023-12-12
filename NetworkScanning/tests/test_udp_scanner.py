import unittest
from NetworkScanning.udp_scanner import single_udp_scan
from NetworkScanning.utils import set_default_interface

class TestUdpScanner(unittest.TestCase):

    def test_open_port(self):
        result = single_udp_scan('google.com', 53)
        self.assertEqual(result, 'Open')

    def test_closed_port(self):
        result = single_udp_scan('google.com', 8080)
        self.assertEqual(result, 'Closed')

    def test_filtered_port(self):
        result = single_udp_scan('google.com', 12345)
        self.assertEqual(result, 'Filtered')

if __name__ == '__main__':
    unittest.main()
