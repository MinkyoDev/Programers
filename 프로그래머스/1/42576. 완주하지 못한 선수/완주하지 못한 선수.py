from collections import Counter

def solution(participant, completion):
    participant = Counter(participant)
    completion = Counter(completion)
    
    for key, value in participant.items():
        if key not in completion.keys():
            return key
        elif completion[key] != value:
            return key