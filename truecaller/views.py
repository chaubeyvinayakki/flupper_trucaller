from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from truecaller.serializers import RegisterUserSerializer, MarkSpamSerializer, UserSerializer, UserDetailSerializer, UserContactDetailSerializer
from truecaller.response import SuccessResponse
from .models import User, UserContact
from rest_framework.authtoken.models import Token

class RegisterUser(APIView):
    """
        class used to register the user
    """
    permission_classes = (AllowAny,)
    serializer_class = RegisterUserSerializer

    def post(self, request):
        """
            post method used to add movie by the admin
        :param request:
        :return:
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return SuccessResponse({"data": serializer.data}, status=status.HTTP_201_CREATED)



class LogIn(APIView):
    """
        class used to register the user
    """
    permission_classes = (AllowAny,)

    def post(self, request):
        """
            post method used to add movie by the admin
        :param request:
        :return:
        """
        params = request.data
        if 'phone_number' not in params:
        	return SuccessResponse({"data": "Phone number is required."}, status=status.HTTP_400_BAD_REQUEST)
        phone_number = params.get('phone_number')
        user = User.objects.filter(phone_number=phone_number).first()
        if not user:
        	return SuccessResponse({"data": "Phone number is invalid."}, status=status.HTTP_400_BAD_REQUEST)
       	token, created = Token.objects.get_or_create(user__id=user.id)
       	serializer = UserSerializer(instance=user)
       	serializer.data.update({'token': token.key})
        return SuccessResponse({"data": serializer.data}, status=status.HTTP_201_CREATED)


class MarkSpam(APIView):
    """
        class used to mark spam
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = MarkSpamSerializer

    def post(self, request):
        """
            post method used to add movie by the admin
        :param request:
        :return:
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.get(id=request.user.id)
       	instance = serializer.save(is_spam=True, user=user)
        return SuccessResponse({"data": serializer.data}, status=status.HTTP_201_CREATED)



class NameSearch(APIView):
    """
        SearchMovie api view to handle the movie search
    """
    serializer_class = UserDetailSerializer

    def get(self, request):
        queryset = User.objects.all()
        # if query params have name, then search by name
        name = request.query_params.get('name', None)
        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        serializer = self.serializer_class(queryset, many=True)
        return SuccessResponse(serializer.data, status=status.HTTP_200_OK)



class PhoneSearch(APIView):
    """
        SearchMovie api view to handle the movie search
    """
    serializer_class = UserDetailSerializer

    def get(self, request):
        queryset = User.objects.all()
        user_contact = UserContact.objects.all()
        # if query params have name, then search by name
        phone_number = request.query_params.get('phone_number', None)
        if phone_number is not None:
        	queryset = queryset.filter(phone_number=phone_number)
        	if queryset:
        		serializer = self.serializer_class(queryset, many=True)
        	else:
        		user_contact = UserContact.objects.filter(phone_number__exact=phone_number)
        		serializer = UserContactDetailSerializer(user_contact, many=True)
        return SuccessResponse(serializer.data, status=status.HTTP_200_OK)

