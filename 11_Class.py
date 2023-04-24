#
# Template for Python program
# Name:line
#

import matplotlib.pyplot as plt
import numpy as np

# 1. Input
xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

# 2. Process




# 3. Output
plt.title("Line between two points")
plt.plot(xpoints, ypoints)
plt.show()



####
import matplotlib.pyplot as plt
import numpy as np

# 1. Input
xpoints = np.array([1, 7])
ypoints = np.array([2, 9])



# 3. Output
plt.title("Line between two points")
plt.plot(xpoints, ypoints)
plt.show()




####
# d1(2,3)
import matplotlib.pyplot as plt
import numpy as np

# 1. Input
xpoints = np.array([2, 4, 9])
ypoints = np.array([3, 6, 10])


# 3. Output
plt.title("Line between two points")
plt.plot(xpoints, ypoints)
plt.show()



#
# Template for Python program
# Name:pie chart
#

import matplotlib.pyplot as plt
import numpy as np

# 1. Input
y = np.array([35, 25, 25, 15])

# 2. Process

# 3. Output
plt.title("Alex")
plt.pie(y)
plt.show()

#
# Template for Python program
# Name:pie plot
#

import matplotlib.pyplot as plt
import numpy as np

# 1. Input
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

# 2. Process

# 3. Output
##grid= line on the axis
plt.title("Scatter plot:Alex")
plt.grid()
plt.scatter(x, y)
plt.show()



#
# Template for Python program
# Name:Histogram
#

import matplotlib.pyplot as plt
import numpy as np

# 1. Input
x = np.random.normal(170, 10, 100)

# 2. Process

# 3. Output
plt.title("Histogram:Alex")
plt.grid()
plt.hist(x)
plt.show()


##change language
#
# Template for Python program
# Name:Histogram
#

import matplotlib.pyplot as plt
import numpy as np

# 1. Input

x = np.random.normal(170, 10, 100)
#code added at the import section-
from matplotlib import font_manager
fontP = font_manager.FontProperties()
fontP.set_family('SimHei')
fontP.set_size(14)
#code added at the title section-
plt.title("Histogram Plot: 姚小珍",fontproperties=fontP)

# 2. Process

# 3. Output
#code added at the title section-
plt.title("Histogram Plot: 姚小珍",fontproperties=fontP)
plt.grid()
plt.hist(x)
plt.show()
#
# Template for Python program
# Name:Histogram
#deviation

import matplotlib.pyplot as plt
import numpy as np

# 1. Input
x = np.random.normal(170, 1, 100)

# 2. Process

# 3. Output
plt.title("Histogram:Alex")
plt.xlim([140, 200])
plt.hist(x)
plt.show()

#
# Template for Python program
# Name:Histogram
#Label

import matplotlib.pyplot as plt
import numpy as np

# 1. Input
x = np.random.normal(91, 1, 100)

# 2. Process

# 3. Output
plt.title("Histogram:Alex")
plt.xlabel("Distribution")
plt.ylabel("Score")
plt.xlim([0, 100])
plt.hist(x)
plt.show()

