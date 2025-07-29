import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from earthkit.data import from_source
from earthkit.data.testing import earthkit_remote_test_data_file

from src.data_loader import extract_timeseries_from_ds, load_sample_grib
from src.nse_metric import nse
from src.plotter import plot_timeseries


def nse(observed, simulated):
    """Calculate Nash-Sutcliffe Efficiency."""
    observed = np.array(observed)
    simulated = np.array(simulated)
    return 1 - np.sum((observed - simulated) ** 2) / np.sum(
        (observed - np.mean(observed)) ** 2
    )


def load_sample_grib():
    """Load a sample GRIB file from EarthKit test data."""
    remote = earthkit_remote_test_data_file(
        "test-data", "era5_temperature_europe_2015.grib"
    )
    ds = from_source("url", remote)
    return ds


def extract_timeseries_from_ds(ds):
    """Extract time‑mean values per time step from EarthKit dataset and ensure clean datetime series."""
    times = []
    values = []

    for f in ds:
        t = f.datetime()
        # If EarthKit returns a dict, extract the "date" or convert manually
        if isinstance(t, dict):
            # Use the 'date' key if available, else fallback to repr
            t = t.get("base_time", None)
        times.append(pd.to_datetime(t))  # convert to pandas datetime

        values.append(float(f.values.mean()))

    df = pd.DataFrame({"date": times, "obs": values, "sim": [v * 1.03 for v in values]})

    return df


def plot_timeseries(df):
    plt.plot(df["date"], df["obs"], label="Observed")
    plt.plot(df["date"], df["sim"], label="Simulated")
    plt.legend()
    plt.title("Observed vs Simulated Streamflow")
    plt.show()


# Step 1: Load EarthKit test data
ds = load_sample_grib()

# Step 2: Extract a synthetic observed vs simulated dataset
df = extract_timeseries_from_ds(ds)

# Step 3: Compute NSE
score = nse(df["obs"], df["sim"])
print(f"Nash-Sutcliffe Efficiency (NSE): {score:.3f}")

# Step 4: Plot
plot_timeseries(df)
