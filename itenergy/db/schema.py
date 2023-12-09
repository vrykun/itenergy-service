from sqlalchemy import Column, Integer, Table

from itenergy.db.engine import metadata

equipment_data = Table(
    'equipment_data',
    metadata,
    Column('id', Integer, primary_key=True, index=True, unique=True),
    Column('current_solar_power', Integer, nullable=False),
    Column('current_wind_power', Integer, nullable=False),
    Column('capacity', Integer, nullable=False),
    Column('solar_battery_power', Integer, nullable=False),
    Column('wind_power', Integer, nullable=False),
    Column('power_consumption', Integer, nullable=False)
)

indicator_data = Table(
    'indicator_data',
    metadata,
    Column('id', Integer, primary_key=True, index=True, unique=True),
    Column('voltage_deviation', Integer, nullable=False),
    Column('phase_voltage_ua', Integer, nullable=False),
    Column('phase_voltage_ub', Integer, nullable=False),
    Column('phase_voltage_uc', Integer, nullable=False),
    Column('interphase_voltage_uab', Integer, nullable=False),
    Column('interphase_voltage_uac', Integer, nullable=False),
    Column('interphase_voltage_ubc', Integer, nullable=False),
    Column('asymmetry_coefficient_k2u', Integer, nullable=False),
    Column('asymmetry_coefficient_k0u', Integer, nullable=False),
    Column('capacity_battery_pb', Integer, nullable=False),
    Column('current_solar_power', Integer, nullable=False),
    Column('current_wind_power', Integer, nullable=False),
    Column('capacity', Integer, nullable=False),
    Column('solar_battery_power', Integer, nullable=False),
    Column('wind_power', Integer, nullable=False),
    Column('power_consumption', Integer, nullable=False)
)
