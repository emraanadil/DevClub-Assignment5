import os

from distutils.command.upload import upload
from re import M
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
# Create your models here.

class Standard(models.Model):
    name = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(null=True,blank=True)
    description = models.TextField(max_length=400,blank=True)

    def __str__(self):
        return self.name
    
    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super().save(*args,**kwargs)

# course class code;
def save_course_image(instance,filename):
    upload_to = 'Images/'
    ext = filename.split('.')[-1]
    if instance.course_id:
        filename = f"SubjectPictures/{instance.course_id}.{ext}"
    return os.path.join(upload_to,filename)



class Course(models.Model):
    course_id = models.CharField(max_length=15,unique=True)
    name = models.CharField(max_length=30)
    slug = models.SlugField(null=True,blank=True)
    standard = models.ForeignKey(Standard,on_delete=models.CASCADE,related_name='courses')
    image = models.ImageField(upload_to= save_course_image,blank=True,verbose_name='Course Image')
    description = models.TextField(max_length=250,blank=True)

    def __str__(self):
        return self.name

    def save(self,*args, **kwargs):
        self.slug = slugify(self.course_id)
        super().save(*args,**kwargs)


### Lesson Model code;_
def save_lesson_files(instance,filename):
    upload_to = 'Images/'
    ext = filename.split('.')[-1]

    if instance.lesson_id:
        filename=f'lesson_media/{instance.lesson_id}/{instance.lesson_id}.{ext}'
        if os.path.exits(filename):
            new_name = str(instance.lesson_id) + str(1)
            filename = f'lesson_media/{instance.lesson_id}/{new_name}.{ext}'
    return os.path.join(upload_to,filename)


class Lesson(models.Model):
    lesson_id = models.CharField(max_length=18,unique=True)
    Standard = models.ForeignKey(Standard,on_delete=models.CASCADE)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    Course = models.ForeignKey(Course,on_delete=models.CASCADE,related_name='lessons')
    name = models.CharField(max_length=50)
    position = models.PositiveSmallIntegerField(verbose_name='Chapter No:')
    slug = models.SlugField(null=True,blank=True)
    video = models.FileField(upload_to=save_lesson_files,verbose_name='Video',blank=True,null=True)
    ppt = models.FileField(upload_to=save_lesson_files,verbose_name='Presentations',blank=True)
    Notes = models.FileField(upload_to=save_lesson_files,verbose_name="Notes",blank=True)

    class Meta:
        ordering = ['position']

    def __str__(self):
        return self.name
    
    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super().save(*args,**kwargs)
    