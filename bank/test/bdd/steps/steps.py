from behave import *
import requests

from bank.bank.bank import Bank


@given(u'I visit the homepage')
def step_impl(context):
    response = requests.get('https://api.github.com/events')
    assert (response.status_code, 200)


@when(u'I enter the account number "1111"')
def step_impl(context):
    print('I enter an account number 1111')


@given(u'I create account {account_number} with balance of {balance}')
def step_impl(context, account_number, balance):
    assert account_number == account_number
    assert balance == balance


@when(u'I enter the account number {account_number}')
def step_impl(context, account_number):
    assert account_number == account_number


@then(u'I see a balance of {balance}')
def step_impl(context, balance):
    assert balance == balance

@given(u'I create the following account')
def step_impl(context):
    for row in context.table:
        a = (row['account_number'], row['balance'])
        return a


@given(u'a set of specific users')
def step_impl(context):
    model = getattr(context, "model", None)
    for row in context.table:
        context.model.add_user(row["name"], department=row["department"])




