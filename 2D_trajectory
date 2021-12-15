import matplotlib.pyplot as plt
import numpy as np
import os
my_path = '/home/eo/Desktop/'
my_file_x = 'X_testfish.csv'
my_file_y = 'Y_testfish.csv'
from numpy import genfromtxt
x_vals = genfromtxt(my_path+my_file_x, delimiter=',')
y_vals = genfromtxt(my_path+my_file_y, delimiter=',')
x_array=np.array(x_vals)
y_array=np.array(y_vals)
plt.gca().invert_yaxis()
plt.plot(x_vals, y_vals, linewidth=1)
plt.ylabel('Y position (px)')
plt.xlabel('X position (px)')
plt.title('Fish Trajectory')
plt.savefig(my_path+'XY_trajectory.tif')
