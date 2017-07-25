from django.conf.urls import include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # Examples:
    # url(r'^$', 'Social.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^account/', include('account.urls')),
    url(r'social-auth/', include('social.apps.django_app.urls', namespace='social')),
    url(r'^images/', include('images.urls', namespace="images")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          docment_root = settings.MEDIA_ROOT)
