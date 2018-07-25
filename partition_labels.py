"""partition a string into as many parts as possible so that each letter appears in at most one part, and return a list of integers representing the        size of these parts """
def partitionLabels(S):
    last_index = {}
    answer, chunk = [], [0,0]
    for i in range(len(S)):
        last_index[S[i]] = i
    for i in range(len(S)):
        if last_index[S[i]] > chunk[1]:
            chunk[1] = last_index[S[i]]
        elif i == chunk[1]:
            answer.append(len(S[chunk[0]:chunk[1]+1]))
            temp = chunk[1]+1
            chunk[0] = temp
            chunk[1] += 1
    return answer