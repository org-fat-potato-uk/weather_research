from pyflow import Workflow, Task
from tasks.verify import run

def hydro_verification_suite():
    suite = Workflow("hydro_verification")
    
    # Add a single task that runs the verification logic
    suite.add(Task("verify", run))
    
    return suite

if __name__ == "__main__":
    hydro_verification_suite().run()
