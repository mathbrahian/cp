from rest_framework import routers
from rest_framework.routers import DefaultRouter

from Notes.views import NoteViewSet

router = DefaultRouter()

router.register("notes", NoteViewSet, 'notas')