import matplotlib.pyplot as plt

# Data must have equal length
x = [2010, 2013, 2016, 2019, 2021]
y = [7.5, 9.23, 3, 5.5, 8]  # Adjusted to match x

plt.bar(x, y)
plt.title('Weather Analysis')
plt.xlabel('Year')
plt.ylabel('Percentage')
plt.show()
