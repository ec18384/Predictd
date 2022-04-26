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

    # Show all past tests
    path('history.html', views.mbti_detail_view),

    # Shows MBTI related data for a given field
    path('profile.html', views.mbtiTypeResponse),

    # Run prediction
    path('predict', views.predict),

    # Send email
    path('sendEmail', views.sendEmail),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),]
