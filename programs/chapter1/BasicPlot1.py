# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt  # import the library

# x = [1, 3, 5, 6, 8, 10, 15]  # define x
# y = x  # define y
#
# plt.figure()  # create a new figure
# plt.plot(x, y)  # plot f(x)= x
# plt.xlabel("X-Axis")  # make a label title on x axis
# plt.ylabel("Y-Axis")  # make a label title on y axis
#plt.show()  # figures will only be shown when you call plt.show()

fig1 = plt.figure(1)
ax1 = plt.subplot(122)
ax1.plot([1, 2, 3])
plt.show()