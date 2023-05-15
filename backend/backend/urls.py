from django.urls import path
from .views import *
# from .views import brandmanager_login
# from .views import brandmanager_register
# from .views import pragency_login
# from .views import pragency_register
# from .views import admin
# from .views import influencer_login
# from .views import influencer_callback
urlpatterns = [
    path('admin/', views.admin, name='admin'),
    path('pragency_register/', views.pragency_register, name='pragency_register'),
    path('brandmanager_register/', views.brandmanager_register, name='brandmanager_register'),
    path('pragency_login/', views.pragency_login, name='pragency_login'),
    path('brandmanager_login/',views.brandmanager_login, name='brandmanager_login'),
    path('influencer_login/', views.influencer_login, name='login'),
    path('influencer_callback/', views.influencer_callback, name='callback'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
