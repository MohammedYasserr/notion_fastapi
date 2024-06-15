from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def root():
    return {"items": "These are the items"}
