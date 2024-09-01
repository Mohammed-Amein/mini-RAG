from fastapi import FastAPI,APIRouter
app=FastAPI()
base_router= APIRouter()

@base_router.get("/")
def welcome():
    return{
        "message":"itworks"
    }