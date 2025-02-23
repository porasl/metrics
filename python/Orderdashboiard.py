import matplotlib.pyplot as plt
import matplotlib.patches as patches
import pandas as pd

# Sample data for the status and inventory tables
status_data = {
    "ready_to_edit": 23,
    "submitted_to_fulfillment": 32,
    "received_by_fulfillment": 120,
    "invoiced": 340,
    "completed": 1232,
    "returned": 23,
    "canceled": 35
}
status_df = pd.DataFrame(list(status_data.items()), columns=["Status", "# of Orders"])

inventory_data = [
    {"bin name": "AC_1406", "skuId": "0224324", "atp_qty": 324, "back_ordered_Qty": 0, "status": 1, "Created Time": "10/09/2024", "updated Time": "10/10/2024"},
    {"bin name": "AC_1556", "skuId": "0124324", "atp_qty": 3423, "back_ordered_Qty": 0, "status": 1, "Created Time": "10/09/2024", "updated Time": "10/10/2024"},
    {"bin name": "AC_1556", "skuId": "0124324", "atp_qty": 22, "back_ordered_Qty": 0, "status": 1, "Created Time": "10/09/2024", "updated Time": "10/10/2024"}
]
inventory_df = pd.DataFrame(inventory_data)

# Create a figure without predefined rows or layout
fig = plt.figure(figsize=(14, 10))

# Plot the status table in the top-left corner
left_ax = fig.add_axes([0.05, 0.55, 0.4, 0.4])  # Custom position for status table
left_ax.axis('off')  # Remove axes completely

# Add updated time for status table above its header
left_ax.text(0.5, 1.1, "Updated: 16:10", fontsize=12, va='center', ha='center', color='gray')

# Plot the status table
table_status = left_ax.table(cellText=status_df.values, colLabels=status_df.columns, cellLoc='center', loc='center', colColours=['blue', 'blue'])
table_status.auto_set_font_size(False)
table_status.set_fontsize(12)  # Adjusted font size for the status table
table_status.scale(1.2, 1.2)

# Set header text color to white
for (i, j), cell in table_status.get_celld().items():
    if i == 0:
        cell.set_text_props(color='white')  # Set header text to white

# Plot the pie chart to the right of the status table
right_ax = fig.add_axes([0.55, 0.55, 0.4, 0.4])  # Custom position for pie chart
max_amount = 2000000  # Max amount $2 Million
current_value = 100000  # Current value $100,000
theta = (current_value / max_amount) * 360
arc = patches.Arc((0, 0), 4.8, 4.8, angle=0, theta1=0, theta2=theta, color='blue', lw=14)
right_ax.add_patch(plt.Circle((0, 0), 2.4, color='lightgray', fill=False, lw=14))
right_ax.add_patch(arc)

# Displaying revenue info inside the pie chart
current_value_usd = "${:,.2f}".format(current_value)
right_ax.text(0, 0.95, "Revenue", fontsize=14, va='center', ha='center', color='black', fontweight='bold')
right_ax.text(0, 0.20, f"{current_value_usd}", fontsize=24, va='center', ha='center', color='black', fontweight='bold')

# Orders and time display
num_orders = 2143
right_ax.text(0, -0.80, f"Orders: {num_orders}", fontsize=20, va='center', ha='center', color='gray')
right_ax.text(0, -0.40, "Updated: 16:10", fontsize=12, va='center', ha='center', color='gray')

# Set pie chart layout and completely remove x and y axes (coordinates)
right_ax.set_xlim([-2.7, 2.7])
right_ax.set_ylim([-2.7, 2.7])
# right_ax.set_aspect('equal', 'box')
right_ax.axis('off')  # Removing all axes and coordinates

# Plot the inventory table below the status table and pie chart
middle_ax = fig.add_axes([0.05, 0.1, 0.9, 0.4])  # Custom position for inventory table
middle_ax.axis('off')  # Remove axes completely

# Add updated time for inventory table above its header
#middle_ax.text(0.5, 1.1, "Updated: 16:10", fontsize=12, va='center', ha='center', color='gray')

# Plot the inventory table
table_inventory = middle_ax.table(cellText=inventory_df.values, colLabels=inventory_df.columns, cellLoc='center', loc='center', colColours=['blue'] * len(inventory_df.columns))
table_inventory.auto_set_font_size(False)
table_inventory.set_fontsize(11)  # Adjusted font size for the inventory table
table_inventory.scale(1, 1)

# Set header text color to white
for (i, j), cell in table_inventory.get_celld().items():
    if i == 0:
        cell.set_text_props(color='white')  # Set header text to white

# Display the figure
plt.show()
