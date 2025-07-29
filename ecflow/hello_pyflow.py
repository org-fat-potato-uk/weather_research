import pyflow
import os
import time
from pwd import getpwuid

passwd = getpwuid(os.getuid())
server_host = 'localhost'
server_port = 3141

scratchdir = os.path.join(os.path.abspath(''), 'scratch')
filesdir = os.path.join(scratchdir, 'files')
outdir = os.path.join(scratchdir, 'out')

if not os.path.exists(filesdir):
    os.makedirs(filesdir, exist_ok=True)

if not os.path.exists(outdir):
    os.makedirs(outdir, exist_ok=True)

# Create a suite using PyFlow
with pyflow.Suite("hello_world_suite",
                  host=pyflow.LocalHost('localhost'),
                  files=filesdir,
                  home=outdir,
                  defstatus=pyflow.state.suspended) as suite:
    with pyflow.Family('hello_family'):
        # Add the tasks to the family
        hello = pyflow.Task(name="hello_task", script=['echo "Hello World from ecFlow!"'])


suite.check_definition()
print(suite)

suite.deploy_suite()
suite.replace_on_server(server_host, server_port)

# Monitor the tasks via the ecFlow UI
print("Suite submitted. You can monitor the tasks in the ecFlow UI.")
