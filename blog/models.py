from django.db import models
from django.utils.timezone import now

# Create your models here.
class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    slug = models.CharField(max_length=120)
    tags = models.CharField(max_length=200, default="all")
    user = models.CharField(max_length=200)
    shortdesc = models.TextField()
    content = models.TextField()
    image = models.ImageField(upload_to='static/images/home/posts', default="")
    timeStamp = models.DateField()

    def __str__(self):
        return self.title + '. at - ' + str(self.timeStamp)

class Comment(models.Model):
    sno = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    content = models.TextField()
    timeStamp = models.DateTimeField(default=now)
    def __str__(self):
        return self.email + '. says - ' + str(self.content)[0:10] + '...'

