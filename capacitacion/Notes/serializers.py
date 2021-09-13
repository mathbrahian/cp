from Notes.models import Note
from rest_framework import serializers


class NoteGetSerializer(serializers.Serializer):
    title = serializers.SerializerMethodField()
    body = serializers.SerializerMethodField()
    created = serializers.SerializerMethodField()
    person_name = serializers.SerializerMethodField()
    person_age = serializers.SerializerMethodField()
    person_country = serializers.SerializerMethodField()
    person_active = serializers.SerializerMethodField()
    buttons = serializers.SerializerMethodField()

    def __init__(self, *args, **kwargs):
        fields_out = kwargs["context"].get("fields_out", [])
        super().__init__(*args, **kwargs)
        for field in fields_out:
            self.fields.pop(field)

    def get_title(self, row):
        return row["title"]

    def get_body(self, row):
        return row["body"]

    def get_created(self, row):
        return row["created"].strftime("%d-%m-%Y")

    def get_person_name(self, row):
        return row["person_name"]

    def get_person_age(self, row):
        return row["person_age"]

    def get_person_country(self, row):
        return row["person_country"]
    
    def get_person_active(self, row):
        return row["person_active"]

    def get_buttons(self, row):
        btns = ""
        detail = f"""<a onclick="return loadModal();" class="btn btn-primary btn-xs">Detalle</a>"""
        btns += detail
        return btns


class NotePostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Note
        fields = [
            "title", "body", "person"
        ]