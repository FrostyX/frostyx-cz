from blog import app, config, routes

app.register_blueprint(routes.app)

if __name__ == '__main__':
    app.run(host=config.host, port=config.port, debug=config.debug)

