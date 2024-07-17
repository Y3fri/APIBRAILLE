from fastapi import HTTPException
from models.gl import Gl  as GlModule
from sqlalchemy.orm import Session
from schemas.gl import Gl
import pytz
from datetime import datetime

local_timezone = pytz.timezone('America/Bogota')

class GlService():

    def __init__(self, db: Session) -> None:
        self.db = db
        
    def get_gl(self) :
        try:
            result = self.db.query(GlModule).all()
            gl_list = [
                {
                    "gl_id": gl.gl_id,
                    "gl_idestado": gl.gl_idestado,
                    "gl_fecha": gl.gl_fecha,
                    "gl_hora": gl.gl_hora,
                    "gl_unol": gl.gl_unol,
                    "gl_dosl": gl.gl_dosl,
                    "gl_tresl": gl.gl_tresl,
                    "gl_cuatrol": gl.gl_cuatrol,
                    "gl_cincol": gl.gl_cincol,
                    "gl_seisl": gl.gl_seisl,
                    "gl_unos": gl.gl_unos,
                    "gl_doss": gl.gl_doss,
                    "gl_tress": gl.gl_tress,
                    "gl_cuatros": gl.gl_cuatros,
                    "gl_cincos": gl.gl_cincos,
                    "gl_seiss": gl.gl_seiss,
                    "nombre_estado": gl.estado.est_nombre,
                }
                for gl in result
            ]
            return gl_list
        except Exception as e:
            self.db.rollback()
            raise HTTPException(status_code=500, detail=str(e))

    def get_gl_by_id(self,id:int) :
        try:
            result = self.db.query(GlModule).filter(GlModule.gl_id ==id).all()
            gl_list = [
                {
                    "gl_id": gl.gl_id,
                    "gl_idestado": gl.gl_idestado,
                    "gl_fecha": gl.gl_fecha,
                    "gl_hora": gl.gl_hora,
                    "gl_unol": gl.gl_unol,
                    "gl_dosl": gl.gl_dosl,
                    "gl_tresl": gl.gl_tresl,
                    "gl_cuatrol": gl.gl_cuatrol,
                    "gl_cincol": gl.gl_cincol,
                    "gl_seisl": gl.gl_seisl,
                    "gl_unos": gl.gl_unos,
                    "gl_doss": gl.gl_doss,
                    "gl_tress": gl.gl_tress,
                    "gl_cuatros": gl.gl_cuatros,
                    "gl_cincos": gl.gl_cincos,
                    "gl_seiss": gl.gl_seiss,
                    "nombre_estado": gl.estado.est_nombre,
                }
                for gl in result
            ]
            return gl_list
        except Exception as e:
            self.db.rollback()
            raise HTTPException(status_code=500, detail=str(e))

        
    def create_gl(self, gl: Gl):
        try:
            current_datetime = datetime.now(local_timezone)
            current_date = current_datetime.date()
            current_time = current_datetime.time()
            new_gl = GlModule(
                gl_idestado = 2,
                gl_fecha = current_date,
                gl_hora = current_time,
                gl_unol = gl.gl_unol,
                gl_dosl = gl.gl_dosl,
                gl_tresl = gl.gl_tresl,
                gl_cuatrol = gl.gl_cuatrol,
                gl_cincol = gl.gl_cincol,
                gl_seisl = gl.gl_seisl,
                gl_unos = gl.gl_unos,
                gl_doss = gl.gl_doss,
                gl_tress = gl.gl_tress,
                gl_cuatros = gl.gl_cuatros,
                gl_cincos = gl.gl_cincos,
                gl_seiss = gl.gl_seiss
            )
            self.db.add(new_gl)
            self.db.commit()
            self.db.refresh(new_gl)
            return new_gl
        except Exception as e:
            self.db.rollback()
            raise HTTPException(status_code=500, detail=str(e))

    def update_gl(self, id: int, gl: Gl):
        try:
            gl_record = self.db.query(GlModule).filter(GlModule.gl_id == id).first()
            if not gl_record:
                raise HTTPException(status_code=404, detail="Gl not found")
            
            gl_record.gl_idestado = gl.gl_idestado
            gl_record.gl_fecha = gl.gl_fecha
            gl_record.gl_hora = gl.gl_hora
            gl_record.gl_unol = gl.gl_unol
            gl_record.gl_dosl = gl.gl_dosl
            gl_record.gl_tresl = gl.gl_tresl
            gl_record.gl_cuatrol = gl.gl_cuatrol
            gl_record.gl_cincol = gl.gl_cincol
            gl_record.gl_seisl = gl.gl_seisl
            gl_record.gl_unos = gl.gl_unos
            gl_record.gl_doss = gl.gl_doss
            gl_record.gl_tress = gl.gl_tress
            gl_record.gl_cuatros = gl.gl_cuatros
            gl_record.gl_cincos = gl.gl_cincos
            gl_record.gl_seiss = gl.gl_seiss

            self.db.commit()
            return gl_record
        except Exception as e:
            self.db.rollback()
            raise HTTPException(status_code=500, detail=str(e))