import uuid

from rest_framework import status
from django.urls import reverse
from django.utils import timezone

from teleworking_project.tests.core.seed_db_test_data import SeedDBTestData
from teleworking_project.office.models import Office, PropertyAmeneties

TEST_PASSWORD = "tp123"

class OfficeTests(SeedDBTestData):
    @classmethod
    def initTestData(cls):
        super().initTestData()

    def test_create_property_ameneties(self):
        """ tests for post_property_ameneties """
        response = self.client.post(
            reverse("token-obtain-pair"),
            {"email": self.shayon_banerjee.email, "password": TEST_PASSWORD}
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue("access" in response.data.keys())
        self.assertTrue("refresh" in response.data.keys())

        sb_auth = "Bearer " + response.data["access"]

        # create property ameneties
        response = self.client.post(
            reverse("property_ameneties"),
            data={
                "wifi": "true",
                "outlet": "true",
                "monitor": "true",
                "heating": "true",
                "air_conditioning": "true",
                "coffee": "true",
                "windows": "true",
                "parking": "true",
                "parking_cost": "30",
                "elevator": "true",
                "wheel_chir_access": "true",
                "adjustable_seating": "true",
                "other": "None"
            },
            HTTP_AUTHORIZATION=sb_auth
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_property_ameneties(self):
        """ tests for patch_property_ameneties """
        response = self.client.post(
            reverse("token-obtain-pair"),
            {"email": self.shayon_banerjee.email, "password": TEST_PASSWORD}
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue("access" in response.data.keys())
        self.assertTrue("refresh" in response.data.keys())

        sb_auth = "Bearer " + response.data["access"]

        # create property ameneties object
        property_ameneties = PropertyAmeneties.create(
            "wifi" = "true",
            "outlet" = "true",
            "monitor" = "true",
            "heating" ="true",
            "air_conditioning" = "true",
            "coffee" = "true",
            "windows" = "true",
            "parking" = "true",
            "parking_cost" = "30",
            "elevator" = "true",
            "wheel_chir_access" = "true",
            "adjustable_seating" = "true",
            "other" = "None"
        )
        
        # Update property ameneties
        response = self.client.patch(
            reverse("property_ameneties", kwargs={"uuid": property_ameneties.id}),
            data = {
                "outlet" = "false",
                "heating" = "false",
                "parking_cost" = "40"
            },
            HTTP_AUTHORIZATION = sb_auth
        )

        # Assert success
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_property_ameneties(self):
        """ tests for get_property_ameneties """
        response = self.client.post(
            reverse("token-obtain-pair"),
            {"email": self.shayon_banerjee.email, "password": TEST_PASSWORD}
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue("access" in response.data.keys())
        self.assertTrue("refresh" in response.data.keys())

        sb_auth = "Bearer " + response.data["access"]

        # create property ameneties object
        property_ameneties = PropertyAmeneties.create(
            "wifi" = "true",
            "outlet" = "true",
            "monitor" = "true",
            "heating" ="true",
            "air_conditioning" = "true",
            "coffee" = "true",
            "windows" = "true",
            "parking" = "true",
            "parking_cost" = "30",
            "elevator" = "true",
            "wheel_chir_access" = "true",
            "adjustable_seating" = "true",
            "other" = "None"
        )

        # Update property ameneties
        response = self.client.get(
            reverse("property_ameneties", kwargs={"uuid": property_ameneties.id}),
            HTTP_AUTHORIZATION = sb_auth
        )

        # Request should succeed
        self.assertEqual(response.status_code, status.HTTP_200_OK)












           