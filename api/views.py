from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import User, Note

# Create your views here.

class CreateNote(ViewSet):
    permission_classes = [IsAuthenticated]

    def get_notes(self, request):
        try:
            user_id = request.auth.get('user_id')
            data = Note.objects.filter(user_id=user_id).values()
            return Response({"data":data}, status=200)
        except Exception as e:
            return Response

    def create_notes(self, request):
        try:
            data = request.data
            if not data:
                raise ValueError("No Data")
            print(request.auth)
            instance = Note.objects.create(name="Check", description="description", user_id=request.auth.get('user_id'))
            return Response({"data":f"Successfully Created the Note - {instance.name}"}, status=200)
        except ValueError as e:
            return Response({"message":f"Body is required - {e}"}, status=400)
        except Exception as e:
            raise Response({"message":"Internal Server Error"}, status=500)

class UserCreation(ViewSet):
    permission_classes = [AllowAny]

    def createuser(self, request):
        try:
            data = request.data
            if not data:
                raise ValueError("No Data")
            username = data.get('username')
            password = data.get("password")
            user = User.objects.create_user(username=username, password=password, is_active=True)
            return Response({"data":f"Successfully Created the User - {user.username}"}, status=200)
        
        except ValueError as e:
            return Response({"message":f"Body is required - {e}"}, status=400)
        except Exception as e:
            raise Response({"message":"Internal Server Error"}, status=500)