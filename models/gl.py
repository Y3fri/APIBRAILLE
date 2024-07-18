from config.database import Base
from sqlalchemy import Column,Integer,ForeignKey,Boolean,Date,Time
from sqlalchemy.orm import relationship

class Gl(Base):
    __tablename__="gl"

    gl_id = Column(Integer, primary_key = True)
    gl_idestado= Column(Integer, ForeignKey("estado.est_id"), nullable=False)
    gl_fecha=Column(Date)
    gl_hora=Column(Time)
    gl_unol=Column(Boolean)
    gl_dosl=Column(Boolean)
    gl_tresl=Column(Boolean)
    gl_cuatrol=Column(Boolean)
    gl_cincol=Column(Boolean)
    gl_seisl=Column(Boolean)
    gl_unos=Column(Boolean)
    gl_doss=Column(Boolean)
    gl_tress=Column(Boolean)
    gl_cuatros=Column(Boolean)
    gl_cincos=Column(Boolean)
    gl_seiss=Column(Boolean)
    

    
    estado = relationship("Estado", back_populates="gl")
    
    