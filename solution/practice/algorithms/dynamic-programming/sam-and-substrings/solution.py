# Denote d[i] as sum of all substring that ends at index i.
# d[0] = n[0] of course.
# d[i] consists of 3 parts:
# * all numbers in d[i-1] multiplied by 10
# * plus n[i] for each number in d[i-1] (there're i numbers in d[i-1], so n[i] * i)
# * n[i] itself
# And finally, the result is the sum of all d[i].

n, m = list(map(int, input())), 10 ** 9 + 7
count, prefix_sum = 0, 0
for i in range(len(n)):
  prefix_sum = (prefix_sum * 10 + n[i] * (i + 1)) % m
  count = (count + prefix_sum) % m
print(count)
