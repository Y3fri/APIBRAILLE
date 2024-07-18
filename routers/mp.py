from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from typing import List
from config.database import Session
from middlewares.jwt_bearer import JWTBearer
from models.mp import Mp
from fastapi.encoders import jsonable_encoder
from service.mp_service import MpService
from schemas.mp import Mp


mp_router = APIRouter()


@mp_router.get('/mp',tags=['Mp'], response_model=list[Mp],dependencies=[Depends(JWTBearer())])
def get_mp()-> List [Mp]:
        db = Session()
        try:
                result = MpService(db).get_mp()
                return JSONResponse(content= jsonable_encoder(result))
        except Exception as e:        
                return JSONResponse(content={"error": f"Error al obtener los Mps: {str(e)}"}, status_code=500)
        finally:
                db.close()

@mp_router.get('/mp/{id}',tags=['Mp'], response_model=list[Mp],dependencies=[Depends(JWTBearer())])
def get_mp(id:int)-> List [Mp]:
        db = Session()
        try:
                result = MpService(db).get_mp_by_id(id)
                return JSONResponse(content= jsonable_encoder(result))
        except Exception as e:        
                return JSONResponse(content={"error": f"Error al obtener los Mps: {str(e)}"}, status_code=500)
        finally:
                db.close()

@mp_router.post('/mp',tags=['Mp'],response_model=dict,dependencies=[Depends(JWTBearer())])
def create_mp(mp:Mp)-> dict:
        db = Session()
        try:
                MpService(db).create_mp(mp)
                return JSONResponse(content={"message":"Se han insertado los datos correctamente"}, status_code=200)
        except Exception as e:
                return JSONResponse(content={"error": f"Error al insertar los datos: {str(e)}"}, status_code=500)


@mp_router.put('/mp/{id}', tags=['Mp'], response_model=dict)
def update_mp(id: int, mp: Mp) -> dict:
        db = Session()
        try:               
                MpService(db).update_mp(id, mp)
                return JSONResponse(content={"message": "mp actualizado"})
        except Exception as e:                
                return JSONResponse(content={"error": f"Error al actualizar el mp: {str(e)}"}, status_code=500)
        finally:
                db.close()