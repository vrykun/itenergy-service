from pydantic import BaseModel


class Forecast(BaseModel):
    forecast_id: str
    v1_state: str
    v2_state: str
    v3_state: str
    v4_state: str
    v5_state: str
    v6_state: str
    v7_state: str
    user_id: int
