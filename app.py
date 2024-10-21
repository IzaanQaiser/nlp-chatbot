from flask import Flask, request, jsonify
from chatbot import Chatbot # Import the Chatbot class that I made

# Create and instance of the Flask application
app = Flask(__name__) # Initialise the Flask app instance with the current module name
chatbot = Chatbot() # Instantiate the Chatbot Object

# Defining a route to handle chat messages
@app.route('/chat', methods=['POST']) # Specifies /chat as the endpoint and accepts POST requests
def chat(): # Function to retrieve the user input from the JSON request body
    user_input = request.json['message'] # Extracts the 'message' field from the incoming JSON
    response = chatbot.get_response(user_input) # Calls the get_response method which returns the response
    return jsonify({'Response': response}) # Returns a JSON response with the chatbot's output

# Defining a route to handle context resetting
@app.route('/reset', methods=['POST']) # Specifies /reset as the endpoint and accepts POST requests
def reset():
    chatbot.reset_context() # Calls the reset_context method to reset the chatbot's conversation context
    return jsonify({'response': 'Chat context has been reset'}) # Returns a JSON response indicating that the context has been reset

# Start this Flask Application is this script is executed directly
if __name__ == "__main__": # Checks if this module if being run directly or if it is being imported as a module in another script (True if being run directly) 
    app.run(debug=True) # Run the application in debug mode for development purposes