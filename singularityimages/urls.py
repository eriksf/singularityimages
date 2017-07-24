"""todolist URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_swagger.views import get_swagger_view
from rest_framework.routers import DefaultRouter
from api.images.views import ImageViewSet


router = DefaultRouter()
router.register(r'images', ImageViewSet)
schema_view = get_swagger_view(title='Singularity Images API')


def print_url_pattern_names(patterns):
    for pat in patterns:
        if pat.__class__.__name__ == 'RegexURLResolver':
            print_url_pattern_names(pat.url_patterns)
        elif pat.__class__.__name__ == 'RegexURLPattern':
            if pat.name is not None:
                print('[API-URL] {} \t\t\t-> {}'.format(pat.name, pat.regex.pattern))


urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^docs/', schema_view),
]

# print_url_pattern_names(urlpatterns)
