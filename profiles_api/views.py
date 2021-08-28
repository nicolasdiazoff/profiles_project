from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from profiles_api.models import UserProfile

# Create your views here.

class ApiViewController(APIView):
    serializer_class = serializers.Serialiazer

    def get(self, request, format=None):
        print(UserProfile)
        profiles = UserProfile.objects.all().values("id", "name", "is_active")
        profiles_list = list(profiles)
        data = {"data": profiles_list}
        return Response(data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            user = UserProfile(name=name)
            user.save()
            message = f'The user was be created {name}'
            return Response({"message": message})
        else:
            return Response(serializer.erros,status=status.HTTP_400_BAD_REQUEST)
