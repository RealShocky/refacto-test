import unittest
from unittest.mock import patch, MagicMock
from api_client import APIClient, ResponseProcessor, CacheManager

class TestAPIClient(unittest.TestCase):
    def setUp(self):
        self.base_url = 'https://api.example.com'
        self.headers = {'Authorization': 'Bearer abc123'}
        self.api_client = APIClient(self.base_url, self.headers)

    @patch('requests.request')
    def test_get_success(self, mock_request):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'id': 1, 'name': 'John'}
        mock_request.return_value = mock_response

        result = self.api_client.get('data')
        self.assertEqual(result, {'id': 1, 'name': 'John'})

    @patch('requests.request')
    def test_get_failure(self, mock_request):
        mock_request.side_effect = requests.exceptions.RequestException()

        result = self.api_client.get('data')
        self.assertIsNone(result)

class TestResponseProcessor(unittest.TestCase):
    def test_process_response_valid(self):
        response = {
            'id': 1,
            'name': 'John',
            'age': 30,
            'address': {'street': '123 Main St', 'city': 'New York'},
            'hobbies': ['reading', 'swimming', {'name': 'painting', 'level': 'beginner'}]
        }
        required_fields = ['id', 'name']

        result = ResponseProcessor.process_response(response, required_fields)
        self.assertEqual(result, {
            'id': 1,
            'name': 'John',
            'age': 30,
            'address': {'street': '123 Main St', 'city': 'New York'},
            'hobbies': ['reading', 'swimming', {'name': 'painting', 'level': 'beginner'}]
        })

    def test_process_response_missing_fields(self):
        response = {'id': 1, 'age': 30}
        required_fields = ['id', 'name']

        result = ResponseProcessor.process_response(response, required_fields)
        self.assertIsNone(result)

class TestCacheManager(unittest.TestCase):
    def setUp(self):
        self.cache_file = 'test_cache.json'
        self.response = {'id': 1, 'name': 'John'}

    def tearDown(self):
        try:
            os.remove(self.cache_file)
        except FileNotFoundError:
            pass

    def test_cache_response_success(self):
        result = CacheManager.cache_response(self.response, self.cache_file)
        self.assertTrue(result)
        self.assertTrue(os.path.exists(self.cache_file))

    def test_get_cached_response_valid(self):
        CacheManager.cache_response(self.response, self.cache_file)
        cached_response = CacheManager.get_cached_response(self.cache_file)
        self.assertEqual(cached_response, self.response)

    def test_get_cached_response_expired(self):
        CacheManager.cache_response(self.response, self.cache_file, ttl=-1)
        cached_response = CacheManager.get_cached_response(self.cache_file)
        self.assertIsNone(cached_response)

if __name__ == '__main__':
    unittest.main()