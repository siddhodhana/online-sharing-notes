from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Updext(models.Model):
	g = [('M',"Male"),('F',"Female")]
	age = models.IntegerField(default=18)
	gender = models.CharField(max_length=7,choices=g)
	im = models.ImageField(upload_to="Profile/",default="profile.png")
	p = models.OneToOneField(User,on_delete=models.CASCADE)

@receiver(post_save,sender=User)
def CrtPfle(sender,instance,created,**kwargs):
	 if created:
	 	Updext.objects.create(p=instance)


class Creatnote(models.Model):
	title=models.CharField(max_length=120)
	date=models.DateField()
	description=models.TextField()
	created_by=models.CharField(max_length=120)
	fl=models.FileField(upload_to="Uploaded/")
	generatekey=models.TextField()
	s=models.ForeignKey(User,on_delete=models.CASCADE)