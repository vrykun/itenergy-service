from pydantic import BaseModel


class Forecast(BaseModel):  # type: ignore
    forecast_id: int
    v1_state: int
    v2_state: int
    v3_state: int
    v4_state: int
    v5_state: int
    v6_state: int
    v7_state: int
    user_id: int
