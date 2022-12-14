from django.urls import path
from . import views

app_name = 'forum'
urlpatterns = [
	path('', views.posts_list, name='index'),
	path('<int:pk>', views.post_detail, name='post'),
	path('<int:pk>/edit/', views.post_edit, name='post_edit'),
	path('<int:pk>/answer/', views.add_answer, name="add_answer"),
	path('delete/<int:an>', views.delete_answer, name="delete_answer"),
	path('post', views.post_new, name='new_post'),
]
