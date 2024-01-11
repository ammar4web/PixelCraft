from flask import Flask

# Create a Flask web application instance
app = Flask(__name__)

# Define a route for the '/' endpoint
@app.route('/')
def example():


    # Return the "Hello Word!" string as the HTTP response for the '/example' endpoint
    return "Hello Word!"

# Run the Flask web application if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True)
