from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('register/', views.register, name='register'),
    path('LoginPage/', views.LoginPage, name='LoginPage'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('Bank_Deposit/', views.Bank_Deposit, name='Bank_Deposit'),
    path('basic/', views.basic, name='basic'),
    path('copy_trade/', views.copy_trade, name='copy_trade'),
    path('crypto_deposit/', views.crypto_deposit, name='crypto_deposit'),
    path('deposit/', views.deposit, name='deposit'),
    path('investment/', views.investment, name='investment'),
    path('kyc/', views.kyc, name='kyc'),
    path('nok/', views.nok, name='nok'),
    path('notification/', views.notification, name='notification'),
    path('premium/', views.premium, name='premium'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.LogoutPage, name='LogoutPage'),
    path('refferal/', views.refferal, name='refferal'),
    path('signals/', views.signals, name='signals'),
    path('standard/', views.standard, name='standard'),
    path('terms/', views.terms, name='terms'),
    path('ultimate/', views.ultimate, name='ultimate'),
    path('withdrawal/', views.withdrawal, name='withdrawal'),
    path('Success/', views.Success, name='Success'),
    path('deposit_review/', views.deposit_review_page, name='deposit_review_page'),

]