from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from typing import List
from config.database import Session
from middlewares.jwt_bearer import JWTBearer
from models.af import Af
from fastapi.encoders import jsonable_encoder
from service.af_service import AfService
from schemas.af import Af


af_router = APIRouter()


@af_router.get('/af',tags=['Af'], response_model=list[Af],dependencies=[Depends(JWTBearer())])
def get_af()-> List [Af]:
        db = Session()
        try:
                result = AfService(db).get_af()
                return JSONResponse(content= jsonable_encoder(result))
        except Exception as e:        
                return JSONResponse(content={"error": f"Error al obtener los Afs: {str(e)}"}, status_code=500)
        finally:
                db.close()

@af_router.get('/af/{id}',tags=['Af'], response_model=list[Af],dependencies=[Depends(JWTBearer())])
def get_af(id:int)-> List [Af]:
        db = Session()
        try:
                result = AfService(db).get_af_by_id(id)
                return JSONResponse(content= jsonable_encoder(result))
        except Exception as e:        
                return JSONResponse(content={"error": f"Error al obtener los Afs: {str(e)}"}, status_code=500)
        finally:
                db.close()

@af_router.post('/af',tags=['Af'],response_model=dict)
def create_af(af:Af)-> dict:
        db = Session()
        try:
                AfService(db).create_af(af)
                return JSONResponse(content={"message":"Se han insertado los datos correctamente"}, status_code=200)
        except Exception as e:
                return JSONResponse(content={"error": f"Error al insertar los datos: {str(e)}"}, status_code=500)


@af_router.put('/af/{id}', tags=['Af'], response_model=dict,dependencies=[Depends(JWTBearer())])
def update_af(id: int, af: Af) -> dict:
        db = Session()
        try:               
                AfService(db).update_af(id, af)
                return JSONResponse(content={"message": "af actualizado"})
        except Exception as e:                
                return JSONResponse(content={"error": f"Error al actualizar el af: {str(e)}"}, status_code=500)
        finally:
                db.close()