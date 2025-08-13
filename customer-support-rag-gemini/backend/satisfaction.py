from collections import defaultdict, deque

_scores = defaultdict(lambda: deque(maxlen=10))

def record_score(session_id, score: int):
    _scores[session_id].append(score)
    avg = sum(_scores[session_id]) / len(_scores[session_id])
    return avg
