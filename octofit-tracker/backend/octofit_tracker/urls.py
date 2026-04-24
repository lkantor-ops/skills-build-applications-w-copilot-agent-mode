"""octofit_tracker URL Configuration"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from octofit_tracker import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'teams', views.TeamViewSet)
router.register(r'activities', views.ActivityViewSet)
router.register(r'workouts', views.WorkoutViewSet)
router.register(r'leaderboard', views.LeaderboardViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.api_root, name='api-root'),
    path('', include(router.urls)),
]
