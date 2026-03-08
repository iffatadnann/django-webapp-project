from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length = 255, verbose_name = "Student Name")
    group = models.CharField(max_length = 255, verbose_name = "Group/ Batch")
    phone = models.CharField(max_length = 255, verbose_name = "Phone Number")
    gr = models.CharField(max_length = 255, verbose_name = "GR Number")
    email = models.CharField(max_length = 255, verbose_name = "Email Address")

    def __str__(self):
        return f"{self.name} ({self.gr})"

class Courses(models.Model):
    group = models.CharField(max_length= 255, verbose_name = "Course Group")
    start_date = models.DateField(max_length= 255, verbose_name = "Start Date")
    description = models.TextField(max_length= 255, verbose_name = "Course Description")

    def __str__(self):
        return self.group

class Staff(models.Model):
    name = models.CharField(max_length= 255, verbose_name = "Staff Name")
    department = models.CharField(max_length= 255, verbose_name ="Department")
    email = models.EmailField(max_length = 500, verbose_name = "Email Address")

    def __str__(self):
        return self.name

class Messages(models.Model):
    name = models.CharField(max_length = 255, verbose_name="Sender Name")
    email = models.EmailField(max_length = 500, verbose_name="Sender Email")
    phone = models.CharField(max_length = 15, verbose_name="Phone Number")
    message = models.TextField(verbose_name="Message Content")

    def __str__(self):
        return f"Message from {self.name}"