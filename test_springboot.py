import logging

from locust import HttpUser, between, task


class MyUser(HttpUser):
    host = "http://localhost:8080"
    wait_time = between(1, 3)

    token = ""

    #
    # def on_start(self):
    #     response = self.client.post("/api/auth/signin", {
    #         "usernameOrEmail": "leanne",
    #         "password": "password"
    #     })
    #     self.token = response.json()["accessToken"]
    #     self.client.headers.update({"Authorization": self.token})
    #     logging.info("Get Token from Auth Login")

    def on_start(self):
        account = {
            "usernameOrEmail": "leanne",
            "password": "password"
        }

        response = self.client.post("/api/auth/signin", json=account)
        self.token = response.json()["accessToken"]
        my_token = f"Bearer {self.token}"

        self.client.headers.update({"Authorization": my_token})
        logging.info("Get Token from Auth Login")

    @task
    def get_my_profile(self):
        self.client.get("/api/users/me")
        print(self.token)
        logging.info("Get My Profile with Token")
