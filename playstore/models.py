from django.db import models
from django.contrib.auth.models import User

class Device(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class App(models.Model):
    title = models.CharField("App title", max_length=100)
    image = models.ImageField("App image", upload_to="apps/images")
    content = models.CharField(max_length=200)
    description = models.TextField("App description", max_length=200, default=0)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    rating = models.FloatField(default=0)  # Average rating
    rating_count = models.IntegerField(default=0)  # Number of ratings
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    video_file = models.FileField("Video file", upload_to="apps/videos", default=0)
    likes = models.PositiveIntegerField("Total likes", default=0)
    category = models.CharField("Category", max_length=50, blank=True)  # Added category field

    def update_rating(self, new_rating):
        total_rating = self.rating * self.rating_count
        self.rating_count += 1
        total_rating += new_rating
        self.rating = total_rating / self.rating_count
        self.save()

    def __str__(self):
        return self.title

class Game(models.Model):
    title = models.CharField("Game title", max_length=100)
    image = models.ImageField("Game image", upload_to="games/images")
    content = models.CharField(max_length=200)
    description = models.TextField("Game description", max_length=200, default=0)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    rating = models.FloatField(default=0)  # Average rating
    rating_count = models.IntegerField(default=0)  # Number of ratings
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    video_file = models.FileField("Video file", upload_to="games/videos")
    thumbnail = models.ImageField(upload_to='games/thumbnails/', blank=True, null=True, default='default_thumbnail.jpg')
    likes = models.PositiveIntegerField("Total likes", default=0)
    category = models.CharField("Category", max_length=50, blank=True)  # Added category field

    def update_rating(self, new_rating):
        total_rating = self.rating * self.rating_count
        self.rating_count += 1
        total_rating += new_rating
        self.rating = total_rating / self.rating_count
        self.save()

    def __str__(self):
        return self.title

class Book(models.Model):
    title = models.CharField("Book title", max_length=100)
    image = models.ImageField("Book cover image", upload_to="books/images")
    content = models.TextField("Book content", max_length=500)
    author_name = models.CharField("Author name", max_length=100)
    created_at = models.DateTimeField(auto_now=True)
    rating = models.FloatField(default=0)  # Average rating
    rating_count = models.IntegerField(default=0)  # Number of ratings
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.PositiveIntegerField("Total likes", default=0)
    price = models.DecimalField("Price", max_digits=10, decimal_places=2, default=0.0)  # Price field
    category = models.CharField("Category", max_length=50, blank=True)  # Added category field

    def update_rating(self, new_rating):
        total_rating = self.rating * self.rating_count
        self.rating_count += 1
        total_rating += new_rating
        self.rating = total_rating / self.rating_count
        self.save()

    def __str__(self):
        return self.title

class Movie(models.Model):
    title = models.CharField("Movie title", max_length=100)
    image = models.ImageField("Movie poster image", upload_to="movies/images")
    content = models.TextField("Movie content", max_length=200)
    description = models.TextField("Movie description", max_length=200, default=0)
    director_name = models.CharField("Director name", max_length=100)
    created_at = models.DateTimeField(auto_now=True)
    rating = models.FloatField(default=0)  # Average rating
    rating_count = models.IntegerField(default=0)  # Number of ratings
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video_file = models.FileField("Video file", upload_to="movies/videos")
    likes = models.PositiveIntegerField("Total likes", default=0)
    price = models.DecimalField("Price", max_digits=10, decimal_places=2, default=0.0)  # Price field
    category = models.CharField("Category", max_length=50, blank=True)  # Added category field

    def update_rating(self, new_rating):
        total_rating = self.rating * self.rating_count
        self.rating_count += 1
        total_rating += new_rating
        self.rating = total_rating / self.rating_count
        self.save()

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField("Comment content")
    created_at = models.DateTimeField(auto_now_add=True)
    app = models.ForeignKey(App, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='comments', null=True, blank=True)
    rating = models.PositiveIntegerField(default=0)  # Add rating field
    
    def __str__(self):
        return f'Comment by {self.user.username} on {self.created_at}'
