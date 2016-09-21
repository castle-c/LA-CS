from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from search.models import Parish, CompanyInfo, CompaniesByParish
from search.serializers import *


class ParishList(viewsets.ModelViewSet):
    model = Parish
    queryset = Parish.objects.all()
    serializer_class = ParishSerializer



class UserList(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer



class CompanyInfoList(viewsets.ModelViewSet):
    model = CompanyInfo
    queryset = CompanyInfo.objects.all()
    serializer_class = CompanyInfoSerializer

    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class CompaniesByParishList(viewsets.ModelViewSet):
    queryset = CompaniesByParish.objects.all()
    serializer_class = CompaniesByParishSerializer



@csrf_exempt
def register_user(request):
    '''Handles the creation of a new user for authentication

    Method arguments:
      request -- The full HTTP request object
    '''

    # Load the JSON string of the request body into a dict
    req_body = json.loads(request.body.decode())

    # Create a new user by invoking the `create_user` helper method
    # on Django's built-in User model
    new_user = User.objects.create_user(
                    username=req_body['username'],
                    password=req_body['password'],
                    email=req_body['email'],
                    first_name=req_body['first_name'],
                    last_name=req_body['last_name'],
                    )

    new_user.visitor.age = req_body['age']
    new_user.visitor.gender = req_body['gender']

    # Commit the user to the database by saving it
    new_user.save()

    return login_user(request)

@csrf_exempt
def login_user(request):
    '''Handles the creation of a new user for authentication

    Method arguments:
      request -- The full HTTP request object
    '''

    # Load the JSON string of the request body into a dict
    req_body = json.loads(request.body.decode())

    # Use the built-in authenticate method to verify
    authenticated_user = authenticate(
            username=req_body['username'],
            password=req_body['password']
            )

    # If authentication was successful, log the user in
    success = True
    if authenticated_user is not None:
        login(request=request, user=authenticated_user)

        # Convert the authenticate user to a JSON object and send back in the reponse
        data = serializers.serialize('json', (authenticated_user,), fields=('username', 'first_name', 'last_name', 'email'))
    else:
        success = False
        data = json.dumps(None)  # Send back null if user does not exist

    return HttpResponse(data, content_type='application/json')


