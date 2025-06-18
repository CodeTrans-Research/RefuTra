import re
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from lang_processer.parser import JavaParser,PythonParser,CPPParser
from common.util import *
from common.traverse import traverseDiv
import copy
def pyReplaceLine(changelist,curline,newcode,changetype):
    changelist.append({"type":"del","line":curline,"changetype":changetype})
    changelist.append({"type":"add","line":curline,"content":newcode,"changetype":changetype})
    changelist.append({"type":"add","line":-1,"content":newcode,"changetype":changetype})

class mypyRewriter:
    errkindformat = [
        ("assignment","Incompatible types in assignment \(expression has type \"([a-zA-Z\[\]\|]+)\", variable has type \"([a-zA-Z\[\]\|]+)\"\)"),
        ("return","Incompatible return value type \(got \"([a-zA-Z\[\]\|]+)\", expected \"([a-zA-Z\[\]\|]+)\"\)"),
        ("call","No overload variant of \"([a-zA-Z\[\]\|\_]+)\""),
        ("argument","Argument [0-9] to \"([a-zA-Z\[\]\|\_]+)\" has incompatible type \"([a-zA-Z\[\]\|]+)\"; expected \"([a-zA-Z\[\]\|]+)\""),
        ("indexable","Value of type \"([a-zA-Z\[\]\|]+)\" is not indexable"),
        ("operator","Unsupported operand types for .+? \(\"([a-zA-Z\[\]\|]+)\" and \"([a-zA-Z\[\]\|]+)\"\)"),
        ("noret","error: No return value expected")
    ]
    rewriterdic = {errtype[0]:[] for errtype in errkindformat}
    def __init_subclass__(cls):
        super().__init_subclass__()
        cls.rewriterdic[cls.errkindformat[cls.errindex][0]].append(cls)
    def __init__(self,env) -> None:
        self.env = env
    def rewrite(self,codeinfo):
        raise NotImplementedError
    def check(self, errparse, errinfo):
        raise NotImplementedError
    def rewrite_dispense(self,errinfo,codeinfo):
        maintype = None
        errparse = None
        changelist = []
        for errformat in self.errkindformat:
            errparse = re.search(errformat[1],errinfo)
            if errparse != None:
                maintype = errformat[0]
                break
        if maintype in self.rewriterdic:
            for subrewriter in self.rewriterdic[maintype]:
                subrewriterinstance = subrewriter(self.env)
                if subrewriterinstance.check(errparse,errinfo):
                    changelist = subrewriterinstance.rewrite(codeinfo) 
                    break
        if len(changelist) > 0:
            Logger.cstwarning(f"type unpreserved: {errinfo}",0)
        return changelist

class mypy_Assign_Floatint_Rewriter(mypyRewriter):
    errindex = 0
    def check(self, errparse, errinfo):
        extype,vartype = errparse.group(1),errparse.group(2)
        return extype.find("float") != -1 and vartype == "int"
    def rewrite(self,codeinfo):
        changetype = "type_"+self.__class__.__name__.split("_")[1] + self.__class__.__name__.split("_")[2]
        code,incond,tolang,curline = codeinfo['code'],codeinfo['incond'],codeinfo['tolang'],codeinfo['curline']
        if code.find("inf") != -1:
            return []
        changelist,newcode = [],code
        pp = PythonParser(code)
        #dumpAST(pp.code,pp.tree.root_node)
        div = []
        traverseDiv(pp.code,pp.tree.root_node,div)
        #Logger.debug(div)
        recheckflg = False
        targetcond = None
        targetcond = set([f"{lv}%{rv}==0" for lv,rv in div]) | set([f"Not({lv}%{rv}!=0)" for lv,rv in div])
        if not(targetcond == None):
            if len(targetcond & incond) != 0: 
                recheckflg = True
        if recheckflg:
            return []
        if tolang == 'python':
            if code.find("/") != -1:
                newcode = code.replace("/","//")
            else:
                codesp = code.split("=")
                newcode = codesp[0] + "= " + "int( " + codesp[1] + " )"
            if newcode != code:
                pyReplaceLine(changelist,curline,newcode,changetype)
        elif tolang == "java":
            env = self.env
            env.propagateJvFloatVar(line=curline)
            changelist.append({"type":"add","line":-1,"content":codeinfo['code'],"changetype":changetype})
        return changelist
