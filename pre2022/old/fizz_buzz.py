# fizz buzz

# every multiple of 3: fizz
# every multiple of 5: buzz
# both: fizzbuzz

N = 100

for i in xrange(0, N):
    if i % 5 == 0 and i % 3 == 0:
        print 'fizzbuzz'
    elif i % 3 == 0:
        print 'fizz'
    elif i % 5 == 0:
        print 'buzz'
    else:
        print i
