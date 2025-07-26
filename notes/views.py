from rest_framework import generics, permissions
from .models import Note
from .serializers import NoteSerializer
# Create your views here.

class NotesListCreateView(generics.ListCreateAPIView):

    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    
    def get_queryset(self):
        return Note.objects.filter(owner=self.request.user).order_by('-created_at')


class NotesDetailView(generics.RetrieveDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def get_queryset(self):
        return Note.objects.filter(owner=self.request.user)
