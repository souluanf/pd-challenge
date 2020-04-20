from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=100)
    bnull = dict(null=True, blank=True)
    slug = models.SlugField(unique=True, max_length=50, **bnull)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'place'

    def __str__(self):
        return self.name
