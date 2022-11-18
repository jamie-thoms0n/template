from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def playerPrices():
    return {"Theo": 9.3}


@app.post('/')
def changePlayerPrices():
    return {"Succes you changed this players price": 8.2}
