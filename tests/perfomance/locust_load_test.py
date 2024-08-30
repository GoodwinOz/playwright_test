import time
from locust import HttpUser, task, between
from prometheus_client import start_http_server, Summary, Counter, Gauge
from functions.functions import get_booking_auth_token
    
# Define Prometheus metrics
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')
ACTIVE_USERS = Counter('active_users', 'Number of active users')
REQUEST_LATENCY = Summary('request_latency_seconds', 'Latency of HTTP requests in seconds')
REQUEST_ERRORS = Counter('http_request_errors_total', 'Total number of HTTP request errors')
USERS_COUNT = Gauge('locust_user_count', 'Number of users currently being simulated by Locust')
HTTP_REQUESTS_TOTAL = Counter('http_requests_total', 'Total number of HTTP requests')
ENDPOINT_COUNTERS = {
    'booking': Counter('http_requests_booking_total', 'Total number of HTTP requests to /booking'),
    'ping': Counter('http_requests_ping_total', 'Total number of HTTP requests to /ping')
}
STATUS_CODE_COUNTERS = {
    '2xx': Counter('http_responses_2xx_total', 'Total number of 2xx responses'),
    '4xx': Counter('http_responses_4xx_total', 'Total number of 4xx responses'),
    '5xx': Counter('http_responses_5xx_total', 'Total number of 5xx responses'),
}

class LoadTestUser(HttpUser):
    wait_time = between(1, 5)  # Simulating user waiting time between tasks
    host = "https://restful-booker.herokuapp.com"

    def on_start(self):
        # Increment the active users counter
        ACTIVE_USERS.inc()

        # Start Prometheus server
        start_http_server(8000)

        self.token = get_booking_auth_token()

    def on_stop(self):
        # Decrement the active users counter
        ACTIVE_USERS.dec()

    @task
    @REQUEST_TIME.time()
    @REQUEST_LATENCY.time()
    def load_test(self):
        headers = {
            "Accept": "application/json",
            "Cookie": f"token={self.token}"
        }
        ENDPOINT_COUNTERS['booking'].inc()
        with self.client.get("/booking", headers=headers) as response:
            HTTP_REQUESTS_TOTAL.inc()
            if response.status_code != 200:
                REQUEST_ERRORS.inc()  # Increment the error counter
            elif response.status_code >= 200 and response.status_code < 300:
                STATUS_CODE_COUNTERS['2xx'].inc()
            elif response.status_code >= 400 and response.status_code < 500:
                STATUS_CODE_COUNTERS['4xx'].inc()
            elif response.status_code >= 500:
                STATUS_CODE_COUNTERS['5xx'].inc()
    
    @task
    def ping(self):
        ENDPOINT_COUNTERS['ping'].inc()
        self.client.get("/ping")