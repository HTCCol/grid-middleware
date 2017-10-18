import subprocess
import json
def submit_job(submit):
    cmd = ["condor_submit",submit]
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)

    out,err = p.communicate()
    jString = json.dumps({"submit": out})
    j = json.loads(jString)
    print (j)
    
submit_job("/home/fabian/Downloads/tesis/grid-middleware/test.submit")