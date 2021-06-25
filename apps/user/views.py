from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.views import token_refresh
from apps.user.models import Users, UserRegister
from apps.user.serializers import UserSerializer, UserLoginSerializer, UserInfoSerializer, UserRegisterSerializer


# Create your views here.

class UserViewSet(ModelViewSet):
    queryset = Users.objects.all()

    def get_serializer_class(self):
        if self.action == "login" or self.action == 'register':
            return UserLoginSerializer
        return UserInfoSerializer

    def get_permissions(self):
        if self.action == 'login' or self.action == 'register':
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
        tmp = UserSerializer(user)
        return Response({"token": token_data, "user": tmp.data})

    @action(detail=False, methods=['post'])
    def add_user(self, request):
        admin = request.user
        if not admin.is_superuser:
            return Response("无法操作")

        data = request.data
        try:
            Users.objects.create_user(username=data.get("username"), password=data.get("password"),
                                      name=data.get("name"))
        except Exception as e:
            return Response(str(e))

        return Response("创建成功")

    @action(detail=False, methods=['post'])
    def new_token(self, request):
        token = token_refresh(request)
        print(token)
        return Response("sss")


class UserRegisterViewSet(ModelViewSet):
    queryset = UserRegister.objects.all()
    serializer_class = UserRegisterSerializer

    def get_permissions(self):
        if self.action == 'register':
            permission_classes = []
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    @action(detail=False, methods=['post'])
    def register(self, request):
        if request.user.is_authenticated:
            return Response("已经登录")

        data = request.data
        if UserRegister.objects.filter(username=data.get("username")).count() > 0 or Users.objects.filter(
                username=data.get("username")).count() > 0:
            return Response("用户已经被注册")
        try:
            user = UserRegister(username=data.get('username'), name=data.get('name'),
                                password=data.get('password'))
            user.save()
        except Exception as e:
            return Response(str(e))

        return Response('注册成功')

    @action(detail=False, methods=['post'])
    def agree(self, request):
        username = request.data.get("username")
        user = UserRegister.objects.get(username=username)
        if user is None:
            return Response("无此用户", status=400)
        Users.objects.create_user(username=username, name=user.name, password=user.password)
        user.delete()
        return Response("创建成功")

    @action(detail=False, methods=['post'])
    def reject(self, request):
        username = request.data.get("username")
        user = UserRegister.objects.get(username=username)
        if user is None:
            return Response("无此用户", status=400)
        user.delete()
        return Response("拒绝成功")
