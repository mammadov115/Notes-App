from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase

from .models import Note

# Create your tests here.


class NoteCRUDTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="test", password="test")
        self.token = self.client.post(
            reverse("token_obtain_pair"), {"username": "test", "password": "test"}
        ).data["access"]
        self.auth_headers = {"HTTP_AUTHORIZATION": f"Bearer {self.token}"}
        self.notes_url = reverse("notes-list-create")

    def test_list_notes(self):
        Note.objects.create(title="Note 1", content="Content 1", owner=self.user)
        response = self.client.get(self.notes_url, **self.auth_headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_create_note(self):
        data = {"title": "title 2", "content": "content 2"}
        response = self.client.post(self.notes_url, data, **self.auth_headers)
        self.assertEqual(response.status_code, 201)

    def test_update_note(self):
        note = Note.objects.create(title="Note 1", content="Content 1", owner=self.user)
        data = {"title": "title 2", "content": "content 2"}
        url = reverse("note-detail", args=[note.id])
        response = self.client.put(url, data, **self.auth_headers)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["title"], data["title"])

    def test_delete_note(self):
        note = Note.objects.create(title="Note 1", content="Content 1", owner=self.user)
        url = reverse("note-detail", args=[note.id])
        response = self.client.delete(url, **self.auth_headers)
        self.assertEqual(response.status_code, 204)
        self.assertFalse(Note.objects.filter(id=note.id).exists())

    def test_note_detail_permission(self):
        other_user = User.objects.create_user(username="other", password="other")
        note = Note.objects.create(
            title="Forbidden", content="Hidden", owner=other_user
        )
        url = reverse("note-detail", args=[note.id])
        response = self.client.get(url, **self.auth_headers)
        self.assertEqual(response.status_code, 404)
