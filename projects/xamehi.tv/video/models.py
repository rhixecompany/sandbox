from django.db import models
from django.contrib.auth.models import User


class Movies(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=500, null=False, unique=True)
    actors = models.CharField(max_length=200, blank=True, null=True)
    category = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to="movies", blank=True)
    image = models.ImageField(upload_to="movies/images", blank=True)

    createdAt = models.DateTimeField(auto_now_add=True)

    rating = models.DecimalField(
        max_digits=9, decimal_places=1, null=True, blank=True)
    likes = models.IntegerField(default=0, null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)

    class Meta:
        ordering = ['createdAt']

    def __str__(self):
        return self.name


class MoviesReview(models.Model):
    movies = models.ForeignKey(Movies, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    comment = models.TextField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    class Meta:
        ordering = ['createdAt']

    def __str__(self):
        return self.comment


class Series(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, blank=False, null=False)
    actors = models.CharField(max_length=200, blank=True, null=True)
    category = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="series/images", blank=True, )
    createdAt = models.DateTimeField(auto_now_add=True)
    rating = models.DecimalField(
        max_digits=9, decimal_places=1, null=True, blank=True)
    likes = models.IntegerField(default=0, null=True, blank=True)

    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.name


class Season(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    seriesModel = models.ForeignKey(
        Series, on_delete=models.SET_NULL, related_name='season', null=True)
    name = models.CharField(max_length=200, blank=False, null=False)
    num = models.IntegerField(default=0)
    image = models.ImageField(upload_to="series/season/images", blank=True,)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    class Meta:
        ordering = ['num']

    def __str__(self):
        return self.name


class Episode(models.Model):
    season_episode = models.ForeignKey(
        Season, on_delete=models.CASCADE, related_name='seasons')
    series_season = models.ForeignKey(
        Series, on_delete=models.SET_NULL, related_name='episodes', null=True)
    num = models.IntegerField(default=0)
    file = models.FileField(upload_to="series/episodes")

    class Meta:
        ordering = ['num']

    def __str__(self):
        return str(self.num)


class SeriesReview(models.Model):
    series = models.ForeignKey(Series, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    comment = models.TextField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    class Meta:
        ordering = ['createdAt']

    def __str__(self):
        return self.comment

from django.db import models
from django.contrib.auth.models import User


class Movies(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=500, null=False, unique=True)
    actors = models.CharField(max_length=200, blank=True, null=True)
    category = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to="movies", blank=True)
    image = models.ImageField(upload_to="movies/images", blank=True)

    createdAt = models.DateTimeField(auto_now_add=True)

    rating = models.DecimalField(
        max_digits=9, decimal_places=1, null=True, blank=True)
    likes = models.IntegerField(default=0, null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)

    class Meta:
        ordering = ['createdAt']

    def __str__(self):
        return self.name


class MoviesReview(models.Model):
    movies = models.ForeignKey(Movies, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    comment = models.TextField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    class Meta:
        ordering = ['createdAt']

    def __str__(self):
        return self.comment


class Series(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, blank=False, null=False)
    actors = models.CharField(max_length=200, blank=True, null=True)
    category = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="series/images", blank=True, )
    createdAt = models.DateTimeField(auto_now_add=True)
    rating = models.DecimalField(
        max_digits=9, decimal_places=1, null=True, blank=True)
    likes = models.IntegerField(default=0, null=True, blank=True)

    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.name


class Season(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    seriesModel = models.ForeignKey(
        Series, on_delete=models.SET_NULL, related_name='season', null=True)
    name = models.CharField(max_length=200, blank=False, null=False)
    num = models.IntegerField(default=0)
    image = models.ImageField(upload_to="series/season/images", blank=True,)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    class Meta:
        ordering = ['num']

    def __str__(self):
        return self.name


class Episode(models.Model):
    season_episode = models.ForeignKey(
        Season, on_delete=models.CASCADE, related_name='seasons')
    series_season = models.ForeignKey(
        Series, on_delete=models.SET_NULL, related_name='episodes', null=True)
    num = models.IntegerField(default=0)
    file = models.FileField(upload_to="series/episodes")

    class Meta:
        ordering = ['num']

    def __str__(self):
        return str(self.num)


class SeriesReview(models.Model):
    series = models.ForeignKey(Series, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    comment = models.TextField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    class Meta:
        ordering = ['createdAt']

    def __str__(self):
        return self.comment
