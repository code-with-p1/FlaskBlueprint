from app import create_app

# Calling create_app method
app = create_app()

@app.route('/')
def index():
    return "<h1> Flask - Blueprint Example </h1>"

# Run the app
app.run(debug=True)