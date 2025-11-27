from django.test import TestCase
from django.urls import reverse


class CoreTests(TestCase):
    """
    A simple test case to ensure core functionality is working.
    """

    def test_admin_login_page_loads(self):
        """Tests that the admin login page loads correctly."""
        admin_url = reverse("admin:index")
        response = self.client.get(admin_url)
        # An unauthenticated user should be redirected (302) to the login page.
        self.assertEqual(response.status_code, 302)
