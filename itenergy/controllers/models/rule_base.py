from typing import Any

from pydantic import BaseModel


class RuleBaseRequest(BaseModel):
    id: int
    input: Any
    switch: Any