class mypy_Assign_Strint_Rewriter(mypyRewriter):
    errindex = 0
    def check(self, errparse, errinfo):
        extype,vartype = errparse.group(1),errparse.group(2)
        return (extype == "int" and vartype == "str") or (extype == "str" and vartype == "int")
    def rewrite(self,codeinfo):
        return [{"type":"add","line":-1,"content":codeinfo['code'],"changetype":"type_"+self.__class__.__name__.split("_")[1] + self.__class__.__name__.split("_")[2]}]
class mypy_Assign_Primclct_Rewriter(mypyRewriter):
    errindex = 0
    def check(self, errparse, errinfo):
        extype,vartype = errparse.group(1),errparse.group(2)
        clcts = ["list","set","dict"]
        return any(c in extype for c in clcts) ^ any(c in vartype for c in clcts)
        #return not [(c in extype and c not in vartype) or (c in vartype and c not in extype) for c in clcts] == [False for c in clcts]
    def rewrite(self,codeinfo):
        return [{"type":"add","line":-1,"content":codeinfo['code'],"changetype":"type_"+self.__class__.__name__.split("_")[1] + self.__class__.__name__.split("_")[2]}]
    

class mypy_Ret_Floatint_Rewriter(mypyRewriter):
    errindex = 1
    def check(self, errparse, errinfo):
        extype,vartype = errparse.group(1),errparse.group(2)
        return extype.find("float") != -1 and vartype == "int"
    def rewrite(self,codeinfo):
        changetype = "type_"+self.__class__.__name__.split("_")[1] + self.__class__.__name__.split("_")[2]
        code,tolang,curline = codeinfo['code'],codeinfo['tolang'],codeinfo['curline']
        if code.find("inf") != -1:
            return []
        changelist = []
        if tolang == 'python':
            if code.find("/") != -1:
                newcode = code.replace("/","//")
            else:
                codesp = code.split("return")
                newcode = code.replace(codesp[1]," int("+codesp[1].strip()+") ")

            if newcode != code:
                pyReplaceLine(changelist,curline,newcode,changetype)
        elif tolang == "java":
            env = self.env
            env.jvtyperewritevars.add("RET@")
            env.propagateJvFloatVar()
            changelist.append({"type":"add","line":-1,"content":codeinfo['code'],"changetype":changetype})
        return changelist
    
class mypy_Ret_Strint_Rewriter(mypyRewriter):
    errindex = 1
    def check(self, errparse, errinfo):
        extype,vartype = errparse.group(1),errparse.group(2)
        return (extype == "int" and vartype == "str") or (extype == "str" and vartype == "int")
    def rewrite(self,codeinfo):
        return [{"type":"add","line":-1,"content":codeinfo['code'],"changetype":"type_"+self.__class__.__name__.split("_")[1] + self.__class__.__name__.split("_")[2]}]
class mypy_Ret_Primclct_Rewriter(mypyRewriter):
    errindex = 1
    def check(self, errparse, errinfo):
        extype,vartype = errparse.group(1),errparse.group(2)
        clcts = ["list","set","dict"]
        return not [(c in extype and c not in vartype) or (c in vartype and c not in extype) for c in clcts] == [False for c in clcts]
    def rewrite(self,codeinfo):
        return [{"type":"add","line":-1,"content":codeinfo['code'],"changetype":"type_"+self.__class__.__name__.split("_")[1] + self.__class__.__name__.split("_")[2]}]
    
