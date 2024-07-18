from config.database import Base
from sqlalchemy import Column,Integer,String,Float
from sqlalchemy.orm import relationship

class Estado(Base):
    __tablename__="estado"

    est_id = Column(Integer, primary_key = True)
    est_nombre=Column(String(30))

    
    user = relationship("User", back_populates="estado")
    af = relationship("Af", back_populates="estado")
    gl = relationship("Gl", back_populates="estado")
    mp = relationship("Mp", back_populates="estado")
    qu = relationship("Qu", back_populates="estado")
    vz = relationship("Vz", back_populates="estado")
    
    
