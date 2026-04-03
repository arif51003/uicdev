from django.urls import path
from apps.accounts.views import (
    EducationCreateAPIView,
    EducationListAPIView,
    EducationDeleteAPIView,
    EducationUpdateAPIView,
    AuthorUpdateAPIView,
    AuthorDeleteAPIView,
    AuthorListAPIView,
    AuthorRetriveAPIView,
    AuthorCreateAPIView
)

urlpatterns = [
    path("education/list",EducationListAPIView.as_view(),name = "education-list"),
    path("education/create/",EducationCreateAPIView.as_view(),name = "education-create"),
    path("education/delete/<int:pk>",EducationDeleteAPIView.as_view(),name="education-delete"),
    path("education/update/<int:pk>",EducationUpdateAPIView.as_view(),name="education-update"),
    path("author/list",AuthorListAPIView.as_view(),name="authors-list"),
    path("author/create",AuthorCreateAPIView.as_view(),name="author-create"),
    path("author/update/<int:pk>",AuthorUpdateAPIView.as_view(),name="author-update"),
    path("author/delete/<int:pk>",AuthorDeleteAPIView.as_view(),name="author-delete"),
    path("author/<int:id>/",AuthorRetriveAPIView.as_view(),name="author-single")
]
