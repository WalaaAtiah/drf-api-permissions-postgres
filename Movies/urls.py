from django.urls import path
from .views import MoveListView,DramaListView,ActionListView,AnimationListView,DramaDetailView,ActionDetailView,AnimationDetailView
urlpatterns = [
   path('', MoveListView.as_view(), name='move_list'),
   path('Drama/', DramaListView.as_view(),name='Drama_list'),
   path('Action/', ActionListView.as_view(),name='Action_list'),
   path('Animation/', AnimationListView.as_view(),name='Animation_list'),
   path('Drama/<int:pk>/', DramaDetailView.as_view(),name='Drama_detail'),
   path('Action/<int:pk>/', ActionDetailView.as_view(),name='Action_detail'),
   path('Animation/<int:pk>/', AnimationDetailView.as_view(),name='Animation_detail')

] 