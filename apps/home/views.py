# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
import time
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


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
            password = "***REMOVED***"
            # Go to linkedin and login
            driver.get('https://www.linkedin.com/login')
            # time.sleep(.5)
            driver.find_element_by_id('username').send_keys(email)
            # time.sleep(.5)
            driver.find_element_by_id('password').send_keys(password)
            # time.sleep(.5)
            driver.find_element_by_id('password').send_keys(Keys.RETURN)
            # time.sleep(1)

            # Go to sign up page
            driver.get('https://www.linkedin.com/in/' + request.GET.get("profileAlias"))
            time.sleep(3)

            aboutSection = driver.find_element_by_class_name("pv-shared-text-with-see-more").text
            print(aboutSection)

            response = aboutSection

            # Finish test and quit driver
            driver.quit()
        except:
            response = json.dumps([{'Error': 'Something went wrong with get_LinkedinSummary'}])
    return HttpResponse(response, content_type='text/json')
