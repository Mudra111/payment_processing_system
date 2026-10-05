from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello():
    return {"message": "Welcome to the Payment Processing System"}


@app.get("/login")
def login():
    return {"message": "Logged in successfully..."}
