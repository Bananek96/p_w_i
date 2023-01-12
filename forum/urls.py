from django.urls import path
from . import views

app_name = 'forum'
urlpatterns = [
	path('', views.posts_list, name='index'),
	path('<int:pk>', views.post_detail, name='post'),
	path('<int:pk>/edit/', views.post_edit, name='post_edit'),
	path('<int:pk>/answer/', views.add_answer, name="add_answer"),
	path('<int:pk>/<int:an>/', views.answer_detail, name='answer'),
	path('<int:pk>/<int:an>/edit_answer/', views.answer_edit, name="edit_answer"),
	path('<int:pk>/<int:an>/delete/', views.delete_answer, name="delete_answer"),
	path('post', views.post_new, name='new_post'),
]
