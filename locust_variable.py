from locust import HttpUser, task, between


class UserBehavior(HttpUser):
    wait_time = between(1, 3)

    # Variabel yang berisi data pengguna yang akan dibuat
    user_data = {
        "name": "John Doe",
        "job": "Software Engineer"
    }

    @task
    def create_user(self):
        # Menggunakan variabel user_data untuk membuat pengguna baru
        response = self.client.post("/api/users", json=self.user_data)
        print(f"Response status code: {response.status_code}, Response content: {response.content}")

    @task
    def get_users(self):
        # Mengambil daftar pengguna
        response = self.client.get("/api/users")
        print(f"Response status code: {response.status_code}, Response content: {response.content}")

    @task
    def update_user(self):
        # Menggunakan variabel user_data untuk memperbarui pengguna dengan ID 2
        response = self.client.put("/api/users/2", json=self.user_data)
        print(f"Response status code: {response.status_code}, Response content: {response.content}")

    @task
    def delete_user(self):
        # Menghapus pengguna dengan ID 2
        response = self.client.delete("/api/users/2")
        print(f"Response status code: {response.status_code}, Response content: {response.content}")
