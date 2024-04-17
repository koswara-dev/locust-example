from locust import TaskSet, task


class TaskCart(TaskSet):

    @task
    def add_product_cart(self):
        payload = {
            "userId": 5,
            "date": "2020-02-03",
            "products": [{"productId": 5, "quantity": 1}, {"productId": 1, "quantity": 5}]
        }
        response = self.client.post("/carts", json=payload)
        print(f"Response status code: {response.status_code}, Response content: {response.content}")

    @task
    def get_carts(self):
        response = self.client.get("/carts")
        print(f"Response status code: {response.status_code}, Response content: {response.content}")

    # TODO: add more test
