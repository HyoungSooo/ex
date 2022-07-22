from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

CATEGORY_CHOICES = (
    ('News', 'Ne'),
    ('Research', 'Re'),
)


class Post(models.Model):
    category = models.CharField(max_length=8, choices=CATEGORY_CHOICES)
    title = models.CharField(max_length=100, unique=True, blank=False)
    content = RichTextUploadingField()
    descirption = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Purpose(models.Model):
    content = RichTextUploadingField()


class Professor(models.Model):
    image = models.ImageField(
        upload_to='images/', blank=False, default='images/default.jfif')
    name = models.CharField(max_length=100, unique=True, blank=False)
    greeting = RichTextUploadingField()
    phone = models.CharField(max_length=100, blank=True)
    fax = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    position = models.CharField(max_length=100, blank=True)
    office = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name


class Timeline(models.Model):
    class Meta:
        ordering = ['date']

    professor = models.ForeignKey(
        Professor, on_delete=models.CASCADE, related_name='timeline', db_column='professor_id')
    date = models.DateField(blank=False)
    title = models.CharField(max_length=100, unique=True, blank=False)
    description = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title


class AboutUs(models.Model):
    POSITION = (
        ('Professor', 'AProf'),
        ('PhD', 'BPhD'),
        ('MS', 'CMS'),
        ('Undergraduate', 'DUn'),
        ('Alumni', 'EAL'),
    )

    CATEGORY = (
        ('AL', 'Alumni'),
        ('LA', 'LabMember')
    )

    name = models.CharField(max_length=100, unique=True, blank=False)
    category = models.CharField(
        max_length=2, choices=CATEGORY, blank=False, default='LA')
    position = models.CharField(max_length=13, choices=POSITION, blank=False)
    image = models.ImageField(
        upload_to='images/', blank=False, default='images/default.jfif')

    def __str__(self):
        return self.name


class Publictions(models.Model):
    content = RichTextUploadingField()
