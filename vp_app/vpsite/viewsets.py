from rest_framework import viewsets
from .models import Cycle, Verse
from .serializers import CycleSerializer, VerseSerializer


class CycleViewSet(viewsets.ModelViewSet):
    queryset = Cycle.objects.all()
    serializer_class = CycleSerializer


class VerseViewSet(viewsets.ModelViewSet):
    queryset = Verse.objects.all()
    serializer_class = VerseSerializer
