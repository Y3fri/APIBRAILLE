from fastapi import APIRouter
from fastapi.responses import JSONResponse
from typing import List
from config.database import Session
from models.gl import Gl
from fastapi.encoders import jsonable_encoder
from service.gl_service import GlService
from schemas.gl import Gl


gl_router = APIRouter()


@gl_router.get('/gl',tags=['Gl'], response_model=list[Gl])
def get_gl()-> List [Gl]:
        db = Session()
        try:
                result = GlService(db).get_gl()
                return JSONResponse(content= jsonable_encoder(result))
        except Exception as e:        
                return JSONResponse(content={"error": f"Error al obtener los Gls: {str(e)}"}, status_code=500)
        finally:
                db.close()

@gl_router.post('/gl',tags=['Gl'],response_model=dict)
def create_gl(gl:Gl)-> dict:
        db = Session()
        try:
                GlService(db).create_gl(gl)
                return JSONResponse(content={"message":"Se han insertado los datos correctamente"}, status_code=200)
        except Exception as e:
                return JSONResponse(content={"error": f"Error al insertar los datos: {str(e)}"}, status_code=500)


@gl_router.put('/gl/{id}', tags=['Gl'], response_model=dict)
def update_gl(id: int, gl: Gl) -> dict:
        db = Session()
        try:               
                GlService(db).update_gl(id, gl)
                return JSONResponse(content={"message": "gl actualizado"})
        except Exception as e:                
                return JSONResponse(content={"error": f"Error al actualizar el gl: {str(e)}"}, status_code=500)
        finally:
                db.close()