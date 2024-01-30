from django.db import models

class Doctor(models.Model):
    full_name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='doctors/', null=True, blank=True)
    job = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)
    description = models.TextField()

    CHARACTER_CHOICES = [
        ('responsible', 'Ответственные'),
        ('operational', 'Оперативные'),
        ('kind', 'Добрые'),
    ]
    character = models.CharField(max_length=20, choices=CHARACTER_CHOICES)


class Education(models.Model):
    doctor = models.ForeignKey(Doctor, related_name='education', on_delete=models.CASCADE)
    institution = models.CharField(max_length=255)
    degree = models.CharField(max_length=100)


class News(models.Model):
    doctor = models.ForeignKey(Doctor, related_name='news', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='news/', null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField()


class Contact(models.Model):
    doctor = models.ForeignKey(Doctor, related_name='contact', on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    work_time = models.CharField(max_length=100)


class PhoneNumber(models.Model):
    contact = models.ForeignKey(Contact, related_name='phone_numbers', on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)


class Email(models.Model):
    contact = models.ForeignKey(Contact, related_name='emails', on_delete=models.CASCADE)
    email = models.EmailField()