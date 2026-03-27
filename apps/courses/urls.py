from django.urls import path

from apps.courses.apis import (
    CategoryRetriveAPIView,
    CategoryCreateAPIView,
    CategoryDeleteAPIView,
    CategoryListAPIView,
    CategoryUpdateAPIView,
    TagCreateAPIView,
    TagDeleteAPIView,
    TagListAPIView,
    TagRetriveAPIView,
    TagUpdateAPIView
)

urlpatterns = [
    path("categories/",CategoryListAPIView.as_view(),name="category-list"),
    path("category/<int:pk>",CategoryRetriveAPIView.as_view(),name="category-single"),
    path("category/update/<int:pk>",CategoryUpdateAPIView.as_view(),name="category-update"),
    path("category/delete/<int:pk>",CategoryDeleteAPIView.as_view(),name= "category-delete"),
    path("category/create/",CategoryCreateAPIView.as_view(),name="category-create"),
    path("tags/",TagListAPIView.as_view(),name="tag-list"),
    path("tag/<int:pk>",TagRetriveAPIView.as_view(),name="tag-single"),
    path("tag/update/<int:pk>",TagUpdateAPIView.as_view(),name="tag-update"),
    path("tag/delete/<int:pk>",TagDeleteAPIView.as_view(),name= "tag-delete"),
    path("tag/create/",TagCreateAPIView.as_view(),name="tag-create"),
    
]