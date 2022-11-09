from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
from rest_framework.parsers import MultiPartParser, FormParser
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

from .models import UserSend,UserProfile,AmazonOptions,UserAmazon
from .serializers import UserSerializer
from .origindata import getdataAmazon,getDataML

# Editar, ver y eliminar usuarios
class UserViewID(APIView):
    parser_classes = (MultiPartParser, FormParser)
    #obtener datos de un usuario

    def get_object(self, pk):
        try:
            return UserProfile.objects.get(pk=pk)
        except UserProfile.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        try:
            usertoken = request.headers['Authorization']
            usertoken = usertoken.replace('Token ', '')
            tokendata = Token.objects.get(key=usertoken)
            userdata = UserProfile.objects.get(pk=tokendata.user.pk)

            if(userdata.pk == pk):
                optionoriginal = self.get_object(pk)
                serializer = UserSerializer(optionoriginal)
                return Response(serializer.data,status=status.HTTP_200_OK)      
            else:
                return Response("",status=status.HTTP_405_METHOD_NOT_ALLOWED)
        except Exception as ex:
            print(ex)
            return Response("",status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk, format=None):
        try:
            usertoken = request.headers['Authorization']
            usertoken = usertoken.replace('Token ', '')
            tokendata = Token.objects.get(key=usertoken)
            userdata = UserProfile.objects.get(pk=tokendata.user.pk).exists()
            if(userdata == True):
                snippet = self.get_object(pk)
                serializer = UserSerializer(snippet, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data,status=status.HTTP_200_OK)
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            return Response("",status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request, pk, format=None):
        try:
            usertoken = request.headers['Authorization']
            usertoken = usertoken.replace('Token ', '')
            tokendata = Token.objects.get(key=usertoken)
            userdata = UserProfile.objects.get(pk=tokendata.user.pk).exists()
            if(userdata == True):
                snippet = self.get_object(pk)
                snippet.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            return Response("",status=status.HTTP_404_NOT_FOUND)

class NewUser(APIView):
    authentication_classes = []
    permission_classes = []
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, format=None):
        newuser = request.data
        newuserdata = {
            "email":newuser['email'],
            "name":newuser['name'],
            "image":newuser.get('image',None)
        }
        newuserregistred = UserProfile(**newuserdata)
        newuserregistred.set_password(newuser['password'])
        newuserregistred.save()

        return Response(status=status.HTTP_200_OK)

class AddItemAmazon(APIView):
    def post(self, request, format=None):
        try:
            linkproduct = request.data['link']
            originlink = request.data['origin']
            usertoken = request.headers['Authorization']
            usertoken = usertoken.replace('Token ', '')

            tokendata = Token.objects.get(key=usertoken)
            userdata = UserProfile.objects.get(pk=tokendata.user.pk)

            quantityoptions = UserAmazon.objects.filter(user=userdata).count()
            if quantityoptions < 3:
                if (originlink == 'amazon'):
                    newitem = getdataAmazon(linkproduct)
                elif (originlink == 'ml'):
                    newitem = getDataML(linkproduct)
                else:
                    newitem = {
                        "link":linkproduct,
                    }

                newregistred = AmazonOptions(**newitem)
                newregistred.save()

                newuseritem={
                    "user":userdata,
                    "amazonOptions":newregistred
                }

                addusergift = UserAmazon(**newuseritem)
                addusergift.save()

                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        except Exception as ex:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        
class EditItemAmazon(APIView):
    def get_object(self, pk):
        try:
            return AmazonOptions.objects.get(pk=pk)
        except AmazonOptions.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        optionoriginal = self.get_object(pk)

        linkproduct = request.data['link']
        originlink = request.data['origin']
        usertoken = request.headers['Authorization']
        usertoken = usertoken.replace('Token ', '')

        tokendata = Token.objects.get(key=usertoken)
        userdata = UserProfile.objects.get(pk=tokendata.user.pk)

        useramazondata = UserAmazon.objects.get(amazonOptions=optionoriginal)
        if (useramazondata.user == userdata):
            if (originlink == 'amazon'):
                newitem = getdataAmazon(linkproduct)
            elif (originlink == 'ml'):
                newitem = getDataML(linkproduct)
            else:
                newitem = {
                    "link":linkproduct,
                }
            optionoriginal.link = newitem['link']
            optionoriginal.name = newitem.get('name',None)
            optionoriginal.imagelink = newitem.get('imagelink',None)
            optionoriginal.price = newitem.get('price',None)
            optionoriginal.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


#Reciver to create token to user
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

