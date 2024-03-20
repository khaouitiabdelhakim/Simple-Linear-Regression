import matplotlib.pyplot as plt

with open('output.txt','r') as file:
    data = file.readlines()

x = []
y1 = []
y2 = []

for line in data:
    x0,y,z = map(float,line.split())
    x.append(x0)
    y1.append(y)
    y2.append(z)

plt.scatter(x,y1,label='data points',color='blue')
plt.plot(x,y2,label='predicted values',color='purple')

plt.xlabel('X coordinate')
plt.ylabel('Y coordinate')
plt.title('Linear regression model')

plt.legend()
plt.show()
