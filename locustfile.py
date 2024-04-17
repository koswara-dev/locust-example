from locust import HttpUser, between

from data_parameterization.locust_data_parameterization import TaskProductData
from tasks.task_cart import TaskCart
from tasks.task_category import TaskCategory
from tasks.task_product import TaskProduct
from validation.locust_validate_response import TaskProductWithValidate


class MyUser(HttpUser):
    wait_time = between(1, 3)
    # bobot pada setiap task set
    # tasks = {TaskProduct: 3, TaskCategory: 1, TaskCart: 2}
    tasks = {TaskProductWithValidate}
