from django.db import models

# Create your models here.
class PostImage(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    desc = models.TextField()

    class GetCatogery(models.TextChoices):
            PEOPLE = ('people')
            NATURE = ('nature')
            FOOD = ('food')
            WORK = ('work')

    catogery = models.CharField(max_length=200,choices=GetCatogery.choices,default=GetCatogery.NATURE)

    tags = models.CharField(max_length=200, default="all")
    image = models.ImageField(upload_to='static/images/home', default="")
    timeStamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title + '. at - ' + str(self.timeStamp)

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=500)
    content = models.TextField()
    timeStamp = models.DateField(auto_now_add=True)
    def __str__(self):
        return str(self.subject)[0:10] + '. by - ' + str(self.first_name)