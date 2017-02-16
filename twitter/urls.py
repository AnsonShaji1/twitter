from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'',views.enter_details,name='enter_details'),
]
