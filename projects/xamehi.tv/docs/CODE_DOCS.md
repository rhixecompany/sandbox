# Xamehi TV — Code Documentation

## Overview

Xamehi TV is a Django-based video streaming platform with React frontend. Features video/series catalog, user authentication, comments, admin CRUD, MongoDB integration for analytics, and email notifications. Combines Django template views with DRF API endpoints.

**Stack:** Django 4.x | Django REST Framework | React 18 | Redux | PostgreSQL | MongoDB | Bootstrap 5  
**Status:** Active Development

---

## 1. Models Layer

**File:** `video/models.py`

### Movies Model

```python
class Movies(models.Model):
    """Individual movie/video entry.

    Represents a single video with metadata, file upload, and social features.

    Attributes:
        user: FK to User who uploaded/created the entry.
        name: Unique movie title (max 500 chars).
        actors: Comma-separated actor names (optional).
        category: Genre/category classification (optional).
        description: Full movie synopsis (optional).
        file: Uploaded video file (stored under 'movies/').
        image: Poster/thumbnail image (stored under 'movies/images/').
        createdAt: Auto-set timestamp on creation.
        rating: Decimal rating value (max 9 digits, 1 decimal place).
        likes: Integer count of likes.
        _id: Auto-increment primary key (overrides default id).
    """
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=500, null=False, unique=True)
    actors = models.CharField(max_length=200, blank=True, null=True)
    category = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    file = models.FileField(upload_to="movies", blank=True)
    image = models.ImageField(upload_to="movies/images", blank=True)

    createdAt = models.DateTimeField(auto_now_add=True)
    rating = models.DecimalField(max_digits=9, decimal_places=1, null=True, blank=True)
    likes = models.IntegerField(default=0, null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)

    class Meta:
        ordering = ['createdAt']

    def __str__(self) -> str:
        return self.name
```

### MoviesReview Model

```python
class MoviesReview(models.Model):
    """User review/comment on a movie.

    Attributes:
        movies: FK to the reviewed Movie (SET_NULL on delete).
        user: FK to the reviewing User (SET_NULL on delete).
        comment: Review text content.
        createdAt: Auto-set timestamp.
        _id: Auto-increment primary key.
    """
    movies = models.ForeignKey(Movies, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    comment = models.TextField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    class Meta:
        ordering = ['createdAt']

    def __str__(self) -> str:
        return str(self.comment)[:50]
```

### Series Model

```python
class Series(models.Model):
    """TV series/collection model.

    Groups multiple Seasons and Episodes under a single series entry.

    Attributes:
        user: FK to creating User.
        name: Series title (max 200 chars).
        actors: Comma-separated actor names.
        category: Genre classification.
        description: Series synopsis.
        image: Series poster/thumbnail.
        createdAt: Auto-set creation timestamp.
        rating: Average rating.
        likes: Like count.
        _id: Auto-increment primary key.
    """
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200, blank=False, null=False)
    actors = models.CharField(max_length=200, blank=True, null=True)
    category = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="series/images", blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    rating = models.DecimalField(max_digits=9, decimal_places=1, null=True, blank=True)
    likes = models.IntegerField(default=0, null=True, blank=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self) -> str:
        return self.name
```

### Season Model

```python
class Season(models.Model):
    """Season grouping within a Series.

    Ordered by season number, contains multiple Episodes.

    Attributes:
        user: FK to creating User.
        seriesModel: FK to parent Series (related_name='season').
        name: Season title (e.g., "Season 1").
        num: Sequential season number.
        image: Season-specific thumbnail.
        createdAt: Auto-set timestamp.
        _id: Auto-increment primary key.
    """
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    seriesModel = models.ForeignKey(Series, on_delete=models.SET_NULL, related_name='season', null=True)
    name = models.CharField(max_length=200)
    num = models.IntegerField(default=0)
    image = models.ImageField(upload_to="series/season/images", blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    class Meta:
        ordering = ['num']

    def __str__(self) -> str:
        return f"{self.seriesModel.name} - {self.name}"
```

### Episode Model

```python
class Episode(models.Model):
    """Individual episode within a Season.

    Contains the actual video file for streaming.

    Attributes:
        season_episode: FK to parent Season (CASCADE delete).
        series_season: FK to parent Series (related_name='episodes').
        num: Sequential episode number within the season.
        file: Uploaded episode video file (stored under 'series/episodes/').
    """
    season_episode = models.ForeignKey(Season, on_delete=models.CASCADE, related_name='seasons')
    series_season = models.ForeignKey(Series, on_delete=models.SET_NULL, related_name='episodes', null=True)
    num = models.IntegerField(default=0)
    file = models.FileField(upload_to="series/episodes")

    class Meta:
        ordering = ['num']

    def __str__(self) -> str:
        return f"Episode {self.num}"
```

