# Refactored code
import requests
import time
from typing import Dict, List, Optional, Union

def make_request(
    method: str,
    url: str,
    headers: Dict[str, str] = {},
    params: Optional[Dict[str, str]] = None,
    data: Optional[Dict[str, Union[str, int]]] = None,
    max_retries: int = 3,
    retry_delay_base: int = 2,
) -> Optional[Dict[str, Union[str, int]]]:
    """
    Make a GET or POST request to the specified URL with optional headers, params, and data.
    Retry the request up to `max_retries` times with exponential backoff if a rate limit error is encountered.
    """
    for attempt in range(max_retries):
        try:
            if method.lower() == "get":
                response = requests.get(url, headers=headers, params=params)
            elif method.lower() == "post":
                response = requests.post(url, headers=headers, json=data)
            else:
                raise ValueError(f"Invalid method: {method}")

            if response.status_code == 200:
                return response.json()
            elif response.status_code == 201:  # Created
                return response.json()
            elif response.status_code == 429:  # Rate limit
                delay = retry_delay_base ** attempt
                print(f"Rate limit exceeded. Retrying in {delay} seconds...")
                time.sleep(delay)
            else:
                print(f"Error: {response.status_code}")
                return None

        except Exception as e:
            print(f"Request failed: {e}")
            if attempt < max_retries - 1:
                delay = retry_delay_base ** attempt
                print(f"Retrying in {delay} seconds...")
                time.sleep(delay)
            else:
                return None

    print("Maximum retries exceeded.")
    return None

def process_response(
    response: Optional[Dict[str, Union[str, int]]], required_fields: List[str]
) -> Optional[Dict[str, Union[str, int]]]:
    """
    Process the API response by checking for required fields and extracting useful data.
    """
    if not response or not isinstance(response, dict):
        return None

    # Check required fields
    for field in required_fields:
        if field not in response:
            print(f"Missing field: {field}")
            return None

    # Process data
    try:
        # Extract useful data from the response
        processed_data = {
            # ...
        }
        return processed_data
    except Exception as e:
        print(f"Error processing response: {e}")
        return None
# Refactored code
import json
import time
from typing import Any, Dict, List, Optional, Union

def process_response(response: Dict[str, Any], fields: List[str]) -> Dict[str, Any]:
    """
    Process the API response by filtering out unwanted fields and recursively processing nested dictionaries and lists.

    Args:
        response (Dict[str, Any]): The API response to be processed.
        fields (List[str]): A list of field names to keep in the processed response.

    Returns:
        Dict[str, Any]: The processed response with only the specified fields and nested dictionaries/lists processed.
    """
    processed_data = {}
    for key, value in response.items():
        if key in fields:
            if isinstance(value, (str, int, float, bool)):
                processed_data[key] = value
            elif isinstance(value, dict):
                processed_data[key] = process_response(value, fields)
            elif isinstance(value, list):
                processed_data[key] = [process_response(item, fields) if isinstance(item, dict) else item for item in value]
    return processed_data

def cache_response(response: Dict[str, Any], file_path: str, ttl: int = 3600) -> bool:
    """
    Cache the API response to a file.

    Args:
        response (Dict[str, Any]): The API response to be cached.
        file_path (str): The path to the cache file.
        ttl (int, optional): The time-to-live (TTL) for the cached response in seconds. Defaults to 3600 (1 hour).

    Returns:
        bool: True if the response was successfully cached, False otherwise.
    """
    if not response:
        return False

    try:
        data = {
            'data': response,
            'timestamp': time.time(),
            'ttl': ttl
        }
        with open(file_path, 'w') as cache_file:
            json.dump(data, cache_file)
        return True
    except Exception as e:
        print(f"Cache error: {e}")
        return False

def get_cached(file_path: str) -> Optional[Dict[str, Any]]:
    """
    Retrieve the cached API response from a file.

    Args:
        file_path (str): The path to the cache file.

    Returns:
        Optional[Dict[str, Any]]: The cached response if it exists and is not expired, None otherwise.
    """
    try:
        with open(file_path, 'r') as cache_file:
            data = json.load(cache_file)
            if time.time() - data['timestamp'] < data['ttl']:
                return data['data']
    except Exception as e:
        print(f"Cache read error: {e}")
    return None