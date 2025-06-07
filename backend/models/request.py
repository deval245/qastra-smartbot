from pydantic import BaseModel

class HealRequest(BaseModel):
    broken_xpath: str
    module: str
