from pets.models import Pet
from pets.serializers import PetSerializer

from django.views import View
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

from rest_framework.response import Response
from rest_framework import exceptions, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView


class ApiHome(View):
    """
    View for CRUD apis.
    """

    def get(self, request):
        html = "<h1 align=center>API</h1><hr><br><h3 align=center><a href='/'>Home</a><br></h3>" \
               "<h3 align=center><a href='list/'>Show animals</a></h3>" \
               "<h3 align=center><a href='create/'>Create a new animal</a></h3>" \
               "<h3 align=center><a href='edit/1/'>Update or Delete a animal</a></h3>"
        return HttpResponse(html)


class Home(View):
    """
    View for main page.
    """

    def get(self, request):
        html = "<h1 align=center>Application for Dogs & Cats</h1><hr><br>" \
               "<h3 align=center><a href='/api'>APIs List</a></h3>" \
               "<h3 align=center><a href='/admin'>Django Admin</a></h3>"
        return HttpResponse(html)


class PetListView(ListAPIView):
    """
    API to list animals.
    """
    serializer_class = PetSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'owner'

    def get_queryset(self):
        try:
            return Pet.objects.filter(owner=self.request.user).order_by('id')
        except ObjectDoesNotExist:
            raise exceptions.NotFound('Object NotFound')


class PetCreateView(CreateAPIView):
    """
    API to create a new animal.
    """
    serializer_class = PetSerializer
    permission_classes = (IsAuthenticated,)
    queryset = Pet.objects.all()

    def post(self, request, *args, **kwargs):
        try:
            if request.data:
                user = User.objects.get(username=self.request.user)
                pet = Pet.objects.create(owner=user,
                                         name=request.data['name'],
                                         type=request.data['type'],
                                         birthday=request.data['birthday'])
                serializer = self.get_serializer(pet)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except exceptions.ValidationError:
            raise exceptions.ValidationError('Error data request')


class PetRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    """
    API to update/delete animal specified by pk.
    """
    serializer_class = PetSerializer
    permission_classes = (IsAuthenticated,)
    lookup_field = 'pk'

    def get_queryset(self):
        try:
            return Pet.objects.filter(owner=self.request.user)
        except ObjectDoesNotExist:
            raise exceptions.NotFound('Object Not found.')
