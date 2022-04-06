from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import TeamList, TeamDetail

urlpatterns = [
    path('teams/', TeamList.as_view()),
    path('teams/<int:pk>/', TeamDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)