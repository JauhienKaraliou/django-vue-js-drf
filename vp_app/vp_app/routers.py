from rest_framework import routers
from vpsite.viewsets import CycleViewSet, VerseViewSet


router = routers.DefaultRouter()
router.register(r'cycle', CycleViewSet)
router.register(r'verse', VerseViewSet)
