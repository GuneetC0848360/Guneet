
import matplotlib.pyplot as plt

Hours_taken = [9,11,12 ,19 ]
Number_of_Neuron = [200, 400, 800, 2000]

plt.plot(Hours_taken, Number_of_Neuron, color='red', marker='o')
plt.title('Time taken VS Number of Neurons')
plt.xlabel('Time taken')
plt.ylabel('Number of Neurons')
plt.show()

Hours_taken_Learning_Rate= [14,1 ,21 ,1 ]
Learning_Rate= [0.0001, 0.001, 0.01, 0.002]
plt.plot(Hours_taken_Learning_Rate, Learning_Rate, color='red', marker='o')
plt.title('Time taken VS Learning Rate')
plt.xlabel('Time taken')
plt.ylabel('Learning Rate')
plt.show()