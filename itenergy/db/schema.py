from sqlalchemy import FLOAT, Column, Integer, Table

from itenergy.db.engine import metadata

equipment_data = Table(
    'equipment',
    metadata,
    Column('id', Integer, primary_key=True, index=True, unique=True),
    Column('voltage_deviation', FLOAT, nullable=True),
    Column('phase_voltage_ua', FLOAT, nullable=True),
    Column('phase_voltage_ub', FLOAT, nullable=True),
    Column('phase_voltage_uc', FLOAT, nullable=True),
    Column('interphase_voltage_uab', FLOAT, nullable=True),
    Column('interphase_voltage_uac', FLOAT, nullable=True),
    Column('interphase_voltage_ubc', FLOAT, nullable=True),
    Column('asymmetry_coefficient_k2u', FLOAT, nullable=True),
    Column('asymmetry_coefficient_k0u', FLOAT, nullable=True),
    Column('capacity_battery_pb', FLOAT, nullable=True),
    Column('current_solar_power', FLOAT, nullable=True),
    Column('current_wind_power', FLOAT, nullable=True),
    Column('capacity', FLOAT, nullable=True),
    Column('solar_battery_power', FLOAT, nullable=True),
    Column('wind_power', FLOAT, nullable=True),
    Column('power_consumption', FLOAT, nullable=True)
)

indicator_data = Table(
    'indicator',
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
