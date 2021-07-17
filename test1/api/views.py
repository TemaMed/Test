from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response as RestResponse
from rest_framework.decorators import action

from api.create.create import create_user
from api.get.get import get_pvd


class Test(viewsets.ViewSet):
    @action(methods=['get'], detail=True)
    def method(self, request):
        return RestResponse(data={},
                            status=status.HTTP_200_OK)

    @action(methods=['get','post'], detail=True)
    def user(self, request):
        if request.method == 'GET':
            username = request.GET.get('username', None)
            try:
                password = get_pvd(username)
            except:
                return RestResponse(data={'detail': 'Object not found'},
                                    status=status.HTTP_404_NOT_FOUND)
            return RestResponse(data={'password': password},
                                status=status.HTTP_200_OK)
        try:
            username = request.data.get('username', None)
            password = request.data.get('password', None)
            print(username)
            print(password)
            create_user(username, password)
        except Exception as e:
            print(e)
            return RestResponse(data={'detail': 'Invalid data'},
                                status=status.HTTP_403_FORBIDDEN)
        return RestResponse(data={'status': 'OK'},
                            status=status.HTTP_403_FORBIDDEN)
