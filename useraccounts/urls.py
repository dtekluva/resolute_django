from django.conf.urls import include, url
from useraccounts import views
from django.urls import path, include
from django.contrib.auth import views as auth_views

# urlpatterns = [
#     url(r'^$', views.indexViews,name='user-index'),
#     url(r'^user/sign-up$', views.signUpView,name='sign-up'),
#     url(r'^user/login$', views.loginView,name='login'),
#     url(r'^user/forgot-password$', views.forgotPasswordView,name='sign-up'),
#     url(r'^user/reset-password$', views.resetPasswordView,name='reset-password'),
# ]

# urlpatterns = [
#     path('register',  views.register,name='register'),
#     path('login', views.loginView, name='login'),
#     path('logout', auth_views.logout),
#  ]

urlpatterns = [
    path('mobile_register',  views.mobile_register, name='mobile_register'),
    path('mobile_signin', views.mobile_signin, name='mobile_signin'),
    path('login', views.loginView, name='login'),
    path('user', views.user, name='user'),
    path('test', views.test, name='test'),
    path('create_user', views.create_user, name='create_user'),
    path('get_users', views.get_users, name='get_users'),
    path('logout', auth_views.LogoutView.as_view(template_name="resolute/registration/login.html"), name='logout'),
    # path('logout', auth_views.logout),
]
