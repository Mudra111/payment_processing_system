from fastapi import FastAPI

app = FastAPI()


@app.post("/register")
def register():
    return {"message": "Registered Successfully.."}


@app.post("/login")
def login():
    return {"message": "Logged in successfully..."}
