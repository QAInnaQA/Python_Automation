import requests
import pytest

from hidden import our_func


def save_data(data):
    with open("log.txt", "a") as f:
        f.write(f"{data}\n")


url = "https://ithillel.ua/_"
url_1 = "https://www.aqa.science/?format=json"


class TestSuite:

    def setup_class(self):
        self.errors = []
        self.data = []
        print("Tests suite started")

    def teardown_class(self):
        with open("data.log", "w+") as f:
            f.write(f"{self.data}")

        print("Tests Suite  done")

    def setup(self):
        print("single test started")

    def teardown(self):
        print("singlle test finished")

    def test_first_check(self):
        response = requests.get(url)
        code = response.status_code
        assert code == 200, self.errors.append(code)

    def test_second_check(self):
        response = requests.get(f"{url}/n/")
        code = response.status_code
        assert response.status_code == 404, self.errors.append(code)

    def test_third_check(self):
        save_data(self.errors)
        response = requests.get(url_1)
        self.data.append(response.text)
        assert response.text == \
               '''{"users":"https://www.aqa.science/users/?format=json",
               "groups":"https://www.aqa.science/groups/?format=json"}'''