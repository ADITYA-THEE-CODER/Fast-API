from fastapi import FastAPI 

app = FastAPI()

@app.get("/")
def home() :
  return {"message" : "Hello.. , WELCOME "}


@app.get("/about")
def about():
  return {"message" : "About Us.. "}


@app.get("/contact")
def contact():
  return {"message" : "Contact us Here"}

@app.get("/skills")
def skills():
  return {"message" : "Python"}
