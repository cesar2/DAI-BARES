from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.

class Bar(models.Model):
	name = models.CharField(max_length=128, unique=True)
	address = models.CharField(max_length=128)
	visits = models.IntegerField(default=0)
	slug = models.SlugField()
	
	def save(self, *args, **kwargs):
		# Uncomment if you don't want the slug to change every time the name changes
		# if self.id is None:
				#self.slug = slugify(self.name)
		self.slug = slugify(self.name)
		super(Bar, self).save(*args, **kwargs)
	
	def __unicode__(self):
		return self.name

class Tapa(models.Model):
	bar = models.ForeignKey(Bar)
	name2 = models.CharField(max_length=128)
	votos = models.IntegerField(default=0)
	url = models.URLField()
	#foto = models.ImageField(upload_to='profile_images', blank=True)
	
	def __str__(self):
		return self.name2
		
class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username
	
	
