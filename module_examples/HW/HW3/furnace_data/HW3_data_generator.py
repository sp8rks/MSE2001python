import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

years = range(1990, 2019)
months = range(12)
year_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leap_year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
mean_values = {}

for year in years:
    leap = False
    year_of_data = np.ones(0)
    if year % 4 == 0:
        leap = True
    for month in months:
        days = year_month[month]
        if month == 1:
            if leap:
                days = 29
        for day in range(days):
            if (day + 1) % 7 == 0:
                if day == 0:
                    continue
                run_time = 6*8
                x = np.linspace(0, 15, run_time)
                noise = np.random.normal(size=(run_time))
                generate_signal = -(x-8)**2 * (40 * np.sin(x) + 70) + 150*noise
                monthly_disturbance = 0.1 * (x-8)**2 * (6*abs(month-6)**1.2) * np.random.normal(size=(run_time))
                generate_signal = generate_signal + monthly_disturbance
                # month_signal = generate_signal[:2 * (month+1)].mean()
                generate_signal[generate_signal > 7000] == np.random.randint(6000, 7500)
                generate_signal[generate_signal < -1000] == np.random.randint(-1200, 0)
                month_signal = generate_signal[:2 * 3].mean()
                generate_signal = (generate_signal - month_signal)
                generate_signal = generate_signal * (year/1000)**8 * 1e-2 / 2
                np.savetxt(f'data/power_usage_{year}_{month}_{day}.txt', generate_signal)
                year_of_data = np.concatenate((year_of_data, generate_signal))
                # plt.plot(x, generate_signal, 'x', alpha=0.7)

    mean_values[year] = year_of_data.mean()
    # plt.plot(x, generate_signal, 'x', alpha=0.3)
    # plt.title([year, month])
    # plt.show()

plt.plot(range(len(mean_values.values())), list(mean_values.values()))

# plt.plot(x, monthly_disturbance, 'x', alpha=0.3)
