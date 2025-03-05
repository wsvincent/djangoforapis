from django.urls import reverse  # new
from django.test import TestCase  # new
from rest_framework.test import APITestCase  # new
from rest_framework import status

from .models import Todo


class TodoModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.todo = Todo.objects.create(title="First Todo", body="A body of text here")

    def test_model_content(self):
        self.assertEqual(self.todo.title, "First Todo")
        self.assertEqual(self.todo.body, "A body of text here")
        self.assertEqual(str(self.todo), "First Todo")


class TodoAPITests(APITestCase):  # new
    @classmethod
    def setUpTestData(cls):
        cls.todo = Todo.objects.create(title="Test Todo", body="Test body content")
        cls.list_url = reverse("todo_list")
        cls.detail_url = reverse("todo_detail", args=[cls.todo.id])

    def test_list_todo(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)
        self.assertGreaterEqual(len(response.data), 1)

    def test_detail_todo(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.todo.title)
        self.assertEqual(response.data["body"], self.todo.body)

    def test_detail_todo_not_found(self):
        response = self.client.get(reverse("todo_detail", args=[999]))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
