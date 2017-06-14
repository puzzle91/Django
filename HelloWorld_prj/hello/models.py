from django.db import models
 
class Contact(models.Model):
 
    class Meta: # include this to ensure build in IDE
        app_label = "hello"
 
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images', default="images/noimage.png")

    def __str__(self):
        return "{0} {1}".format(self.first_name, self.last_name)

# Create your models here.