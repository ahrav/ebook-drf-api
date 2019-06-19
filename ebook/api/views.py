from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
    get_object_or_404,
)
from rest_framework.exceptions import ValidationError
from .permissions import IsAdminUserOrReadOnly, IsOwnerOrReadyOnly

from ..models import Ebook, Review
from .serializers import EbookSerializer, ReviewSerializer


class EbookListCreateAPIView(ListCreateAPIView):
    queryset = Ebook.objects.all().order_by("-id")
    serializer_class = EbookSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class EbookDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer


class ReviewCreateAPIView(CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        ebook_pk = self.kwargs.get("ebook_pk")
        ebook = get_object_or_404(Ebook, pk=ebook_pk)
        review_author = self.request.user
        review_queryset = Review.objects.filter(
            ebook=ebook, review_author=review_author
        )

        if review_queryset.exists():
            raise ValidationError("You have already reviewed this ebook")

        serializer.save(ebook=ebook, review_author=review_author)


class ReviewDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_class = [IsOwnerOrReadyOnly]
