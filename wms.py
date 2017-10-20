import subprocess
import json

class Wms:
    
    def status(self):
        cmd = ["condor_status"]
        p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)

        out,err = p.communicate()
        jString = json.dumps({"status": out})
        j = json.loads(jString)
        return j
   
    def job_Q(self):
        cmd = ["condor_q"]
        p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)

        out,err = p.communicate()
        jString = json.dumps({"job": out})
        j = json.loads(jString)
        return j
    
    def log(self, log):
        file = open(log, "r")
        file_r = file.read()
        jString = json.dumps({"output": file_r})
        j = json.loads(jString)
        return j
    
    def output(self, output):
        file=open(output,"r")
        file_r=file.read()
        jString = json.dumps({"output": file_r})
        j = json.loads(jString)
        return j
    
    def submit(self, submit):
        cmd = ["condor_submit",submit]
        p = subprocess.Popen(cmd, stdout = subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            stdin=subprocess.PIPE)

        out,err = p.communicate()
        jString = json.dumps({"submit": out})
        j = json.loads(jString)
        return j
    
    def version(self):
        v = "8.0.5"
        return v


#obj2 = Wms()
#print(obj2.status())


