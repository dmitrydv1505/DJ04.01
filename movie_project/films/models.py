from django.db import models

# Create your models here.
class Film(models.Model):
    title = models.CharField(max_length=100)  # Поле для названия фильма
    description = models.TextField()  # Поле для описания фильма
    review = models.TextField()  # Поле для отзыва о фильме

    def __str__(self):
        return self.title
