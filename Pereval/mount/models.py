from django.db import models

# Для функции: сохранить фото в файл media через админ панель
from .services import get_path_upload_photos


class Users(models.Model):
    email = models.EmailField(max_length=128)
    last_name = models.CharField(max_length=128)
    first_name = models.CharField(max_length=128)
    patronymic = models.CharField(max_length=128)
    phone = models.CharField(max_length=128)


class Pereval(models.Model):
    NEW = 'NW'
    PENDING = 'PN'
    ACCEPTED = 'AC'
    REJECTED = 'RJ'
    STATUS_CHOICES = (
        ('NW', 'new'),
        ('PN', 'pending'),
        ('AC', 'accepted'),
        ('RJ', 'rejected'),
    )

    beauty_title = models.CharField(max_length=128)
    title = models.CharField(max_length=128)
    other_titles = models.CharField(max_length=128)
    connect = models.CharField(max_length=128)
    add_time = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    coord_id = models.OneToOneField('Coords', on_delete=models.CASCADE)
    tourist_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default="NW")
    level = models.ForeignKey('Level', on_delete=models.CASCADE)


class Coords(models.Model):
    latitude = models.DecimalField(decimal_places=8, max_digits=10)
    longitude = models.DecimalField(decimal_places=8, max_digits=10)
    height = models.IntegerField(default=0)


class Level(models.Model):
    winter = '4A'
    spring = '2A'
    summer = '1A'
    autumn = '3A'

    LEVEL_CHOICES = (
        ('4A', 'winter'),
        ('2A', 'spring'),
        ('1A', 'summer'),
        ('3A', 'autumn'),
    )
    winter_lev = models.CharField(max_length=2, choices=LEVEL_CHOICES, default=winter)
    spring_lev = models.CharField(max_length=2, choices=LEVEL_CHOICES, default=winter)
    summer_lev = models.CharField(max_length=2, choices=LEVEL_CHOICES, default=winter)
    autumn_lev = models.CharField(max_length=2, choices=LEVEL_CHOICES, default=winter)


class Images(models.Model):
    # # Переход к изображению по ссылке
    # image = models.ImageField(upload_to='static/images')

    # Для функции: сохранить фото в файл media через админ панель
    image = models.ImageField(upload_to=get_path_upload_photos, verbose_name='picture', blank=True, null=True)
    title = models.CharField(max_length=128)
    pereval_id = models.ForeignKey(Pereval, on_delete=models.CASCADE, related_name='images')

    # # Переход к изображению по ссылке
    # def __str__(self):
    #     return self.title

    # Для функции: сохранить фото в файл media через админ панель
    def __str__(self):
        return f"{self.pk}: {self.title}"

    class Meta:
        verbose_name = "pictures"
        verbose_name_plural = "pictures"
