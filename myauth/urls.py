from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('signup', views.signUp.as_view(), name="signup"),
    path('logout', views.Logout.as_view(), name="logout"),
    path('sections', views.SectionViews.as_view()),
    path('destitutes', views.DestituteViews.as_view()),
    path('sections/<int:pk>', views.DeleteSectionView.as_view()),
    path('destitutes/<int:pk>', views.DeleteDestituteView.as_view()),
    path('cards', views.CardsViews.as_view()),
    path('cards/<int:pk>', views.DeleteCardView.as_view()),
    path('profile', views.ProfileViews.as_view()),
]