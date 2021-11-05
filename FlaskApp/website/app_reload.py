from flask import Flask, render_template, Blueprint
import os
import signal 

reload_blueprint = Blueprint("app_reload", __name__)

# Reload route is
@reload_blueprint.route('/reload', methods=['GET'])

# Index page contents
def app_reload():
	os.kill(os.getpid(), signal.SIGINT)

