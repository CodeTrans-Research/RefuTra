import os
import json
def generateJavaEval(modelname,repair=False):
    if not repair:
        transfilepath = f"result/translate/{modelname}/python2java/java"
        oraclepath = "dataset/python2java/java"
        evalpath = f"result/translate/{modelname}/python2java/java_eval"
    else:
        transfilepath = f"result/repair/{modelname}/python2java/java_repair"
        oraclepath = "dataset/python2java/java"
        evalpath = f"result/repair/{modelname}/python2java/java_repair_eval"
    oracleset = set()
    for _,_,fs in os.walk(oraclepath):
        for f in fs:
            oracleset.add(f)
    cnt = 0
    for _,_,fs in os.walk(transfilepath):
        for f in fs:
            if f in oracleset:
                transcode = open(os.path.join(transfilepath,f)).read()
                newtranscode = ""
                for line in transcode.split("\n"):
                    if 'import' in line:
                        continue
                    newtranscode += line + "\n"
                transcode = newtranscode
                if 'class' in transcode or 'main' in transcode:
                    print(os.path.join(transfilepath,f))
                transcode = transcode.replace("static","").replace("public","").replace("f_gold","f_filled").replace("'''","").strip()
                oraclecode = open(f"{oraclepath}/{f}").read().replace("import javafx.util.Pair;","")
                newcode = oraclecode.replace("//TOFILL","static " + transcode)
                open(os.path.join(evalpath,f),"w").write(newcode)
                cnt += 1

def generateCPPEval(modelname,repair=False):
    if not repair:
        transfilepath = f"result/translate/{modelname}/java2cpp/c++"
        oraclepath = "dataset/java2cpp/cpp"
        evalpath = f"result/translate/{modelname}/java2cpp/c++_eval"
    else:
        transfilepath = f"result/repair/{modelname}/java2cpp/c++_repair"
        oraclepath = "dataset/java2cpp/cpp"
        evalpath = f"result/repair/{modelname}/java2cpp/c++_repair_eval"
    oracleset = set()
    for _,_,fs in os.walk(oraclepath):
        for f in fs:
            oracleset.add(f)
    cnt = 0
    for _,_,fs in os.walk(transfilepath):
        for f in fs:
            if f in oracleset:
                transcode = open(os.path.join(transfilepath,f)).read()
                '''newtranscode = ""
                for line in transcode.split("\n"):
                    if 'import' in line:
                        continue
                    newtranscode += line + "\n"
                transcode = newtranscode'''
                if 'class' in transcode or 'main' in transcode:
                    print(os.path.join(transfilepath,f))
                transcode = transcode.replace("static","").replace("public","").replace("f_gold","f_filled").replace("'''","").replace("//","").strip()
                oraclecode = open(f"{oraclepath}/{f}").read()
                newcode = oraclecode.replace("//TOFILL",transcode)
                open(f"{evalpath}/{f}","w").write(newcode)
                cnt += 1
                print(cnt)
def generatePythonEval(modelname,repair=False):
    if not repair:
        transfilepath = f"result/translate/{modelname}/java2python/python"
        oraclepath = "dataset/java2python/python"
        evalpath = f"result/translate/{modelname}/java2python/python_eval"
    else:
        transfilepath = f"result/repair/{modelname}/java2python/python_repair"
        oraclepath = "dataset/java2python/python"
        evalpath = f"result/repair/{modelname}/java2python/python_repair_eval"
    oracleset = set()
    for _,_,fs in os.walk(oraclepath):
        for f in fs:
            oracleset.add(f)
    cnt = 0
    newimport = '''import sys
import math
import heapq
from queue import Queue
import numpy as np
'''
    for _,_,fs in os.walk(transfilepath):
        for f in fs:
            if f in oracleset:
                transcode = open(os.path.join(transfilepath,f)).read()
                transcode = transcode.replace("f_gold","f_filled").replace("'''","").strip()
                oraclecode = newimport + open(f"{oraclepath}/{f}").read()
                orieval = '''for i, parameters_set in enumerate(param):
        if f_filled(*parameters_set) == f_gold(*parameters_set):
            n_success+=1
    print("#Results: %i, %i" % (n_success, len(param)))'''
                neweval = '''for i, parameters_set in enumerate(param):
        import copy
        p2 = copy.deepcopy(parameters_set)
        filledres = f_filled(*parameters_set)
        goldres = f_gold(*p2)
        if filledres == goldres:
            n_success+=1
        else:
            if set([filledres,goldres]) <= set([float("inf"),sys.maxsize,2147483647]) or set([filledres,goldres]) <= set([float("-inf"),-sys.maxsize-1,-sys.maxsize,-2147483648]):
                n_success += 1
    print("#Results: %i, %i" % (n_success, len(param)))
'''
                newcode = oraclecode.replace("#TOFILL",transcode).replace(orieval,neweval)
                open(os.path.join(evalpath,f),"w").write(newcode)
                cnt += 1
                print(cnt)
def generateCPPEval2(modelname,repair=False):
    if not repair:
        transfilepath = f"result/translate/{modelname}/java2cpp2/c++"
        oraclepath = "dataset/java2cpp2/cpp"
        evalpath = f"result/translate/{modelname}/java2cpp2/c++_eval"
    else:
        transfilepath = f"result/repair/{modelname}/java2cpp2/c++_repair"
        oraclepath = "dataset/java2cpp2/cpp"
        evalpath = f"result/repair/{modelname}/java2cpp2/c++_repair_eval"
    oracleset = set()
    for _,_,fs in os.walk(oraclepath):
        for f in fs:
            oracleset.add(f)
    cnt = 0
    for _,_,fs in os.walk(transfilepath):
        for f in fs:
            if f in oracleset:
                
                transcode = open(os.path.join(transfilepath,f)).read()
                '''newtranscode = ""
                for line in transcode.split("\n"):
                    if 'import' in line:
                        continue
                    newtranscode += line + "\n"
                transcode = newtranscode'''
                if 'class' in transcode or 'main' in transcode:
                    print(os.path.join(transfilepath,f))
                transcode = transcode.replace("static","").replace("public","").replace("f_gold","f_filled").replace("'''","").replace("//","").strip()
                oraclecode = open(f"{oraclepath}/{f}").read()
                newcode = oraclecode.replace("//TOFILL",transcode)
                open(f"dataset3/{modelname}/c++_repair_eval/{f}","w").write(newcode)
                cnt += 1
                print(cnt)
if __name__ == "__main__":
    generateJavaEval("transcoder",repair=True)
    #generateJavaEval("starchat",repair=True)
    #generateJavaEval("chatgpt",repair=True)
    #generateJavaEval("transcoder")
    #generateJavaEval("starchat")
    #generateJavaEval("chatgpt")

    #generatePythonEval("chatgpt")
    #generatePythonEval("transcoder")
    #generatePythonEval("starchat")
    #generatePythonEval("transcoder",repair=True)
    #generatePythonEval("starchat",repair=True)
    #generatePythonEval("chatgpt",repair=True)
    
    #generateCPPEval("transcoder",repair=True)
    #generateCPPEval("starchat",repair=True)
    #generateCPPEval("chatgpt",repair=True)