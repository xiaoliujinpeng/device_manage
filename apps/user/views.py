from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from apps.user.models import Users
from apps.user.serializers import UserSerializer, UserLoginSerializer, UserInfoSerializer


# Create your views here.

class UserViewSet(ModelViewSet):
    queryset = Users.objects.all()

    def get_serializer_class(self):
        if self.action == "login":
            return UserLoginSerializer
        return UserInfoSerializer

    def get_permissions(self):
        if self.action == 'login':
            permission_classes = []
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    @action(detail=False, methods=['post'])
    def login(self, request):
        serializer = self.get_serializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=201)

        username = serializer.data.get("username")
        password = serializer.data.get("password")
        user = authenticate(username=username, password=password)
        if not user:
            return Response("用户名或密码错误", status=201)
        refresh = RefreshToken.for_user(user)
        token_data = {
            'token': str(refresh.access_token),
            'refresh': str(refresh),
        }
        return Response(token_data)

    @action(detail=False, methods=['post'])
    def add_user(self, request):
        admin = request.user
        if not admin.is_superuser:
            return Response("无法操作")

        data = request.data
        try:
            Users.objects.create_user(username=data.get("username"), password=data.get("password"), name=data.get("name"))
        except Exception as e:
            return Response(str(e))

        return Response("创建成功")

