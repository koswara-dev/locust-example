from locust import TaskSet, task


class TaskProduct(TaskSet):
    product_data = {
        "title": "test product",
        "price": 13.5,
        "description": "lorem ipsum set",
        "image": "https://i.pravatar.cc",
        "category": "electronic"
    }

    @task
    def create_product(self):
        response = self.client.post("/products", json=self.product_data)
        print(f"Response status code: {response.status_code}, Response content: {response.content}")

    @task
    def get_products(self):
        response = self.client.get("/products")
        print(f"Response status code: {response.status_code}, Response content: {response.content}")

    @task
    def get_product_by_id(self):
        for product_id in range(5):
            response = self.client.get(f"/products/{product_id + 1}", name="/products/[id]")
            print(f"Response status code: {response.status_code}, Response content: {response.content}")

    @task
    def get_product_in_category(self):
        category_list = [
            "electronics",
            "jewelery",
            "men's clothing",
            "women's clothing"
        ]
        for category in category_list:
            response = self.client.get(f"/products/category/{category}", name="/products/category/[category]")
            print(f"Response status code: {response.status_code}, Response content: {response.content}")

    # TODO: add more test
