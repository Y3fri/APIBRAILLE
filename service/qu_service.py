from fastapi import HTTPException
from models.qu import Qu  as QuModule
from sqlalchemy.orm import Session
from schemas.qu import Qu
import pytz
from datetime import datetime

local_timezone = pytz.timezone('America/Bogota')

class QuService():

    def __init__(self, db: Session) -> None:
        self.db = db
        
    def get_qu(self) :
        try:
            result = self.db.query(QuModule).all()
            qu_list = [
                {
                    "qu_id": qu.qu_id,
                    "qu_idestado": qu.qu_idestado,
                    "qu_fecha": qu.qu_fecha,
                    "qu_hora": qu.qu_hora,
                    "qu_unol": qu.qu_unol,
                    "qu_dosl": qu.qu_dosl,
                    "qu_tresl": qu.qu_tresl,
                    "qu_cuatrol": qu.qu_cuatrol,
                    "qu_cincol": qu.qu_cincol,                    
                    "qu_unos": qu.qu_unos,
                    "qu_doss": qu.qu_doss,
                    "qu_tress": qu.qu_tress,
                    "qu_cuatros": qu.qu_cuatros,
                    "qu_cincos": qu.qu_cincos,                    
                    "nombre_estado": qu.estado.est_nombre,
                }
                for qu in result
            ]
            return qu_list
        except Exception as e:
            self.db.rollback()
            raise HTTPException(status_code=500, detail=str(e))

        
    def create_qu(self, qu: Qu):
        try:
            current_datetime = datetime.now(local_timezone)
            current_date = current_datetime.date()
            current_time = current_datetime.time()
            new_qu = QuModule(
                qu_idestado = 2,
                qu_fecha = current_date,
                qu_hora = current_time,
                qu_unol = qu.qu_unol,
                qu_dosl = qu.qu_dosl,
                qu_tresl = qu.qu_tresl,
                qu_cuatrol = qu.qu_cuatrol,
                qu_cincol = qu.qu_cincol,                
                qu_unos = qu.qu_unos,
                qu_doss = qu.qu_doss,
                qu_tress = qu.qu_tress,
                qu_cuatros = qu.qu_cuatros,
                qu_cincos = qu.qu_cincos,                
            )
            self.db.add(new_qu)
            self.db.commit()
            self.db.refresh(new_qu)
            return new_qu
        except Exception as e:
            self.db.rollback()
            raise HTTPException(status_code=500, detail=str(e))

    def update_qu(self, id: int, qu: Qu):
        try:
            qu_record = self.db.query(QuModule).filter(QuModule.qu_id == id).first()
            if not qu_record:
                raise HTTPException(status_code=404, detail="Qu not found")
            
            qu_record.qu_idestado = qu.qu_idestado
            qu_record.qu_fecha = qu.qu_fecha
            qu_record.qu_hora = qu.qu_hora
            qu_record.qu_unol = qu.qu_unol
            qu_record.qu_dosl = qu.qu_dosl
            qu_record.qu_tresl = qu.qu_tresl
            qu_record.qu_cuatrol = qu.qu_cuatrol
            qu_record.qu_cincol = qu.qu_cincol            
            qu_record.qu_unos = qu.qu_unos
            qu_record.qu_doss = qu.qu_doss
            qu_record.qu_tress = qu.qu_tress
            qu_record.qu_cuatros = qu.qu_cuatros
            qu_record.qu_cincos = qu.qu_cincos            

            self.db.commit()
            return qu_record
        except Exception as e:
            self.db.rollback()
            raise HTTPException(status_code=500, detail=str(e))