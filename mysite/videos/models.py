from django.db import models

# Create your models here.
class Video(models.model):
    title = models.CharField() #fill in something here
    source_url = models.CharField? #Check documentation on this
    embed_link = models.CharField? # Same as above
    type_id = models.ForeignKey() # Type, more on this later


class Type(models.model):
    name = models.CharField()


class Rules(models.model):
    rule = models.CharField()


class Solstice(models.model):
    period = models.CharField() #Example: 'Summmer', 'Winter'
    year = models.CharField()
    title = models.CharField()
    description = models.CharField()
