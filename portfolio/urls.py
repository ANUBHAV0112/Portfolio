from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from . import views
from .views import contact_view, contact_success

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', contact_view, name='contact'),
    path('contact/success/', contact_success, name='contact_success')
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)