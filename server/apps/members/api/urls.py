from django.urls import path

from apps.members.api.views.general_views import MemberDestroyAPIView, MemberListAPIView, MemberCreateAPIView, MemberRetrieveAPIView, MemberUpdateAPIView

urlpatterns = [
    path('', MemberListAPIView.as_view(), name = 'members'),    
    path('create/', MemberCreateAPIView.as_view(), name = 'member_add'),
    path('<int:pk>/', MemberRetrieveAPIView.as_view(), name = 'member_retrieve'),
    path('destroy/<int:pk>/', MemberDestroyAPIView.as_view(), name = 'member_destroy'),
    path('update/<int:pk>/', MemberUpdateAPIView.as_view(), name = 'member_destroy'),
]