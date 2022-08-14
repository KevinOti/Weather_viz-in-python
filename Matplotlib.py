import csv
from datetime import datetime
import matplotlib.pyplot as plt
plt.style.use('seaborn')
fig, ax =plt.subplots()

filename = 'sitka_weather_2018_full.csv'
with open(filename) as f:
	reader = csv.reader(f)
	header_row = next(reader)
	dates, highs ,lows = [] ,[], []
	for row in reader:
		current_date = datetime.strptime(row[2], '%d/%m/%Y')
		high = int(row[8])
		low = int(row[9])
		highs.append(high)
		lows.append(low)
		dates.append(current_date)

ax.plot(dates, highs, c ='red')
ax.plot(dates, lows, c='blue')
ax.set_title('Daily Temperatures(2018/19)',fontsize = 15)
ax.set_xlabel('Dates')
ax.set_ylabel('Temperatures (F)')
ax.tick_params(axis = 'both', which = 'major', labelsize = 10)
ax.fill_between(dates,highs, lows, facecolor = 'lightblue')
fig.autofmt_xdate()
plt.show()





		
		
