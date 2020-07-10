from django.urls import path
from water import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ranking', views.ranking, name='ranking'),
    # path('login', views.login, name='login'),
    path('graph1', views.avg_consumption_2, name='avg_consumption_2'),
    path('graph2', views.curr_week_consumption, name='curr_week_consumption'),
    path('graph3', views.season_consumption, name='season_consumption'),
    path('graph4', views.season_consumption_sunburst, name='season_consumption_sunburst'),
    path('graph5', views.weekday_consumption, name='weekday_consumption'),
]
