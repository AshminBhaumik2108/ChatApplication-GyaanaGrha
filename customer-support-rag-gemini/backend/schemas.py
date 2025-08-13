from pydantic import BaseModel
from typing import List, Optional, Dict

class ChatRequest(BaseModel):
    session_id: str
    query: str

class ChatTurn(BaseModel):
    role: str
    text: str
    sentiment: Optional[str] = None
    intent: Optional[str] = None

class ChatResponse(BaseModel):
    answer: str
    sources: List[Dict]
    sentiment: Dict
    escalation: Dict
    latency_ms: int

class SatisfactionRequest(BaseModel):
    session_id: str
    score: int
