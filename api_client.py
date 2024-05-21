import requests
import time

from logging_config import logger

class APIClient:
    def __init__(self, config):
        self.base_url = config.BASE_URL
        self.candidate_id = config.CANDIDATE_ID
        self.retry_limit = config.RETRY_LIMIT
        self.retry_delay = config.RETRY_DELAY
    
    def _make_request_with_retry(self, method, endpoint, data=None):
        url = f"{self.base_url}{endpoint}"
        headers = {"Content-Type": "application/json"}
        
        for attempt in range(self.retry_limit):
            response = method(url, headers=headers, json=data)
            
            if response.status_code == 200:
                logger.info(f"{method.__name__.upper()} request to {url} succeeded.")
                return response.json()
            
            elif response.status_code == 429:  # Too Many Requests
                logger.warning(f"{method.__name__.upper()} request to {url} rate limited. Retrying in {self.retry_delay} seconds...")
                time.sleep(self.retry_delay)
            
            else:
                logger.error(f"{method.__name__.upper()} request to {url} failed with status code {response.status_code}.")
                response.raise_for_status()
        
        raise Exception(f"Failed to complete the {method.__name__.upper()} request after retries")

    def post(self, endpoint, data):
        return self._make_request_with_retry(requests.post, endpoint, data)

    def delete(self, endpoint, data):
        return self._make_request_with_retry(requests.delete, endpoint, data)

    def get_map_goal(self):
        endpoint = f"/map/{self.candidate_id}/goal"
        return self._make_request_with_retry(requests.get, endpoint)['goal']