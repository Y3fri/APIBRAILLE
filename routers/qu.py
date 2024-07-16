from fastapi import APIRouter
from fastapi.responses import JSONResponse
from typing import List
from config.database import Session
from models.qu import Qu
from fastapi.encoders import jsonable_encoder
from service.qu_service import QuService
from schemas.qu import Qu


qu_router = APIRouter()


@qu_router.get('/qu',tags=['Qu'], response_model=list[Qu])
def get_qu()-> List [Qu]:
        db = Session()
        try:
                result = QuService(db).get_qu()
                return JSONResponse(content= jsonable_encoder(result))
        except Exception as e:        
                return JSONResponse(content={"error": f"Error al obtener los Qus: {str(e)}"}, status_code=500)
        finally:
                db.close()

@qu_router.post('/qu',tags=['Qu'],response_model=dict)
def create_qu(qu:Qu)-> dict:
        db = Session()
        try:
                QuService(db).create_qu(qu)
                return JSONResponse(content={"message":"Se han insertado los datos correctamente"}, status_code=200)
        except Exception as e:
                return JSONResponse(content={"error": f"Error al insertar los datos: {str(e)}"}, status_code=500)


@qu_router.put('/qu/{id}', tags=['Qu'], response_model=dict)
def update_qu(id: int, qu: Qu) -> dict:
        db = Session()
        try:               
                QuService(db).update_qu(id, qu)
                return JSONResponse(content={"message": "qu actualizado"})
        except Exception as e:                
                return JSONResponse(content={"error": f"Error al actualizar el qu: {str(e)}"}, status_code=500)
        finally:
                db.close()