from django.urls import path
from .views import register
from .views import pr_login
from .views import brandmanager_login
from .views import brandmanager_register
from .views import pragency_login
from .views import pragency_register
from .views import admin
from .views import influencer_login
from .views import influencer_callback

urlpatterns = [
    path('admin/', admin, name='admin'),
    path('pragency_register/', pragency_register, name='pragency_register'),
    path('brandmanager_register/', brandmanager_register, name='brandmanager_register'),
    path('pragency_login/', pragency_login, name='pragency_login'),
    path('brandmanager_login/', brandmanager_login, name='brandmanager_login'),
    path('influencer_login/', influencer_login, name='login'),
    path('influencer_callback/', influencer_callback, name='callback'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
