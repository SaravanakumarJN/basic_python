def max_question(difficulty, upto_diff):
    answered_count = 0
    skipped_count = 0

    for ele in difficulty:
        if ele <= upto_diff:
            answered_count += 1
        elif skipped_count < 1:
            skipped_count += 1
        else:
            return answered_count
    return answered_count
            

N, X = map(int, input().strip().split())
difficulty = list(map(int, input().strip().split()))

print(max_question(difficulty, X))
