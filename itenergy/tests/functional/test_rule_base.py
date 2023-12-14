import random

from fastapi.testclient import TestClient


def test_rule_base_controller(test_client: TestClient) -> None:
    rule_base_id = random.randint(0, 9)
    input_json = {"input": [
        {
            "name": "Відхилення напруги δUy",
            "setsName": [
                "Low",
                "Normal",
                "High"
            ],
            "sets": [
                [
                    0,
                    0,
                    0.9,
                    0.95
                ],
                [
                    0.9,
                    0.95,
                    1.05,
                    1.1
                ],
                [
                    1.05,
                    1.1,
                    2,
                    2
                ]
            ]
        }]
    }
    switch_json = {
        "switch": [
            {
                "mkol_off": 16,
                "mkol_on": 26,
                "kol_off_diap": [
                    2,
                    2,
                    2,
                    2,
                    2,
                    2,
                    2,
                    2
                ]
            }
        ]
    }
    rule_base_body = dict(
        id=rule_base_id,
        input=input_json,
        switch=switch_json)

    with test_client:
        # test POST
        create_equipment = test_client.post(
            url='/rule_base/',
            json=rule_base_body)

        assert create_equipment.status_code == 201

        # test GET
        create_equipment = test_client.get(
            url=f'/rule_base/{rule_base_id}')

        assert create_equipment.status_code == 200

        # test DELETE
        create_equipment = test_client.delete(url=f'/rule_base/{rule_base_id}')

        assert create_equipment.status_code == 204
