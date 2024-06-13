from django.db import models
 
class Books(models.Model):
    title=models.CharField(max_length=40)
    name=models.CharField(max_length=40)
    year=models.CharField(max_length=40)
    image=models.FileField(null=True,blank=True)

    def __str__ (self):
        return self.name
    
    
