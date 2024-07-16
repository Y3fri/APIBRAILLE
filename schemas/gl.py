from pydantic import BaseModel
from datetime import date, time
from typing import Optional

class Gl(BaseModel):
    gl_id: Optional[int] = None
    gl_idestado: int
    gl_fecha: Optional[date] 
    gl_hora: Optional[time] 
    gl_unol: Optional[bool] 
    gl_dosl: Optional[bool] 
    gl_tresl: Optional[bool] 
    gl_cuatrol: Optional[bool] 
    gl_cincol: Optional[bool] 
    gl_seisl: Optional[bool] 
    gl_unos: Optional[bool] 
    gl_doss: Optional[bool] 
    gl_tress: Optional[bool] 
    gl_cuatros: Optional[bool] 
    gl_cincos: Optional[bool] 
    gl_seiss: Optional[bool]     
