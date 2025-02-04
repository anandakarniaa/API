from fastapi import FastAPI
import pandas as pd

app = FastAPI()

data = pd.read_csv('data.csv')

#coba buat root
@app.get("/")
def root():
    return{'message' : 'My LOVE:'}

@app.get("/name/{name}")
def greet(name):
    return{'message': f'Hai {name}, how are you?'}

@app.get('/data')
def get_data():
    return data.to_dict(orient='records')

@app.get('/data/{id}')
def search_data(id:int):
    result = data[data['id']==id]
    return {'result': result.to_dict(orient='records')}

# @app.post('/data/add/')