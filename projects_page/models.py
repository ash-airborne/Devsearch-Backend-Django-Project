from doctest import master
from django.db import models
import uuid

class PROJECT_TABLE(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    tags = models.ManyToManyField('TAG_TABLE', blank=True)
    # if we had the TAG_TABLE class above the PROJECT_TABLE class we could have put it as
    # -- tags = models.ManyToManyField(TAG_TABLE)
    # but since it is below this class we reference it by putting it inside quotes like 'TAG_TABLE'
    
    vote_count = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    
    
    def __str__(self):
        return self.title
    
class REVIEW_TABLE(models.Model):
    VOTE_TYPE = (
        ('up','UPVOTE'),
        ('down','DOWNVOTE')
    )
    #owner=
    project = models.ForeignKey(PROJECT_TABLE, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        return self.value
    
class TAG_TABLE(models.Model):
    
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        return self.name
    
    