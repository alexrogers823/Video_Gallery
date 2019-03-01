from django.db import models

# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=200) #fill in something here
    source_url = models.URLField()#Check documentation on this
    embed_link = models.CharField(max_length=300) # Same as above
    type_id = models.ForeignKey('Type', on_delete=models.PROTECT) # Type, more on this later


class Type(models.Model):
    name = models.CharField(max_length=200)


class Rules(models.Model):
    rule = models.CharField(max_length=200)


class Solstice(models.Model):
    period = models.CharField(max_length=200) #Example: 'Summmer', 'Winter'
    year = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