class mypy_Call_Floatint_Rewriter(mypyRewriter):
    errindex = 2
    def check(self, errparse, errinfo):
        self.funcname = errparse.group(1)
        pmtst = errinfo.split("matches argument type")[1][1:].replace("[call-overload]","").replace("\"","").strip()
        self.pmtlist = [pmt.strip() for pmt in pmtst.split(",")]
        targetfunclist = ["__getitem__","__setitem__","range"]
        
        return "float" in self.pmtlist and self.funcname in targetfunclist
    def rewrite(self, codeinfo):
        code,incond,tolang,curline = codeinfo['code'],codeinfo['incond'],codeinfo['tolang'],codeinfo['curline']
        changetype = "type_"+self.__class__.__name__.split("_")[1] + self.__class__.__name__.split("_")[2]
        changelist,newcode = [],code
        if tolang == "python":
            if code.find("/") != -1:
                newcode = code.replace("/","//")
                '''tmpmap = {}
                for cond in incond:
                    mt = re.findall("(.+)%(.+)==0",cond) + re.findall("Not\((.+)%(.+)!=0\)",cond)
                    cnt = 0
                    for v1,v2 in mt:
                        maskexp = "@"+str(cnt)
                        try:
                            newcode = re.sub(f"{v1}\s*/\s*{v2}",maskexp,newcode)
                        except:
                            continue
                        tmpmap[maskexp] = f"{v1}/{v2}" 
                        cnt += 1
                if newcode.find("/") != -1:
                    newcode = code.replace("/","//")
                else:
                    newcode = code'''
                '''for old,new in tmpmap.items():
                    newcode = newcode.replace(old,new)'''
            else:
                if self.funcname == "range":
                    codepre = code[:code.find(self.funcname)]
                    codecall = code[code.find(self.funcname):]
                    newcodecall = self.funcname + "("
                    callargs = ""
                    codepost = ""
                    cnt = 0
                    callflg = False
                    postflg = False
                    for c in codecall:
                        if callflg:
                            if cnt == 0:
                                postflg = True
                                callflg = False
                            elif cnt > 0:
                                callargs += c
                        elif postflg:
                            codepost += c
                        if c == '(':
                            cnt += 1
                            callflg = True
                        elif c == ')':
                            cnt -= 1
                    callargs = callargs[:-1]
                    #Logger.debug(callargs)
                    #Logger.debug(codepost)
                    codesp = callargs.split(',')
                    for index,arg in enumerate(codesp):
                        if self.pmtlist[index] == "float":
                            newcodecall += "int (" + arg + "),"
                        else:
                            newcodecall += arg + ","
                    newcodecall = newcodecall[:-1] + ")"
                    newcode = codepre + newcodecall + codepost
                    detailerrortype = "floatint"
            if newcode != code:
                pyReplaceLine(changelist,curline,newcode,changetype)
        return changelist
    
class mypy_Arg_Floatint_Rewriter(mypyRewriter):
    errindex = 3
    def check(self, errparse, errinfo):
        extype,vartype = errparse.group(1),errparse.group(2)
        return extype == "float" and vartype == "int"
    def rewrite(self,codeinfo):
        changetype = "type_"+self.__class__.__name__.split("_")[1] + self.__class__.__name__.split("_")[2]
        code,tolang,curline = codeinfo['code'],codeinfo['incond'],codeinfo['tolang'],codeinfo['curline']
        changelist,newcode = [],code
        if tolang == 'python':
            if code.find("/") != -1:
                newcode = code.replace("/","//")
            if newcode != code:
                pyReplaceLine(changelist,curline,newcode,changetype)
        return changelist
    
class mypy_Arg_Len_Rewriter(mypyRewriter):
    errindex = 3
    def check(self, errparse, errinfo):
        return errparse.group(1) == "len"
    def rewrite(self,codeinfo):
        return [{"type":"add","line":-1,"content":codeinfo['code'],"changetype":"type_"+self.__class__.__name__.split("_")[1] + self.__class__.__name__.split("_")[2]}]
    
class mypy_Indexable_Rewriter(mypyRewriter):
    errindex = 4
    def check(self, errparse, errinfo):
        return True
    def rewrite(self,codeinfo):
        return [{"type":"add","line":-1,"content":codeinfo['code'],"changetype":"type_indexable"}]

class mypy_Operator_Str_Rewriter(mypyRewriter):
    errindex = 5
    def check(self, errparse, errinfo):
        extype,vartype = errparse.group(1),errparse.group(2)
        return (vartype == "str") or (extype == "str")
    def rewrite(self,codeinfo):
        return [{"type":"add","line":-1,"content":codeinfo['code'],"changetype":"type_"+self.__class__.__name__.split("_")[1] + self.__class__.__name__.split("_")[2]}]        

class mypy_Noret_Rewriter(mypyRewriter):

    errindex = 6
    def check(self, errparse, errinfo):
        return True
    def rewrite(self,codeinfo):
        return [{"type":"add","line":-1,"content":codeinfo['code'],"changetype":"type_noret"}]
    
