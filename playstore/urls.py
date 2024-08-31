# from django.urls import path 
# from . import views

# urlpatterns = [
#     path('', views.home_view, name='home'),
#     path('apps/', views.app_list_view, name='app_list'),
#     path('games/', views.game_list_view, name='game_list'),  # New URL for games
#     path('login/', views.login_view, name='login'),
#     path('register/', views.register_view, name='register'),
#     path('logout/', views.logout_view, name='logout'),
#     # path('profile/', views.profile, name='profile'),

    
   
#     path('app/<int:id>/like', views.inc_like, name='inc_like'),
#     path('app/<int:id>/detail', views.detail_view, name='detail'),
#     path('device/<int:device_id>/', views.device_apps, name='device_app'),
#     # path('api/rate-app/<int:app_id>/', views.rate_app, name='rate_app'),
    
   
    
# ]



from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('apps/', views.app_list_view, name='app_list'),
    path('games/', views.game_list_view, name='game_list'),
    path('books/', views.book_list_view, name='book_list'),
    path('movies/', views.movie_list_view, name='movie_list'),
    path('device/<int:device_id>/', views.device_apps, name='device_app'),
    path('<str:type>/<int:id>/', views.detail_view, name='detail'),
    path('like/<int:id>/', views.inc_like, name='inc_like'),
    path('rate/<str:type>/<int:id>/', views.rate_item, name='rate_item'),  # Added for rating
    path('comment/delete/<int:comment_id>/', views.delete_comment, name='delete_comment'),  # Added for comment deletion
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
]
