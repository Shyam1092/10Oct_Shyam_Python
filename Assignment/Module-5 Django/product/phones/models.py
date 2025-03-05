from django.db import models

class PhoneCompany(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Phone(models.Model):
    company = models.ForeignKey(PhoneCompany, related_name='phones', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    ram = models.CharField(max_length=50)
    rom = models.CharField(max_length=50)
    processor = models.CharField(max_length=100)
    photo = models.URLField(max_length=4000)

    def __str__(self):
        return self.name
