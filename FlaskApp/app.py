from website import run_app

if __name__ == "__main__":
	app = run_app()
	app.run(host=HOSTNAME, debug=True)
