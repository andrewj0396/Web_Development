from flask import Flask

# Returns the main app
def run_app():
	app = Flask(__name__)

	# Pull in our main index route (aka home page)
	from website.index import index
	app.register_blueprint(index, url_prefix="/")

	# Pull in the reload route
	from .reload import reload_blueprint
	app.register_blueprint(reload_blueprint, url_prefix="/")

	return app
