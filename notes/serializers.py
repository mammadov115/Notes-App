from rest_framework import serializers

from .models import Note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ["title", "content"]
        read_only_fields = ["owner"]

    def create(self, validate_data):
        user = self.context["request"].user
        return Note.objects.create(owner=user, **validate_data)
