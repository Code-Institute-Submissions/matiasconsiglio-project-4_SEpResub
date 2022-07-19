from . import views
from django.urls import path

urlpatterns = [
    path("", views.EventList.as_view(), name="home"),
    path(
     'delete_comment/<int:comment_id>',
     views.delete_comment, name='delete_comment'
     ),
    path('<slug:slug>/', views.EventDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path(
     'update_comment/<int:pk>',
     views.UpdateComment.as_view(), name='update_comment'
    ),
]
