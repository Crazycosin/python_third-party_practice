# - * - coding: utf-8 - * -
import persistent


class OutOfFunds(Exception):
    pass


class Account(persistent.Persistent):
    def __init__(self, name, start_balance):
        self.name = name
        self.balance = start_balance

    def __str__(self):
        return f"Account: {self.name}, balance: {self.balance}"

    def __repr__(self):
        return f"Account: {self.name}, balance: {self.balance}"

    def deposit(self, amount):
        """
        save amount into the balance
        :param amount:
        :return:
        """
        self.balance += amount

    def withdraw(self, amount):
        """
        withdraw from balance
        :param amount:
        :return:
        """
        if amount > self.balance:
            raise OutOfFunds
        self.balance -=amount
        return self.balance
