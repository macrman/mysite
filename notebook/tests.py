from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from notebook.views import homepage

class HomePageTest(TestCase):

    def test_root_url_resolves_to_homepage_view(self):
        found = resolve('/')
        self.assertEqual(found.func, homepage)

    def test_homepage_returns_correct_html(self):
        request = HttpRequest()
        response = homepage(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>mac</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))
