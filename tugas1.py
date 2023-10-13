sequenceGenerator = lambda start, stop: list(range(start, stop+1)); fizzBuzz = lambda a, b: [('Fizz'*(i%3==0) + 'Buzz'*(i%5==0)) or i for i in range(a, b)]; twoNumber = lambda l: [l[i] + l[i+1] for i in range(len(l)-1)]
print(sequenceGenerator(1, 10)) 
print(fizzBuzz(1, 16))
print(twoNumber([1, 2, 3, 4, 5]))
