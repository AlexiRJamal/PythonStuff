# PANDAS
import pandas as pd
import matplotlib.pyplot as plt

iris = pd.read_csv('DEXUSEU.csv', names=["Date", "Rate"])
# print(iris)

# MATPLOTLIB

fig, ax = plt.subplots()

ax.scatter(iris['Date', 'Rate'])

ax.set_title('Database')
ax.set_xlabel('Date')
ax.set_ylabel('Rate')