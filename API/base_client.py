import requests
from Config import BASE_URL
from logger import log_request

class BaseClient:
    def __init__(self):
        self.base_url = BASE_URL
        self.session = requests.Session()
        self.session.hooks["response"] = [log_request]

    def _request(self, method, endpoint, **kwargs):
        url = f"{self.base_url}{endpoint}"
        return self.session.request(method, url, **kwargs)

    def set_auth_cookie(self, token: str):
        self.session.cookies.set("token", token)