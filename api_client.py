import requests
import json
import time
from typing import Dict, Any, List, Union

class APIClient:
    def __init__(self, base_url: str, headers: Dict[str, str] = None):
        self.base_url = base_url
        self.headers = headers or {}

    def get(self, endpoint: str, params: Dict[str, Any] = None, max_retries: int = 3) -> Union[Dict[str, Any], None]:
        return self._make_request("GET", endpoint, params=params, max_retries=max_retries)

    def post(self, endpoint: str, data: Dict[str, Any], max_retries: int = 3) -> Union[Dict[str, Any], None]:
        return self._make_request("POST", endpoint, json=data, max_retries=max_retries)

    def _make_request(self, method: str, endpoint: str, max_retries: int = 3, **kwargs) -> Union[Dict[str, Any], None]:
        url = f"{self.base_url}/{endpoint}"
        for attempt in range(max_retries):
            try:
                response = requests.request(method, url, headers=self.headers, **kwargs)
                if response.status_code == 200:
                    return response.json()
                elif response.status_code == 429:
                    time.sleep(2 ** attempt)
            except requests.exceptions.RequestException as e:
                print(f"Request failed: {e}")
                if attempt < max_retries - 1:
                    time.sleep(2 ** attempt)
        return None

class ResponseProcessor:
    @staticmethod
    def process_response(response: Dict[str, Any], required_fields: List[str] = None) -> Union[Dict[str, Any], None]:
        if not response or not isinstance(response, dict):
            return None

        required_fields = required_fields or []
        if not all(field in response for field in required_fields):
            missing_fields = set(required_fields) - set(response.keys())
            print(f"Missing fields: {missing_fields}")
            return None

        processed_data = {}
        for key, value in response.items():
            if isinstance(value, (str, int, float, bool)):
                processed_data[key] = value
            elif isinstance(value, dict):
                processed_data[key] = ResponseProcessor.process_response(value)
            elif isinstance(value, list):
                processed_data[key] = [
                    ResponseProcessor.process_response(item) if isinstance(item, dict) else item
                    for item in value
                ]
        return processed_data

class CacheManager:
    @staticmethod
    def cache_response(response: Dict[str, Any], cache_file: str, ttl: int = 3600) -> bool:
        if not response:
            return False

        try:
            data = {
                'data': response,
                'timestamp': time.time(),
                'ttl': ttl
            }
            with open(cache_file, 'w') as f:
                json.dump(data, f)
            return True
        except IOError as e:
            print(f"Cache error: {e}")
            return False

    @staticmethod
    def get_cached_response(cache_file: str) -> Union[Dict[str, Any], None]:
        try:
            with open(cache_file, 'r') as f:
                data = json.load(f)
                if time.time() - data['timestamp'] < data['ttl']:
                    return data['data']
        except (IOError, json.JSONDecodeError) as e:
            print(f"Cache read error: {e}")
        return None

# Example usage
api_client = APIClient('https://api.example.com', headers={'Authorization': 'Bearer abc123'})
cache_file = 'cache.json'

cached_response = CacheManager.get_cached_response(cache_file)
if cached_response:
    result = ResponseProcessor.process_response(cached_response, ['id', 'name'])
else:
    response = api_client.get('data', params={'limit': 10})
    if response:
        result = ResponseProcessor.process_response(response, ['id', 'name'])
        CacheManager.cache_response(result, cache_file)