from config.database import Base
from sqlalchemy import Column,Integer,ForeignKey,Boolean,Date,Time
from sqlalchemy.orm import relationship

class Qu(Base):
    __tablename__="qu"

    qu_id = Column(Integer, primary_key = True)
    qu_idestado= Column(Integer, ForeignKey("estado.est_id"), nullable=False)
    qu_fecha=Column(Date)
    qu_hora=Column(Time)
    qu_unol=Column(Boolean)
    qu_dosl=Column(Boolean)
    qu_tresl=Column(Boolean)
    qu_cuatrol=Column(Boolean)
    qu_cincol=Column(Boolean)    
    qu_unos=Column(Boolean)
    qu_doss=Column(Boolean)
    qu_tress=Column(Boolean)
    qu_cuatros=Column(Boolean)
    qu_cincos=Column(Boolean)    
    

    
    estado = relationship("Estado", back_populates="qu")
    
    