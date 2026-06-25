<<<<<<< HEAD
from django.contrib import admin
from .models import *
# Register your models here.
admin.site.site_header = "Xamehi Tv Admin"
admin.site.site_title = "Xamehi Tv Admin Area"
admin.site.index_title = "Welcome to the Xamehi Tv admin area"


class MoviesReviewInline(admin.TabularInline):
    model = MoviesReview
    extra = 1


class MoviesAdmin(admin.ModelAdmin):

    inlines = [MoviesReviewInline]


class EpisodeInline(admin.TabularInline):
    model = Episode
    extra = 1


class SeasonInline(admin.TabularInline):
    model = Season
    extra = 1


class SeriesReviewInline(admin.TabularInline):
    model = SeriesReview
    extra = 1


class SeriesAdmin(admin.ModelAdmin):
    inlines = [SeasonInline, EpisodeInline, SeriesReviewInline]


admin.site.register(Movies, MoviesAdmin)

admin.site.register(Series, SeriesAdmin)
=======
from django.contrib import admin
from .models import *
# Register your models here.
admin.site.site_header = "Xamehi Tv Admin"
admin.site.site_title = "Xamehi Tv Admin Area"
admin.site.index_title = "Welcome to the Xamehi Tv admin area"


class MoviesReviewInline(admin.TabularInline):
    model = MoviesReview
    extra = 1


class MoviesAdmin(admin.ModelAdmin):

    inlines = [MoviesReviewInline]


class EpisodeInline(admin.TabularInline):
    model = Episode
    extra = 1


class SeasonInline(admin.TabularInline):
    model = Season
    extra = 1


class SeriesReviewInline(admin.TabularInline):
    model = SeriesReview
    extra = 1


class SeriesAdmin(admin.ModelAdmin):
    inlines = [SeasonInline, EpisodeInline, SeriesReviewInline]


admin.site.register(Movies, MoviesAdmin)

admin.site.register(Series, SeriesAdmin)
>>>>>>> 6031d8f (chore: initial local project setup for xamehi.tv)
