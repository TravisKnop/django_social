from django.db import models
from django.core.validators import RegexValidator
import(django_social)

__author__ = 'travisknop'


class Name(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    username = models.CharField(max_length=20)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'."
                                         " Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], blank=True)
    sex = models.CharField(max_length=10)
    bio = models.CharField(max_length=500)
    number_followers = Followers.followers.count()
    number_following = Following.following.count()

    def __str__(self):
        return self.name


class Gram(models.Model):
    author = models.ForeignKey(Name)
    entry = models.FileField()
    caption = models.CharField(max_length=500)
    gram_datetime = models.DateTimeField(auto_now=True)
    number_of_likes = Like.liked_gram.count()


class Like(models.Model):
    liked_gram = models.ForeignKey(Gram)
    liker = models.ForeignKey(Name)
    like_datetime = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    commented_post = models.ForeignKey(Gram)
    commenter = models.ForeignKey(Name)
    comment = models.CharField(max_length=500)
    comment_datetime = models.DateTimeField(auto_now=True)


class Followers(models.Model):
    follower = models.ForeignKey(Name)

    def __str__(self):
        return self.follower


class Following(models.Model):
    following = models.ForeignKey(Name)

    def __str__(self):
        return self.following

class Test(models.Model):
    def testname(self):
        print("hi?")





