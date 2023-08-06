import uvicorn
from dotenv import load_dotenv
load_dotenv("env/.env")
import os

if __name__ == "__main__":
    print(os.getenv("RUNTIME_ENV"))
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True, debug=True)