from pydantic import BaseModel
from fastapi import FastAPI


app = FastAPI()



class RequestHandler(BaseModel):
    """
    Class Handler that handles the request.
    
    """
    task : str


@app.get("/")
async def root():
    return {"message": "Hello World"}