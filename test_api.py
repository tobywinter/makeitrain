from api import api
from algorithm import Algorithm
import unittest

class ApiTestCase(unittest.TestCase):

    def test_root(self):
        tester = api.test_client(self)
        response = tester.get("/", content_type="html/txt")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'1D Trend')

class AlgorithmTestCase(unittest.TestCase):

    def setUp(self):
        self.test_alg = Algorithm('collated_data_without_headers.csv')

    def test_split_data(self):
        data_length = self.test_alg.dataset.shape[0]
        self.test_alg.split_data()
        test_data_length = len(self.test_alg.features_test)
        train_data_length = len(self.test_alg.features_train)

        self.assertEqual(test_data_length + train_data_length, data_length)


if __name__ == "__main__":
    unittest.main()
