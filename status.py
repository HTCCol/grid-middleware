import subprocess
import json
def status():
    cmd = ["condor_status"]
    p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)

    out,err = p.communicate()
    jString = json.dumps({"status": out})
    j = json.loads(jString)
    print(jString)

    #return j
status()