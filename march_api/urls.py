from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import BracketDetail #, TeamList, RegionList, RegionDetail

urlpatterns = [
    path('brackets/<int:pk>/', BracketDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)