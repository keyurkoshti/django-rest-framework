from rest_framework import serializers
from .models import userData

class userDataserializer(serializers.ModelSerializer):
    class Meta:
        model = userData
        fields = ['id','username','email']
