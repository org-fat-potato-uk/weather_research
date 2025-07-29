def plot_diff(diff):
    diff.mean(dim=["latitude", "longitude"]).plot()
    plt.title("Mean forecast–analysis temperature difference")
    plt.show()
