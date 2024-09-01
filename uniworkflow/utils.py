import requests

def make_api_request(url, method="GET", headers=None, data=None):
    """Utility function to make API requests"""
    response = requests.request(method, url, headers=headers, json=data)
    response.raise_for_status()
    return response.json()
