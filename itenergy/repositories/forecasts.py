from dataclasses import dataclass

from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.engine import Connection

from itenergy.db.schema import equipment_data


@dataclass
class EquipmentData:
    id: int
    current_solar_power: int
    current_wind_power: int
    capacity: int
    solar_battery_power: int
    wind_power: int
    power_consumption: int


def new(id: int, current_solar_power: int, current_wind_power: int, capacity: int,
        solar_battery_power: int, wind_power: int, power_consumption: int, conn: Connection
        ) -> EquipmentData:
    stmt = insert(equipment_data).values(
        id=id,
        current_solar_power=current_solar_power,
        current_wind_power=current_wind_power,
        capacity=capacity,
        solar_battery_power=solar_battery_power,
        wind_power=wind_power,
        power_consumption=power_consumption,
    ).returning(equipment_data)
    return EquipmentData(**conn.execute(stmt).mappings().one())


def get_forecasts(conn: Connection) -> list[EquipmentData]:
    forecasts = conn.execute(equipment_data.select()).mappings().fetchall()

    return [EquipmentData(**forecast) for forecast in forecasts]


def get_forecast(id: int, conn: Connection) -> EquipmentData:
    forecast = conn.execute(equipment_data.select().where(
        equipment_data.c.id == id)).mappings().one()

    return EquipmentData(**forecast)


def delete(id: int, conn: Connection) -> None:
    conn.execute(equipment_data.delete().where(equipment_data.c.id == id))