def rewriteFuncName(code,namenode,calllis,orifuncname,replacename,funcnode):
    code = code[:namenode.start_byte - funcnode.start_byte] + replacename + code[namenode.end_byte- funcnode.start_byte: ] 
    #Logger.debug(code)
    oneplacedif = len(replacename) - len(orifuncname)
    placedif = oneplacedif
    for node in calllis:
        code = code[:node.start_byte+placedif- funcnode.start_byte] + replacename + code[node.end_byte+placedif- funcnode.start_byte:]
        placedif += oneplacedif
    return code

def rewriteFuncDecl(oripycode,rettype,formaltypes):
    codeline = oripycode.split("\n")
    funcdef = codeline[0]
    funcdef2 = ""
    cnt = 0
    #Logger.debug(funcdef)
    for ch in funcdef:
        if ch == "," or ch == ")":
            jvformaltp = removeBlank(formaltypes[cnt][0])
            if jvformaltp in TYPEMAP:
                funcdef2 += (" : " + TYPEMAP[jvformaltp] + " " + ch)
            else:
                Logger.debug("not map for %s" %(jvformaltp))
                funcdef2 += ch  
            cnt += 1
        elif ch == ":":
            rettype = removeBlank(rettype)
            if rettype != "void" and rettype in TYPEMAP:
                funcdef2 += ("-> " + TYPEMAP[rettype] + ch)
            else:
                
                if rettype != "void":
                    Logger.debug("not map for %s" %(rettype))
                else:
                    funcdef2 += " -> None"
                funcdef2 += ch

                
        else:
            funcdef2 += ch
    return oripycode.replace(funcdef,funcdef2)

def rewriteSingleAssign(assignstr,localtypedic,localarrinitdic,changelist,curline,blank,assigned):
    assignsp = assignstr.split("=")
    #Logger.debug(assignsp)
    #Logger.debug(assignsp)
    if len(assignsp) != 2:
        return [assignstr]
    leftv = assignsp[0].strip()
    newassign = []
    if leftv.find(",") == -1:
        if isSingleVariable(leftv) and leftv not in assigned:
            assigned.add(leftv)
            if leftv in localtypedic:
                if localtypedic[leftv] in TYPEMAP:
                    if localtypedic[leftv] in ARRTYPEINITMAP:
                        newarrinitstr = ""
                        initfmt = ARRTYPEINITMAP[localtypedic[leftv]]
                        argcnt = 0
                        args = localarrinitdic[leftv]
                        spcnt = 0
                        for c in initfmt:
                            if c == "#":
                                spcnt += 1
                        rightv = assignsp[1].strip()
                    newassign.append(leftv + " : " + TYPEMAP[localtypedic[leftv]] + " = " + assignsp[1]) 
                    assigned.add(leftv)
                    del localtypedic[leftv]
                else:
                    Logger.debug("not map for %s" %(localtypedic[leftv]))
                    newassign.append(leftv + " : Any = " + assignsp[1])
            else:
                newassign.append(leftv + " : Any = " + assignsp[1])
        else:
            newassign.append(assignstr)
    else:
        leftvs = leftv.split(",")
        rightvs = assignsp[1].split(",")
        if len(leftvs) != len(rightvs):
            return [assignstr]
        for leftv,rightv in zip(leftvs,rightvs):
            leftv = leftv.strip()
            rightv = rightv.strip()
            if isSingleVariable(leftv) and leftv not in assigned:
                assigned.add(leftv)
                if leftv in localtypedic:
                    if localtypedic[leftv] in TYPEMAP:
                        newassign.append(leftv + " : " + TYPEMAP[localtypedic[leftv]] + " = " + rightv) 
                        del localtypedic[leftv] 
                    else:
                        newassign.append(leftv + " : Any = " + assignsp[1])
                else:
                    newassign.append(leftv + " : Any = " + assignsp[1])
            else:
                newassign.append(assignstr)
    return newassign
def rewriteAssign(oricode,oldassigndic,newassigndic):

    oricodesp = oricode.split("\n")
    neworicode = ""
    cnt = 1
    for oricodeline in oricodesp:
        if cnt in oldassigndic:
            blankcnt = blankCount(oricodeline)
            indent = ""
            for i in range(0,blankcnt):
                indent += " "
            newassign = ""
            for ass in newassigndic[cnt]:
                newassign += (indent + ass + "\n")
            neworicode += newassign   
        else:
            neworicode += (oricodeline + "\n")
        cnt += 1
    return neworicode
