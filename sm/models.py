from django.db import models

# Create your models here.
class apartments(models.Model):
    
    name = models.CharField(max_length=100)
    desc = models.TextField()
    img1 = models.ImageField(upload_to='pics')
    img2 = models.ImageField(upload_to='pics')
    img3 = models.ImageField(upload_to='pics')
    img4 = models.ImageField(upload_to='pics')
    img5 = models.ImageField(upload_to='pics')
    img6 = models.ImageField(upload_to='pics')
    img7 = models.ImageField(upload_to='pics')
    img8 = models.ImageField(upload_to='pics')
    bed = models.IntegerField()
    ter = models.IntegerField()
    sf = models.IntegerField()
    sqfeet =  models.BooleanField(default=False)
    sqyard = models.BooleanField(default=False)



