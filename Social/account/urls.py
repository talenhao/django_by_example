# url+view
from django.conf.urls import url
from . import views

# use django.contrib.auth.views
from django.contrib.auth.views import login, logout, logout_then_login, password_change, password_change_done


urlpatterns = [
    # url(r'^login/$', views.user_login, name='user_login'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^logout-then-login/$', logout_then_login, name='logout_then_login'),
    url(r'^$', views.dashboard, name='dashboard'),
    # change password
    # templates/registration/password_change_form.html
    url(r'^password-change/$', password_change, name='password_change'),
    # templates/registration/password_change_done.html
    url(r'^password-change/done/$', password_change_done, name='password_change_done'),
]