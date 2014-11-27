from django.db import models

from  django.contrib.auth.models import User

class Employee(models.Model):
      user = models.OneToOneField(User)
      telefono = models.IntegerField(max_length=200)
      email = models.EmailField()
      def __unicode__(self):
              return self.user.username
