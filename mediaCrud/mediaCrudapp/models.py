from django.db import models

# Create your models here.
class FileModel(models.Model):
	rno=models.IntegerField(primary_key=True)
	name=models.CharField(max_length=30)
	file=models.FileField(upload_to='media/')

	def __str__(self):
		return self.name
