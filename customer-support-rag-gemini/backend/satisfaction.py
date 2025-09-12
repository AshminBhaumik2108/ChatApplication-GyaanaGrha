from collections import defaultdict, deque

# Store satisfaction scores for each user session : 10 Score can be stored at Max....
_scores = defaultdict(lambda: deque(maxlen=10))

# function for the Score to record for the Average Value.....
def record_score(session_id, score: int):
    _scores[session_id].append(score)
    avg = sum(_scores[session_id]) / len(_scores[session_id])
    return avg
