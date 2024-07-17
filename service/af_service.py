from fastapi import HTTPException
from models.af import Af  as AfModule
from sqlalchemy.orm import Session
from schemas.af import Af
import pytz
from datetime import datetime

local_timezone = pytz.timezone('America/Bogota')

class AfService():

    def __init__(self, db: Session) -> None:
        self.db = db
        
    def get_af(self) :
        try:
            result = self.db.query(AfModule).all()
            af_list = [
                {
                    "af_id": af.af_id,
                    "af_idestado": af.af_idestado,
                    "af_fecha": af.af_fecha,
                    "af_hora": af.af_hora,
                    "af_unol": af.af_unol,
                    "af_dosl": af.af_dosl,
                    "af_tresl": af.af_tresl,
                    "af_cuatrol": af.af_cuatrol,
                    "af_cincol": af.af_cincol,
                    "af_seisl": af.af_seisl,
                    "af_unos": af.af_unos,
                    "af_doss": af.af_doss,
                    "af_tress": af.af_tress,
                    "af_cuatros": af.af_cuatros,
                    "af_cincos": af.af_cincos,
                    "af_seiss": af.af_seiss,
                    "nombre_estado": af.estado.est_nombre,
                }
                for af in result
            ]
            return af_list
        except Exception as e:
            self.db.rollback()
            raise HTTPException(status_code=500, detail=str(e))

    def get_af_by_id(self,id:int) :
        try:
            result = self.db.query(AfModule).filter(AfModule.af_id==id).all()
            af_list = [
                {
                    "af_id": af.af_id,
                    "af_idestado": af.af_idestado,
                    "af_fecha": af.af_fecha,
                    "af_hora": af.af_hora,
                    "af_unol": af.af_unol,
                    "af_dosl": af.af_dosl,
                    "af_tresl": af.af_tresl,
                    "af_cuatrol": af.af_cuatrol,
                    "af_cincol": af.af_cincol,
                    "af_seisl": af.af_seisl,
                    "af_unos": af.af_unos,
                    "af_doss": af.af_doss,
                    "af_tress": af.af_tress,
                    "af_cuatros": af.af_cuatros,
                    "af_cincos": af.af_cincos,
                    "af_seiss": af.af_seiss,
                    "nombre_estado": af.estado.est_nombre,
                }
                for af in result
            ]
            return af_list
        except Exception as e:
            self.db.rollback()
            raise HTTPException(status_code=500, detail=str(e))

    def create_af(self, af: Af):
        try:
            current_datetime = datetime.now(local_timezone)
            current_date = current_datetime.date()
            current_time = current_datetime.time()
            new_af = AfModule(
                af_idestado = 2,
                af_fecha = current_date,
                af_hora = current_time,
                af_unol = af.af_unol,
                af_dosl = af.af_dosl,
                af_tresl = af.af_tresl,
                af_cuatrol = af.af_cuatrol,
                af_cincol = af.af_cincol,
                af_seisl = af.af_seisl,
                af_unos = af.af_unos,
                af_doss = af.af_doss,
                af_tress = af.af_tress,
                af_cuatros = af.af_cuatros,
                af_cincos = af.af_cincos,
                af_seiss = af.af_seiss
            )
            self.db.add(new_af)
            self.db.commit()
            self.db.refresh(new_af)
            return new_af
        except Exception as e:
            self.db.rollback()
            raise HTTPException(status_code=500, detail=str(e))

    def update_af(self, id: int, af: Af):
        try:
            af_record = self.db.query(AfModule).filter(AfModule.af_id == id).first()
            if not af_record:
                raise HTTPException(status_code=404, detail="Af not found")
            
            af_record.af_idestado = af.af_idestado
            af_record.af_fecha = af.af_fecha
            af_record.af_hora = af.af_hora
            af_record.af_unol = af.af_unol
            af_record.af_dosl = af.af_dosl
            af_record.af_tresl = af.af_tresl
            af_record.af_cuatrol = af.af_cuatrol
            af_record.af_cincol = af.af_cincol
            af_record.af_seisl = af.af_seisl
            af_record.af_unos = af.af_unos
            af_record.af_doss = af.af_doss
            af_record.af_tress = af.af_tress
            af_record.af_cuatros = af.af_cuatros
            af_record.af_cincos = af.af_cincos
            af_record.af_seiss = af.af_seiss

            self.db.commit()
            return af_record
        except Exception as e:
            self.db.rollback()
            raise HTTPException(status_code=500, detail=str(e))