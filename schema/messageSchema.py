from pydantic import BaseModel, ValidationError, validator
from typing import Dict, Union
from datetime import datetime

class MessageSchema(BaseModel):
    data: Dict[str, Union[str, int, float, bool, datetime]]

    @validator('data', pre=True, always=True)
    def validate_data(cls, value):
        if not isinstance(value, dict):
            raise ValidationError('Must be a dictionary')
        return value
