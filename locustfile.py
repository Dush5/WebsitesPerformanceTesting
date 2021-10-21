from locust import HttpUser, task, between, constant, TaskSet


class WebsiteTest(TaskSet):

    @task(1)
    def load_on_website(self):
        self.client.get("/")


class MyLoadTest(HttpUser):
    host = "http://e6.df"
    wait_time = constant(1)

    def on_start(self):
        print("Load test has started")
        pass

    def on_stop(self):
        print("Load testing has been finished")
        pass

    tasks = [WebsiteTest]