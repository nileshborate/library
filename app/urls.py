from django.urls import path
from .views import *

urlpatterns = [
    path("members/", MemberAPI.as_view()),
    path("books/", BookAPI.as_view()),
    path("loans/", LoanAPI.as_view()),
    path("returnbook/", ReturnBookAPI.as_view()),
    path("register/", RegisterUserAPI.as_view()),
]