### ER Diagram (Key Relationships)

```
User
  ├── Movies (created_by)
  ├── Series (created_by)
  ├── Season (created_by)
  ├── MoviesReview (author)
  └── SeriesReview (author)

Series
  ├── Season (1:N via seriesModel FK)
  │     └── Episode (1:N via season_episode FK)
  └── Episode (also via series_season FK)

Movies
  └── MoviesReview (1:N via movies FK)
```

---

## 2. Views Layer

### Template Views

**File:** `video/view.py`

| Function | Route | Description |
|----------|-------|-------------|
| `index()` | `/` | Homepage — featured movies (active, featured, limit 3) |
| `movies()` | `/movies/` | Paginated movie list (5/page) with `MoviesFilter` |
| `movie()` | `/<slug:slug>/` | Movie detail with comment form |
| `sendEmail()` | `/send_email/` | Contact form → email via Gmail SMTP |
| `loginPage()` | `/login/` | Email-based login (looks up User by email) |
| `registerPage()` | `/register/` | User registration with `CustomUserCreationForm` |
| `logoutUser()` | `/logout/` | Session logout |
| `createMovie()` | `/create_movie/` | Admin: create movie with `MoviesForm` |
| `updateMovie()` | `/<slug:slug>/update/` | Admin: update movie |
| `deleteMovie()` | `/<slug:slug>/delete/` | Admin: delete movie with confirmation |
| `userAccount()` | `/account/` | User profile page |
| `updateProfile()` | `/update_profile/` | Edit profile form |

**Auth Pattern:** `@admin_only` decorator + `@login_required` for CRUD views.

### REST API Views

**Files:** `video/views/movies_views.py`, `video/views/series_views.py`, `video/views/user_views.py`

#### Movies API

| Endpoint | Method | Auth | Description |
|----------|--------|------|-------------|
| `getMovies()` | GET /api/movies/ | Public | Paginated list with keyword search, 5/page |
| `getTopMovies()` | GET /api/movies/top/ | Public | Top 5 rated movies (rating >= 4) |
| `getMovie()` | GET /api/movies/:pk/ | Public | Single movie detail |
| `createMovie()` | POST /api/movies/ | Admin | Create sample movie |
| `updateMovie()` | PUT /api/movies/:pk/ | Admin | Update movie fields |
| `deleteMovie()` | DELETE /api/movies/:pk/ | Admin | Delete movie |
| `uploadFile()` | POST /api/upload/ | Auth | Upload video file to movie |

#### Series API

| Endpoint | Method | Auth | Description |
|----------|--------|------|-------------|
| `getSeries()` | GET /api/series/ | Public | Paginated list with keyword search |
| `getTopSeries()` | GET /api/series/top/ | Public | Top 5 rated series |
| `getSerie()` | GET /api/series/:pk/ | Public | Single series detail |
| `createSeries()` | POST /api/series/ | Admin | Create sample series |
| `updateSeries()` | PUT /api/series/:pk/ | Admin | Update series fields |
| `deleteSeries()` | DELETE /api/series/:pk/ | Admin | Delete series |
| `uploadImage()` | POST /api/series/upload/ | Admin | Upload series image |

#### User API

| Endpoint | Method | Auth | Description |
|----------|--------|------|-------------|
| `loginUser()` | POST /api/users/login/ | Public | JWT token login |
| `getUserProfile()` | GET /api/users/profile/ | Auth | Get profile |
| `registerUser()` | POST /api/users/register/ | Public | Register new user |
| `updateUserProfile()` | PUT /api/users/profile/update/ | Auth | Update profile |
| `getUsers()` | GET /api/users/ | Admin | List all users |
| `getUserById()` | GET /api/users/:pk/ | Admin | Get user detail |
| `updateUser()` | PUT /api/users/:pk/update/ | Admin | Update user (admin) |
| `deleteUser()` | DELETE /api/users/:pk/delete/ | Admin | Delete user |

---

## 3. Serializers Layer

**File:** `video/serializers.py`

