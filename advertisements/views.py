from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from .models import Advertisement
from .serializers import AdvertisementSerializer
from .filters import AdvertisementFilter
from .permissions import IsOwnerOrReadOnly, IsNotDraftForOthers


# TODO: настройте ViewSet, укажите атрибуты для кверисета,
#   сериализаторов и фильтров


class AdvertisementViewSet(viewsets.ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = AdvertisementFilter
    throttle_classes = [UserRateThrottle, AnonRateThrottle]

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsOwnerOrReadOnly()]
        return []

    def perform_create(self, serializer):
        # Проверка на 10 открытых объявлений
        open_ads = Advertisement.objects.filter(
            creator=self.request.user,
            status=Advertisement.STATUS_OPEN
        ).count()

        if open_ads >= 10:
            raise serializers.ValidationError("Нельзя иметь больше 10 открытых объявлений")

        serializer.save(creator=self.request.user)

    # Для дополнительного задания (избранное)
    @action(detail=True, methods=['post'])
    def favorite(self, request, pk=None):
        ad = self.get_object()
        if ad.creator == request.user:
            return Response(
                {"error": "Нельзя добавлять свои объявления в избранное"},
                status=status.HTTP_400_BAD_REQUEST
            )
        # Логика добавления в избранное
        return Response({"status": "ok"})


