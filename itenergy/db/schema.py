from sqlalchemy import Column, Integer, Table

from itenergy.db.engine import metadata

forecast_switch = Table(
    'forecast_switch',
    metadata,
    Column('forecast_id', Integer, primary_key=True, index=True, unique=True),
    Column('v1_state', Integer, nullable=False),
    Column('v2_state', Integer, nullable=False),
    Column('v3_state', Integer, nullable=False),
    Column('v4_state', Integer, nullable=False),
    Column('v5_state', Integer, nullable=False),
    Column('v6_state', Integer, nullable=False),
    Column('v7_state', Integer, nullable=False),
    Column('user_id', Integer, nullable=False)
)
