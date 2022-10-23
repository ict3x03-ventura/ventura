
"""Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from . import views
urlpatterns = [
    path('', views.index, name='webindex'),
    path('about', views.about, name='webabout'),
    path('contact', views.contact, name='webcontact'),
    path('login', views.login, name='weblogin'),
    path('register', views.register, name='webregister'),
]