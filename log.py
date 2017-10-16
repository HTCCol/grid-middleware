import json
def log(log):
    file = open(log, "r")
    file_r = file.read()
    jString = json.dumps({"output": file_r})
    j = json.loads(jString)
    print (j)

log("/home/fabian/Downloads/tesis/grid-middleware/test.log")