from locust import HttpUser, task, constant
from functions.functions import get_booking_auth_token
from prometheus_client import start_http_server, Summary, Counter, Gauge

class SpikeTestUser(HttpUser):
    wait_time = constant(1)  # Constant time between requests
    host = "https://restful-booker.herokuapp.com"

    def on_start(self):
        # Getting auth token
        self.token = get_booking_auth_token()

    @task
    def spike_test(self):
        headers = {"Authorization": f"Bearer {self.token}"}
        self.client.get("/booking", headers=headers)