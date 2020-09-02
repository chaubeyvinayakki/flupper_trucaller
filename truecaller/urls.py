from django.urls import path
from .views import *

app_name = 'truecaller'

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register-user'),
    path('mark-spam/', MarkSpam.as_view(), name='mark-spam'),
    path('log-in/', LogIn.as_view(), name='log-in'),
    path('name-search/', NameSearch.as_view(), name='name-search'),
    path('phone-search/', PhoneSearch.as_view(), name='name-search'),
]
