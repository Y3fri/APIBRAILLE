from config.database import Base
from sqlalchemy import Column,Integer,ForeignKey,Boolean,Date,Time
from sqlalchemy.orm import relationship

class Vz(Base):
    __tablename__="vz"

    vz_id = Column(Integer, primary_key = True)
    vz_idestado= Column(Integer, ForeignKey("estado.est_id"), nullable=False)
    vz_fecha=Column(Date)
    vz_hora=Column(Time)
    vz_unol=Column(Boolean)
    vz_dosl=Column(Boolean)
    vz_tresl=Column(Boolean)
    vz_cuatrol=Column(Boolean)
    vz_cincol=Column(Boolean)    
    vz_unos=Column(Boolean)
    vz_doss=Column(Boolean)
    vz_tress=Column(Boolean)
    vz_cuatros=Column(Boolean)
    vz_cincos=Column(Boolean)    
    

    
    estado = relationship("Estado", back_populates="vz")
    
    