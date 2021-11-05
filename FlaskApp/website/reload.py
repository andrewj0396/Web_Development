import os
import signal 
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask, request, render_template, Blueprint, url_for, redirect

reload_blueprint = Blueprint("app_reload", __name__)

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# Reload route is
@reload_blueprint.route('/reload', methods=['GET', 'POST'])

# Reload page logic
def app_reload():
	if request.method == 'POST':
		reload_key = request.form.get('reload_key')

		if reload_key == os.environ['RELOAD_KEY']:
			os.kill(os.getpid(), signal.SIGINT)
		else:
			return redirect(url_for('index.home'))
	else:
		return redirect(url_for('index.home'))
