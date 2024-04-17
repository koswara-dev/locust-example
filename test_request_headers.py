# Header options from RapidApi GeoDB Cities
# Use only 1 user, 1 ramp up, time 30s

import logging

from locust import HttpUser, between, task


class UserGeo(HttpUser):
    host = "https://wft-geo-db.p.rapidapi.com"
    wait_time = between(1, 3)

    def on_start(self):
        header_options = {
            "X-RapidAPI-Key": "064fb264d2msha77d9532cfe6675p1ec1e4jsn9524e55334c6",
            "X-RapidAPI-Host": "wft-geo-db.p.rapidapi.com"
        }
        self.client.headers.update(header_options)
        logging.info("Add header options")

    @task
    def get_admin_divisions(self):
        self.client.get("/v1/geo/adminDivisions")
        logging.info("Get Data Admin Divisions")

    @task
    def get_countries(self):
        self.client.get("/v1/geo/countries")
        logging.info("Get Data Countries")
