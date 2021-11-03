from datetime import datetime

from auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name}-{self.last_name}"

    def full_name(self):
        return f"{self.first_name}-{self.last_name}"

    class Meta:
        verbose_name = "Yazar"
        verbose_name_plural = "Yazarlar"


class Publisher(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=50)
    year = models.SmallIntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(datetime.now().year)]
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Yayın Evi"
        verbose_name_plural = "Yayın Evleri"


class Category(models.Model):
    name = models.CharField(max_length=31)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Kategori"
        verbose_name_plural = "Kategoriler"


class Book(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    image = models.ImageField(upload_to="uploads/% Y/% m/% d/")
    owner = models.ForeignKey(User, verbose_name="ekleyen", on_delete=models.CASCADE)
    author = models.ForeignKey(
        Author, verbose_name="yazarın_ismi", on_delete=models.CASCADE
    )
    description = models.TextField(blank=True, null=True)
    category = models.ManyToManyField(Category, verbose_name="kategori")
    publisher = models.ForeignKey(
        Publisher, on_delete=models.CASCADE, verbose_name="yayin_evi"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    score = models.SmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
    )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} - {self.author}"

    class Meta:
        verbose_name = "Kitap"
        verbose_name_plural = "Kitaplar"


class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="comment")
    from_user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.book} - {self.from_user.username}"

    class Meta:
        verbose_name = "Yorum"
        verbose_name_plural = "Yorumlar"
