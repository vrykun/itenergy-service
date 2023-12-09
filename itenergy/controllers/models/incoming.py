from pydantic import BaseModel


class Forecast(BaseModel):
    id: int
    current_solar_power: int
    current_wind_power: int
    capacity: int
    solar_battery_power: int
    wind_power: int
    power_consumption: int
