from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config.database import engine,Base
from middlewares.error_handler import ErrorHandler
from routers.estado import estado_router
from routers.user import user_router
from routers.af import af_router
from routers.gl import gl_router
from routers.mp import mp_router
from routers.qu import qu_router
from routers.vz import vz_router

app = FastAPI(
    title= 'BRAILLE',
    description= 'API de aprendizaje braille ',
    version= '0.0.1',
)


origins = [    
    "http://localhost:3000",    
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(ErrorHandler)
app.include_router(estado_router)
app.include_router(user_router)
app.include_router(af_router)
app.include_router(gl_router)
app.include_router(mp_router)
app.include_router(qu_router)
app.include_router(vz_router)


Base.metadata.create_all(bind=engine)



