# -- FILE: features/environment.py
from behave import fixture, use_fixture



def before_all(context):
    context.url= 'https://jsonplaceholder.typicode.com'


def before_feature(context, feature):
    pass