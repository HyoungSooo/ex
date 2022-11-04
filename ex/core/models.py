from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
# Create your models here.

CATEGORY_CHOICES = (
    ('News', 'Ne'),
    ('Research', 'Re'),
    ('Outstanding', 'Os')
)


class Post(models.Model):

    @property
    def short_des(self):
        return 'this is some comment'

    short_des.fget.short_description = '적용 위치'

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    title = models.CharField(max_length=100, unique=True, blank=False)
    content = RichTextUploadingField()
    descirption = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class PhotoVedio(models.Model):

    @property
    def short_des(self):
        return 'this is some comment'

    short_des.fget.short_description = '적용 위치'

    thumbnail = models.ImageField(
        upload_to='post_images', blank=True, default='images/img.jpg')
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

    @property
    def short_des(self):
        return 'this is some comment'

    short_des.fget.short_description = '적용 위치'

    ordering = models.IntegerField(default=0)
    image = models.ImageField(
        upload_to='images/', blank=False, default='images/default.jfif')
    name = models.CharField(max_length=100, unique=True, blank=False)
    phone = models.CharField(max_length=100, blank=True)
    fax = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    position = models.CharField(max_length=100, blank=True)
    office = models.CharField(max_length=100, blank=True)
    member_since = models.DateField()

    def __str__(self):
        return self.name


class Timeline(models.Model):
    class Meta:
        ordering = ['date']

    @property
    def short_des(self):
        return 'this is some comment'

    short_des.fget.short_description = '적용 위치'

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
        ('PH.D', 'PH.D'),
        ('PH.D Student', 'PH.D Student'),
        ('Post Graduate', 'Post Graduate'),
        ('Undergraduate', 'Undergraduate'),
    )

    @property
    def short_des(self):
        return 'this is some comment'

    short_des.fget.short_description = '적용 위치'

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

    @property
    def short_des(self):
        return 'this is some comment'

    short_des.fget.short_description = '적용 위치'

    category = models.CharField(
        max_length=12, choices=CATEGORY_CHOICES, blank=False)
    title = models.CharField(max_length=100, blank=False)
    start_date = models.DateField()
    end_date = models.DateField()
    member = models.ForeignKey(
        AboutUs, on_delete=models.CASCADE, related_name="MemberReaSearch")

    def __str__(self):
        return self.title


class ProfTimeline(models.Model):

    @property
    def short_des(self):
        return 'this is some comment'

    short_des.fget.short_description = '적용 위치'

    category = models.CharField(
        max_length=12, choices=CATEGORY_CHOICES, blank=False)
    title = models.CharField(max_length=100, blank=False)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    member = models.ForeignKey(
        Professor, on_delete=models.CASCADE, related_name="MemberReaSearch")

    def __str__(self):
        return self.title


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

    @property
    def short_des(self):
        return 'this is some comment'

    short_des.fget.short_description = '적용 위치'

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
        ('International Papers', 'International Papers'),
        ('International Conference', 'International Conference'),
        ('Domestic Papers', 'Domestic Papers'),
        ('Domestic Conference', 'Domestic Conference'),
        ('Patents', 'Patents'),
    )

    @property
    def short_des(self):
        return 'this is some comment'

    short_des.fget.short_description = '적용 위치'

    category = models.CharField(max_length=500, choices=CATEGORY, blank=False)
    title = models.CharField(max_length=100, unique=True, blank=False)
    members = models.ManyToManyField(AboutUs, related_name='member')
    date = models.DateField(blank=False)

    def __str__(self):
        return self.title


class Project(models.Model):

    @property
    def short_des(self):
        return 'this is some comment'

    short_des.fget.short_description = '적용 위치'

    title = models.CharField(max_length=100, unique=True, blank=False)
    client = models.CharField(max_length=100)
    users = models.ManyToManyField(AboutUs, related_name='users')
    statue = models.CharField(max_length=10, choices=(
        ('Active', 'Active'), ('Completed', 'Completed'), ('Scheduled', 'Scheduled'), ('Pending', 'Pending')))
    start_date = models.DateField()
    end_date = models.DateField(blank=True)

    def __str__(self):
        return self.title


class PictureCa(models.Model):

    @property
    def short_des(self):
        return 'this is some comment'

    short_des.fget.short_description = '적용 위치'

    image = models.ImageField(
        upload_to='images/indexPic', blank=None)
    image_thumbnail = ImageSpecField(source='image',
                                     processors=[ResizeToFill(800, 400)],
                                     format='JPEG',
                                     options={'quality': 60})

    def __str__(self):
        return self.image.name


class IndexResearch(models.Model):
    title = models.CharField(max_length=100, blank=False)
    thumbnail = models.ImageField(upload_to='images/indexresearch', blank=None)
    description = models.CharField(max_length=200, blank=False)

class tasks(models.Model):
    work = models.CharField(max_length=100, blank=False)
    date = models.DateField(blank=False)

    class Meta:
        ordering = ['-date']


    def __str__(self) -> str:
        return self.work
    