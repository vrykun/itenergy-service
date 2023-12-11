from dataclasses import dataclass

from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.engine import Connection

from itenergy.db.schema import equipment_data


@dataclass
class Equipment:
    id: int
    voltage_deviation: float | None = None
    phase_voltage_ua: float | None = None
    phase_voltage_ub: float | None = None
    phase_voltage_uc: float | None = None
    interphase_voltage_uab: float | None = None
    interphase_voltage_uac: float | None = None
    interphase_voltage_ubc: float | None = None
    asymmetry_coefficient_k2u: float | None = None
    asymmetry_coefficient_k0u: float | None = None
    capacity_battery_pb: float | None = None
    current_solar_power: float | None = None
    current_wind_power: float | None = None
    capacity: float | None = None
    solar_battery_power: float | None = None
    wind_power: float | None = None
    power_consumption: float | None = None


def new(id: int,
        voltage_deviation: float | None,
        phase_voltage_ua: float | None,
        phase_voltage_ub: float | None,
        phase_voltage_uc: float | None,
        interphase_voltage_uab: float | None,
        interphase_voltage_uac: float | None,
        interphase_voltage_ubc: float | None,
        asymmetry_coefficient_k2u: float | None,
        asymmetry_coefficient_k0u: float | None,
        capacity_battery_pb: float | None,
        current_solar_power: float | None,
        current_wind_power: float | None,
        capacity: float | None,
        solar_battery_power: float | None,
        wind_power: float | None,
        power_consumption: float | None,
        conn: Connection
        ) -> Equipment:
    set_fields = dict(
        id=id,
        voltage_deviation=voltage_deviation,
        phase_voltage_ua=phase_voltage_ua,
        phase_voltage_ub=phase_voltage_ub,
        phase_voltage_uc=phase_voltage_uc,
        interphase_voltage_uab=interphase_voltage_uab,
        interphase_voltage_uac=interphase_voltage_uac,
        interphase_voltage_ubc=interphase_voltage_ubc,
        asymmetry_coefficient_k2u=asymmetry_coefficient_k2u,
        asymmetry_coefficient_k0u=asymmetry_coefficient_k0u,
        capacity_battery_pb=capacity_battery_pb,
        current_solar_power=current_solar_power,
        current_wind_power=current_wind_power,
        capacity=capacity,
        solar_battery_power=solar_battery_power,
        wind_power=wind_power,
        power_consumption=power_consumption)
    stmt = (insert(equipment_data).values(
        set_fields,
    ).on_conflict_do_update(constraint='equipment_pkey', set_=set_fields).returning(equipment_data))
    return Equipment(**conn.execute(stmt).mappings().one())


def get_equipments(conn: Connection) -> list[Equipment]:
    equipments = conn.execute(equipment_data.select()).mappings().fetchall()

    return [Equipment(**equipment) for equipment in equipments]


def get_equipment(id: int, conn: Connection) -> Equipment:
    equipment = conn.execute(equipment_data.select().where(
        equipment_data.c.id == id)).mappings().one()

    return Equipment(**equipment)


def delete(id: int, conn: Connection) -> None:
    conn.execute(equipment_data.delete().where(equipment_data.c.id == id))
