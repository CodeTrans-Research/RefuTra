import os
import subprocess
import json
def execPy(modelname,repair=False):
    if not repair:
        evalpath = f"result/translate/{modelname}/java2python/python_eval/"
        outputpath = f"result/translate/{modelname}/java2python/jv2pyresult.json"
    else:
        evalpath = f"result/repair/{modelname}/java2python/python_repair_eval"
        outputpath = f"result/repair/{modelname}/java2python/jv2pyresult_repair.json"
    reslog = {}
    cnt = 0
    for _,_,fs in os.walk(evalpath):
        for f in fs:
            try:
                res = subprocess.run(['python3',os.path.join(evalpath,f)],capture_output=True,timeout=30)
                stdout = res.stdout.decode()
                stderr = res.stderr.decode()
            except:
                stdout = ""
                stderr = "loop"
            cnt += 1
            print(f'{cnt}:{f}',stderr)
            reslog[f[:-3]] = {"stdout":stdout,"stderr":stderr}
    json.dump(sumupRes(reslog),open(outputpath,"w"),indent=4)
def execJv(modelname,repair=False):
    if not repair:
        evalpath = f"result/translate/{modelname}/python2java/java_eval/"
        outputpath = f"result/translate/{modelname}/python2java/py2jvresult.json"
    else:
        evalpath = f"result/repair/{modelname}/python2java/java_repair_eval"
        outputpath = f"result/repair/{modelname}/python2java/py2jvresult_repair.json"
    reslog = {}
    cnt = 0
    for _,_,fs in os.walk(evalpath):
        for f in fs:
            try:
                res = subprocess.run(['java',os.path.join(evalpath,f)],capture_output=True,timeout=30)
                stdout = res.stdout.decode()
                stderr = res.stderr.decode()
            except:
                stdout = ""
                stderr = "loop"
            cnt += 1
            print(f'{cnt}:{f}')
            reslog[f[:-5]] = {"stdout":stdout,"stderr":stderr}
    json.dump(sumupRes(reslog),open(outputpath,"w"),indent=4)

def execCPP(modelname,repair=False,id=""):
    if not repair:
        evalpath = f"result/translate/{modelname}/java2cpp{id}/c++_eval"
        outputpath = f"result/translate/{modelname}/java2cpp{id}/jv2cppresult.json"
    else:
        evalpath = f"result/repair/{modelname}/java2cpp{id}/c++_repair_eval"
        outputpath = f"result/repair/{modelname}/java2cpp{id}/jv2cppresult_repair.json"
    reslog = {}
    cnt = 0
    for _,_,fs in os.walk(evalpath):
        for f in fs:
            cnt += 1
            print(f'{cnt}:{f}')
            res = subprocess.run(['g++',os.path.join(evalpath,f)],capture_output=True,timeout=30)
            stdout = res.stdout.decode()
            stderr = res.stderr.decode()
            if stderr != '':
                reslog[f[:-4]] = {"stdout":stdout,"stderr":"CompError!"+stderr}
                continue
            else:
                try:
                    res = subprocess.run(['./a.exe'],capture_output=True,timeout=30)
                    stdout = res.stdout.decode()
                    stderr = res.stderr.decode()
                except:
                    stdout = ""
                    stderr = "loop"
            
                reslog[f[:-4]] = {"stdout":stdout,"stderr":stderr}
    json.dump(sumupRes(reslog),open(outputpath,"w"),indent=4)

def sumupRes(reslog):
    reslis = []
    for key,item in reslog.items():
        result = ""
        if item["stdout"] != "":
            if item["stdout"].find("#Results: 10, 10") != -1 or item["stdout"].find("#Results:10, 10") != -1 :
                result = "Correct"
            else:
                result = "ComputeError"
        else:
            if item["stderr"] == "loop":
                result = "Loop"
            elif item["stderr"].find("Exception in thread") != -1:
                result = "RuntimeError"
            else:
                result = "CompileError"
        item["state"] = result
        if result == "Correct":
            item["WhyError"] = ""
        else:
            item["WhyError"] = result+"_"
        item["filename"] = key
        reslis.append(item)
    return reslis
        
if __name__ == "__main__":
    #execPy("transcoder",repair=True)
    #execPy("chatgpt",repair=True)
    #execPy("starchat",repair=True)
    #execPy("chatgpt")
    #execPy("transcoder")
    #execPy("starchat")
    #execJv("transcoder",repair=True)
    #execJv("starchat",repair=True)
    #execJv("chatgpt",repair=True)
    #execJv("transcoder")
    #execJv("chatgpt")
    #execJv("starchat")
    #execCPP("transcoder")
    #execCPP("transcoder",id="2")
    #execCPP("starchat")
    #execCPP("chatgpt")

