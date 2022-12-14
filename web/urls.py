
"""Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path

from . import views
urlpatterns = [
    path('', views.index, name='webindex'),
    path('about', views.about, name='webabout'),
    path('contact', views.contact, name='webcontact'),
    path('login', views.loginPage, name='weblogin'),
    path('register', views.registerPage, name='webregister'),
    re_path(r'^payment/(?P<room_id>.+)/$', views.payment, name='webpayment'),
    path('account', views.account, name='webaccount'),
    path('room', views.room, name='webroom'),
    path('booking', views.booking, name='paybooking'),
    path('paymentconfirmation', views.paymentconfirmation, name='paymentconfirmation'),
    path('logout', views.logoutUser, name='weblogout'),
    re_path(r'^verify/(?P<uidb64>.+)/(?P<token>.+)/$', views.verification, name='verification'),
    path('forgot-password', views.forgot_password, name='forgot-password'),
    path('update-password', views.update_password, name='update-password'),
]