class Printer():
    """docstring for Printer"""
    def __init__(self, ppm):
        self.pageRate = ppm
        self.currentTask = None
        self.timeRemaining = 0

    def tick(self):
        if self.currentTask != None:
            self.timeRemaining -= 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False

    def startNext(self, newTask):
        self.currentTask = newTask
        self.timeRemaining = newTask.getPages() * 60 / self.pageRate

import random
class Task():
    """docstring for Task"""
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, currentTime):
        return currentTime - self.timestamp

from queue import Queue

def simulation(numSeconds, pagesPerMinute):
    labPrinter = Printer(pagesPerMinute)
    printQueue = Queue()
    waitingTimes = []

    for currentSecond in range(numSeconds):
        if newPrintTask():
            task = Task(currentSecond)
            printQueue.enqueue(task)

        if (not labPrinter.busy()) and (not printQueue.isEmpty()):
            nextTask = printQueue.dequeue()
            waitingTimes.append(nextTask.waitTime(currentSecond))
            labPrinter.startNext(nextTask)

        labPrinter.tick()

    averageWait = sum(waitingTimes) / len(waitingTimes)
    print("Average Wait %6.2f secs %3d tasks remaining, total %s." %(averageWait, printQueue.size(), len(waitingTimes)))

def newPrintTask():
    num = random.randrange(1, 91)
    if num == 90:
        return True
    else:
        return False

# trials
for i in range(10):
    simulation(3600, 10)
