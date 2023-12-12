import unittest
from NetworkScanning.banner_grabber import grab_banner

class TestBannerGrabber(unittest.TestCase):

    def test_valid_banner(self):
        result = grab_banner('example.com', 80, protocol="TCP")
        self.assertTrue(result.startswith('HTTP'))

    def test_invalid_banner(self):
        result = grab_banner('example.com', 8080, protocol="TCP")
        self.assertEqual(result, "No banner received")

if __name__ == '__main__':
    unittest.main()
