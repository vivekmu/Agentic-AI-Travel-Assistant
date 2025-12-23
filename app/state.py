from typing import Optional, Dict, List
from pydantic import BaseModel

class TravelState(BaseModel):
    goal: str
    user: Dict
    retries: int = 0
    approved: bool = False
    flights: Optional[List[Dict]] = None
    selected_flight: Optional[Dict] = None
    booking_result: Optional[Dict] = None