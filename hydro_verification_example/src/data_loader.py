import pandas as pd
from earthkit.data import from_source
from earthkit.data.testing import earthkit_remote_test_data_file

def load_sample_grib():
    """Load a sample GRIB file from EarthKit test data."""
    remote = earthkit_remote_test_data_file("test-data", "era5_temperature_europe_2015.grib")
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

    df = pd.DataFrame({
        "date": times,
        "obs": values,
        "sim": [v * 1.03 for v in values]
    })

    return df
