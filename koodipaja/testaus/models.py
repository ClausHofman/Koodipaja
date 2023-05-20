from django.db import models
from users.models import Profile


class Person(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')

    def __str__(self):
        return self.name


class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)


class MyModel(models.Model):
    my_boolean_field = models.BooleanField(default=False)
    id = models.AutoField(primary_key=True)


# Memory game

class Muistipeli(models.Model):
    owner = models.ForeignKey(
        Profile, null=True, blank=True, on_delete=models.SET_NULL)
    featured_image = models.ImageField(
        null=True, blank=True, upload_to="users/", default="default.jpg")
    title = models.CharField(max_length=200)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.title

    @property
    def imageURL(self):
        try:
            url = self.featured_image.url
        except:
            url = ''
        return url


class Malli1(models.Model):
    owner = models.ForeignKey(
        Profile, null=True, blank=True, on_delete=models.SET_NULL)
    muistipeli = models.ForeignKey(
        Muistipeli, on_delete=models.CASCADE, null=True)
    question = models.CharField(max_length=500, null=True, blank=True)
    answer = models.CharField(max_length=2000, null=True, blank=True)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.question


class Malli2(models.Model):
    owner = models.ForeignKey(
        Profile, null=True, blank=True, on_delete=models.SET_NULL)
    muistipeli = models.ForeignKey(
        Muistipeli, on_delete=models.CASCADE, null=True)
    question = models.CharField(max_length=500, null=True, blank=True)
    answer = models.CharField(max_length=2000, null=True, blank=True)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.question
