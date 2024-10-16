def solution(participant: list, completion: list):
    hash_dict = {}
    sum_hash = 0

    # 1. hash : participant의 dict 만들기
    # 2. completion의 sum(hash) 구하기
    for part in participant:
        hash_dict[hash(part)] = part
        sum_hash += hash(part)

    # 3. completion의 sum(hash) 빼기
    for comp in completion:
        sum_hash -= hash(comp)

    # 4. 남은 값이 완주하지 못한 선수의 hash 값이 된다
    return hash_dict[sum_hash]