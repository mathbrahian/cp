from django.urls import path, include
from Notes.urls.apis import router
from Notes.views import IndexView, NoteViewSet
from Notes.javascript import var_javascript

app_name = "Notes"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("javascript", var_javascript, name="js"),
    path("api/v1/", include(router.urls))
]