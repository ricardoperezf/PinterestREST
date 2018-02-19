from pinterest import pinterest_app

@pinterest_app.route("/example")
def example():
    return "This is an example"