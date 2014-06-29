from django.shortcuts import render


from rest_framework import viewsets

from bank.models import Account, Transaction

class AccountViewSet(viewsets.ModelViewSet):

    model =  Account


class TransactionViewSet(viewsets.ModelViewSet):
  
    model = Transaction
