import requests
from secrets import PIXELA_TOKEN, PIXELA_ENDPOINT, PIXELA_USERNAME

class Pixela:

    def __init__(self):
        self.endpoint = PIXELA_ENDPOINT
        self.username = PIXELA_USERNAME
        self.token = PIXELA_TOKEN

    def create_user_account(self):
        parameters = {
            "token": self.token,
            "username": self.username,
            "agreeTermsOfService": "yes",
            "notMinor": "yes"
        }
        response = requests.post(
            url=PIXELA_ENDPOINT,
            json=parameters
        )
        return response.text

    def create_graph(self, graph_id, graph_name):
        graph_endpoint = f"{self.endpoint}/{self.username}/graphs"
        headers = {
            "X-USER-TOKEN": self.token
        }
        parameters = {
            "id": graph_id,
            "name": graph_name,
            "unit": "hours",
            "type": "float",
            "color": "ajisai",
        }
        response = requests.post(
            url=graph_endpoint,
            json=parameters,
            headers=headers
        )
        return response.text
