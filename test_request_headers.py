# Header options from RapidApi GeoDB Cities
# Use only 1 user, 1 ramp up, time 30s

import logging
import os

from dotenv import load_dotenv
from locust import HttpUser, between, task


class UserGeo(HttpUser):
    host = "https://wft-geo-db.p.rapidapi.com"
    wait_time = between(1, 3)

    # load rapid key from .env file
    load_dotenv()
    rapid_key = os.getenv("RAPID_KEY")

    def on_start(self):
        header_options = {
            "X-RapidAPI-Key": self.rapid_key,
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
