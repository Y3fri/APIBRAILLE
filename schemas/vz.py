from pydantic import BaseModel
from datetime import date, time
from typing import Optional

class Vz(BaseModel):
    vz_id: Optional[int] = None
    vz_idestado: int
    vz_fecha: Optional[date] 
    vz_hora: Optional[time] 
    vz_unol: Optional[bool] 
    vz_dosl: Optional[bool] 
    vz_tresl: Optional[bool] 
    vz_cuatrol: Optional[bool] 
    vz_cincol: Optional[bool]     
    vz_unos: Optional[bool] 
    vz_doss: Optional[bool] 
    vz_tress: Optional[bool] 
    vz_cuatros: Optional[bool] 
    vz_cincos: Optional[bool]          
