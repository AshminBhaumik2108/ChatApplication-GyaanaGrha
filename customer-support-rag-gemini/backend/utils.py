import time
import numpy as np

# It's Works like a Decoder function for the file.....
def timeit(fn):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = fn(*args, **kwargs)
        latency = int((time.time() - start) * 1000)
        return result, latency
    return wrapper

def clean_text(text):
    return text.strip().replace("\n", " ")

def summarize_source_for_citation(text):
    return clean_text(text)[:120] + "..."

def cosine_similarity(a, b):
    a = np.array(a)
    b = np.array(b)
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b) + 1e-8)
