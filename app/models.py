from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey, Text, Date
from sqlalchemy.orm import relationship
from .db import Base


class College(Base):
    __tablename__ = "colleges"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    type = Column(String, default="govt")
    state = Column(String, index=True)
    district = Column(String, index=True)
    has_hostel = Column(Boolean, default=False)
    medium = Column(String, default="English")

    programs = relationship("Program", back_populates="college")


class Program(Base):
    __tablename__ = "programs"

    id = Column(Integer, primary_key=True, index=True)
    college_id = Column(Integer, ForeignKey("colleges.id"))
    name = Column(String, nullable=False)
    degree = Column(String, nullable=False)
    duration_months = Column(Integer, default=36)

    college = relationship("College", back_populates="programs")
    cutoffs = relationship("ProgramCutoff", back_populates="program")


class ProgramCutoff(Base):
    __tablename__ = "program_cutoffs"

    id = Column(Integer, primary_key=True, index=True)
    program_id = Column(Integer, ForeignKey("programs.id"))
    year = Column(Integer, nullable=False)
    category = Column(String, default="GEN")
    exam = Column(String, default="STATE")
    cutoff_score = Column(Float, nullable=True)

    program = relationship("Program", back_populates="cutoffs")


class Scholarship(Base):
    __tablename__ = "scholarships"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    state = Column(String, index=True)
    level = Column(String, default="UG")
    amount = Column(Integer, default=0)
    deadline = Column(Date, nullable=True)
    provider = Column(String, default="State")
    eligibility_text = Column(Text, default="")


