from fastapi import HTTPException
from models.mp import Mp  as MpModule
from sqlalchemy.orm import Session
from schemas.mp import Mp
import pytz
from datetime import datetime

local_timezone = pytz.timezone('America/Bogota')

class MpService():

    def __init__(self, db: Session) -> None:
        self.db = db
        
    def get_mp(self) :
        try:
            result = self.db.query(MpModule).all()
            mp_list = [
                {
                    "mp_id": mp.mp_id,
                    "mp_idestado": mp.mp_idestado,
                    "mp_fecha": mp.mp_fecha,
                    "mp_hora": mp.mp_hora,
                    "mp_unol": mp.mp_unol,
                    "mp_dosl": mp.mp_dosl,
                    "mp_tresl": mp.mp_tresl,
                    "mp_cuatrol": mp.mp_cuatrol,
                    "mp_cincol": mp.mp_cincol,                    
                    "mp_unos": mp.mp_unos,
                    "mp_doss": mp.mp_doss,
                    "mp_tress": mp.mp_tress,
                    "mp_cuatros": mp.mp_cuatros,
                    "mp_cincos": mp.mp_cincos,                    
                    "nombre_estado": mp.estado.est_nombre,
                }
                for mp in result
            ]
            return mp_list
        except Exception as e:
            self.db.rollback()
            raise HTTPException(status_code=500, detail=str(e))

        
    def create_mp(self, mp: Mp):
        try:
            current_datetime = datetime.now(local_timezone)
            current_date = current_datetime.date()
            current_time = current_datetime.time()
            new_mp = MpModule(
                mp_idestado = 2,
                mp_fecha = current_date,
                mp_hora = current_time,
                mp_unol = mp.mp_unol,
                mp_dosl = mp.mp_dosl,
                mp_tresl = mp.mp_tresl,
                mp_cuatrol = mp.mp_cuatrol,
                mp_cincol = mp.mp_cincol,                
                mp_unos = mp.mp_unos,
                mp_doss = mp.mp_doss,
                mp_tress = mp.mp_tress,
                mp_cuatros = mp.mp_cuatros,
                mp_cincos = mp.mp_cincos,                
            )
            self.db.add(new_mp)
            self.db.commit()
            self.db.refresh(new_mp)
            return new_mp
        except Exception as e:
            self.db.rollback()
            raise HTTPException(status_code=500, detail=str(e))

    def update_mp(self, id: int, mp: Mp):
        try:
            mp_record = self.db.query(MpModule).filter(MpModule.mp_id == id).first()
            if not mp_record:
                raise HTTPException(status_code=404, detail="Mp not found")
            
            mp_record.mp_idestado = mp.mp_idestado
            mp_record.mp_fecha = mp.mp_fecha
            mp_record.mp_hora = mp.mp_hora
            mp_record.mp_unol = mp.mp_unol
            mp_record.mp_dosl = mp.mp_dosl
            mp_record.mp_tresl = mp.mp_tresl
            mp_record.mp_cuatrol = mp.mp_cuatrol
            mp_record.mp_cincol = mp.mp_cincol            
            mp_record.mp_unos = mp.mp_unos
            mp_record.mp_doss = mp.mp_doss
            mp_record.mp_tress = mp.mp_tress
            mp_record.mp_cuatros = mp.mp_cuatros
            mp_record.mp_cincos = mp.mp_cincos            

            self.db.commit()
            return mp_record
        except Exception as e:
            self.db.rollback()
            raise HTTPException(status_code=500, detail=str(e))