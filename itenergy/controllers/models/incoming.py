from decimal import Decimal

from pydantic import BaseModel, condecimal


class EquipmentRequest(BaseModel):
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
