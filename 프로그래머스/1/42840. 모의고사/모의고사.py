def solution(answers):
    patterns = [[1,2,3,4,5], [2,1,2,3,2,4,2,5], [3,3,1,1,2,2,4,4,5,5]]

    scores = []
    for pattern in patterns:
        score = 0
        a1 = len(answers) // len(pattern) + (1 if len(answers) % len(pattern) != 0 else 0)
        for p, answer in zip((pattern * a1)[:len(answers)], answers):
            score += 1 if p == answer else 0 
        scores.append(score)
    
    return [idx+1 for idx, score in enumerate(scores) if score == max(scores)]