from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome Home"}

@app.get("/about")
def about():
    return {"message": "This is About Page"}

@app.get("/contact")
def contact():
    return {"message": "Contact us here"}
