import numpy as np
import matplotlib.pyplot as plt
import random

random.seed(2)
# variable arrival rate; could take on these values: 0.2, 0.4, 0.5, 0.6, 0.65, 0.7, 0.72, 0.74, and 0.745
arrivalRate = [0.2, 0.4, 0.5, 0.6, 0.65, 0.7, 0.72, 0.74, 0.745]

# fixed service rate
serviceRate = 0.75

# initialize parameters queue, queue length, average delay, average queue length, theoretical average queue delay, and rho
queue = [0] * 9
qLength = [0] * 9
avgDelay = [0] * 9
avgQLength = [0] * 9
avgDelayTheoretical = [0] * 9
rho = [0] * 9

def generatePacket():
    # iterate through each value of lambda
    for i in range(9):
        for j in range(1000000):
            # packet arrival
            # generate a random number between 0 and 1 
            arrivalRandInt = random.random()

            # if number is less than arrivalRate, a packet arrives -> increment queue length
            if arrivalRandInt < arrivalRate[i]:
                queue[i] += 1

            # packet departure
            # generate another random number between 0 and 1
            serviceRandInt = random.random()

            # check if there is a waiting packet and if a packet can be serviced -> decrement queue length
            if serviceRandInt < serviceRate and queue[i] > 0:
                queue[i] -= 1

            # update queue length
            qLength[i] += queue[i]

        # update average variables
        avgQLength[i] = qLength[i] / 1000000
        print("Average queue length for iteration " + str(i + 1) + " is: " + str(avgQLength[i]))

        # update average queue delay using Little's law
        avgDelay[i] = avgQLength[i] / arrivalRate[i]
        print("Average queue delay for iteration " + str(i + 1) + " is: " + str(avgDelay[i]))

        # calculate rho
        rho[i] = (arrivalRate[i] * (1 - serviceRate)) / ((1 - arrivalRate[i]) * serviceRate)
        print("Rho for iteration " + str(i + 1) + " is: " + str(rho[i]))

        # get the theoretical average queue delay
        avgDelayTheoretical[i] = (rho[i]) / (arrivalRate[i] * (1 - rho[i]))
        print("Average theoretical queue delay for iteration " + str(i + 1) + " is: " + str(avgDelayTheoretical[i]))
        print("")

generatePacket()

# produce plot of arrival rate vs queueing delay
plt.plot(arrivalRate, avgDelay)
plt.title("Arrival Rate vs Queueing Delay")
plt.savefig("arrival_vs_queue.png")
plt.clf()

# produce plot of theoretical curve of arrival rate vs theoretical queueing delay
plt.plot(arrivalRate, avgDelayTheoretical)
plt.title("Arrival Rate vs Theoretical Queueing Delay")
plt.savefig("arrival_vs_queue_theoretical.png")
plt.clf()

# produce both plots from above
plt.plot(arrivalRate, avgDelayTheoretical, arrivalRate, avgDelayTheoretical, "r--")
plt.title("Arrival Rate vs Theoretical Queueing Delay")
plt.savefig("combined_arrival_queue_theoretical.png")
plt.clf()