import uuid

from rest_framework import status
from django.urls import reverse
from django.utils import timezone

from teleworking_project.tests.core.seed_db_test_data import SeedDBTestData

TEST_PASSWORD = "tp123"

class HostTests(SeedDBTestData):
    @classmethod
    def initTestData(cls):
        super().initTestData()

    def test_login_and_refresh(self):

        # obtain authentication credentials
        response = self.client.post(
            reverse("token-obtain-pair"),
            {"email": self.shayon_banerjee.email, "password": TEST_PASSWORD}
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue("access" in response.data.keys())
        self.assertTrue("refresh" in response.data.keys())

        sb_auth = "Bearer " + response.data["access"]
        sb_refresh = response.data["refresh"]

        # refresh authentication credentials
        response = self.client.post(reverse("token-refresh"), {"refresh": sb_refresh})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue("access" in response.data.keys())
        self.assertTrue("refresh" in response.data.keys())

    