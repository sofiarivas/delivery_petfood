from django.conf.urls import url
from django.contrib import admin
from login import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'login/$', 
	views.LoginView.as_view(),
    	name='login'
    	),

]
