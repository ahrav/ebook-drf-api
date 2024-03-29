from django.urls import path

from .views import (
    EbookListCreateAPIView,
    EbookDetailAPIView,
    ReviewCreateAPIView,
    ReviewDetailAPIView,
)

urlpatterns = [
    path("ebooks/", EbookListCreateAPIView.as_view(), name="api-ebook-list"),
    path(
        "ebooks/<int:pk>/",
        EbookDetailAPIView.as_view(),
        name="api-ebook-detail",
    ),
    path(
        "ebooks/<int:ebook_pk/review",
        ReviewCreateAPIView.as_view(),
        name="api-ebook-review",
    ),
    path(
        "reviews/<int:pk>/",
        ReviewDetailAPIView.as_view(),
        name="api-review-detail",
    ),
]
