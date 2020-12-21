from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views


# Application Namespace
app_name = 'core'

# Account Patterns ('account/')
account_urls = [
    path('', views.stub)
]

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(),
         name='password_reset'),
    path('signup/', views.stub),
    path('account/', include(account_urls))
]
