import calendar
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

# Get the current year and month
current_year = datetime.now().year
current_month = datetime.now().month

# Generate a calendar for the current month
cal = calendar.Calendar(firstweekday=calendar.SUNDAY)

# Create a list of weeks for the month
month_days = cal.monthdayscalendar(current_year, current_month)

# Plot the calendar grid
fig, ax = plt.subplots(figsize=(10, 1))  # Aspect ratio 10:1 to fit the bottom of the portrait image
canvas = FigureCanvas(fig)

# Remove axes for a clean grid look
ax.axis('off')
ax.axis('tight')

# Create a table to represent the calendar grid
table = ax.table(
    cellText=month_days,
    colLabels=list(calendar.day_abbr),
    cellLoc='center',
    loc='center',
    edges='closed'
)

# Adjust the table columns to be more rectangular, fitting a typical calendar layout
table.auto_set_font_size(False)
table.set_fontsize(10)
table.scale(1, 1.5)  # Scale the height to make cells more rectangular

# Save the calendar grid image
calendar_grid_path = 'C:/outp/calendar_grid.png'
fig.savefig(calendar_grid_path, transparent=True, bbox_inches='tight', pad_inches=0)

calendar_grid_path
