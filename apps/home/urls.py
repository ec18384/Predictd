# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    # Summary endpoint
    path('getSummary', views.get_LinkedinSummary),

    # MBTI Test List endpoint
    path('getAllMBTITests', views.get_MBTITestsJsonList),

    # MBTI Current User Test List endpoint
    path('getCurrentUsersMBTITests', views.get_CurrentUsersMBTITestsJsonList),

    path('history.html', views.mbti_detail_view),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),]
