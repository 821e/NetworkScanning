import unittest
from NetworkScanning.tcp_scanner import single_tcp_scan

class TestTcpScanner(unittest.TestCase):

    def test_open_port(self):
        result = single_tcp_scan('example.com', 80)
        self.assertEqual(result, 'Open')

    def test_closed_port(self):
        result = single_tcp_scan('example.com', 8080)
        self.assertEqual(result, 'Closed')

    def test_filtered_port(self):
        result = single_tcp_scan('example.com', 12345)
        self.assertEqual(result, 'Filtered')

if __name__ == '__main__':
    unittest.main()
