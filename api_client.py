import requests
import json
import time

def get(url, h={}, p=None, t=3):
    """get data from api"""
    r = None
    try:
        for i in range(t):
            try:
                r = requests.get(url, headers=h, params=p)
                if r.status_code == 200:
                    return r.json()
                elif r.status_code == 429:  # rate limit
                    time.sleep(2 ** i)  # exponential backoff
                    continue
                else:
                    print(f"Error: {r.status_code}")
                    return None
            except Exception as e:
                print(f"Request failed: {e}")
                if i < t - 1:  # not last attempt
                    time.sleep(2 ** i)
                    continue
                return None
    except Exception as e:
        print(f"Fatal error: {e}")
        return None

def post(url, d, h={}, t=3):
    """post data to api"""
    r = None
    try:
        for i in range(t):
            try:
                r = requests.post(url, json=d, headers=h)
                if r.status_code in [200, 201]:
                    return r.json()
                elif r.status_code == 429:  # rate limit
                    time.sleep(2 ** i)
                    continue
                else:
                    print(f"Error: {r.status_code}")
                    return None
            except Exception as e:
                print(f"Request failed: {e}")
                if i < t - 1:
                    time.sleep(2 ** i)
                    continue
                return None
    except Exception as e:
        print(f"Fatal error: {e}")
        return None

def process_response(r, required_fields=[]):
    """process api response"""
    if not r or not isinstance(r, dict):
        return None
    
    # Check required fields
    for f in required_fields:
        if f not in r:
            print(f"Missing field: {f}")
            return None
    
    # Process data
    try:
        # Extract useful fields
        d = {}
        for k, v in r.items():
            if isinstance(v, (str, int, float, bool)):
                d[k] = v
            elif isinstance(v, dict):
                d[k] = process_response(v)
            elif isinstance(v, list):
                d[k] = [process_response(i) if isinstance(i, dict) else i for i in v]
        return d
    except Exception as e:
        print(f"Processing error: {e}")
        return None

def cache_response(r, f, ttl=3600):
    """cache api response"""
    if not r:
        return False
    
    try:
        data = {
            'data': r,
            'timestamp': time.time(),
            'ttl': ttl
        }
        with open(f, 'w') as cache_file:
            json.dump(data, cache_file)
        return True
    except Exception as e:
        print(f"Cache error: {e}")
        return False

def get_cached(f):
    """get cached response"""
    try:
        with open(f, 'r') as cache_file:
            data = json.load(cache_file)
            if time.time() - data['timestamp'] < data['ttl']:
                return data['data']
    except Exception as e:
        print(f"Cache read error: {e}")
    return None

# Example usage
api_url = 'https://api.example.com/data'
headers = {'Authorization': 'Bearer abc123'}
params = {'limit': 10}

# Try to get from cache first
cached_data = get_cached('cache.json')
if cached_data:
    result = process_response(cached_data, ['id', 'name'])
else:
    # Make API request
    response = get(api_url, headers, params)
    if response:
        # Process and cache response
        result = process_response(response, ['id', 'name'])
        cache_response(result, 'cache.json')
