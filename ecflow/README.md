# ecflow

This directory contains resources and examples for setting up and running [EcFlow](https://confluence.ecmwf.int/display/ECFLOW) workflows. EcFlow is a workflow manager developed by ECMWF for running complex suites of tasks, commonly used in meteorological and hydrological research.

This directory was created using `wellies-quickstart`:
```sh
wellies-quickstart hello-world
cd hello-world
```

## Contents

- **quickstart templates**: Example EcFlow suite definitions and scripts to help you get started.
- **server setup scripts**: Utilities for launching and managing an EcFlow server locally.
- **suite examples**: Sample EcFlow suites for weather and hydrological verification workflows.

## Usage

1. **Install EcFlow**  
   Configure your environment:
   ```sh
   conda env update -n ecflow_env -f environment.yml
   ```

2. **Start EcFlow Server**  
   Use the provided scripts or run:
   ```sh
   ecflow_server.sh &
   ```

3. **Run Example Suite**  
   Edit and submit a suite definition:
   ```sh
   ./build.sh user
   ecflow_client --host localhost --port 3141 --load /home/vscode/pyflow/hello_world/hello_world.def
   ```

4. **Monitor and Control**  
   Use EcFlow's GUI or CLI to monitor suite progress and manage tasks.

### Alternative Usage

If using VSCode and Remote Containers extension, it is possible to use the .devcontainer setup to use the repeatable environment. 'Reopen in container' and start from step 3 above.

## Pyflow

There is also a separate Pyflow example in this directory. It can be run with:

```sh
python hello_pyflow.py
```

And then monitored in the same way as above.

## Documentation

- [EcFlow User Guide](https://confluence.ecmwf.int/display/ECFLOW/EcFlow+User+Guide)
- [EcFlow Tutorials](https://confluence.ecmwf.int/display/ECFLOW/Tutorials)
- [Pyflow Getting Started](https://pyflow-workflow-generator.readthedocs.io/en/latest/content/introductory-course/getting-started.html)

## Notes

- Example suite definitions are provided for reference and can be customized.
- Scripts may require adjustment for your local environment or cluster setup.

## License

See the repository