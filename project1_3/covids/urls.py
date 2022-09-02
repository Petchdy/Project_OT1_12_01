from django.urls import path
from . import views

app_name = 'covids'
urlpatterns = [
    path('', views.main, name='main'),
    # path('user_info/', views.user_info, name='user_info'),
    path('compare_sentiment/', views.compare_sentiment, name='compare_sentiment'),
    path('compare_types/', views.compare_types, name='compare_types'),
    path('compare_level/', views.compare_levels, name='compare_levels'),
    # month
    path('January/', views.January, name='January'),
    path('February/', views.February, name='February'),
    path('March/', views.March, name='March'),
    path('April/', views.April, name='April'),
    path('May/', views.May, name='May'),
    path('June/', views.June, name='June'),
    path('July/', views.July, name='July'),
    path('August/', views.August, name='August'),   
    path('September/', views.September, name='September'),   
    path('October/', views.October, name='October'),
    path('November/', views.November, name='November'),
    path('December/', views.December, name='December'),
    path('Contract/', views.Contract, name='Contract'),
]   

