import matplotlib.pyplot as plt

def plot_timeseries(df):
    plt.plot(df["date"], df["obs"], label="Observed")
    plt.plot(df["date"], df["sim"], label="Simulated")
    plt.legend()
    plt.title("Observed vs Simulated Streamflow")
    plt.show()
