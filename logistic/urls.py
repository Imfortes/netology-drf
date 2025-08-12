from rest_framework.routers import DefaultRouter

from logistic.views import ProductViewSet, StockViewSet

# Регистрируем ViewSet для пустой страницы
# router.register('', IndexView, basename='index')

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('stocks', StockViewSet)

urlpatterns = router.urls