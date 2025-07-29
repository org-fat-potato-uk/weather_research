from src.data_loader import load_sample_grib, extract_timeseries_from_ds
from src.nse_metric import nse
from src.plotter import plot_timeseries

# Step 1: Load EarthKit test data
ds = load_sample_grib()

# Step 2: Extract a synthetic observed vs simulated dataset
df = extract_timeseries_from_ds(ds)

# Step 3: Compute NSE
score = nse(df["obs"], df["sim"])
print(f"Nash-Sutcliffe Efficiency (NSE): {score:.3f}")

# Step 4: Plot
plot_timeseries(df)
