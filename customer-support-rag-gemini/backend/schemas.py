from pydantic import BaseModel
from typing import List, Optional, Dict

# Only for the pydantic-basemodel : ChatRequest
class ChatRequest(BaseModel):
    session_id: str
    query: str

class ChatTurn(BaseModel):
    role: str
    text: str
    sentiment: Optional[str] = None
    intent: Optional[str] = None

# Chat Response Model : TypeSafty : BaseModel....
class ChatResponse(BaseModel):
    answer: str
    sources: List[Dict]
    sentiment: Dict
    escalation: Dict
    latency_ms: int

class SatisfactionRequest(BaseModel):
    session_id: str
    score: int
