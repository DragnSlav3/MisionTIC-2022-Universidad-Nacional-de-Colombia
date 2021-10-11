"""authProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls                    import path 
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView) 
from authApp                        import views 
 
urlpatterns = [ 
    path('login/',         TokenObtainPairView.as_view()), 
    path('refresh/',       TokenRefreshView.as_view()), 
    path('user/',          views.UserCreateView.as_view()), 
    path('user/<int:pk>/', views.UserDetailView.as_view()), 
    path('transaction/create/',                     views.TransactionCreateView.as_view()), # create a new transaction
    path('transaction/<int:user>/<int:pk>/',        views.TransactionsDetailView.as_view()), # view information for a transaction
    path('transaction/update/<int:user>/<int:pk>/', views.TransactionsUpdateView.as_view()), # update a transaction
    path('transaction/remove/<int:user>/<int:pk>/', views.TransactionsDeleteView.as_view()), # delete a transaction
    path('transactions/<int:user>/<int:account>/',  views.TransactionsAccountView.as_view()), # view all transactions for an specific account
    path('deposit/create/',                         views.DepositCreateView.as_view()), # create a new deposit
    path('deposit/<int:user>/<int:pk>/',            views.DepositDetailView.as_view()), # view information for a deposit
    path('deposits/<int:user>/<int:account>/',      views.DepositsAccountView.as_view()), # view all depositss for an specific account
]