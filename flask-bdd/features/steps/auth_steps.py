from behave import *

@given(u'flaskr is set up')
def flask_is_setup(context):
	assert context.client