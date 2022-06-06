from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
app = FastAPI()

class Cord(BaseModel):
    timestamp: str
    latitude: str
    longitude: str
    speed: Optional[str] = ...
    
# class JsonList(BaseModel):
#     data: List[Cord]

origins = ['https://localhost:3000',
"http://localhost",
"http://localhost:5500",
"http://127.0.0.1:5500"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return("hello": "there!")

# collected_data = []    
# @app.post("/analyse")
# async def post_todo(dataRec:List[Cord]):
#     for item in dataRec:
#         collected_data.append([item.timestamp, item.latitude, item.longitude, item.speed])
#     print(collected_data)
#     df = pd.DataFrame(collected_data, columns =['timestamp', 'latitude', 'longitude', 'speed'])
#     print(df)
#     return dataRec

# @app.get("/score")
# async def getScore():
#     readData()
#     print(".........1st execution done..........")
#     extractFeatures()
#     print(".........2nd execution done..........")
#     markEvents()
#     print(".........3rd execution done..........")
#     responseGot = getCDF()
#     print(".........4th execution done..........")
#     return [{"Harsh Acceleration": responseGot[0][0],"Harsh Braking": responseGot[0][1],"Harsh Turning": responseGot[0][2]}]
# print(collectedData)
