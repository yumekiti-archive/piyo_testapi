from fastapi import FastAPI

app = FastAPI()

@app.get("/buses")
@app.get("/drivers")
@app.get("/users")
@app.get("/passengers")

@app.get("/")
async def root():
  return {"message": "Hello World"}