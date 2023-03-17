from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
<<<<<<< HEAD

class UserSerializer(ModelSerializer):
=======
class UserSerializer(ModelSerializer):

>>>>>>> 80bc9ff6232c54c345c73b938e0ac50b391fc199
    class Meta:
        model=User
        fields=['username','password']

    # we need to overwrite the create function
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super(UserSerializer, self).create(validated_data)
    