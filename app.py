from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from config import Config

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Enable CORS (Cross-Origin Resource Sharing)
CORS(app)

# Initialize Database
db = SQLAlchemy(app)

# Import and register routes
from routes.auth import auth_bp
from routes.user import user_bp
# from routes.forum import forum_bp
# from routes.chatbot import chatbot_bp
# from routes.feedback import feedback_bp

app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(user_bp, url_prefix="/user")
# app.register_blueprint(forum_bp, url_prefix="/forum")
# app.register_blueprint(chatbot_bp, url_prefix="/chatbot")
# app.register_blueprint(feedback_bp, url_prefix="/feedback")

# Default route
@app.route("/")
def home():
    return "Welcome to the Flask Backend!"

# Run the application
if __name__ == "__main__":
    app.run(debug=True)
