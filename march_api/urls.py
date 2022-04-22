from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import(
     BracketDetailView, TeamListView, TeamDetailView,
     BracketTeamDetailView, UserPickView
)

urlpatterns = [
    path('teams/', TeamListView.as_view()),
    path('teams/<int:pk>/', TeamDetailView.as_view()),
    path('brackets/<int:pk>/', BracketDetailView.as_view()),
    path('bracketteams/<int:pk>/', BracketTeamDetailView.as_view()),
    path('userpicks/', UserPickView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)