c = [1, 10, 2, 9] 
m = sorted(c)[len(c) // 2] 
print(sum(abs(v - m) for v in c))