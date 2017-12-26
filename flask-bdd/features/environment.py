import os
import sys
# add module to syspath

pwd = os.path.abspath(os.path.dirname(__file__))
project = os.path.basename(pwd)
new_path = pwd.strip(project)
full_path = os.path.join(new_path,'flaskr')

try:
	from flaskr import app
except ImportError:
	sys.path.append(full_path)
	from flaskr import app

def before_feature(context, feature):
	context.client = app.test_client()