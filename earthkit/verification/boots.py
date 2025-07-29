import earthkit.data as ekd

def load_data():
    url = "https://get.ecmwf.int/repository/test-data/earthkit-data/examples/test4.grib"
    return ekd.from_source("url", url)
