

# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# import pandas as pd
# import numpy as np
# from typing import List

# # Inisialisasi FastAPI
# app = FastAPI()

# # Load data CSV
# data_file = 'duration_sec (1).csv'  # Ganti dengan path data CSV Anda
# df = pd.read_csv(data_file)

# @app.get('/data')
# def greet():
#     return df.to_dict(orient='records')


# # Endpoint return data
# # @app.get("/data")

# # def get_data():
# #     return df.to_dict()

# #Endpoint penghapusan data
# @app.delete("/delete/{row}")

# def del_data(row:int):
#     if row in df.index:
#         df.drop(row, inplace=True) #Lupa inplace True kalo gk pake ini datanya gk bakal ke update pas diapus.
#         return {'message':f'Data pada row {row} telah dihapus'}
#     else:
#         raise HTTPException(status_code=404, detail="Row tidak ketemu!")




from fastapi import FastAPI, Header, HTTPException #digunakan import karena FastApi berada di package fastapi
import pandas as pd 


secret = "hectiv8jayajaya"


#membuat instance/object
app = FastAPI()




#membuat endpoint, aturan request dari client
#endpoint untuk menampilkan halaman utama
@app.get('/')
def getHone():
    df = pd.read_csv ('data.csv')
    #proses yang digunakan pada server
    return{
        "data": df.to_dict(orient='records') #mengembalikan data ke panda #digunakan orients records agar sesuai dengan list dictionary dan kolom
    }
#*fastapi dev main.py* untuk mengalakan server


#menampilkan data hasil filter
@app.get('/data/{filter}')
def getData(filter: str):
    df = pd.read_csv ('data.csv')
    #proses yang digunakan pada server

    result = df[df.nama == filter]
    # result = df.query(f"name == '{filter}")
    return result.to_dict(orient='records')
    
    

@app.delete('/data/{filter}')
def deleteData(filter: str,api_key=Header(None)):
    if api_key is not None and api_key == secret:
        print("password benar")
        df = pd.read_csv ('data.csv')
        #proses yang digunakan pada server

        result = df[df.nama != filter]

        result.to_csv('data.csv', index =False)
        # result = df.query(f"name == '{filter}")
        return result.to_dict(orient='records')
    else:
        raise HTTPException(400, "password salah")
