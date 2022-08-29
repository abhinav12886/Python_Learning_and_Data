import json

def run():
       for i in range(10000):
               test(i**i)
               if i % 1000 == 0:
                        print('Main Loop ' + str(i))

def test(k):
    if k % 1000 == 1:
       print("Value", k%2)

run()