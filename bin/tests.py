from main import Request
import unittest

class TestCase1(Request, unittest.TestCase):
    def test1(self):
        import xml.etree.ElementTree as ET
        import requests

    def test2(self):
        assert Request.httpcode == '<Response [200]>'

    def test3(self):
        assert len(Request.document) > 0

    def test4(self):
        assert type(Request.tagContent(Request, 'version')) == str

    def test5(self):
        assert Request.tagContent(Request, 'version') == 'Version 1.0'

    def tearDown(self):
        pass

    def setUp(self):
        pass

if __name__ == "__main__":
    unittest.main()