from locust import HttpUser, task, between


class UserCheckout(HttpUser):
    wait_time = between(1, 3)

    product_data = {
        "title": "test product",
        "price": 13.5,
        "description": "lorem ipsum set",
        "image": "https://i.pravatar.cc",
        "category": "electronic"
    }

    @task(3)
    def get_all_product(self):
        response = self.client.get("/products")
        print(f"Response status code: {response.status_code}, Response content: {response.content}")

    @task(2)
    def get_product_by_id(self):
        for product_id in range(5):
            response = self.client.get(f"/products/{product_id + 1}", name="/product_by_id")
            print(f"Response status code: {response.status_code}, Response content: {response.content}")

    @task(1)
    def get_product_in_category(self):
        category_list = [
            "electronics",
            "jewelery",
            "men's clothing",
            "women's clothing"
        ]
        for category in category_list:
            response = self.client.get(f"/products/category/{category}", name="/product_in_category")
            print(f"Response status code: {response.status_code}, Response content: {response.content}")

    @task(1)
    def create_product(self):
        self.client.post("/products", json=self.product_data)

    @task(1)
    def update_product(self):
        self.client.post("/products/7", json=self.product_data)
