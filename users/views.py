# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from users.forms import UserCreateForm
from users.models import User


def createUser(request):
    form = UserCreateForm()
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            form = UserCreateForm()
            messages.success(request, 'Saved User Successfully')
            return render(request, 'users/createUser.html', {'form': form})
    return render(request, 'users/createUser.html', {'form': form})


class LoginView(APIView):
    def post(self, request):
        data = request.POST
        username = data.get('username', None)
        password = data.get('password', None)
        user = User.objects.get(username=username)
        if user.check_password(password):
            return Response({'status': 'Success', 'account_type': user.account_type, 'user_id': user.id})
        return Response({'Error', 'Wrong Username or Password'}, status=400)
