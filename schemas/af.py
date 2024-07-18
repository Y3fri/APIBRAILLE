from pydantic import BaseModel
from datetime import date, time
from typing import Optional

class Af(BaseModel):
    af_id: Optional[int] = None
    af_idestado: int
    af_fecha: Optional[date] 
    af_hora: Optional[time] 
    af_unol: Optional[bool] 
    af_dosl: Optional[bool] 
    af_tresl: Optional[bool] 
    af_cuatrol: Optional[bool] 
    af_cincol: Optional[bool] 
    af_seisl: Optional[bool] 
    af_unos: Optional[bool] 
    af_doss: Optional[bool] 
    af_tress: Optional[bool] 
    af_cuatros: Optional[bool] 
    af_cincos: Optional[bool] 
    af_seiss: Optional[bool]     
