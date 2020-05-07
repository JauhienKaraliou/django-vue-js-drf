from django.db import models


class Cycle(models.Model):
    cycle_title = models.CharField(max_length=100)
    cycle_description = models.TextField()
    cycle_year = models.CharField(max_length=250)


class Verse(models.Model):
    verse_id = models.AutoField(primary_key=True)
    verse_cycle = models.ManyToManyField(Cycle)
    verse_title = models.CharField(max_length=250)
    verse_body = models.TextField()
    verse_year = models.CharField(max_length=250)
    pub_date = models.DateTimeField('date published')


