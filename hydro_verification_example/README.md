# Hydrological Verification Example

This project demonstrates a simple **hydrological verification** workflow using:
- [EarthKit](https://github.com/ecmwf/earthkit) for data access
- Nash-Sutcliffe Efficiency (NSE) as the verification metric
- Freely available sample data

## How to Run
```bash
python3 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
python main.py


The files are collapsed into one verify file for the pyflow example