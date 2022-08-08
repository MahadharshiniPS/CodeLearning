from fastapi import FastAPI

app = FastAPI()


@app.get("/get")
def root():
    return {'data': {'name': 'maha'}}

@app.get("/about")
def about():
    return {}