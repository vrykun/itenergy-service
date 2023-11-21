from dataclasses import dataclass

from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.engine import Connection

from itenergy.db.schema import forecast_switch


@dataclass
class ForecastSwitch:
    forecast_id: int
    v1_state: int
    v2_state: int
    v3_state: int
    v4_state: int
    v5_state: int
    v6_state: int
    v7_state: int
    user_id: int


def new(forecast_id: int, v1_state: int, v2_state: int, v3_state: int, v4_state: int, v5_state: int,
        v6_state: int, v7_state: int, user_id: int, conn: Connection) -> ForecastSwitch:
    stmt = insert(forecast_switch).values(
        forecast_id=forecast_id,
        v1_state=v1_state,
        v2_state=v2_state,
        v3_state=v3_state,
        v4_state=v4_state,
        v5_state=v5_state,
        v6_state=v6_state,
        v7_state=v7_state,
        user_id=user_id
    ).returning(forecast_switch)
    return ForecastSwitch(**conn.execute(stmt).mappings().one())


def get_forecasts(conn: Connection) -> list[ForecastSwitch]:
    forecasts = conn.execute(forecast_switch.select()).mappings().fetchall()

    return [ForecastSwitch(**forecast) for forecast in forecasts]


def get_forecast(forecast_id: int, conn: Connection) -> ForecastSwitch:
    forecast = conn.execute(forecast_switch.select().where(
        forecast_switch.c.forecast_id == forecast_id)).mappings().one()

    return ForecastSwitch(**forecast)


def delete(forecast_id: int, conn: Connection) -> None:
    conn.execute(forecast_switch.delete().where(forecast_switch.c.forecast_id == forecast_id))
