from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify
import itertools

class Holliday(models.Model):
	name = models.CharField(max_length=200)
	created_date = models.DateTimeField(default=timezone.now)
	updated_at = models.DateTimeField(default=timezone.now)
	slug = models.SlugField(null=True, blank=True, unique=True, max_length=100)
	
	def __str__(self):
		return self.name
	
	def save(self, *args, **kwargs):
		self.updated_at = timezone.now()
		self.slug = orig = slugify(self.name)[:50]
		for x in itertools.count(1):
			if not self.__class__.objects.filter(slug=self.slug).exclude(pk=self.pk).exists():
				break
			# Truncate the original slug dynamically. Minus 1 for the hyphen.
			# self.slug = "%s-%d" % (orig[:50 - len(str(x)) - 1], x)
		return super(Holliday, self).save(*args, **kwargs)
		
		
class Room(models.Model):
	### Relationships
	holliday = models.ForeignKey(Holliday, on_delete=models.CASCADE)
	parent_room = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
	
	### Attributes
	name = models.CharField(max_length=200)
	page_number = models.PositiveIntegerField(default=0)
	content = models.CharField(max_length=50000, blank=True)

	afi_komen = models.BooleanField(default=False)
	
	created_date = models.DateTimeField(default=timezone.now)
	updated_at = models.DateTimeField(default=timezone.now)
	
	slug = models.SlugField(null=True, blank=True, unique=True, max_length=100)
	
	def __str__(self):
		return self.name
	
	def save(self, *args, **kwargs):
		self.updated_at = timezone.now()
		self.slug = orig = slugify(self.name)[:50]
		for x in itertools.count(1):
			if not self.__class__.objects.filter(slug=self.slug).exclude(pk=self.pk).exists():
				break
			# Truncate the original slug dynamically. Minus 1 for the hyphen.
			self.slug = "%s-%d" % (orig[:50 - len(str(x)) - 1], x)
		return super(Room, self).save(*args, **kwargs)
