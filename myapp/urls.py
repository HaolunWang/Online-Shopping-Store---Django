"""mysiteS19 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.urls import include
from myapp import views

app_name = 'myapp'

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', views.indexView.as_view(), name='index'),
    #url(r'^$', views.index,name='index'),
    #path('accounts/', include('django.contrib.auth.urls')),
    url(r'^register/$', views.register, name='register'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^login/$', views.user_login, name='login'),
    url('myapp/about',views.about,name='about'),
    #url(r'^myapp/(?P<cat_no>\d)+', views.detailView.as_view(), name='detail'),
    url(r'^myapp/(?P<cat_no>\d)+', views.detail, name='detail'),
    url('myapp/products',views.products,name='product'),
    url('myapp/place_order',views.place_order,name='place_order'),
    url(r'^myapp/products/(?P<prod_id>\d)+',views.productdetail,name='productdetail'),
    url('myapp/order_response', views.place_order, name='order_response'),
    url('^myorder/$', views.myorder, name = 'myorder'),
    ]


