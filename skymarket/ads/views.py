from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import pagination, viewsets

from ads.models import Ad, Comment
from ads.serializers import CommentSerializer

ADS_PAGE_SIZE = 4


class AdPagination(pagination.PageNumberPagination):
    page_size = ADS_PAGE_SIZE


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.select_related('author').all()
    pagination_class = AdPagination
    filter_backends = (DjangoFilterBackend)
    filterset_class = AdFilter

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update', 'retrieve']:
            return AdCreateSerializer
        else:
            return AdListSerializer

    def create(self, request, *args, **kwargs):
        request.data._mutable = True
        request.data['author'] = request.user.pk
        return super().create(request, *args, **kwargs)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = AdPagination

    def get_queryset(self):
        return Comment.objects.prefetch_related('author')\
            .filter(ad=self.kwargs['ad_pk'])

