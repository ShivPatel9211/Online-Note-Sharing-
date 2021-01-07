from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Signup(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=15 )
    branch = models.CharField(max_length=30)
    role = models.CharField(max_length=30)

    def __str__(self):
        return self.user.username

class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    uploadingdate = models.CharField(max_length= 30)
    branch = models.CharField(max_length= 30)
    subject = models.CharField(max_length= 30)
    notesfile = models.FileField()

    filetype = models.CharField(max_length= 30)
    discription = models.CharField(max_length= 200)
    status = models.CharField(max_length= 200)

    def __str__(self):
        return self.Signup.user.username + "" + self.status

