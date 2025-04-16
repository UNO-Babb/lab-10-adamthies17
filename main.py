#MapPlot.py
#Name:
#Date:
#Assignment:
import matplotlib.pyplot as plt
import consumer_price_index
report = consumer_price_index.get_report()
num_items = len(report)
prices = []
years = []
for spot in range(num_items):
    year = report[spot]["Year"]
    meat_price = report[spot]["Data"]["Meat"]["Beef"]
    
    
    prices.append(meat_price)
    years.append(year)


plt.plot(years, prices, 'ro')
plt.ylabel('Meat Price')
plt.xlabel("Year")
plt.savefig("Output")