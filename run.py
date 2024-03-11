from app import create_app

# Calling create_app method
app = create_app()

@app.route('/api')
def index():
    return "<h1> Home Page </h1>"

# Run the app
app.run(debug=True)