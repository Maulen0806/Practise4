word = input()
y = iter(word)
print(next(y))
print(next(y))
for i in word:
    print(i)
class nums:
    def __iter__(self):
        self.num = 1
        return self
    def __next__(self):
        n = self.num
        self.num += 1
        return n
result = nums()
res_iter = iter(result)

for i in range(10):
    print(next(res_iter))
