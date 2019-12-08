import matplotlib.pyplot as plt
import pandas as pd


def plot_candle_chart(path_to_csv: str, date_format="%Y-%m-%d") -> None:
    """
    Simple function to plot a candle chart.
    This assumes that the file has 4 columns:

    - Date: The date in the specified format
    - Open: The open price
    - Close: The Close price
    - High: The highest price
    - Low: The lowest price

    The exact names of the columns do not matter, that the csv needs to have a header with the columns in this order.

    :param path_to_csv: Path to the csv file
    :param date_format: The format of the Date column
    """


    pass

