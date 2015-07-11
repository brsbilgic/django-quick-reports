import json
from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import APIClient


class QuickReportsAPITests(TestCase):

    def setUp(self):
        user = User.objects.get_or_create(username='testy')[0]
        user.is_staff = True
        user.is_superuser = True
        user.set_password('pass')
        user.save()
        self.client = APIClient()
        self.client.login(username='testy', password='pass')

    def test_get_apps(self):
        res = self.client.get("/reports/api/apps/")
        self.assertEqual(res.status_code, 200)

        apps = json.loads(res.content)
        self.assertEqual(len(apps), 2)


    def test_get_models(self):
        res = self.client.get("/reports/api/apps/")
        self.assertEqual(res.status_code, 200)
        apps = json.loads(res.content)

        model_count = 0
        for app in apps:
            model_count += len(app["models"])

        self.assertEqual(model_count, 2)

    def test_report_slug_uniqueness(self):
        res = self.client.get("/reports/api/apps/")
        self.assertEqual(res.status_code, 200)
        apps = json.loads(res.content)

        for app in apps:
            for model in app["models"]:
                report_list = []
                for report in model["reports"]:
                    assert report["slug"] not in report_list, "Duplicate report name %s" % report["slug"]
                    report_list.append(report["slug"])
