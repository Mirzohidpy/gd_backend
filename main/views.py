from django.shortcuts import render
from rest_framework import status, generics
from .models import Portfolio, Category, JobType, TeamMember, Blog
from .serializers import PortfolioSerializer, CategorySerializer, JobTypeSerializer, TeamMemberSerializer, \
    BlogSerializer
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.


class PortfolioListView(generics.ListAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {'service': ['exact'], 'on_top': ['exact']}


class PortfolioDetailView(generics.RetrieveAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class JobTypeListView(generics.ListAPIView):
    queryset = JobType.objects.all()
    serializer_class = JobTypeSerializer


class JobTypeDetailView(generics.RetrieveAPIView):
    queryset = JobType.objects.all()
    serializer_class = JobTypeSerializer


class TeamMemberListView(generics.ListAPIView):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {'job_type': ['exact']}


class TeamMemberDetailView(generics.RetrieveAPIView):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer


class BlogListView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {'category': ['exact']}


class BlogDetailView(generics.RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
