from django.urls import path

from . import views

urlpatterns = [
    path("", views.NotesListCreateView.as_view(), name="notes-list-create"),
    path("<int:pk>/", views.NotesDetailView.as_view(), name="note-detail"),
]
