# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import json

import null as null
import requests
from django import template
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.db.models import Avg
from django.http import HttpResponse, HttpResponseRedirect, QueryDict, JsonResponse
from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from django.utils.html import format_html
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from core import settings
from .models import *


# Program to find most frequent
# element in a list
def most_frequent(List):
    return max(set(List), key=List.count)


@login_required(login_url="/login/")
def index(request):
    totalUsers = User.objects.count()
    totalTestsRan = MBTITest.objects.count()
    averageTestAccuracy = MBTITest.objects.aggregate(Avg("probability"))
    averageTestAccuracy = averageTestAccuracy["probability__avg"]
    averageTestAccuracy = "{:.2f}".format(averageTestAccuracy)
    typeOccurrenceList = list(MBTITest.objects.all().values_list('type', flat=True))
    mostCommonType = most_frequent(typeOccurrenceList)

    context = {'segment': 'index',
               "totalUsers": totalUsers,
               "totalTestsRan": totalTestsRan,
               "averageTestAccuracy": averageTestAccuracy,
               "mostCommonType": mostCommonType}

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


@login_required(login_url="/login/")
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

            # Go to users profile
            driver.get('https://www.linkedin.com/in/' + profileAlias)

            # Extract full name
            target = driver.find_element_by_xpath(xpath="//h1").text

            # Click see more button, if it exists
            try:
                driver.find_element_by_css_selector(
                    ".inline-show-more-text__link-container-collapsed:nth-child(3) > .inline-show-more-text__button").click()
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

            response = json.dumps({'summary': aboutText, 'profilePicUrl': profileUrl, 'target': target})

            # Finish test and quit driver
            driver.quit()
        except:
            response = json.dumps({'Error': 'Something went wrong with get_LinkedinSummary'})
    return HttpResponse(response, content_type='application/json')


@login_required(login_url="/login/")
def mbti_detail_view(request):
    allMBTITests = MBTITest.objects.all().order_by('-date')
    context = {
        'segment': 'history',
        "allMBTITests": allMBTITests,
    }

    return render(request, 'home/history.html', context)


# Run external API prediction request
@login_required(login_url="/login/")
def predict(request):
    # Get input to run test on
    input = str(request.GET.get("input"))
    target = str(request.GET.get("target"))
    profilePicUrl = str(request.GET.get("profilePicUrl"))
    ownProfile = str(request.GET.get("ownProfile"))

    # Get request from prediction classifier endpoint
    requestUrl = "https://25rbpvhg52gkmpg7.anvil.app/_/private_api/7NQCNJNTZ7OKFGT7FTKDWVPT/prediction"
    response = requests.get(requestUrl, params={"input": input, "target": target, "profilePicUrl": profilePicUrl})

    # Sample output
    print(response.text)

    # Convert to JSON
    responseDict = json.loads(response.text)

    # Creat and store test object
    test_obj = MBTITest(target=responseDict["target"],
                        input=input,
                        date=responseDict["date"],
                        type=responseDict["type"],
                        IvsE=responseDict["IvsE"],
                        IvsS=responseDict["IvsS"],
                        TvsF=responseDict["TvsF"],
                        JvsP=responseDict["JvsP"],
                        probability=responseDict["probability"],
                        profile_picture_url=responseDict["profilePicUrl"],
                        initiator_id=request.user.id)

    if test_obj != null:
        test_obj.save()
        print("Stored new test object")

    # Check if user said this was their own profile, then we update their profile accordingly with the test result
    if ownProfile == "true":
        print("Updating users own profile")
        user = User.objects.get(pk=request.user.id)
        user.profile.testResult_id = test_obj.id
        user.save()

    responseJson = json.dumps({
        "type": responseDict["type"],
        "IvsE": responseDict["IvsE"],
        "IvsS": responseDict["IvsS"],
        "TvsF": responseDict["TvsF"],
        "JvsP": responseDict["JvsP"],
        "probability": responseDict["probability"],
        "IP Address": responseDict["IP Address"],
        "target": responseDict["target"],
        "date": responseDict["date"],
        "profilePicUrl": responseDict["profilePicUrl"]})

    print(responseJson)

    return HttpResponse(responseJson, content_type='application/json')


