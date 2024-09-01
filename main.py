from fastapi import FastAPI
from routes import base
app=FastAPI()
app.include_router(base.base_router)

@app.get("/welcome")
def welcome():
    return{
        "message":"hello 4"
    }