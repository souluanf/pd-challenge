from rest_framework.generics import ListAPIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins
from .serializers import PlaceSerializer
from .models import Place


class PlaceListFilterByName(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PlaceSerializer
    queryset = Place.objects.all()

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Place.objects.none()

        name = self.kwargs['name']
        queryset = Place.objects.filter(name=name)
        return queryset


class PlaceListFilterBySlug(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PlaceSerializer
    queryset = Place.objects.all()

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Place.objects.none()

        slug = self.kwargs['slug']
        queryset = Place.objects.filter(slug=slug)
        return queryset


class PlaceViewSet(GenericViewSet,
                   mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin):
    permission_classes = (IsAuthenticated,)
    serializer_class = PlaceSerializer
    queryset = Place.objects.all()
