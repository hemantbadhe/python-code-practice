# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import EmailMessage

from rto_app.models import *


def user_login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            # return render(request, 'dashboard.html')
            return redirect('rto_app:dashboard')
        else:
            messages.warning(request, "Enter Valid User Name and Password.")
            return render(request, 'login.html')


@login_required(login_url='/')
def dashboard(request):
    images = VehicleNumberImages.objects.all().count()
    fined_users = FineApplied.objects.all().count()
    context = {'images_count': images, 'fined_users_count': fined_users}
    return render(request, 'dashboard.html', context)


@login_required(login_url='/')
def latest_images(request):
    objs = VehicleNumberImages.objects.all()
    context = {"objs": objs}
    return render(request, 'latest_images.html', context)


@login_required(login_url='/')
def apply_fine(request):
    if request.method == 'POST':
        vehicle_no = request.POST.get('vehicle_no')
        fine_amt = request.POST.get('fine_amt')

        if vehicle_no:
            user_obj = User.objects.get(vehicle_number=vehicle_no.upper())
            body = "Hello, you have been fined RS.{} for fancy no plate, Kindly pay it earlier.".format(fine_amt)
            email = EmailMessage('Fancy no. plate fine', body, to=[user_obj.email])
            email.send()

            fined_user_obj = FineApplied.objects.create(user=user_obj, fine=fine_amt)
        return HttpResponse(json.dumps({'message': 'Fine applied success..!'}))


@login_required(login_url='/')
def fine_applied(request):
    objs = FineApplied.objects.all()
    context = {'objs': objs}
    return render(request, 'fine_applied_users.html', context)
