scores = []
result_f = open("results.txt")
for line in result_f:
    (name, score, age) = line.split()
    scores.append(str(name))   # 'joseph ' != 'joseph'
result_f.close()
scores.sort()
scores.reverse()
print("The three surfers' names were:")
print(scores[0])
print(scores[1])
print(scores[2])