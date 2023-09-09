from main import app
from dotenv import load_dotenv
load_dotenv()
import os
# import subprocess


# print("Generating requirements.txt...")
# subprocess.run("pip freeze > requirements.txt", shell=True)
# print("Requirements file generated.")

PORT = int(os.getenv("PORT", default=10010))

if __name__ == "__main__":
    app.run(port=PORT)



