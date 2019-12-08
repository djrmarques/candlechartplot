import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle as rect
import pandas as pd


def plot_candle_chart(path_to_csv: str, date_format="%Y-%m-%d") -> None:
    """
    Simple function to plot a candle chart.
    This assumes that the files header has 4 columns:

    - Date: The date in the specified format
    - Open: The open price
    - Close: The Close price
    - High: The highest price
    - Low: The lowest price

    :param path_to_csv: Path to the csv file
    :param date_format: The format of the Date column
    """

    # Read the dataframe and convert the index to date format
    df = pd.read_csv(path_to_csv, index_col=0)
    df.index = pd.to_datetime(df.index, format=date_format)

    # Create auxiliary columns
    df["index"] = list(range(df.shape[0]))
    df["bar_width"] = 1  # This is the width of each bar
    df["line_width"] = 0.1  # This is the width of each line
    df["diff_open_close"] = (df["Close"] - df["Open"]).abs()
    df["diff_high_low"] = (df["High"] - df["Low"]).abs()
    df["bar_x"] = df["index"] - (df["bar_width"] / 2)  # Lower left corner
    df["bar_y"] = df[["Open", "Close"]].min(axis=1)  # Lower left corner
    df["line_x"] = df["index"] - (df["line_width"] / 2)  # Lower left corner
    df["line_y"] = df[["High", "Low"]].min(axis=1)  # Lower left corner
    df["color"] = df[["Close", "Open"]].apply(lambda prices: "red" if prices[1] > prices[0] else "green", axis=1)

    plt.figure()
    ax = plt.gca()
    for _, row in df.iterrows():
        ax.add_patch(rect((row["bar_x"], row["bar_y"]), width=row["bar_width"], height=row["diff_open_close"],
                          color=row["color"]))
        ax.add_patch(rect((row["line_x"], row["line_y"]), width=row["line_width"], height=row["diff_high_low"],
                          color=row["color"]))

    plt.xlim(0, df.shape[0])
    plt.ylim(df["Low"].min(), df["High"].max())

    # Set the sticks
    plt.xticks(df["index"], df.index.date, rotation=90)

    plt.show()
