"""

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

'''
    The urlpatterns variable in the site (not the app) is a list of paths (or endpoints)
    and the files that resolve them.
    for example, the root path (http://127.0.0.1:8000) 
    is resolved by the urls.py file in the "home" app.
'''

urlpatterns = [
    path("admin/", admin.site.urls),
    
    # Make sure all urlpatterns specified in home.urls file are available at the root.
    path('', include('home.urls')),
    
    # Make sure all urlpatterns specified in notes.urls file are available at root/smart
    path('products/',include('traders.urls')), 
]

if settings.DEBUG:  # Only add this when in debug mode
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
