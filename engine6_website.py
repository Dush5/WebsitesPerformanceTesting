# locust -f engine6_website.py --headless --users 10 --spawn-rate 1 -H
# http://palmen-dev-dealerfire-com.website.tp6373.df-tp.com --run-time 20s

from locust import HttpUser, task, constant, TaskSet


class WebsiteTest(TaskSet):

    @task
    def engine6_webpage(self):
        count = 0
        with open("file.txt") as fp:
            for line in fp:
                self.client.get(line.strip())


class MyLoadTest(HttpUser):
    host = "http://palmen-dev-dealerfire-com.website.tp6373.df-tp.com"
    wait_time = constant(1)

    def on_start(self):
        print("Load test has started")
        pass

    def on_stop(self):
        print("Load testing has been finished")
        pass

    tasks = [WebsiteTest]
