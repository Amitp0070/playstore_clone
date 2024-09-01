from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import App, Device, Game, Book, Movie, Comment
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages

# Home view
def home_view(request):
    app_list = App.objects.order_by('-created_at')
    game_list = Game.objects.order_by('-created_at')
    book_list = Book.objects.order_by('-created_at')
    movie_list = Movie.objects.order_by('-created_at')
    device_list = Device.objects.all()
    latest_app = App.objects.order_by('-created_at')[:4]
    latest_game = Game.objects.order_by('-created_at')[:4]
    latest_book = Book.objects.order_by('-created_at')[:4]
    latest_movie = Movie.objects.order_by('-created_at')[:4]
    paginator = Paginator(app_list, 8)
    page = request.GET.get('p', 1)
    app = paginator.get_page(page)
    query = request.GET.get('q')
    if query:
        app = App.objects.filter(title__icontains=query)
        if app is None:
            app = App.objects.all()
    ctx = {
        'apps': app,
        'devices': device_list,
        'latest_app': latest_app,
        'latest_game': latest_game,
        'latest_book': latest_book,
        'latest_movie': latest_movie,
        'games': game_list,
        'books': book_list,
        'movies': movie_list,
        'item_type': 'app'  # Adjust as needed for the view
    }
    return render(request, 'playstore/home.html', ctx)

# List all games view
def game_list_view(request):
    games = Game.objects.all().order_by('-created_at')
    return render(request, 'playstore/game_list.html', {'games': games})

# List all apps view
def app_list_view(request):
    apps = App.objects.all().order_by('-created_at')
    return render(request, 'playstore/app_list.html', {'apps': apps})

# List all books view
def book_list_view(request):
    books = Book.objects.all().order_by('-created_at')
    query = request.GET.get('q')
    if query:
       book = Book.objects.filter(title=query)
    else:
       book = Book.objects.all()
    return render(request, 'playstore/book_list.html', {'books': books, 'query':query, 'book': book})

# List all movies view
def movie_list_view(request):
    movies = Movie.objects.all().order_by('-created_at')
    return render(request, 'playstore/movie_list.html', {'movies': movies})

# View apps by device
def device_apps(request, device_id):
    device = get_object_or_404(Device, id=device_id)
    apps = App.objects.filter(device=device)
    return render(request, 'playstore/app_by_device.html', {'device': device, 'apps': apps})

# Increment like
@login_required
def inc_like(request, id):
    app = get_object_or_404(App, id=id)
    app.likes += 1
    app.save()
    return redirect('detail', type='app', id=id)  # Adjusted to include type parameter

# Rate item
@login_required
def rate_item(request, type, id):
    if type == 'app':
        item = get_object_or_404(App, id=id)
    elif type == 'game':
        item = get_object_or_404(Game, id=id)
    elif type == 'book':
        item = get_object_or_404(Book, id=id)
    elif type == 'movie':
        item = get_object_or_404(Movie, id=id)
    else:
        return redirect('home')  # Handle invalid type

    if request.method == 'POST':
        rating = request.POST.get('rating')
        if rating:
            try:
                rating = int(rating)
                if rating < 1 or rating > 5:
                    raise ValueError("Rating must be between 1 and 5")
                # Update the item's rating
                item.rating = rating
                item.save()
                messages.success(request, "Rating submitted successfully!")
            except ValueError as e:
                messages.error(request, str(e))
        else:
            messages.error(request, "Rating cannot be empty!")

    return redirect('detail', type=type, id=id)

# Detail view with comment functionality
def detail_view(request, type, id):
    if type == 'app':
        item = get_object_or_404(App, id=id)
        similar_items = App.objects.filter(category=item.category).exclude(id=id)[:5]
        template_name = 'playstore/detail.html'
    elif type == 'game':
        item = get_object_or_404(Game, id=id)
        similar_items = Game.objects.filter(category=item.category).exclude(id=id)[:5]
        template_name = 'playstore/detail.html'
    elif type == 'book':
        item = get_object_or_404(Book, id=id)
        similar_items = Book.objects.filter(category=item.category).exclude(id=id)[:5]
        template_name = 'playstore/book_detail.html'
    elif type == 'movie':
        item = get_object_or_404(Movie, id=id)
        similar_items = Movie.objects.filter(category=item.category).exclude(id=id)[:5]
        template_name = 'playstore/movie_detail.html'
    else:
        return redirect('home')  # Redirect if the type is invalid

    # Handle comment and rating submission
    if request.method == 'POST' and request.user.is_authenticated:
        content = request.POST.get('comment_content')
        rating = request.POST.get('rating')
        if content and rating:
            try:
                rating = int(rating)
                if rating < 1 or rating > 5:
                    raise ValueError("Rating must be between 1 and 5")
                comment = Comment(user=request.user, content=content, rating=rating)
                if type == 'app':
                    comment.app = item
                elif type == 'game':
                    comment.game = item
                elif type == 'book':
                    comment.book = item
                elif type == 'movie':
                    comment.movie = item
                comment.save()
                messages.success(request, "Comment added successfully!")
            except ValueError as e:
                messages.error(request, str(e))
        else:
            messages.error(request, "Comment and rating cannot be empty!")
        return redirect('detail', type=type, id=id)

    comments = Comment.objects.filter(
        app=item if type == 'app' else None,
        game=item if type == 'game' else None,
        book=item if type == 'book' else None,
        movie=item if type == 'movie' else None
    ).order_by('-created_at')

    ctx = {
        'item': item,
        'similar_items': similar_items,
        'type': type,  # Pass type to the template context
        'comments': comments,  # Pass comments to the template context
    }
    return render(request, template_name, ctx)

# Delete comment view
@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user == comment.user:
        if comment.app:
            item_type = 'app'
        elif comment.game:
            item_type = 'game'
        elif comment.book:
            item_type = 'book'
        elif comment.movie:
            item_type = 'movie'
        else:
            messages.error(request, "Invalid comment.")
            return redirect('home')

        item_id = comment.app.id if comment.app else (comment.game.id if comment.game else (comment.book.id if comment.book else comment.movie.id))
        comment.delete()
        messages.success(request, "Comment deleted successfully!")
        return redirect('detail', type=item_type, id=item_id)
    else:
        messages.error(request, "You do not have permission to delete this comment.")
        return redirect('home')

# Register view
def register_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('pass')
        cpassword = request.POST.get('cpass')
        if password != cpassword or len(password) == 0 or len(cpassword) == 0:
            messages.error(request, "Passwords do not match")
            return redirect('register')
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register')
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect('register')
        user = User.objects.create_user(username, email, password)
        messages.success(request, "Account created successfully")
        return redirect('login')
    else:
        return render(request, 'accounts/register.html')

# Login view
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('pass')
        if len(username) == 0 or len(password) == 0:
            messages.error(request, "Bad Login details!")
            return redirect('login')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            messages.success(request, "Logged in successfully")
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials!")
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

# Logout view
def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('login')


