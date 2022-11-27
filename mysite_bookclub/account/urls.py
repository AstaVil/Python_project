from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('register/', views.registration_view, name="register"),
    path('logout/', views.logout_view, name="logout"),
    path('login/', views.login_view, name="login"),

    path('account/', views.account_view, name="account"),
    path('accounts/', views.accounts_list, name='accounts_list'),

    # pagrindinis view skirtingoms paskyroms
    path('dashboard', views.dashboard, name="dashboard"),
    path('teacher', views.teacher, name="teacher"),
    path('student', views.student, name="student"),

    # django auth_views privalomi path
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='register/password_change.html'), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='register/password_change_done.html'), name='password_change_done'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='register/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='register/password_reset_complete.html'), name='password_reset_complete'),
]


