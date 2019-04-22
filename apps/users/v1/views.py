from urbvan_framework import views
from rest_framework.permissions import AllowAny
from apps.users.permissions import IsTier2, IsTier3

from .serializers import UserSerializer
from .schemas import UserSchema
from ..models import User

class UserCreateView(views.CreateAPIView):
	serializer_class = UserSerializer
	schema_class = UserSchema
	queryset = User.objects.all()
	permission_classes = (AllowAny,)

class UserRetrieveView(views.RetrieveAPIView):
	serializer_class = UserSerializer
	queryset = User.objects.all()
	schema_class = UserSchema
	permission_classes = (IsTier2,)

class UserUpdateView(views.UpdateAPIView):
	serializer_class = UserSerializer
	queryset = User.objects.all()
	schema_class = UserSchema
	permission_classes = (IsTier2,)

class UserDestroyView(views.DestroyAPIView):
	serializer_class = UserSerializer
	queryset = User.objects.all()
	schema_class = UserSchema
	permission_classes = (IsTier3,)

class UserManageView(views.BaseManageView):
	    VIEWS_BY_METHOD = {
        'DELETE': UserDestroyView.as_view,
        'GET': UserRetrieveView.as_view,
        'PUT': UserUpdateView.as_view,
        'PATCH': UserUpdateView.as_view
    }