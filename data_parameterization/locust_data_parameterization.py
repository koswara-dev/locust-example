import csv

from locust import TaskSet, task


class TaskProductData(TaskSet):

    @task
    def create_product(self):
        with open('data_parameterization/products.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                row: dict
                product_data = {
                    "title": row["title"],
                    "price": float(row["price"]),
                    "description": row["description"],
                    "image": row["image"],
                    "category": row["category"]
                }
                response = self.client.post("/products", json=product_data)
                print(f"Response status code: {response.status_code}, Response content: {response.content}")
