from fastapi import FastAPI,APIRouter
import os

app=FastAPI()
base_router= APIRouter()

@base_router.get("/")
def welcome():
     app_name=os.getenv('APP_NAME')
     return{
       
        "message":"itworks",
        "NAME":app_name
    }