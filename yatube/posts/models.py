from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    group = models.ForeignKey(
        'Group', blank=True, null=True,
        on_delete=models.CASCADE
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )


class Group(models.Model):

    # название группы
    title = models.CharField(max_length=200)
    # например, для группы любителей котиков slug будет равен cats: group/cats
    slug = models.SlugField(unique=True)
    # текст, описывающий сообщество
    description = models.TextField()

    # чтобы при печати объекта модели Group выводилось поле title
    def __str__(self) -> str:
        return self.title
