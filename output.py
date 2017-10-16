import json

def outputFile(output):
    file=open(output,"r")
    file_r=file.read()
    jString = json.dumps({"output": file_r})
    j = json.loads(jString)
    print (j)
    
outputFile("/home/fabian/Downloads/tesis/grid-middleware/test.output")