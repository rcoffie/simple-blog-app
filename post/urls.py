from django.urls import include, path

from post import views

urlpatterns = [
    path("", views.posts_list, name="posts_list"),
    path("create-post/", views.create_post, name="create_post"),
    path("<int:id>/", views.post_detail, name="post_detail"),
    path("<int:id>/update/", views.update_post, name="update_post"),
    path("<int:id>/delete/", views.delete_post, name="delete_post"),
    path("draft", views.draft, name="draft"),
    path("category/<str:category>/", views.category, name="category"),
    path("likes/<int:pk>", views.like_post, name="like_post"),
    path("search/", views.search_post, name="search_post"),
]
