from django.contrib import admin
from django.urls import path

from apps.members.api.views.general_views import MemberListAPIView

urlpatterns = [
    path('members/', MemberListAPIView.as_view(), name = 'miembros'),
]