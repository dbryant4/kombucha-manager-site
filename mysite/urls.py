from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers

from kombucha_manager import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'batches', views.BatchViewSet)
router.register(r'sources', views.SourceViewSet)
router.register(r'teatypes', views.TeaTypeViewSet)
router.register(r'teas', views.TeaViewSet)
router.register(r'flavors', views.FlavorViewSet)
router.register(r'bottles', views.BottleViewSet)
router.register(r'vessels', views.VesselViewSet)

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^api/v1/', include(router.urls)),
    url(r'^api/v1/auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
]
