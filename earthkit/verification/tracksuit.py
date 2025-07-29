from earthkit.data import FieldList

def extract_temp(ds):
    """
    Convert the input (GRIBReader or SimpleFieldList) to a full FieldList,
    then filter temperature fields (shortName='t'),
    and convert to xarray.
    """
    # Convert input iterable to a list of fields
    fields_list = list(ds)
    
    # Build a full FieldList from the list of fields
    full_fields = FieldList.from_fields(fields_list)

    # Filter fields by shortName == 't' (temperature)
    temp_fields = full_fields.sel(shortName="t")
    
    # Convert to xarray Dataset and return
    return temp_fields.to_xarray()




def compute_difference(fc, an):
    """
    Computes the difference between a forecast (fc) and analysis (an).
    Can be used as a simple verification metric.
    """
    return fc - an
