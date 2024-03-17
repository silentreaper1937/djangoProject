import uuid
from app01 import models
from rest_framework.views import APIView
from rest_framework.response import Response
from ext.per import MyPermission1, MyPermission2
from ext.throttle import MyThrottling
from ext.version import MyVersion
from rest_framework.parsers import JSONParser, FormParser
from rest_framework.negotiation import DefaultContentNegotiation
from rest_framework import serializers


class LoginView(APIView):
    authentication_classes = []
    throttle_classes = [MyThrottling, ]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user_obj = models.UserInfo.objects.filter(username=username, password=password).first()
        if not user_obj:
            return Response({'status': False, 'error': '用户不存在'})

        token = str(uuid.uuid4())
        user_obj.token = token
        user_obj.save()
        return Response({'status': True, 'data': token})


class UserView(APIView):

    def get(self, request):
        print(request.user, request.auth)
        return Response({'status': True, 'user': request.user.username})

    def check_permissions(self, request):
        no_permission_objects = []
        for permission in self.get_permissions():
            if permission.has_permission(request, self):
                return
            else:
                no_permission_objects.append(permission)
        self.permission_denied(request, message=getattr(no_permission_objects[0], 'message', None),
                                   code=getattr(no_permission_objects[0], 'code', None))


class HomeView(APIView):

    authentication_classes = []
    parser_classes = [JSONParser, FormParser]
    versioning_class = MyVersion
    content_negotiation_class = DefaultContentNegotiation

    def get(self, request):
        return Response("这是版本{}的信息".format(request.version))

    def post(self, request, *args, **kwargs):
        print(request.data, type(request.data))
        return Response('...')


class TestSerializer(serializers.ModelSerializer):
    age = serializers.IntegerField()
    age = serializers.SerializerMethodField()
    gender = serializers.CharField(source='get_gender_display')
    depart = serializers.CharField(source='depart.title')
    datetime = serializers.DateTimeField(format='%Y-%m-%d')

    class Meta:
        model = models.Member
        fields = ['name', 'age', 'gender', 'depart', 'datetime']


class TestView(APIView):
    authentication_classes = []

    def get(self, request, *args, **kwargs):
        ser = TestSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
        else:
            print(ser.errors)
        print(ser.data, type(ser.data))
        context = {'status': True, 'data': ser.data}
        return Response(context)