```python
class UserSerializer(serializers.ModelSerializer):
    """Serialize User model with computed fields.

    Custom fields:
        name: Returns first_name or falls back to email.
        _id: Exposes Django's internal id as _id.
        isAdmin: Maps to is_staff.
    """
    name = serializers.SerializerMethodField()
    _id = serializers.SerializerMethodField()
    isAdmin = serializers.SerializerMethodField()

class UserSerializerWithToken(UserSerializer):
    """Extends UserSerializer with JWT access token."""
    token = serializers.SerializerMethodField()

class MoviesSerializer(serializers.ModelSerializer):
    """Full movie serialization with all fields."""
    class Meta:
        model = Movies
        fields = '__all__'

class SeriesSerializer(serializers.ModelSerializer):
    """Series serialization with nested episodes."""
    episodes = serializers.StringRelatedField(many=True)
    class Meta:
        model = Series
        fields = ['_id', 'name', 'actors', 'category', 'description', 'image', 'createdAt', 'rating', 'likes', 'episodes']
```

---

## 4. MongoDB Integration

**File:** `video/pymongo_views.py`

```python
import pymongo

# MongoDB Atlas connection
client = pymongo.MongoClient(
    'mongodb+srv://bot:Rhixe&company%401@rhixecompany.ejlsb.mongodb.net/test'
)

dbname = client['xamehitv']
collection = dbname['movies']
```

**Note:** Connection string contains inline credentials — must be moved to environment variables.

**Usage:** MongoDB is used for analytics/activity logging alongside PostgreSQL. The `movies` collection stores movie metadata for fast read access.

---

## 5. URL Configuration

**File:** `video/url.py`

```python
urlpatterns = [
    path('', views.index, name='index'),
    path('movies/', views.movies, name='movies'),
    path('movies/<slug:slug>/', views.movie, name='movie'),
    path('send_email/', views.sendEmail, name="send_email"),
    path('login/', views.loginPage, name="login"),
    path('register/', views.registerPage, name="register"),
    path('logout/', views.logoutUser, name="logout"),
    path('account/', views.userAccount, name="account"),
    path('update_profile/', views.updateProfile, name="update_profile"),
    # CRUD
    path('create_movie/', views.createMovie, name="create_movie"),
    path('update_movie/<slug:slug>/', views.updateMovie, name="update_movie"),
    path('delete_movie/<slug:slug>/', views.deleteMovie, name="delete_movie"),
]
```

Additional routing files in `video/urls/`:
- `movies_urls.py` — REST API movie endpoints
- `series_urls.py` — REST API series endpoints
- `user_urls.py` — REST API auth/user endpoints

---

## 6. Filters & Forms

**Filters:** `video/filters.py`

```python
class MoviesFilter(django_filters.FilterSet):
    """Filter movies by category, name search, and rating range."""
    class Meta:
        model = Movies
        fields = ['category', 'name', 'rating']

class SeriesFilter(django_filters.FilterSet):
    """Filter series by category and rating."""
    class Meta:
        model = Series
        fields = ['category', 'rating']
```

**Forms:** `video/forms.py`
- `MoviesForm` — Movie create/edit form with file upload
- `SeriesForm` — Series create/edit form
- `CustomUserCreationForm` — Registration with email
- `ProfileForm` — User profile editing
- `UserForm` — User details form

---

## 7. Decorators

**File:** `video/decorators.py`

```python
from django.http import HttpResponse
from django.shortcuts import redirect

def admin_only(view_func):
    """Restrict view access to admin users only.

    Redirects non-admin users to the index page.
    """
    def wrapper(request, *args, **kwargs):
        if request.user.is_staff:
            return view_func(request, *args, **kwargs)
        return redirect('index')
    return wrapper
```

---

## 8. React Frontend

**File:** `frontend/src/`

### State Management (Redux)

```
store.js → Root reducer combining:
  ├── movieReducers    → movies, topMovies, movie details
  ├── seriesReducers   → series, topSeries, series details
  └── userReducers     → user login, register, profile
```

### Key Screens

| Screen | Route | Data Source |
|--------|-------|-------------|
| HomeScreen | `/` | Latest movies, top movies, top series |
| MovieScreen | `/movie/:id` | Single movie with reviews |
| MoviesScreen | `/movies` | Paginated movie list |
| SerieScreen | `/serie/:id` | Single series with episodes |
| SeriesScreen | `/series` | Paginated series list |
| LoginScreen | `/login` | JWT authentication |
| RegisterScreen | `/register` | User registration |
| ProfileScreen | `/profile` | User profile |
| UserListScreen | `/admin/users` | Admin user management |
| MoviesEditScreen | `/admin/movies/:id/edit` | Movie editing |
| MoviesListScreen | `/admin/movies` | Admin movie list |
| SeriesListScreen | `/admin/series` | Admin series list |
