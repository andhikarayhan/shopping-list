from django.test import Client, TestCase


class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/mainApp/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/mainApp/')
        self.assertTemplateUsed(response, 'main.html')