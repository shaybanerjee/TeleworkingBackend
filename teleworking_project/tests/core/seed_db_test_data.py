from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model

from teleworking_project.users.models import User
from teleworking_project.hosts.models import Host

class SeedDBTestData(APITestCase):
    """ this will seed our db with test users and data """

    @classmethod
    def initTestData(cls):
        cls.superuser = get_user_model().objects().create_superuser(
            email="test@tp.com", password="tp123"
        )

        cls.shayon_banerjee = get_user_model().objects.create_user(
            email="shayon@tp.com", password="tp123"
        )

        cls.keerthu_sh = get_user_model().objects.create_user(
            email="keerthu@tp.com", password="tp123"
        )

        cls.kanye_west = get_user_model().objects.create_user(
            email="kanye@west.com", password="tp123"
        )

        cls.donkey_kong = get_user_model().objects.create_user(
            email="donkey@kong.com", password="tp123"
        )

        # create host: Shayon Banerjee
        Host.objects.create(
            user=cls.shayon_banerjee, 
            city="Toronto", 
            description="Male/23.", 
            identity_verified="true", 
            company_name="AWS"
        )

        # create host: Donkey Kong
        Host.objects.create(
            user=cls.donkey_kong,
            city="Ottawa",
            description="Male/103",
            identity_verified="true",
            company_name="Jungle"
        )

        # create teleworker: Keerthu Sh
        User.objects.create(
            user=cls.keerthu_sh,
            date_of_birth="1997-03-04",
            email=cls.keerthu_sh.email,
            first_name="keerthu",
            last_name="Sh",
            gender="0",
            company="NASA",
            city="Toronto",
            country="Canada",
            profile_picture = "http://www.random.com",
            is_verified="true",
            phone_number="5142334233"
        )
        
        # create teleworker: kanye_west
        User.objects.create(
            user=cls.kanye_west,
            date_of_birth="1943-03-04",
            email=cls.kanye_west.email,
            first_name="kanye",
            last_name="west",
            gender="0",
            company="West Coast Productions",
            city="LA",
            country="USA",
            profile_picture = "http://www.kanye_west.com",
            is_verified="true",
            phone_number="1234567890"
        )
