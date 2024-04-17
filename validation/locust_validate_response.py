from locust import TaskSet, task


class TaskProductWithValidate(TaskSet):

    @task
    def get_products(self):
        response = self.client.get("/products")
        # validasi menggunakan assert
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        response_content = response.text
        assert "title" in response_content, "Key title not found in JSON response"
