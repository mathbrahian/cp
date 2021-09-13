from django.db import models
from django.db.models.expressions import F, Case, Value, When
from Persons.models import Person


class NoteManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().select_related(
            "person", "person__country"
        )

    def get_all_info(self):
        """get_all_info [summary]

        Returns:
            [type]: [description]
        """
        valores = [
            "title",
            "body",
            "created",
            "person_name",
            "person_age",
            "person_country",
            "person_active"
        ]

        query = self.annotate(
            person_name=F("person__name"),
            person_age=F("person__age"),
            person_country=F("person__country__name"),
            person_active=Case(
                When(person__is_active=True, then=Value("Si")),
                When(person__is_active=False, then=Value("No")),
            )
        ).only(*valores).values(*valores)
        return query


class Note(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = NoteManager()

    def __str__(self):
        return self.title

