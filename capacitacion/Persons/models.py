from django.db import models


class Person(models.Model):
    """Person [summary]

    Args:
        models ([type]): [description]

    Returns:
        [type]: [description]
    """
    country = models.ForeignKey("Country.Country", on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    age = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        """__str__ [summary]

        Returns:
            [type]: [description]
        """
        return self.name
