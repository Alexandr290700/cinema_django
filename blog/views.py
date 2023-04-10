import django_filters
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from rest_framework import filters
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import generics
from django.contrib.auth.models import User

from .models import *
from .serializers import *


# auth
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class AuthTokenView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response ({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'name': user.first_name
        })
    

class RegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializers
    
    def post(self, request, *args, **kwargs):
        serializer = UserRegistrationSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.create_user(username=serializer.validated_data['username'], password=serializer.validated_data['password'])
        token, created = Token.objects.get_or_create(user=user)
        return Response({
                'username': user.username,
                'token': token.key
            }
        )


# class MovieFilter(django_filters.FilterSet):
#     start_date = django_filters.NumberFilter(field_name='rental_start_date__year')
#     class Meta:
#         model = Movie
#         fields = ('start_date', )

class MovieListAPIView(ListAPIView):
    serializer_class = MovieSerializers
    filter_backends = (filters.SearchFilter, filters.OrderingFilter, django_filters.rest_framework.DjangoFilterBackend)
    # filterset_fields = ('sales_company', )
    search_fields = ('name', 'sales_company')
    # filterset_class = MovieFilter

    def get_queryset(self):
        queryset = Movie.objects.all()
        return queryset
    
class MovieCreateAPIViews(CreateAPIView):
    serializer_class = MovieSerializers
    
    def get_queryset(self):
        queryset = Movie.objects.all()
        return queryset


class MovieRetrieveAPIView(RetrieveAPIView):
    serializer_class = MovieDetailSerializer
    queryset = Movie.objects.all()

class SaloonFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    class Meta:
        model = Saloon
        fields = ('name', )

class SaloonListAPIViews(ListAPIView):
    serializer_class = SaloonSerializers
    filter_backends = (filters.SearchFilter, filters.OrderingFilter, django_filters.rest_framework.DjangoFilterBackend)
    filterset_fields = ('name', )

    def get_queryset(self):
        queryset = Saloon.objects.all()
        return queryset
    
class SaloonRetrieveAPIViews(RetrieveAPIView):
    serializer_class = SaloonDetailSerializers
    queryset = Saloon.objects.all()
    
class SaloonCreateAPIViews(CreateAPIView):
    serializer_class = SaloonSerializers
    queryset = Saloon.objects.all()


class SeansRetrieveAPIView(RetrieveAPIView):
    serializer_class = SeansDetailSerializers
    queryset = Seans.objects.all()

class SeansFilter(django_filters.FilterSet):
    start_date = django_filters.DateFilter(field_name='date')
    class Meta:
        model = Seans
        fields = ('start_date', ) 

class SeansListAPIViews(ListAPIView, CreateAPIView):
    serializer_class = SeansSerializers
    filter_backends = (filters.SearchFilter, filters.OrderingFilter, django_filters.rest_framework.DjangoFilterBackend)
    filterset_fields = ('saloon', 'movie', )
    search_fields = ('saloon', 'movie', )
    filterset_class = SeansFilter

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        queryset = Seans.objects.all()
        return queryset

    
class SeansCreateAPIViews(CreateAPIView):
    serializer_class = SeansSerializers
    queryset = Seans.objects.all()


class TitleFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    class Meta:
        model = JobTitle
        fields = ('title', )

class JobTitleListAPIViews(ListAPIView):
    serializer_class = JobTitleSerializers
    filter_backends = (filters.SearchFilter, filters.OrderingFilter, django_filters.rest_framework.DjangoFilterBackend)
    filterset_fields = ('title', )
    filterset_class = TitleFilter

    def get_queryset(self):
        queryset = JobTitle.objects.all()
        return queryset

class JobTitleRetrieveAPIViews(RetrieveAPIView):
    serializer_class = JobTitleDetailSerializers
    queryset = JobTitle.objects.all()

class JobTitleCreateAPIViews(CreateAPIView):
    serializer_class = JobTitleSerializers
    queryset = JobTitle.objects.all()


class PlacesFilter(django_filters.FilterSet):
    saloon_name = django_filters.CharFilter(field_name='saloon', lookup_expr='name')
    class Meta:
        model = Places
        fields = ('saloon_name', )

class PlacesListAPIViews(ListAPIView):
    serializer_class = PlacesSerializers
    filter_backends = {filters.SearchFilter, filters.OrderingFilter, django_filters.rest_framework.DjangoFilterBackend}
    filterset_fields = ('saloon__name', )   
    queryset = Places.objects.all()
    filterset_class = PlacesFilter

class PlacesRetrieveAPIViews(RetrieveAPIView):
    serializer_class = PlacesDetailSerializers
    queryset = Places.objects.all()

class PlacesCreateAPIViews(CreateAPIView):
    serializer_class = PlacesSerializers
    queryset = Places.objects.all()


class SectorSaloonFilter(django_filters.FilterSet):
    sector_name = django_filters.CharFilter(field_name='name', lookup_expr='name')
    class Meta:
        model = SectorSaloon
        fields = ('name', )

class SectorSaloonListAPIViews(ListAPIView):
    serializer_class = SectorSaloonSerializers
    filter_backends = {filters.SearchFilter, filters.OrderingFilter, django_filters.rest_framework.DjangoFilterBackend}
    filterset_fields = ('saloon__name', )
    filterset_class = SectorSaloonFilter
    queryset = SectorSaloon.objects.all()

class SectorSaloonCreateAPIViews(CreateAPIView):
    serializer_class = SectorSaloonSerializers
    queryset = SectorSaloon.objects.all()

class SectorSaloonRetrieveAPIViews(RetrieveAPIView):
    serializer_class = SectorSaloonDetailSerializers
    queryset = SectorSaloon.objects.all()



class EmployeesFilter(django_filters.FilterSet):
    employee_name = django_filters.CharFilter(field_name='name', lookup_expr='name')
    class Meta:
        model = Employees
        fields = ('name', )

class EmployeesListAPIViews(ListAPIView):
    serializer_class = EmployeesSerializers
    filter_backends = (filters.SearchFilter, filters.OrderingFilter, django_filters.rest_framework.DjangoFilterBackend)
    filterset_fields = ('title__title', )
    filterset_class = EmployeesFilter
    queryset = Employees.objects.all()
    
    
class EmployeesRetrieveAPIView(RetrieveAPIView):
    serializer_class = EmployeeDetailSerializers
    queryset = Employees.objects.all()
    
class EmployeesCreateAPIViews(CreateAPIView):
    serializer_class = EmployeesSerializers
    # queryset = Employees.objects.all()
    def get_queryset(self):
        queryset = Employees.objects.all()
        return queryset


class PriceForTicketsFilter(django_filters.FilterSet):
    seans = django_filters.CharFilter(field_name='seanse', lookup_expr='icontains')
    class Meta:
        model = PriceForTickets
        fields = ('seans', )

class PriceForTicketsListAPIViews(ListAPIView):
    serializer_class = PriceForTicketsSerializers
    filter_backends = {filters.SearchFilter, filters.OrderingFilter, django_filters.rest_framework.DjangoFilterBackend}
    filterset_fields = ('sector__name', )
    filterset_class = PriceForTicketsFilter
    queryset = PriceForTickets.objects.all()

class PriceForTicketsCreateAPIViews(CreateAPIView):
    serializer_class = PriceForTicketsSerializers
    queryset = PriceForTickets.objects.all()

class PriceForTicketsRetrieveAPIViews(RetrieveAPIView):
    serializer_class = PriceForTicketsDetailSerializers
    queryset = PriceForTickets.objects.all()
