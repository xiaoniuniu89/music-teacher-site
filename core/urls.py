from django.contrib import admin
from django.urls import path, include
from .views import landing, load_login_form, load_register_form

urlpatterns = [
    path("", landing, name="landing"),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('dashboard/', include('dashboard.urls')),
]

htmx_urlpatterns = [
    path('load-login-form/', load_login_form, name="load_login_form"),
    path('load-reg-form/', load_register_form, name="load_register_form"),
]

urlpatterns += htmx_urlpatterns