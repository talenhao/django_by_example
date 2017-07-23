# url+view
from django.conf.urls import url
from . import views

# use django.contrib.auth.views
from django.contrib.auth.views import login, logout, logout_then_login, password_change, password_change_done, \
    password_reset, password_reset_done, password_reset_confirm, password_reset_complete


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

    # password reset confirm
    # templates/registration/password_reset_form.html
    url(r'^password-reset/$', password_reset, name='password_reset'),
    # templates/registration/password_reset_done.html and password_reset_email.html
    url(r'^password-reset/done/$', password_reset_done, name='password_reset_done'),
    # templates/registration/password_reset_confirm.html
    url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', password_reset_confirm,
        name='password_reset_confirm'),
    # templates/registration/password_reset_complete.html
    url(r'^password-reset/complate/$', password_reset_complete, name='password_reset_complete'),

    # register
    url(r'^register/$', views.register, name='register'),
]