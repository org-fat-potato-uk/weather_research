# Weather & Hydrological Verification Research

This repository contains example projects and workflow templates for hydrological and meteorological data verification using [EarthKit](https://github.com/ecmwf/earthkit), [PyFlow](https://github.com/ecmwf/pyflow), and [Wellies](https://github.com/ecmwf/pyflow-wellies).

> **Disclaimer:**  
> This repository contains internal research, fact-finding, and experimental workflows. The code and examples provided are for demonstration and exploration purposes only. They are **not** intended for production use and do **not** represent production-quality code or official ECMWF workflows.

## Structure

- **hydro_verification_example/**  
  Standalone Python example for hydrological verification using EarthKit and Nash-Sutcliffe Efficiency (NSE).
- **earthkit/**  
  EarthKit demos, scripts, and verification utilities.
- **ecflow/**  
  EcFlow server and workflow examples, including quickstart templates.

## Quickstart

All examples use Conda to manage the environments. The below steps install many of the dependencies required for the examples.

### 1. Create and Activate Environment

```sh
conda create -n ecflow_env python=3.11 -y
conda activate ecflow_env
conda install -c conda-forge ecflow
```

### 2. Install some common dependencies

```sh
pip install earthkit-data earthkit-hydro earthkit-meteo
pip install pyflow-wellies pyflow-workflow-generator tracksuite
pip install xarray pandas matplotlib seaborn netcdf4
```

## Documentation

- [EarthKit Documentation](https://earthkit.readthedocs.io/)
- [PyFlow Documentation](https://pyflow-workflow-generator.readthedocs.io/)
- [Wellies Documentation](https://pyflow-wellies.readthedocs.io/)
