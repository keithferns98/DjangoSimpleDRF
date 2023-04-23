from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("postviewsets", views.PostViewSet, basename='postviewsets')
urlpatterns = [
    path('homepage/', views.homepage, name='post_homepage'),
    # path('list_posts/', views.list_posts, name="list_posts"),
    # path('<int:post_id>/', views.get_details, name="index_details"),
    # path("update/<int:post_id>/", views.update_post, name='update_post'),
    # path('delete/<int:post_id>/', views.delete_post, name="delete_post"),
    path('list_posts/', views.PostListCreateView.as_view(), name='list_view'),
    path('<int:pk>/', views.PostRetrieveUpdateDeleteView.as_view(),
         name="post_details"),
    path('', include(router.urls))
]
