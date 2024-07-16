from pydantic import BaseModel
from datetime import date, time
from typing import Optional

class Qu(BaseModel):
    qu_id: Optional[int] = None
    qu_idestado: int
    qu_fecha: Optional[date] 
    qu_hora: Optional[time] 
    qu_unol: Optional[bool] 
    qu_dosl: Optional[bool] 
    qu_tresl: Optional[bool] 
    qu_cuatrol: Optional[bool] 
    qu_cincol: Optional[bool]     
    qu_unos: Optional[bool] 
    qu_doss: Optional[bool] 
    qu_tress: Optional[bool] 
    qu_cuatros: Optional[bool] 
    qu_cincos: Optional[bool]         
