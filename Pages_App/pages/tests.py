from django.test import SimpleTestCase
from django.urls import reverse


class HomePageTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "pages/home.html")

    def test_template_content(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "Home")


class AboutPageTests(SimpleTestCase):
    def test_about_page_status_code(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get(reverse("about"))
        self.assertTemplateUsed(response, "pages/about.html")

    def test_template_content(self):
        response = self.client.get(reverse("about"))
        self.assertContains(response, "About")
