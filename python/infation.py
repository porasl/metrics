months = ["09:01", "09:02", "09:03", "09:04", "09:05", "09:06","09:07", "09:08", "09:09", "09:10", "09:11", "09:12","09:13", "09:14", "09:15", "09:16", "09:17", "09:18","09:19", "09:20","09:21", "09:22", "09:23", "09:24","09:25", "09:26", "09:27", "09:28", "09:29", "09:30", "09:31", "09:32","09:33", "09:34", "09:35", "09:36","09:37", "09:38", "09:39", "09:40"]

# Corresponding inflation rates
inflation_rates =[6.4, 6.0, 5.0, 4.9, 4.0, 3.0, 3.2, 3.7, 3.7, 3.2, 3.1, 3.4, 3.1, 3.2, 3.5, 3.4, 3.3, 3.0, 2.9, 2.5,6.4, 6.0, 5.0, 4.9, 4.0, 3.0, 3.2, 3.7, 3.7, 3.2, 3.1, 3.4, 3.1, 3.2, 3.5, 3.4, 3.3, 3.0, 2.9, 2.5]

# Plotting the data
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))
plt.bar(months, inflation_rates, color='skyblue')
plt.xlabel('Order/Minute')
plt.ylabel('Orders')
plt.title('Orders Per Minute')
plt.xticks(rotation=45)

# Add value labels on the bars
for i, value in enumerate(inflation_rates):
 plt.text(i, value -1, str(value), ha='center')

plt.tight_layout()
plt.show()