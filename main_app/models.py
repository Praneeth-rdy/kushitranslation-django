from django.db import models

# Create your models here.

# Models of homepage
class Service(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.TextField()
    icon_code = models.CharField(max_length=50)

class Faq(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=300)
    answer = models.TextField()

class Testimonial(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    image = models.ImageField(upload_to='home/testimonials/')
    quotation = models.TextField()

class Language(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

class Slider(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    title_size = models.IntegerField(default=44)
    text = models.TextField()
    image = models.ImageField(upload_to='home/slider/')
    image_space_right = models.IntegerField(default=0)
    image_space_top = models.IntegerField(default=0)

class Counter(models.Model):
    id = models.AutoField(primary_key=True)
    number = models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    duration = models.IntegerField(default=2000)

class WhyUs(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.TextField()
    icon_code = models.CharField(max_length=50)