from config.database import Base
from sqlalchemy import Column,Integer,ForeignKey,Boolean,Date,Time
from sqlalchemy.orm import relationship

class Af(Base):
    __tablename__="af"

    af_id = Column(Integer, primary_key = True)
    af_idestado= Column(Integer, ForeignKey("estado.est_id"), nullable=False)
    af_fecha=Column(Date)
    af_hora=Column(Time)
    af_unol=Column(Boolean)
    af_dosl=Column(Boolean)
    af_tresl=Column(Boolean)
    af_cuatrol=Column(Boolean)
    af_cincol=Column(Boolean)
    af_seisl=Column(Boolean)
    af_unos=Column(Boolean)
    af_doss=Column(Boolean)
    af_tress=Column(Boolean)
    af_cuatros=Column(Boolean)
    af_cincos=Column(Boolean)
    af_seiss=Column(Boolean)
    

    
    estado = relationship("Estado", back_populates="af")
    
    