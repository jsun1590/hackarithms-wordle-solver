from app import create_app
from decouple import config

app = create_app()
if __name__ == "__main__":
    app.run(port=config("PORT", 5000))