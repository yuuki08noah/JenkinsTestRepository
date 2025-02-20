from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return "HELLO WORLD!"

@app.get("/fuck")
def fuck():
    return "FUCK!!!!!"