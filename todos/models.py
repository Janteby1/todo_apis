from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone #make sure to set the timezone 
import uuid


# Create your models here.

class UserProfile(models.Model):
    # this line links UserProfile to a user model instance
    user = models.OneToOneField(User)
    # here we can add aditional attributes 
    token = models.UUIDField(default=uuid.uuid4)

class Todos(models.Model):
    content = models.CharField(max_length=400)
    userid = models.ForeignKey(User) # adds a FK
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField()
    finished = models.BooleanField(default=False) 

    # this is a custom save method
    def save(self, *args, **kwargs):
        self.updated_at = timezone.now()
        self.user = user
        if not self.id:
            self.created_at = timezone.now()
        super(Todos, self).save(*args, **kwargs)

    def to_json ():
        pass 
    # send the contenxt to the view 



