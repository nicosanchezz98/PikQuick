from django.db import models

# Create your models here.
class User(models.Model):
    id = models.CharField('id', max_lenth 15)
    mail = models.CharField('mail', max_lenth 30)
    password = models.CharField('password', max_lenth 10)
    def __str__(self):
        return self.id

class Post(models.Model):
    class Meta:
        ordering=['-fecha_pub']
    desscription = models.CharField('description', max_lenth 150)
    date = models.DateTimeField('fecha', auto_now_true_True)
    user = models.ForeignKey(User)
    def __str__(self):
        return self.description

class Coment(models.Model):
    class Meta:
        ordering=['-fecha_pub']
    content = models.TextFiled('content', max_lenth 150)
    user = models.ForeignKey(User)
    def __str__(self):
        return self.content

class Options(models.Model):
    img = models.ImageField('photo')
    description = models.TextField('content', max_lenth 15)
    def __str__(self):
        return self.photo
