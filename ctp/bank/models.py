from django.db import models


class Account(models.Model):

    title = models.CharField(max_length=100)
    base = models.IntegerField()


class Transaction(models.Model):

    amount = models.IntegerField()
    account = models.ForeignKey(Account)
