from fastapi import HTTPException
from models.vz import Vz  as VzModule
from sqlalchemy.orm import Session
from schemas.vz import Vz
import pytz
from datetime import datetime

local_timezone = pytz.timezone('America/Bogota')

class VzService():

    def __init__(self, db: Session) -> None:
        self.db = db
        
    def get_vz(self) :
        try:
            result = self.db.query(VzModule).all()
            vz_list = [
                {
                    "vz_id": vz.vz_id,
                    "vz_idestado": vz.vz_idestado,
                    "vz_fecha": vz.vz_fecha,
                    "vz_hora": vz.vz_hora,
                    "vz_unol": vz.vz_unol,
                    "vz_dosl": vz.vz_dosl,
                    "vz_tresl": vz.vz_tresl,
                    "vz_cuatrol": vz.vz_cuatrol,
                    "vz_cincol": vz.vz_cincol,                    
                    "vz_unos": vz.vz_unos,
                    "vz_doss": vz.vz_doss,
                    "vz_tress": vz.vz_tress,
                    "vz_cuatros": vz.vz_cuatros,
                    "vz_cincos": vz.vz_cincos,                    
                    "nombre_estado": vz.estado.est_nombre,
                }
                for vz in result
            ]
            return vz_list
        except Exception as e:
            self.db.rollback()
            raise HTTPException(status_code=500, detail=str(e))

    def get_vz_by_id(self,id:int) :
        try:
            result = self.db.query(VzModule).filter(VzModule.vz_id==id).all()
            vz_list = [
                {
                    "vz_id": vz.vz_id,
                    "vz_idestado": vz.vz_idestado,
                    "vz_fecha": vz.vz_fecha,
                    "vz_hora": vz.vz_hora,
                    "vz_unol": vz.vz_unol,
                    "vz_dosl": vz.vz_dosl,
                    "vz_tresl": vz.vz_tresl,
                    "vz_cuatrol": vz.vz_cuatrol,
                    "vz_cincol": vz.vz_cincol,                    
                    "vz_unos": vz.vz_unos,
                    "vz_doss": vz.vz_doss,
                    "vz_tress": vz.vz_tress,
                    "vz_cuatros": vz.vz_cuatros,
                    "vz_cincos": vz.vz_cincos,                    
                    "nombre_estado": vz.estado.est_nombre,
                }
                for vz in result
            ]
            return vz_list
        except Exception as e:
            self.db.rollback()
            raise HTTPException(status_code=500, detail=str(e))
        
    def create_vz(self, vz: Vz):
        try:
            current_datetime = datetime.now(local_timezone)
            current_date = current_datetime.date()
            current_time = current_datetime.time()
            new_vz = VzModule(
                vz_idestado = 2,
                vz_fecha = current_date,
                vz_hora = current_time,
                vz_unol = vz.vz_unol,
                vz_dosl = vz.vz_dosl,
                vz_tresl = vz.vz_tresl,
                vz_cuatrol = vz.vz_cuatrol,
                vz_cincol = vz.vz_cincol,                
                vz_unos = vz.vz_unos,
                vz_doss = vz.vz_doss,
                vz_tress = vz.vz_tress,
                vz_cuatros = vz.vz_cuatros,
                vz_cincos = vz.vz_cincos,                
            )
            self.db.add(new_vz)
            self.db.commit()
            self.db.refresh(new_vz)
            return new_vz
        except Exception as e:
            self.db.rollback()
            raise HTTPException(status_code=500, detail=str(e))

    def update_vz(self, id: int, vz: Vz):
        try:
            vz_record = self.db.query(VzModule).filter(VzModule.vz_id == id).first()
            if not vz_record:
                raise HTTPException(status_code=404, detail="Vz not found")
            
            vz_record.vz_idestado = vz.vz_idestado
            vz_record.vz_fecha = vz.vz_fecha
            vz_record.vz_hora = vz.vz_hora
            vz_record.vz_unol = vz.vz_unol
            vz_record.vz_dosl = vz.vz_dosl
            vz_record.vz_tresl = vz.vz_tresl
            vz_record.vz_cuatrol = vz.vz_cuatrol
            vz_record.vz_cincol = vz.vz_cincol            
            vz_record.vz_unos = vz.vz_unos
            vz_record.vz_doss = vz.vz_doss
            vz_record.vz_tress = vz.vz_tress
            vz_record.vz_cuatros = vz.vz_cuatros
            vz_record.vz_cincos = vz.vz_cincos            

            self.db.commit()
            return vz_record
        except Exception as e:
            self.db.rollback()
            raise HTTPException(status_code=500, detail=str(e))