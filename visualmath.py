import matplotlib.pyplot as plt
import random

maxNumber = 100

x_values = range(1, maxNumber + 1)
values = [random.randint(1, maxNumber) for x in x_values]
y_values = [values.count(x) for x in x_values]

plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=5)

ax.set_title(f"Random Number Occurrences (N = {maxNumber})", fontsize=18)
ax.set_xlabel("Number", fontsize=14)
ax.set_ylabel("Occurrences", fontsize=14)

ax.tick_params(axis="both", which="major", labelsize=14)

plt.show()