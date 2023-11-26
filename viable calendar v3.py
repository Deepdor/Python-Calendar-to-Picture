import calendar
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

# Get the current year and month
current_year = datetime.now().year
current_month = datetime.now().month

# Generate a calendar for the current month
cal = calendar.Calendar(firstweekday=calendar.MONDAY)

# Create a list of weeks for the month
month_days = cal.monthdayscalendar(current_year, current_month)

# Modify the month_days to replace zeros with empty strings
month_days = [['' if day == 0 else str(day) for day in week] for week in month_days]

# Plot the calendar grid
fig, ax = plt.subplots(figsize=(10, 2))  # Adjusted figure size for the extra row
canvas = FigureCanvas(fig)

# Remove axes for a clean grid look
ax.axis('off')
ax.axis('tight')

# Create the title table
title_table = plt.table(cellText=[[f"{calendar.month_name[current_month]} {current_year}"]],
                        cellLoc='center', loc='bottom', bbox=[0, 0.9, 1, 0.1])
title_table.auto_set_font_size(False)
title_table.set_fontsize(12)
title_table.scale(1, 2)

# Create a table to represent the calendar grid
calendar_table = plt.table(cellText=month_days,
                           colLabels=list(calendar.day_abbr),
                           cellLoc='center', loc='bottom', bbox=[0, 0, 1, 0.9])
calendar_table.auto_set_font_size(False)
calendar_table.set_fontsize(10)
calendar_table.scale(1, 1.5)  # Scale the height to make cells more rectangular

# Save the calendar grid image
calendar_grid_path = 'calendar_grid.png'
fig.savefig(calendar_grid_path, transparent=True, bbox_inches='tight', pad_inches=0)

calendar_grid_path
