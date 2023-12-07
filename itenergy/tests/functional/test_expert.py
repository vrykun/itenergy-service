from fastapi.testclient import TestClient


def test_add_weather_forecast(test_client: TestClient) -> None:
    with test_client:
        create_weather_forecast = test_client.post(
            url='/expert/forecast_switch',
            json=dict(
                forecast_id=7,
                v1_state=1,
                v2_state=1,
                v3_state=1,
                v4_state=1,
                v5_state=0,
                v6_state=0,
                v7_state=1,
                user_id=2))

        assert create_weather_forecast.status_code == 201
