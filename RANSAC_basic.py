import random
import numpy as np
import matplotlib.pyplot as plt

# Generate random points
x_gen1 = [random.randint(1, 20) for _ in range(20)]
y_gen1 = [random.randint(1, 20) for _ in range(20)]

# medium number of points
x_gen2 = [random.randint(15, 40) for _ in range(30)]
y_gen2 = [random.randint(15, 40) for _ in range(30)]

# more number of points 
x_gen3 = [random.randint(35, 70) for _ in range(40)]
y_gen3 = [random.randint(35, 70) for _ in range(40)]

# Combine all sections

x_gen = x_gen1 + x_gen2 + x_gen3
y_gen = y_gen1 + y_gen2 + y_gen3

tolerance = 2 
max_inliers = 0  
best_slope = 0
best_intercept = 0

for _ in range(100):  # 100 iterations 
 # Randomly select two points
  idx1, idx2= random.sample(range(90), 2)
  x1, y1 = x_gen[idx1], y_gen[idx1]
  x2, y2 = x_gen[idx2], y_gen[idx2]
                                               # this section is for lines 
  if x2 - x1 == 0:
    continue 
  slope = (y2 - y1) / (x2 - x1)
  intercept = y1 - slope * x1
    
  inlier_counter = 0
  for i in range(90):
    distance = abs(slope * x_gen[i] - y_gen[i] + intercept) / np.sqrt(slope**2 + 1)  # here its calculating distance
    if distance < tolerance:
     inlier_counter += 1
    
    # finding best model 
  if inlier_counter > max_inliers:
    max_inliers = inlier_counter
    best_slope = slope
    best_intercept = intercept

x_line = [min(x_gen), max(x_gen)]
y_line = [best_slope * x_line[0] + best_intercept, best_slope * x_line[1] + best_intercept]


inlier_counter = 0
for i in range(90):
  distance = abs(best_slope * x_gen[i] - y_gen[i] + best_intercept) / np.sqrt(best_slope**2 + 1)
  if distance < tolerance:
    plt.scatter(x_gen[i], y_gen[i], color="green") 
    inlier_counter += 1
  else:
    plt.scatter(x_gen[i], y_gen[i], color="red")

plt.plot(x_line, y_line, color="navy", linewidth=2)  
plt.grid(True)
print("No. of safe points:", inlier_counter)
plt.show()