from django.conf.urls import include, url
from django.contrib import admin
from regandloginapp import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^reg/', views.reg_view),
    url(r'^$', views.login_view),
    url('r^login/', views.login_view),
]
