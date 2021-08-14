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

    def create_pixel(self, graph_id, activity_date, activity_time):
        pixel_endpoint = f"{self.endpoint}/{self.username}/graphs/{graph_id}"
        headers = {
            "X-USER-TOKEN": self.token
        }
        parameters = {
            "date": activity_date,
            "quantity": activity_time,
            # "optionalData": activity[2]
        }
        response = requests.post(
            url=pixel_endpoint,
            json=parameters,
            headers=headers
        )
        return response.text

    def update_pixel(self, graph_id, activity_date, activity_time):
        pixel_endpoint = f"{self.endpoint}/{self.username}/graphs/{graph_id}/{activity_date}"
        headers = {
            "X-USER-TOKEN": self.token
        }
        parameters = {
            "quantity": activity_time,
            # "optionalData": activity[2]
        }
        response = requests.put(
            url=pixel_endpoint,
            json=parameters,
            headers=headers
        )
        return response.text

    def delete_pixel(self, graph_id, activity_date):
        pixel_endpoint = f"{self.endpoint}/{self.username}/graphs/{graph_id}/{activity_date}"
        headers = {
            "X-USER-TOKEN": self.token
        }
        response = requests.delete(
            url=pixel_endpoint,
            headers=headers
        )
        return response.text