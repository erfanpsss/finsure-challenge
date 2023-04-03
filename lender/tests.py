from rest_framework.test import APITestCase
from django.urls import reverse

class TestLenderViewSet(APITestCase):

    def test_create(self):
        url = reverse("lenders")
        data = {
            "name": "Commonwealth Bank",
            "code": "CBA",
            "upfront_commission_rate": 0,
            "trial_commission_rate": 1,
            "active": True
        }
        res = self.client.post(url, data=data)
        self.assertEqual(res.status_code, 201)