@login_required(login_url="/login/")
def mbtiTypeResponse(request):
    print(request.GET.get("type"))
    type = request.GET.get("type")

    mbtiTypeData = mbtiModel.objects.get(typeName=type)
    context = {
        'segment': 'profile',
        "mbtiTypeData": mbtiTypeData,
    }

    return render(request, 'home/profile.html', context)


@login_required(login_url="/login/")
def profileRedirect(request):
    userId = request.user.id
    userData = User.objects.get(pk=userId)

    testId = userData.profile.testResult_id

    if testId:
        test = MBTITest.objects.get(pk=testId)

        context = {
            "test": test,
        }

        return render(request, 'home/profileRedirect.html', context)
    else:
        return HttpResponseRedirect('classify-user.html')


@login_required(login_url="/login/")
def getUsers(request):
    users = User.objects.all().order_by('-last_login')
    context = {
        'segment': 'hreditor',
        "users": users,
    }

    return render(request, 'home/HR-Editor.html', context)


@login_required(login_url="/login/")
def getUsersForLMView(request):
    users = User.objects.all().order_by('-last_login')
    context = {
        'segment': 'theditor',
        "users": users,
    }

    return render(request, 'home/TH-Editor.html', context)


def sendEmail(request):
    # Send a welcome email on form submit
    sender = request.GET.get("sender")
    subject = "Predictd email from: " + sender
    target = request.GET.get("target")
    plain_message = request.GET.get("message")
    html_message = format_html(plain_message)
    send_mail(subject, plain_message, settings.EMAIL_HOST_USER, [target], fail_silently=False,
              html_message=html_message)

    print("Email successfully sent")

    return HttpResponse(json.dumps({'Success': 'Your email was sent!'}), content_type='application/json')


# PUT Request to update an existing user
@login_required(login_url="/login/")
def update_user(request):
    request = QueryDict(request.body)
    print(request)
    user = User.objects.get(id=request.get('formId'))
    profile = user.profile

    user.username = request.get('formName')
    user.email = request.get('formEmail')
    profile.role = request.get('formRole')
    profile.team = request.get('formTeam')

    user.save()

    return JsonResponse({
        'name': user.username,
        'email': user.email,
        'role': profile.role,
        'team': profile.team,
    })


# POST Request to create a new user
@login_required(login_url="/login/")
def new_user(request):
    request = request
    name = request.POST.get('NewUsername')
    email = request.POST.get('NewEmail')
    role = request.POST.get('NewRole')
    team = request.POST.get('NewTeam')
    password = request.POST.get('NewPassword')

    user = User.objects.create_user(username=name, email=email, password=password)

    user.save()

    user = User.objects.get(username=name)

    profile = user.profile

    profile.role = role
    profile.team = team

    profile.save()

    return JsonResponse({
        'id': user.id,
        'name': user.username,
        'email': user.email,
        'role': user.profile.role,
        'team': user.profile.team,
    })


# POST Request to release desired user from a team
@login_required(login_url="/login/")
def releaseUser(request):
    user = User.objects.get(id=request.GET.get('id'))
    profile = user.profile

    profile.role = "Pending"
    profile.team = "Pending"

    profile.save()

    return JsonResponse({
        "Result": "Success",
    })

    return render(request, 'home/index.html', context)


@login_required(login_url="/login/")
def getStats(request):
    team = str(request.GET.get("team"))

    users = User.objects.filter(profile__team=team)

    testIdList = []

    for user in users:
        testId = user.profile.testResult_id
        if testId:
            testIdList.append(testId)

    testObjectList = []
    for testId in testIdList:
        testObject = MBTITest.objects.filter(pk=testId)
        if testObject:
            testIdList.append(testId)


    for element in IvsE_list:
        print("a")

    return JsonResponse({
        'key': "val",
    })