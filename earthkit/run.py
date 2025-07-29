from earthkit.data import from_source
from earthkit.data.testing import earthkit_remote_test_data_file

def load_era5_sample():
    path = earthkit_remote_test_data_file("test-data", "era5_temperature_europe_2015.grib")
    return from_source("url", path)

import earthkit.data as ekd

def load_cams_pm25():
    ds = ekd.from_source(
        "ads",
        "cams-global-reanalysis-eac4",
        variable=["particulate_matter_2.5um"],
        date="2020-01-01",
        time="12:00",
        area=[70, -50, -10, 40],  # [N, W, S, E]
    )
    return ds



def extract_t2m(ds):
    xr = ds.to_xarray()  # auto recognizes valid_time/time/step dims
    return xr["t2m"]

def split_an_fc(xr):
    an = xr.sel(type="an")
    fc = xr.sel(type="fc")
    return an, fc


if __name__ == "__main__":
    data = load_cams_pm25()
    print("Data loaded successfully.")
    print(data)
    t2m = extract_t2m(data)
    print("Data extracted successfully.")
    print(t2m)
    an, fc = split_an_fc(t2m)
    
    print("Data split into analysis and forecast.")
    print("Analysis data:", an)
    print("Forecast data:", fc)
    print("Analysis data shape:", an.shape)
    print("Forecast data shape:", fc.shape)