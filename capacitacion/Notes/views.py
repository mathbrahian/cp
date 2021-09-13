from rest_framework.viewsets import ModelViewSet
from .serializers import NoteGetSerializer, NotePostSerializer
from .models import Note

from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"


class NoteViewSet(ModelViewSet):
    http_method_names = ["get", "post"]
    serializer_class = NoteGetSerializer
    queryset = Note.objects.get_all_info()

    def get_serializer_class(self):
        if self.action in ["create", "update"]:
            return NotePostSerializer
        return super().get_serializer_class()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        if self.action == "retrieve":
            context["fields_out"] = ["created", "person_age", "person_country"]
        return context