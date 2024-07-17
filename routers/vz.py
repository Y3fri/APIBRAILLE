from fastapi import APIRouter
from fastapi.responses import JSONResponse
from typing import List
from config.database import Session
from models.vz import Vz
from fastapi.encoders import jsonable_encoder
from service.vz_service import VzService
from schemas.vz import Vz


vz_router = APIRouter()


@vz_router.get('/vz',tags=['Vz'], response_model=list[Vz])
def get_vz()-> List [Vz]:
        db = Session()
        try:
                result = VzService(db).get_vz()
                return JSONResponse(content= jsonable_encoder(result))
        except Exception as e:        
                return JSONResponse(content={"error": f"Error al obtener los Vzs: {str(e)}"}, status_code=500)
        finally:
                db.close()

@vz_router.get('/vz/{id}',tags=['Vz'], response_model=list[Vz])
def get_vz(id:int)-> List [Vz]:
        db = Session()
        try:
                result = VzService(db).get_vz_by_id(id)
                return JSONResponse(content= jsonable_encoder(result))
        except Exception as e:        
                return JSONResponse(content={"error": f"Error al obtener los Vzs: {str(e)}"}, status_code=500)
        finally:
                db.close()                

@vz_router.post('/vz',tags=['Vz'],response_model=dict)
def create_vz(vz:Vz)-> dict:
        db = Session()
        try:
                VzService(db).create_vz(vz)
                return JSONResponse(content={"message":"Se han insertado los datos correctamente"}, status_code=200)
        except Exception as e:
                return JSONResponse(content={"error": f"Error al insertar los datos: {str(e)}"}, status_code=500)


@vz_router.put('/vz/{id}', tags=['Vz'], response_model=dict)
def update_vz(id: int, vz: Vz) -> dict:
        db = Session()
        try:               
                VzService(db).update_vz(id, vz)
                return JSONResponse(content={"message": "vz actualizado"})
        except Exception as e:                
                return JSONResponse(content={"error": f"Error al actualizar el vz: {str(e)}"}, status_code=500)
        finally:
                db.close()