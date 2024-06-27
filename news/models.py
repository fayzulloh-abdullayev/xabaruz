from django.db import models
from django.utils import timezone


class PublishChoice(models.TextChoices):
    cancel='Bekor qilish'
    success="To'g'ri"

class StateManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(state=PublishChoice.success)
    

class Category(models .Model):
    
    name=models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
    
class News(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    title=models.CharField(max_length=250)
    slug=models.SlugField(max_length=250)
    image=models.ImageField(upload_to='news')
    text=models.TextField()
    created_date=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(auto_now=True)
    state=models.CharField(max_length=30,choices=PublishChoice.choices,default=PublishChoice.cancel)
    publish_time=models.DateTimeField(auto_now=timezone.now())

    objects=models.Manager()
    published=StateManager()


    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name='Yangilik'
        verbose_name_plural='Yangiliklar'
        ordering=('-created_date',)

class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    message=models.TextField()


    def __str__(self):
        return self.email
    


    




    


