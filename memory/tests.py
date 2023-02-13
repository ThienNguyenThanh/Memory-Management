from django.contrib.auth.models import User
from django.test import TestCase

from .models import Images, Memory


# Create your tests here.
class MemoryTestCase(TestCase):
    def setUp(self):
        test_user1 = User.objects.create()
        Memory.objects.create(user=test_user1,location='Vung Tau, Viet Nam',
                            comment='This place is cool !', visited_at='2022-01-11'
        )
        Memory.objects.create(user=test_user1,location='Ha Noi, Viet Nam',
                            comment='This place is capital of Viet Name !', visited_at='2022-08-12'
        )

    # Test Memory created or not
    def test_queryset_count(self):
        qs = Memory.objects.all()
        self.assertEqual(qs.count(), 2)

    # Test Memory created or not
    def test_queryset_flter(self):
        qs = Memory.objects.filter(user=1)
        self.assertEqual(qs[0].location, "Vung Tau, Viet Nam")
        self.assertEqual(qs[1].location, "Ha Noi, Viet Nam")
