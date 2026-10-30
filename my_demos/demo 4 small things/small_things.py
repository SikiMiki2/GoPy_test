from out import small_things

c = small_things.Counter()
c.Inc(); c.Inc()
print(c.N)

print(small_things.Twice(lambda v: v + 3, 1))