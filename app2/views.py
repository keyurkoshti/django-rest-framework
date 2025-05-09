from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import userData
from .serializer import userDataserializer
# Create your views here.

class userApiview(APIView):
    def get(self, request):
        users=userData.objects.all()
        serializer = userDataserializer(users, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer=userDataserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


def user_data(request):
    users=userData.objects.all()
    return render(request, 'userdata.html',{'users':users})
