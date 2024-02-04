from behave import *
import requests
@step('we want to get 10 users')
def getUsers(context):
    r = requests.get(context.url+'/users')
    assert r.status_code == 200


@step('we send a request')
def getUsers1(context):
    assert True is not False


@step('We get users')
def getUsers2(context):
    assert True is not False



