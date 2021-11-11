from django.urls import path
from .renderers import UserJSONRenderer
from .views import RegistrationAPIView, LoginAPIView
renderer_classes = (UserJSONRenderer,)

app_name = 'authentication'
urlpatterns = [
    path('users/', RegistrationAPIView.as_view()),
    path('users/login/', LoginAPIView.as_view()),
]