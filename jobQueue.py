import subprocess
import json
def job_Q():
    cmd = ["condor_q"]
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)

    out,err = p.communicate()
    jString = json.dumps({"job": out})
    j = json.loads(jString)
    print (j)
    #return j
job_Q()