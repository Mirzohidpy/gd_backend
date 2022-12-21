from rest_framework import serializers
from .models import Portfolio, Category, JobType, TeamMember, Blog


class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = ['id', 'image', 'title', 'description', 'order', 'on_top']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']


class JobTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobType
        fields = ['id', 'title']


class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = ['id', 'full_name',
                  'image',
                  'job_type',
                  'linkedin',
                  'facebook',
                  'instagram',
                  'twitter',
                  'telegram', ]


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['id', 'image', 'title', 'body']
