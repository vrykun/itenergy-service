from typing import Any

from pydantic import BaseModel, Json


class RuleBaseRequest(BaseModel):
    id: int
    input: Any
    switch: Any
