from django.db import models


class Post(models.Model):
    post_id = models.IntegerField(primary_key=True)
    category = models.CharField(max_length=50)
    from_whom = models.CharField(max_length=120)
    title = models.CharField(max_length=255)
    text = models.TextField()
    thedate = models.DateField()
