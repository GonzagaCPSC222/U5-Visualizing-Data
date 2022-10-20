import pandas as pd

# DATA VIS NOTES
# EDA: exploratory data analysis
# getting familiar with your data
# exploring data, visualizing data,
# mining data (looking for patterns, groups, 
# outliers, associations, etc.)

# goals of data visualization
# 1. clearly and accurately represent data
# 2. be creative, with the goal of increasing understanding
# 3. label units and points of interest

# some jargon
# chart: a 2D visualization
# plot: a chart of data points (e.g. scatter)
# graph: a chart of a math function (e.g. sine)

# we are going to use the matplotlib library
# 3 ways to use matplotlib
# 1. using the pyplot submodule
import matplotlib.pyplot as plt
# note: there is always a "current figure"
# 2. using the OOP interface
# 3. a mix of the first two

# lets start with a simple line chart
def line_chart_example(x, y, y2, filename):
    # x and y are "sequences"
    # lists, series, numpy arrays, etc.
    # they are parallel
    plt.plot(x, y, label="PTS", color="purple", lw=5)
    plt.plot(x, y2, label="MIN")

    # lets beautify the plot
    plt.xticks(rotation=45, ha="right")
    plt.xlabel("Player")
    plt.ylabel("Season Point Total")
    plt.title("21/22 GU Men's Basketball")
    plt.grid()
    plt.legend()

    plt.tight_layout() # call right before plt.show() or plt.savefig()

    # 3 ways to "show" the chart
    # 1. plt.show()
    # plt.show() # shows an interactive window
    # 2. plt.savefig()
    plt.savefig(filename)
    # 3. inline inside of a jupyter notebook
    # (more on this later)

def scatter_chart_example(x, y, filename):
    plt.figure() # creates a new *current figure*
    plt.scatter(x, y, s=200, marker="x")
    plt.savefig(filename)

def bar_chart_example(x, y, filename):
    plt.figure() # creates a new *current figure*
    plt.bar(x, y, facecolor="red", edgecolor="blue", lw=5)
    plt.savefig(filename)

def pie_chart_example(labels, values, filename):
    plt.figure() # creates a new *current figure*
    plt.pie(values, labels=labels, autopct="%1.1f%%")
    plt.savefig(filename)

def histogram_chart_example(values, filename):
    plt.figure() # creates a new *current figure*
    # default number of bins is 10
    plt.hist(values, bins=5, edgecolor="black")
    plt.savefig(filename)

def main():
    df = pd.read_csv("bball.csv", index_col=0)
    print(df)

    new_row_df = pd.DataFrame([["G",12,20,1]], columns=df.columns, index=["Joe Few"])
    new_row_df.index.name = df.index.name
    df = pd.concat([df, new_row_df])
    print(df)

    df["CLASS"] = ["Sr", "Jr", "Fr", "Fr", "Jr", "Fr", "So", "Fr", "Jr", "Sr", "Fr", "Sr", "Sr", "Fr"]
    print(df)

    class_counts_ser = df["CLASS"].value_counts()
    print(class_counts_ser)

    grouped_by_class = df.groupby("CLASS")
    mean_pts_ser = grouped_by_class["PTS"].mean()
    print(mean_pts_ser)

    ppg_ser = df["PTS"] / df["GP"]
    print(ppg_ser.max())
    print(ppg_ser[ppg_ser == ppg_ser.max()])
    # OR
    max_position = ppg_ser.argmax()
    print(ppg_ser.index[max_position])

    # task: add another line to our chart 
    # for "MIN"
    line_chart_example(df.index, df["PTS"], df["MIN"], "line_example.png")
    # game plan
    # 1. line (check)
    # 2. scatter
    scatter_chart_example(df.index, df["PTS"], "scatter_example.png")
    # 3. bar 
    # bar_chart_example(df.index, df["PTS"], "bar_example.png")
    bar_chart_example(class_counts_ser.index, class_counts_ser, "bar_example.png")
    # 4. pie 
    # (great for showing parts of a whole)
    pie_chart_example(class_counts_ser.index, class_counts_ser, "pie_example.png")
    # 5. histogram
    histogram_chart_example(df["PTS"], "histogram_example.png")
    # 6. (later) boxplots

main()