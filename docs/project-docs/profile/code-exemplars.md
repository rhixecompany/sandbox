# Code Exemplars — profile

## 1. Django Model with CKEditor

```python
from django.db import models
from ckeditor.fields import RichTextField

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = RichTextField()
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/blog/{self.slug}/"
```

## 2. Admin Customization

```python
from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "created_at"]
    list_filter = ["tags", "created_at"]
    search_fields = ["title", "content"]
    prepopulated_fields = {"slug": ("title",)}
```
