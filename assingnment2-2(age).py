scores = []
result_f = open("results.txt")
for line in result_f:
    (name, score, age) = line.split()
    scores.append(int(age))
result_f.close()
scores.sort()
scores.reverse()
print("The top three elders were:")
print(scores[0])
print(scores[1])
print(scores[2])