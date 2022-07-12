from dataclasses import fields
from rest_framework import serializers
from safaris.models import *
from django.contrib.auth.models import User, Group


class TouristSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tourist
        fields = ['admin','name',  'email','phone', 'bio', 'password','verified']

class SafarisSerializer(serializers.ModelSerializer):
    image = serializers.ImageField()
    
    class Meta:
        model = Safaris
        fields = ('name', 'description', 'location', 'pub_date','image')


class TourguideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tourguide
        fields = ( 'name','email','location','safaris')

# class TouristSignupSerializer(serializers.ModelSerializer):
#     password2 = serializers.CharField(style={"input_type":"password2"}, write_only=True)
#     class Meta:
#         model = User
#         fields=['username', 'email', 'password','password2']
#         extra_kwargs={
#             'password':{'write_only':True}
#         }
#     def save(self, **kwargs):
#         user=User(
#             username=self.validated_data['username'],
#             email=self.validated_data['email']
#         )
#         password=self.validated_data['password']
#         password2=self.validated_data['password2']
#         if password !=password2:
#             raise serializers.ValidationError({"error":"password do not match"})
#         user.set_password(password)
#         user.is_tourist=True
#         user.save()
#         Tourist.objects.create(user=user)
#         return user

# class TourguideSignupSerializer(serializers.ModelSerializer):
#     password2 = serializers.CharField(style={"input_type":"password2"}, write_only=True)
#     class Meta:
#         model = User
#         fields=['username', 'email', 'password','password2']
#         extra_kwargs={
#             'password':{'write_only':True}
#         }
# def save(self, **kwargs):
#         user=User(
#             username=self.validated_data['username'],
#             email=self.validated_data['email']
        # )
        # password=self.validated_data['password']
        # password2=self.validated_data['password2']
        # if password !=password2:
        #     raise serializers.ValidationError({"error":"password do not match"})
        # user.set_password(password)
        # user.is_tourguide=True
        # user.save()
        # Tourguide.objects.create(user=user)
        # return user

# class UpdateTourguideProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Tourguide
#         fields = ['name', 'email', 'contact', 'company_bio', 'address', 'company_pic']



# class UpdateUserProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Profile
#         fields = ['full_name','profile_image','contact','email','bio','resume','skills','work_experience','address','referees']

# class SignUpSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', 'username', 'email']

