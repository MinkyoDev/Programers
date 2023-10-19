def n_number(n, k):
    result = []
    for i in range(100):
        quotient, remainder = divmod(n, k)
        if quotient >= k:
            result.append(remainder)
            n = quotient
        else:
            result.append(remainder)
            result.append(quotient)
            break
            
    answer = ''.join(map(str, result[::-1]))
    return answer


def solution(n, k):
    answer = n_number(n, k)

    # nums = list(filter(None, answer.split('0')))
    nums = [int(i) for i in answer.split('0') if i != '']

    prime_numbers = []
    for num in nums:
        if num == 1:
            pass
        else:
            tmp = [i for i in range(2, int(num**0.5)+1) if num % i == 0]
            print(tmp)
            if len(tmp) == 0:
                prime_numbers.append(num)
            
    return len(prime_numbers)