import pandas as pd
import matplotlib.pyplot as plt 

def line_chart_example(x_ser, y_ser, y2_ser):
    plt.plot(x_ser, y_ser, label="PTS", lw=5, ls="--")
    plt.plot(x_ser, y2_ser, label="MIN")

    # lets beautify the plot
    # lets the overlapping x tick labels
    plt.xticks(rotation=25, ha="right")
    plt.xlabel("Players")
    plt.ylabel("Total")
    plt.title("Gonzaga 2021-22 Season Total")
    plt.grid()
    plt.legend()
    # task: add another parameter to our line_chart_example function
    # for the total minutes played
    # and add a line to the chart for total minutes played
    # are points and minutes played related?
    
    # right before "rending" the figure, good to call
    plt.tight_layout()
    # 3 ways to "render" a figure
    # 1. plt.show()
    # create a modal window to interact with the figure
    # plt.show()
    # 2. plt.savefig(path)
    # save the figure to a file (major file types are 
    # supported... png, jpg, pdf, ...)
    plt.savefig("line_example.png")
    # 3. inline inside a jupyter notebook (stay tuned...)

def scatter_chart_example(x_ser, y_ser):
    plt.figure() # to create a new "current" figure
    plt.scatter(x_ser, y_ser, color="red", marker="x", s=200)
    plt.savefig("scatter_example.png")

def bar_chart_example(x_ser, y_ser):
    plt.figure() # to create a new "current" figure
    plt.bar(x_ser, y_ser)
    plt.savefig("bar_example.png")

def pie_chart_example(x_ser, y_ser):
    plt.figure() # to create a new "current" figure
    plt.pie(y_ser, labels=x_ser, autopct="%.2f%%")
    plt.savefig("pie_example.png")

def histogram_chart_example(x_ser):
    plt.figure() # to create a new "current" figure
    plt.hist(x_ser, bins=5) # default is 10 bins
    plt.savefig("histogram_example.png")

def main():
    df =  pd.read_csv("bball.csv", index_col=0)
    print(df)
    
    new_row = pd.Series(["G",12,20,1], index=df.columns)
    new_row.name = "Joe Few"
    df = df.append(new_row) # use ignore_index=True
    # if no name for the series
    print(df)

    df["Class"] = ["Sr", "Jr", "Fr", "Fr", "Jr", "Fr", "So", "Fr", "Jr", "Sr", "Fr", "Sr", "Sr", "Fr"]
    print(df)

    class_counts_ser = df["Class"].value_counts()
    print(class_counts_ser)

    grouped_by_class = df.groupby("Class")
    mean_pts_ser = grouped_by_class["PTS"].mean()
    print(mean_pts_ser)

    ppg_ser = df["PTS"] / df["GP"]
    print(ppg_ser)
    # lots of ways to do this...
    print(ppg_ser[ppg_ser == ppg_ser.max()])

    # EDA: exploratory data analysis
    # getting familiar with your data
    # summarizing it using stats, visualizing it, 
    # mining it for patterns, relationships, groups, etc.

    # goals of data visualization
    # 1. clearly and accurately represent data
    # 2. be creative, with the goal of increasing readability
    # and understanding
    # 3. label axes, units, and points of interest

    # some jargon
    # chart: 2D visualization
    # plot: a chart of data points (e.g. scatter plot)
    # graph: a chart of a math function (e.g. sine curve)

    # we are going to use the matplotlib library for our plotting
    # a few ways to use this
    # 1. pyplot module 
    # there is always a "current" figure
    # 2. OOP (object oriented programming) interface
    # 3. a mix of the #1 and #2
    # we will do #1, and drop down to #3 if we have to

    # let's start with a simple line chart
    # we will show players on the x-axis 
    # and PTS on the y-axis
    # note: line chart is not the best way to display
    # continuous data (PTS) grouped by discrete values (players)
    print(df.columns)
    line_chart_example(df.index, df["PTS"], df["MIN"])
    # different chart types
    # 1. scatter
    scatter_chart_example(df.index, df["PTS"])
    # 2. bar
    # task: call bar_chart_example twice
    # A. pts per player data
    # B. count of each class (Sr, Jr, ...)
    # bar_chart_example(df.index, df["PTS"])
    plt.xkcd()
    bar_chart_example(class_counts_ser.index, class_counts_ser)

    # 3. pie 
    pie_chart_example(class_counts_ser.index, class_counts_ser)
    
    # 4. histogram
    # showing the distribution of a numeric attribute
    # by showing the counts of values for "bins" number of 
    # equal width bins
    histogram_chart_example(df["MIN"])

    # 5. (later) box plot

main()