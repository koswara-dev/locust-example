import logging

from locust import HttpUser, between, task


class RestWithToken(HttpUser):
    host = "https://fakestoreapi.com"
    wait_time = between(1, 3)

    token = ""

    def on_start(self):
        response = self.client.post("/auth/login", {
            "username": "mor_2314",
            "password": "83r5^_"
        })
        # self.token = str(response.content.decode().find("token"))
        self.token = response.json()["token"]
        self.client.headers.update({"Authorization": self.token})
        logging.info("Scrape Token from Auth Login")

    @task
    def get_products(self):
        self.client.get("/products")
        # add request header token
        # self.client.get("/products", headers={"Authorization": self.token})
        # if use Bearer
        # self.client.get("/products", headers={"Authorization": f"Bearer {self.token}"})
        print(self.token)
        logging.info("Get All Product")

    @task
    def get_limit_products(self):
        limit = 5
        self.client.get(f"/products?limit={limit}")
        logging.info(f"Get Limit {limit} Products")
