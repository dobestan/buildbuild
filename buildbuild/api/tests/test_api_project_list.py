from django.test import TestCase
from django.test.client import Client

from projects.models import Project
from teams.models import Team


class TestAPIUserList(TestCase):
    def setUp(self):
        self.team = Team.objects.create_team(
            name="test_team_name",
        )
        self.project = Project.objects.create_project(
            name="test_project_name",
        )

        self.client = Client()
        self.response = self.client.get("/api/projects/")

    def test_api_project_list_request_should_return_200(self):
        self.assertEqual(self.response.status_code, 200)

    def test_api_project_list_request_should_return_json(self):
        self.assertEqual(self.response["Content-Type"], "application/json")

    def test_api_project_list_request_should_contain_project_id_and_name(self):
        self.assertContains(self.response, self.project.id)
        self.assertContains(self.response, self.project.name)
