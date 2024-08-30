from locust import HttpUser, task, constant_pacing
from functions.functions import get_booking_auth_token
from prometheus_client import start_http_server, Summary, Counter, Gauge

REQUEST_ERRORS = Counter('http_spike_request_errors_total', 'Total number of HTTP request errors')

class StressTestUser(HttpUser):
    wait_time = constant_pacing(0.5)  # Requests are made as fast as possible
    host = "https://restful-booker.herokuapp.com"

    def on_start(self):
        # Getting auth token
        self.token = get_booking_auth_token()

    @task
    def stress_test(self):
        headers = {"Authorization": f"Bearer {self.token}"}
        self.client.get("/booking", headers=headers)