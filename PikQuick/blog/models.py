from django.db import models

# Create your models here.
<<<<<<< HEAD
=======
class User(models.Model):
    name = models.CharField('id', max_length=15, unique=True)
    mail = models.CharField('mail', max_length=30)
    password = models.CharField('password', max_length=10)
    def __str__(self):
        return self.id

class Post(models.Model):
    class Meta:
        ordering=['-date']
    desscription = models.CharField('description', max_length=150)
    date = models.DateTimeField('fecha', auto_now_add=True)
    user = models.ForeignKey(User)
    def __str__(self):
        return self.description

class Coment(models.Model):
    class Meta:
        ordering=['-date']
    date = models.DateTimeField('fecha', auto_now_add=True)
    content = models.TextField('content', max_length=150)
    user = models.ForeignKey(User)
    def __str__(self):
        return self.content


>>>>>>> e6c1cf87e696cce669465697b78f57f511bd6229
