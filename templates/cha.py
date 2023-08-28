import akshare as ak
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

symbol="sz123209"

# Function to fetch and update data (replace this with your data retrieval logic)
def fetch_data():
    return ak.bond_zh_hs_cov_min(symbol=symbol, period='1')

def update_plot(frame):
    # Fetch updated data
    df = fetch_data()
    print(df)

    # Calculate the difference between closing and opening prices
    df['差价'] = df['收盘'] - df['开盘']

    # Calculate 5-day moving average of the price difference
    df['5日均线'] = df['差价'].rolling(window=5).mean()

    # Create df_positive and df_negative with zeros
    df_positive = pd.DataFrame({'差价': [0] * len(df)})
    df_negative = pd.DataFrame({'差价': [0] * len(df)})

    # Assign positive values to df_positive and negative values to df_negative
    df_positive.loc[df['差价'] > 0, '差价'] = df.loc[df['差价'] > 0, '差价']
    df_negative.loc[df['差价'] < 0, '差价'] = df.loc[df['差价'] < 0, '差价']

    # Calculate the mean of positive and negative differences
    mean_positive = df_positive['差价'].rolling(window=5).mean()
    mean_negative = df_negative['差价'].rolling(window=5).mean()

    # Clear previous plot
    plt.clf()

    # Plot the updated data
    #plt.plot(df['时间'], df['差价'], marker='o', linestyle='-', label='Price Difference')
    plt.plot(df['时间'], df['5日均线'], color='r', linestyle='--', label='5-Moving Average')

    # Plot mean values as horizontal lines
    plt.plot(df['时间'], mean_positive, color='g', linestyle='--', label='Mean (Positive)')
    plt.plot(df['时间'], mean_negative, color='b', linestyle='--', label='Mean (Negative)')

    plt.xlabel('time')
    plt.ylabel('current')
    plt.title(symbol)
    plt.xticks(rotation=45)
    plt.grid()
    plt.legend()  # Show the legend with labels

    plt.tight_layout()

# Create the initial plot
plt.figure(figsize=(10, 6))
update_plot(0)  # Manually update the plot for the first time

ani = FuncAnimation(plt.gcf(), update_plot, interval=60000)  # Update every 1 minute (60000 ms)

plt.show()  # Display the plot and start the animation
