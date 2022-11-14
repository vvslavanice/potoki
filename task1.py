'''

Task1

'''


import threading


class Counterforpotoki(threading.Thread):

    counter = 0
    rounds = 100000

    def run(self):
        for _ in range(Counterforpotoki.rounds):
            Counterforpotoki.counter += 1


if __name__ == '__main__':

    counter1 = Counterforpotoki()
    counter2 = Counterforpotoki()

    c1.start()
    c2.start()


    print(Counterforpotoki.counter)