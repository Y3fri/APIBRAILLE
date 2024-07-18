from pydantic import BaseModel
from datetime import date, time
from typing import Optional

class Mp(BaseModel):
    mp_id: Optional[int] = None
    mp_idestado: int
    mp_fecha: Optional[date] 
    mp_hora: Optional[time] 
    mp_unol: Optional[bool] 
    mp_dosl: Optional[bool] 
    mp_tresl: Optional[bool] 
    mp_cuatrol: Optional[bool] 
    mp_cincol: Optional[bool]      
    mp_unos: Optional[bool] 
    mp_doss: Optional[bool] 
    mp_tress: Optional[bool] 
    mp_cuatros: Optional[bool] 
    mp_cincos: Optional[bool]          
