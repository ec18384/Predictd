# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
import profile
from xmlrpc.client import Boolean

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))


def get_LinkedinSummary(request):
    response = ""
    if request.method == 'GET':
        try:
            driver = webdriver.Chrome('apps/home/chromedriver')

            # direct the webdriver to where the browser file is:
            # your secret credentials:
            email = "andricozach@gmail.com"
            password = ",6CWV7TKk(Rr3mJ"
            # Go to linkedin and login
            driver.get('https://www.linkedin.com/login')

            # time.sleep(.5)
            driver.find_element_by_id('username').send_keys(email)
            # time.sleep(.5)
            driver.find_element_by_id('password').send_keys(password)
            # time.sleep(.5)
            driver.find_element_by_id('password').send_keys(Keys.RETURN)
            # time.sleep(1)

            # Manual wait incase security intervention is needed
            WebDriverWait(driver, 30).until(EC.visibility_of_all_elements_located((By.ID, "global-nav")))

            # Set profileAlias
            profileAlias = request.GET.get("profileAlias")

            # Go to sign up page
            driver.get('https://www.linkedin.com/in/' + profileAlias)

            # Click see more button, if it exists
            try:
                driver.find_element_by_css_selector(".inline-show-more-text__link-container-collapsed:nth-child(3) > .inline-show-more-text__button").click()
                print("See more button was present and was clicked")
            except:
                print("See more button not present and not clicked")

            aboutText = ""
            aboutSection = driver.find_elements_by_xpath(xpath="//div[3]/div/div/div/span")

            for elements in aboutSection:
                aboutText += elements.text

            # Handle two cases, one where the profile you are viewing is another users, and another when you are viewing your own profile

            # Get profile photo url and add it to the response if profile is not for self
            try:
                driver.find_element_by_xpath(xpath="//div/div/button/img").click()
                profilePicture = driver.find_element_by_class_name("pv-member-photo-modal__profile-image")
                profileUrl = profilePicture.get_attribute("src")
                print("Extracted another users photo")
            except:
                print("Could not extract another users photo")

            # Get profile picture if user is self
            try:
                profilePicture = driver.find_element_by_class_name("profile-photo-edit__preview")
                profileUrl = profilePicture.get_attribute("src")
                print("Extracted your own photo")
            except:
                print("Could not extract your own photo")

            response = json.dumps({'summaryText': aboutText, 'profilePicUrl': profileUrl})

            # Finish test and quit driver
            driver.quit()
        except:
            response = json.dumps({'Error': 'Something went wrong with get_LinkedinSummary'})
    return HttpResponse(response, content_type='application/json')
