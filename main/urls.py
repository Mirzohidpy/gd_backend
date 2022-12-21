from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import PortfolioListView, PortfolioDetailView, BlogListView, BlogDetailView, CategoryListView, \
    CategoryDetailView, JobTypeListView, JobTypeDetailView, TeamMemberListView, TeamMemberDetailView

urlpatterns = [
    # Organization
    path('portfolio/', PortfolioListView.as_view()),
    path('portfolio/<int:pk>/', PortfolioDetailView.as_view()),
    path('blog/', BlogListView.as_view()),
    path('blog/<int:pk>/', BlogDetailView.as_view()),
    path('category/', CategoryListView.as_view()),
    path('category/<int:pk>/', CategoryDetailView.as_view()),
    path('jobtype/', JobTypeListView.as_view()),
    path('jobtype/<int:pk>/', JobTypeDetailView.as_view()),
    path('team-member/', TeamMemberListView.as_view()),
    path('team-member/<int:pk>/', TeamMemberDetailView.as_view()),

]
