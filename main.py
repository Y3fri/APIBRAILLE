from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config.database import engine,Base
from middlewares.error_handler import ErrorHandler


app = FastAPI(
    title= 'prendiendo FastApi',
    description= 'Una API ',
    version= '0.0.1',
)


origins = [    
    "http://localhost:3000", 
    "https://master--rec1claje.netlify.app", 
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(ErrorHandler)


Base.metadata.create_all(bind=engine)



