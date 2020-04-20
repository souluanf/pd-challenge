from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path, include, re_path
from pdchallenge.views import ReadMeView
from place.views import PlaceListFilterByName, PlaceListFilterBySlug, PlaceViewSet


schema_view = get_schema_view(
    openapi.Info(
        title="PLAND Test :: By Luan 2020",
        default_version='v1',
        description="""The test consists of building a REST API to create, edit , list and filter places by name.

      Test and know the endpoints in the "place" and documentation below. 
      """,
        contact=openapi.Contact(email="souluan@live.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register('places', PlaceViewSet, basename='places')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(template_name='place/login3.html'), name='login'),
    path('', ReadMeView.as_view(), name='home'),
    path('readme/', ReadMeView.as_view(), name='readme'),
    path('api/auth/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('api/v1.0/', include((router.urls, 'api-root'), namespace='api-root')),
    path('api/v1.0/places/search/name/<str:name>', PlaceListFilterByName.as_view(), name='search-name'),
    path('api/v1.0/places/search/slug/<str:slug>', PlaceListFilterBySlug.as_view(), name='search-slug'),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

admin.site.site_header = "PlanD Python Test Admin"
admin.site.site_title = "PlanD Python Test Admin Portal"
admin.site.index_title = "Welcome to PlanD Test"
