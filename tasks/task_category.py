from locust import TaskSet, task


class TaskCategory(TaskSet):

    @task
    def get_categories(self):
        response = self.client.get("/products/categories")
        print(f"Response status code: {response.status_code}, Response content: {response.content}")

    # TODO: add more test
