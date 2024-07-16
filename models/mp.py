from config.database import Base
from sqlalchemy import Column,Integer,ForeignKey,Boolean,Date,Time
from sqlalchemy.orm import relationship

class Mp(Base):
    __tablename__="mp"

    mp_id = Column(Integer, primary_key = True)
    mp_idestado= Column(Integer, ForeignKey("estado.est_id"), nullable=False)
    mp_fecha=Column(Date)
    mp_hora=Column(Time)
    mp_unol=Column(Boolean)
    mp_dosl=Column(Boolean)
    mp_tresl=Column(Boolean)
    mp_cuatrol=Column(Boolean)
    mp_cincol=Column(Boolean)    
    mp_unos=Column(Boolean)
    mp_doss=Column(Boolean)
    mp_tress=Column(Boolean)
    mp_cuatros=Column(Boolean)
    mp_cincos=Column(Boolean)    
    

    
    estado = relationship("Estado", back_populates="mp")
    
    