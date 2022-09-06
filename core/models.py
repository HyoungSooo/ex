from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
# Create your models here.

CATEGORY_CHOICES = (
    ('News', 'Ne'),
    ('Research', 'Re'),
)


class Post(models.Model):
    thumbnail = models.ImageField(
        upload_to='post_images', blank=True, default='images/img.jpg')
    category = models.CharField(max_length=8, choices=CATEGORY_CHOICES)
    title = models.CharField(max_length=100, unique=True, blank=False)
    content = RichTextUploadingField()
    descirption = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Purpose(models.Model):
    title = models.CharField(max_length=100, unique=True)
    content = RichTextUploadingField()
    dt_created = models.DateTimeField(auto_now_add=True)


class Professor(models.Model):
    ordering = models.IntegerField(default=0)
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
        ('Professor', '1'),
        ('PhD', '2'),
        ('MS', '3'),
        ('Undergraduate', '4'),
    )

    name = models.CharField(max_length=100, unique=True, blank=False)
    position = models.CharField(max_length=13, choices=POSITION, blank=False)
    image = models.ImageField(
        upload_to='images/', blank=True, default='images/default.jfif')
    phone = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    address = models.CharField(max_length=100, blank=True)
    headerEx = models.CharField(max_length=100, blank=True)
    join_date = models.DateField(default='2020-01-01')

    def __str__(self):
        return self.name


CATEGORY_CHOICES = (
    ('Education', 'Education'),
    ('Interest', 'Interest'),
    ("Experience", 'Experience')
)


class MembersTimeline(models.Model):
    category = models.CharField(
        max_length=12, choices=CATEGORY_CHOICES, blank=False)
    title = models.CharField(max_length=100, blank=False)
    start_date = models.DateField()
    end_date = models.DateField()
    member = models.ForeignKey(
        AboutUs, on_delete=models.CASCADE, related_name="MemberReaSearch")


class ProfTimeline(models.Model):
    category = models.CharField(
        max_length=12, choices=CATEGORY_CHOICES, blank=False)
    title = models.CharField(max_length=100, blank=False)
    start_date = models.DateField()
    end_date = models.DateField()
    member = models.ForeignKey(
        Professor, on_delete=models.CASCADE, related_name="MemberReaSearch")


# class ResearchCategory(models.Model):
#     name = models.CharField(max_length=100, unique=True, blank=False)
#     image = models.ImageField(
#         upload_to='images/', blank=True, default='images/img.jpg')

#     def __str__(self):
#         return self.name


# class Researchs(models.Model):
#     category = models.ForeignKey(
#         ResearchCategory, related_name='researchs', on_delete=models.CASCADE, db_column='category_id')
#     title = models.CharField(max_length=100, unique=True, blank=False)
#     content = RichTextUploadingField()
#     thumbnail = models.ImageField(
#         default='images/img.jpg', blank=True, upload_to='research/')

class ResearchArena(models.Model):
    title = models.CharField(max_length=100, unique=True, blank=False)
    content = RichTextUploadingField()
    thumnail = models.ImageField(
        upload_to='images/', blank=True, default='images/default.jfif')
    description = models.CharField(max_length=500, blank=True)
    dt_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class Publications(models.Model):
    CATEGORY = (
        ('Journal', 'Journal'),
        ('Conference', 'Conference'),
        ('Patents', 'Patents')
    )
    category = models.CharField(max_length=12, choices=CATEGORY, blank=False)
    title = models.CharField(max_length=100, unique=True, blank=False)
    members = models.ManyToManyField(AboutUs, related_name='member')
    detail = RichTextUploadingField()
    link = models.URLField(blank=True)
    file = models.FileField(upload_to='files/', blank=True, default=None)
    date = models.DateField(blank=False)

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=100, unique=True, blank=False)
    client = models.CharField(max_length=100)
    users = models.ManyToManyField(AboutUs, related_name='users')
    statue = models.CharField(max_length=10, choices=(
        ('Active', 'Active'), ('Completed', 'Completed'), ('Scheduled', 'Scheduled'), ('Pending', 'Pending')))
    start_date = models.DateField()
    end_date = models.DateField(blank=True)


class PictureCa(models.Model):
    image = models.ImageField(
        upload_to='images/indexPic', blank=None)
    image_thumbnail = ImageSpecField(source='image',
                                     processors=[ResizeToFill(800, 400)],
                                     format='JPEG',
                                     options={'quality': 60})
