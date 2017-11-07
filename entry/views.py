# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from entry.models import DataEntry
from users.models import Employee, User


class EntryAPI(APIView):
    def post(self, request):
        data = request.POST
        employee_id = data.get('employee_id', None)
        if employee_id:
            supervisor_id = data.get('supervisor_id', None)
            quality = data.get('quality')
            quantity = data.get('quantity')
            employee = Employee.objects.get(id=employee_id)
            supervisor = User.objects.get(id=supervisor_id)
            entry = DataEntry.objects.create(employee=employee, created_by=supervisor, quality=quality,
                                             quantity=quantity)
            return Response({'status': 'Saved', 'transaction_id': entry.id})
        return Response({'error', 'Employee ID Parameter Missing'}, status=400)


