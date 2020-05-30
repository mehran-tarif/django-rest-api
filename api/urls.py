from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('', views.CourseView)
router.register('user', views.UserView)

urlpatterns = [
	path('v1/', include(router.urls)),
]
