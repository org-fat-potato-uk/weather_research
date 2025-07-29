import earthkit.data
import earthkit.maps
source_filename = "era5-2t-mslp-christmas-2010.grib"
earthkit.data.download_example_file(source_filename)
data = earthkit.data.from_source("file", source_filename)
earthkit.maps.quickplot(data)
print("Plotting complete. Check the output for the map visualization.")