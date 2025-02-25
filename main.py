from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return "HELLO WORLD!"

@app.get("/fuck")
def fuck():
    return "FUCK!!!!!"

@app.get("/wow")
def wow():
    return "해냇다 시바!!!"

@app.get("/describe")
def dec():
    return "There are two github repositories that manage this test project, one for code and other the for the helm chart. Jenkins observes the code repository and builds docker image with timestamp tag. It also updates helm manifest to the new image tag. \nArgoCD observes the helm repository and deploys the newly updated helm manifest to kubernetes environment."