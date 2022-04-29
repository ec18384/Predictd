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

    # Shows data relevant to redirect profile
    path('profileRedirect.html', views.profileRedirect),

    # Run prediction
    path('predict', views.predict),

    # HR View Data
    path('HR-Editor.html', views.getUsers),

    # Team Head View Data
    path('TH-Editor.html', views.getUsersForLMView),

    # Send email
    path('sendEmail', views.sendEmail),

    # Add a new user
    path('new_user/', views.new_user, name='new_user'),

    # Update user
    path('update_user/', views.update_user, name='update_user'),

    # Release user
    path('releaseUser', views.releaseUser),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'), ]
