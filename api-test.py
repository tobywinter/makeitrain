from api import api
import unittest

class ApiTestCase(unittest.TestCase):

    def test_root(self):
        tester = api.test_client(self)
        response = tester.get("/", content_type="html/txt")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Make it rain!')

if __name__ == "__main__":
    unittest.main()
