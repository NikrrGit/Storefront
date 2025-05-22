from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

class Tag(models.Model):
    label = models.CharField(max_length=255)

class TaggedItem(models.Model):
    # what tag applied  to what objects:
    tag =  models.ForeignKey(Tag,on_delete=models.CASCADE)
    content_type   = models.ForeignKey(ContentType,on_delete=models.CASCADE)
    object_id  = models.PositiveIntegerField()
    content_object = GenericForeignKey()                                        # to Get exact object :


