from locust import HttpUser, between, task


class MyUser(HttpUser):
    wait_time = between(1, 3)
    host = "http://localhost:5000"

    @task
    def get_products(self):
        response = self.client.get("/api/v1/products")
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
