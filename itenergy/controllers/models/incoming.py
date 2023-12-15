from pydantic import BaseModel


class EquipmentRequest(BaseModel):
    id: int
    voltage_deviation: float | None = 1
    phase_voltage_ua: float | None = 35
    phase_voltage_ub: float | None = 205
    phase_voltage_uc: float | None = 140
    interphase_voltage_uab: float | None = 220
    interphase_voltage_uac: float | None = 350
    interphase_voltage_ubc: float | None = 300
    asymmetry_coefficient_k2u: float | None = 3
    asymmetry_coefficient_k0u: float | None = 6
    capacity_battery_pb: float | None = 0.5
    current_solar_power: float | None = 1.2
    current_wind_power: float | None = 0.3
    capacity: float | None = 1.7
    solar_battery_power: float | None = 1
    wind_power: float | None = 2
    power_consumption: float | None = 1.5
