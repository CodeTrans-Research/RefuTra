import tree_sitter as ts
import os
import json
import re
import subprocess
import random
import math
import copy
import itertools
import sys
import argparse
from pathlib import Path
from z3 import *
sys.path.append(str(Path(__file__).resolve().parent.parent))
from lang_processer.parser import JavaParser,PythonParser,CPPParser
from common.dataflow import DefineReach,ConditionReach
from common.util import *
from lang_processer.cfg import *
from common.traverse import *
from cstchecker.writer import mypyRewriter,rewriteSingleAssign,rewriteAssign,rewriteFuncDecl,rewriteFuncName,rewriteOpAssExpr


class CheckManager:
    def __init__(self,fraddr,toaddr,pytypedaddr,filename,fr,to):
        self.frlang = fr
        self.tolang = to
        self.controlnoequeal = 0
        self.filename = filename
        self.fraddr = fraddr
        self.toaddr = toaddr
        self.pytypedaddr = pytypedaddr
        self.cfgmap = {}
        self.orifrcode = open(self.fraddr).read()
        self.oritocode = open(self.toaddr).read()
        self.cftmap = {}
        self.arrshapeinfo = {}
        self.arrvalueinfo = {}
        self.arrdefmap = {}
        self.error = False
        self.changelist = []
        envinitmap = {"java":self.initjvenv,"python":self.initpyenv,"cpp":self.initcenv}
        frerror = envinitmap[self.frlang](self.orifrcode)
        toerror = envinitmap[self.tolang](self.oritocode)
        self.parseerror = frerror & toerror
        if not self.parseerror:
            return
        self.initVarMap()
        self.omitListInArray()
        if (self.frlang,self.tolang) != ("python","java"):
            self.tovartypemap = {}
            for v,tp in self.oracletypemap.items():
                newv = v
                if v in self.varmap:
                    newv = self.varmap[v]
                self.tovartypemap[newv] = tp
            oritomap = None
            if self.tolang == "java":
                oritomap = self.jvvartypemap
            elif self.tolang == "cpp":
                oritomap = self.cvartypemap
            if oritomap != None:
                for v,tp in oritomap.items():
                    if v not in self.tovartypemap:
                        self.tovartypemap[v] = tp
        else:
            self.tovartypemap = self.oracletypemap
        '''self.initjvenv(self.orijvcode)
        self.initpyenv(self.oripycode)'''
    def initcenv(self,oricode):
        self.oriccode = oricode
        self.comitcfts = []
        self.creviselist = []
        tokenplace = oricode.find("*[")
        while tokenplace != -1:
            oricode = oricode.replace("*[","[",1)
            self.creviselist.append(((tokenplace,tokenplace+1),"*["))
            tokenplace = oricode.find("*[")
        tokenplace = oricode.find("* [")
        while tokenplace != -1:
            oricode = oricode.replace("* [","[")
            self.creviselist.append(((tokenplace,tokenplace+1),"* ["))
            tokenplace = oricode.find("* [")
        self.creviselist.sort()
        self.creviselist.reverse()
        if self.frlang == "cpp":
            self.frcode = oricode
        else:
            self.tocode = oricode
        cp = CPPParser(oricode)
        
        self.ccd , self.ctree = cp.code,cp.tree
        error = findError(self.ctree.root_node)
        self.error = self.error or error
        if error:
            return False
        self.ccft = CPPCftConstruct(self.ccd,self.ctree.root_node)
        if self.ccft != None and type(self.ccft) != type([]):
            self.ccft = [self.ccft]
 
        self.clineindex = splitLineAST(self.ccd,self.ctree.root_node)
        if self.tolang == "cpp":
            self.tolineindex = self.clineindex
        self.ccfg = CFG(self.clineindex,"cpp")
        self.cftmap["cpp"] = self.ccft
        tp = cp.getFunctions()[0]
        self.crettype = removeBlank(tp[0]).replace("std::","")
        self.cformaltypes = tp[1]
        self.clocaltypes = tp[2]
        self.carrinitvalues = tp[5]
        self.carrinitvalues = {info[1]:info[2] for info in self.carrinitvalues}
        self.arrdefmap["cpp"] = tp[6]
        self.cvartypemap = {}
        self.carrinfos = {}
        self.cvartypemap["RET@"] = self.crettype
        self.cfuncname = tp[-1]
        for item in self.cformaltypes:
            vname,typ = item[1],removeBlank(item[0]).replace("std::","")
            self.cvartypemap[vname] = typ
            if checkCArray(typ):
                self.carrinfos[vname] = {}

        for item in self.clocaltypes:
            vname,typ,lenginfo = item[1],removeBlank(item[0]).replace("std::",""),item[2]
            self.cvartypemap[vname] = typ
            if checkCArray(typ):
                if lenginfo != None:
                    if "vector" in typ and len(lenginfo) == 0: # not list, exclude
                        self.carrinitvalues.pop(vname,None)
                        #self.carrinitvalues = [info for info in self.carrinitvalues if info[1] != vname]
                    else:
                        self.carrinfos[vname] = [removeBlank(l) for l in lenginfo]
        self.arrshapeinfo["cpp"] = self.carrinfos
        if self.frlang == "cpp" or self.frlang == "python":
            self.oracletypemap = self.cvartypemap
        self.cstart,self.cend = tp[3],tp[4]
        CFGConstruct(self.ccd,self.ccft,{"start":tp[3],"end":tp[4]},self.ccfg)
        self.traverseReturn(self.ctree.root_node,self.ccfg)
        CDefUseTvs(self.ccd,self.ctree.root_node,self.ccfg,'U',[],{})
        self.ccfg.reduceDRinFor()
        self.cfgmap['cpp'] = self.ccfg
        for arrd in self.arrdefmap["cpp"]:
            typ,vname,df = arrd[0],arrd[1],arrd[2]
            if vname not in self.carrinitvalues or vname not in self.carrinfos:
                continue
            if type(df) == list:
                df = df[0]
            oriv = self.carrinitvalues[vname]
            initv = traverseArrInit(self.ccd,df,vname,self.carrinfos[vname],self.ccfg,self.ccft,defaultvalue=oriv)            
            self.carrinitvalues[vname] = initv
        self.arrvalueinfo['cpp'] = self.carrinitvalues   
        return True
    def initjvenv(self,orijvcode):
        self.orijvcode = orijvcode
        if orijvcode.find("class") == -1:
            orijvcode = "class shi1ro{\n"+orijvcode+"\n}\n"
        orijvcode = orijvcode.replace('public','').replace('static','')
        if self.frlang == "java":
            self.frcode = orijvcode
        else:
            self.tocode = orijvcode
        jp = JavaParser(orijvcode)
        self.jvcd , self.jvtree = jp.code,jp.tree
        #dumpAST(self.jvcd,self.jvtree.root_node)
        error = findError(self.jvtree.root_node)
        self.error = self.error or error
        if error:
            return False
        self.jvcft = JavaCftConstruct(self.jvcd,self.jvtree.root_node)
        if self.jvcft != None and type(self.jvcft) != type([]):
            self.jvcft = [self.jvcft]
        self.cftmap["java"] = self.jvcft
        self.jvlineindex = splitLineAST(self.jvcd,self.jvtree.root_node)
        if self.tolang == "java":
            self.tolineindex = self.jvlineindex
        self.jvcfg = CFG(self.jvlineindex,"java")
        tp = jp.getFunctions()[0]
        self.jvrettype = tp[0]
        self.jvformaltypes = tp[1]
        self.jvlocaltypes = tp[2]
        self.jvstart,self.jvend = tp[3],tp[4]
        self.jvfuncname = tp[-1]
        self.jvvartypemap = {}
        self.jvarrinfos = {}
        self.jvtyperewritevars = set()
        #self.jvtyperewritevardone = set()
        jvarrdefs = []
        self.jvvartypemap["RET@"] = self.jvrettype
        for item in self.jvformaltypes:
            vname,typ = item[1],removeBlank(item[0])
            self.jvvartypemap[vname] = typ
            if checkJVArray(typ):
                self.jvarrinfos[vname] = {}
        self.jvdeflineplaces = {}
        self.jvarrinitvalues = {}
        for item in self.jvlocaltypes:
            vname,typ,lenginfo,definfo = item[1],removeBlank(item[0]),item[2],item[3]
            if lenginfo == ['nan']:
                lenginfo = []
                self.jvarrinitvalues[vname] = 'Other'
            for i in range(len(lenginfo)):
                leng = lenginfo[i]
                try:
                    leng = int(leng)
                    if leng < 0:
                        lenginfo[i] = str(-leng)
                        self.jvarrinitvalues[vname] = 'Other'
                except:
                    continue
            self.jvvartypemap[vname] = typ
            self.jvdeflineplaces[vname] = getLinebyPlace(self.jvlineindex,definfo.start_byte)
            if checkJVArray(typ):
                self.jvarrinfos[vname] = [removeBlank(l) for l in lenginfo]
                jvarrdefs.append((typ,vname,definfo))
        self.arrdefmap["java"] = jvarrdefs
        #Logger.debug(self.jvlocaltypes)
        self.arrshapeinfo["java"] = self.jvarrinfos
        localarrinitdic = {}
        for ts in self.jvlocaltypes:
            var = ts[1]
            if removeBlank(ts[0]) in ARRTYPEINITMAP:
                localarrinitdic[var] = ts[2]
        if self.frlang == "java" or self.frlang == "python":
            self.oracletypemap = self.jvvartypemap
        CFGConstruct(self.jvcd,self.jvcft,{"start":self.jvstart,"end":self.jvend},self.jvcfg)
        for arrd in jvarrdefs:
            vname = arrd[1]
            if vname in self.jvarrinitvalues:
                continue
            lenginfo = self.jvarrinfos[vname]
            initv = traverseArrInit(self.jvcd,arrd[2],vname,lenginfo,self.jvcfg,self.jvcft,defaultvalue='0')
            self.jvarrinitvalues[vname] = initv
            #Logger.debug(initv)
        self.arrvalueinfo['java'] = self.jvarrinitvalues
        self.traverseReturn(self.jvtree.root_node,self.jvcfg)
        jvDefUseTvs(self.jvcd,self.jvtree.root_node,self.jvcfg,'U',[],{})
        self.jvcfg.reduceDRinFor()
        self.cfgmap['java'] = self.jvcfg
        '''for n in self.jvcfg.nodelist:
            Logger.debug(n)'''
        return True 
    def initpyenv(self,oripycode):
        pp = PythonParser(oripycode)
        if self.frlang == "python":
            self.frcode = oripycode
        else:
            self.tocode = oripycode
        self.oripycode = oripycode
        self.pycd , self.pytree = pp.code,pp.tree
        error = findError(self.pytree.root_node)
        #dumpAST(self.pycd,self.pytree.root_node)
        if oripycode.find("++") != -1 or oripycode.find("--") != -1:
            error = True
        self.error = self.error or error
        if error:
            return False
        self.pycft = PythonCftConstruct(self.pycd,self.pytree.root_node)
        if self.pycft != None and type(self.pycft) != type([]):
            self.pycft = [self.pycft]
        self.cftmap["python"] = self.pycft
        self.pylineindex = splitLineAST(self.pycd,self.pytree.root_node)
        self.pycfg = CFG(self.pylineindex,"python")
        if self.tolang == "python":
            self.tolineindex = self.pylineindex
        #funclis = []
        #findPyFGold(self.pycd,self.pytree.root_node,funclis)
        goldfunc = pp.getFunctions()[0]
        CFGConstruct(self.pycd,self.pycft,goldfunc,self.pycfg)
        self.traverseReturn(self.pytree.root_node,self.pycfg)
        if self.tolang == "python":
            info = [v for v in self.arrshapeinfo[self.frlang]]
        else:
            info = []
        pyDefUseTvs(self.pycd,self.pytree.root_node,self.pycfg,'U',info,{})
        self.pycfg.reduceDRinFor()
        arrinfo = self.pycfg.extractPyArr()
        self.arrshapeinfo["python"] = {v:info['length'] for v,info in arrinfo.items()}
        self.pyarrinitvalueinfo = {}
        for v,info in arrinfo.items():
            self.pyarrinitvalueinfo[v] = normalizeArrValue(info['value'])
        self.arrvalueinfo['python'] = self.pyarrinitvalueinfo
        pyarrdefs = [(None,v,info['node']) for v,info in arrinfo.items()]
        self.pystrset = goldfunc["strset"]
        STMTCONVERT[("python","java")] = self.py2jv
        STMTCONVERT[("java","python")] = self.jv2py
        STMTTRANSPILE2PY["java"] = self.jv2py
        self.arrdefmap["python"] = pyarrdefs
        self.cfgmap['python'] = self.pycfg
        #self.Logger.debugCFG()
        return True
    def resetEnv(self,lang,key):
        if lang == "cpp":
            cft, lineindex, code, tree, start, end = self.ccft, self.clineindex, self.ccd, self.ctree.root_node, self.cstart, self.cend
            dutrafunc = CDefUseTvs
        elif lang == "java":
            cft, lineindex, code, tree, start, end = self.jvcft, self.jvlineindex, self.jvcd, self.jvtree.root_node, self.jvstart, self.jvend
            dutrafunc = jvDefUseTvs
        newcfg = CFG(lineindex,lang)
        cft,changeflg,_ = omitCFTbyCFG(cft,newcfg,key)
        if changeflg:
            CFGConstruct(code,cft,{"start":start,"end":end},newcfg)
            self.traverseReturn(tree,newcfg)
            dutrafunc(code,tree,newcfg,'U',[],{})
            newcfg.reduceDRinFor()
            if lang == 'cpp':
                self.ccfg = newcfg
                self.ccft = cft
                self.cfgmap['cpp'] = newcfg
            elif lang == "java":
                self.jvcft = cft
                self.jvcfg = newcfg
                self.cfgmap['java'] = newcfg
    def reduceCCFG(self,frcfg):
        self.resetEnv("cpp","delete")
        tocfg = self.cfgmap[self.tolang]
        if not(self.cfgnodeTypeCheck(frcfg,tocfg)):
            self.resetEnv("cpp","new")
        tocfg = self.cfgmap[self.tolang]
        if not(self.cfgnodeTypeCheck(frcfg,tocfg)):
            self.resetEnv("cpp","literal")
        #tocfg = self.cfgmap[self.tolang]
        #Logger.debug((self.cfgnodeTypeCheck(frcfg,tocfg)))
    def reduceJVCFG(self):
        self.resetEnv("java","literal")
    
    def py2jv(self,st):
        return py2jv(st,self.jvvartypemap)
    def jv2py(self,st):
        return jv2py(st,self.jvvartypemap)

    def rewriteArrayDimen(self,vname,frcfg,tocfg):
        def getArrExpr(info):
            if 'expr' in info:
                return info['expr']
            elif 'lv' in info:
                return info['lv']
            else:
                return None
        changelist = []
        if self.cfgnodeTypeCheck(frcfg,tocfg):
            frarrs = []
            toarrs = []
            for node in frcfg.nodelist:
                for ud in node['UD']:
                    if renamevar(ud[0],self.varmap) == vname:
                        frarrexpr = getArrExpr(ud[3])
                        if frarrexpr != None:
                            frarrs.append(frarrexpr)
            for node in tocfg.nodelist:
                for ud in node['UD']:
                    if ud[0] == vname:
                        toarrexpr = getArrExpr(ud[3])
                        if toarrexpr != None:
                            toarrs.append((toarrexpr,ud[2]))
            if len(frarrs) == len(toarrs):
                for i in range(0,len(frarrs)):
                    frexp = frarrs[i]
                    toexp = toarrs[i][0]
                    toline = toarrs[i][1]
                    correctexp = STMTCONVERT[(self.frlang,self.tolang)](frexp)
                    changelist.append({"type":"replace","line":toline,"old":toexp,"new":correctexp,"changetype":"arrdimen"})
        return changelist
    def rewriteIf(self,errorinfo,tosplitline):
        oritocode = self.tocode
        orifrcode = self.frcode
        frifnode = errorinfo['frcond_node']
        toifnode = errorinfo['tocond_node']
        toifnodestmt = oritocode[toifnode.start_byte:toifnode.end_byte]
        frifnodestmt = orifrcode[frifnode.start_byte:frifnode.end_byte]
        changelist = []
        changelist.append({"type":"add","content":toifnodestmt,"line":-1,"changetype":"ifcond"})
        line = getLinebyPlace(tosplitline,toifnode.start_byte)
        newif = STMTCONVERT[(self.frlang,self.tolang)](frifnodestmt)
        newif = renamevar(newif,self.varmap)
        if self.tolang == "java": #python: if(var) -> java:if(var != 0)
            cc = ConditionComparar()
            #Logger.debug(newif)
            transif = cc.post2Func(cc.infix2postfix(newif),lang=self.tolang)[0]
            if cc.normalized and not self.checkBoolVar(cc.normalizedexp,self.jvvartypemap):
                newif = "(" + transif + ")"
        Logger.cstwarning(f"if-statement unpreserved: src: {errorinfo['frcond']}, tgt: {errorinfo['tocond']}",line)
        changelist.append({"type":"replace","old":toifnodestmt,"new":newif,"line":line,"changetype":"ifcond"})
        return changelist
    def rewriteWhile(self,errorinfo,tosplitline):
        oritocode = self.tocode
        changelist = []
        startb = errorinfo["toplace"][0]
        endb = errorinfo["toplace"][1]
        if self.tolang == "python":
            blank,startline,_ = getSELine(startb,endb,oritocode,tosplitline)
            cond = errorinfo["frcond"]
            cond = renamevar(cond,self.varmap)
            cond = cond.replace("length()","length")
            f = re.findall('[a-zA-Z0-9\[\]_]*\.length',cond)
            for matched in f:
                m = re.match('([a-zA-Z0-9\[\]_]*)\.length',matched)
                cond = cond.replace(matched,"len(" + m[1] + ")")
            whilestatement = "while " + STMTTRANSPILE2PY[self.frlang](cond) + " :"
            changelist.append({"type":"add","content":errorinfo["frcond"],"line":-1,"changetype":"whileloop"})
            Logger.cstwarning(f"while-statement unpreserved: src: {errorinfo['frcond']}, tgt: {errorinfo['tocond']}",startline)
            changelist.append({"type":"del","line":startline,"changetype":"while"})
            changelist.append({"type":"add","content":blank + whilestatement,"line":startline,"changetype":"while"})
        elif self.tolang == "java" or self.tolang == "cpp":
            endb = errorinfo['towhileplace'][1]
            _,startline,_ = getSELine(startb,endb,oritocode,tosplitline)
            cond = STMTCONVERT[(self.frlang,self.tolang)](errorinfo['frcond'])
            newcode = f"while ({cond})"
            changelist.append({"type":"add","content":errorinfo["frcond"],"line":-1,"changetype":"whileloop"})
            Logger.cstwarning(f"while-statement unpreserved: src: {errorinfo['frcond']}, tgt: {errorinfo['tocond']}",startline)
            changelist.append({"type":"replace","line":startline,"old":oritocode[startb:endb],"new":newcode,"changetype":"while"})
        return changelist
    def rewriteFor(self,errorinfo,tosplitline):
        oritocode = self.tocode
        changelist = []
        startb = errorinfo["toplace"][0]
        detailtype = errorinfo['detailtype'] if 'detailtype' in errorinfo else None
        endb = errorinfo["toplace"][1]
        if self.tolang == "python":
            blank,startline,endline = getSELine(startb,endb,oritocode,tosplitline)
            frinit = errorinfo["frinit"]
            initst = ""
            for st in frinit:
                st = st.replace(";","")
                st = st.strip()
                stsplit = st.split(" ")
                if stsplit[0] in TYPEMAP:
                    stsplit.pop(0)
                newst = ""
                for s in stsplit:
                    newst += s + " "
                initst += blank + newst + "\n"
            initst = initst[:-1]
            frcond = errorinfo["frcond"]
            cond = ""
            if len(frcond) == 1:
                cond = frcond[0]
            elif len(frcond) > 1:
                for c in frcond:
                    cond += "(" + c + ")" + "&&"
                cond = cond[:-2]
            else:
                cond = "True"
            cond = renamevar(cond,self.varmap)
            cond = cond.replace("length()","length")
            f = re.findall('[a-zA-Z0-9\[\]_]*\.length',cond)
            for matched in f:
                m = re.match('([a-zA-Z0-9\[\]_]*)\.length',matched)
                cond = cond.replace(matched,"len(" + m[1] + ")")
            whilestatement = "while " + STMTTRANSPILE2PY[self.frlang](cond) + " :"
            frupdate = errorinfo["frupdate"]
            updatest = ""
            for st in frupdate:
                newst = st
                if st.find("++") != -1:
                    lv = st.replace("++","")
                    newst = lv + " += 1"
                elif st.find("--") != -1:
                    lv = st.replace("--","")
                    newst = lv + " -= 1"
                updatest += blank + "    " + newst + "\n"
            updatest = updatest[:-1]          
            changelist.append({"type":"add","content":errorinfo["frupdate"],"line":-1,"changetype":"forloop"})
            changelist.append({"type":"add","content":initst,"line":startline,"changetype":"forinit","errtype":detailtype})
            changelist.append({"type":"del","line":startline,"changetype":"forinit"})
            changelist.append({"type":"add","content":blank + whilestatement,"line":startline,"changetype":"forst"})
            changelist.append({"type":"add","content":updatest,"line":endline+1,"changetype":"forupdate"})
        elif self.tolang == "java" or self.tolang == "cpp":
            endb = errorinfo['toforplace'][1]
            _,startline,endline = getSELine(startb,endb,oritocode,tosplitline)
            startstrip_pre,endstrip_post = self.checkForSEStrip(startline,endline,startb,endb,oritocode,tosplitline)
            initstmt = ""
            udpstmt = ""
            for i in errorinfo['frinit']:
                newinit = "int " + STMTCONVERT[(self.frlang,self.tolang)](i) + ","
                if self.tolang == "java":
                    if i.count("=") > 0:
                        lv = i.split("=")[0].strip()
                        if lv in self.jvdeflineplaces:
                            if self.jvdeflineplaces[lv] < startline:
                                newinit = newinit[3:]
                initstmt += newinit 
            for i in errorinfo['frupdate']:
                udpstmt += STMTCONVERT[(self.frlang,self.tolang)](i) + ","
            initstmt,udpstmt = initstmt[:-1],udpstmt[:-1]
            if len(errorinfo['frcond']) == 1:
                cond = STMTCONVERT[(self.frlang,self.tolang)](errorinfo['frcond'][0])
            else:
                cond = ""
            newcode = f"for ({initstmt};{cond};{udpstmt})"
            changelist.append({"type":"add","content":errorinfo["frcond"],"line":-1,"changetype":"forloop","errtype":detailtype})
            changelist.extend(self.changeJCFor(startstrip_pre,endstrip_post,startline,endline,startb,endb,oritocode,tosplitline,newcode))
        Logger.cstwarning(f"for-statement unpreserved: src_init:{str(errorinfo['frinit'])}, src_condition:{str(errorinfo['frcond'])}, src_update:{str(errorinfo['frupdate'])}, tgt_init:{str(errorinfo['toinit'])}, tgt_condition:{str(errorinfo['tocond'])}, tgt_update:{str(errorinfo['toupdate'])}",startline)
        
        return changelist
    
    def traverseBinary(self,node,info):
        if node.type == "binary_expression":
            cnt = 0
            for child in node.children:
                if cnt == 0:
                    lnode = child
                elif cnt == 1:
                    op = child
                else:
                    rnode = child
                    break
                cnt += 1
            ltp = self.traverseBinary(lnode,info)
            rtp = self.traverseBinary(rnode,info)
            if ltp == "int" and rtp == "int":
                tp = "int"
            elif ltp == "float" or rtp == "float":
                tp = "float"
            else:
                tp = "unknown"
            if tp == "int" and getToken(self.jvcd,op) == "/":
                info.append(removeBlank(getToken(self.jvcd,lnode) + "/" + getToken(self.jvcd,rnode)))
            return tp
        elif node.type == "identifier":
            var = getToken(self.jvcd,node)
            if var in self.oracletypemap:
                return self.oracletypemap[var]
            else:
                return "unknown"
        elif node.type == "decimal_integer_literal":
            return "int"
        elif node.type == "decimal_floating_point_literal":
            return "float"
        elif node.type == "parenthesized_expression":
            for child in node.children:
                if child.type not in ['(',')']:
                    return self.traverseBinary(child,info)
        elif node.type == "array_access":
            arracc = getToken(self.jvcd,node)
            arr = arracc[:arracc.find('[')].strip()
            if arr in self.oracletypemap:
                tp = self.oracletypemap[arr]
                tp = tp.replace('[','').replace(']','').strip()
                return tp
            else:
                return 'Unknown'
        elif node.type == "cast_expression":
            cflg = False
            cst = 'Unknown'
            for child in node.children:
                if child.type == "(":
                    cflg = True
                elif cflg:
                    cst = getToken(self.jvcd,child)
                    break
            return cst
        else:
            tp = "unknown"
            for child in node.children:
                trytp = self.traverseBinary(child,info)
                if trytp != "unknown" and tp == "unknown":
                    tp = trytp
    def generateFuncDecl(self,rettype,funcname,formaltypedic):
        newdecl = f"{rettype} {funcname}"
        newargstr = ""
        for vname,tp in formaltypedic.items():
            tp = tp.replace('const','const ')
            tp = tp.replace('unsigned','unsigned ')
            if '[' in tp:
                if self.tolang == "cpp":
                    primtp = tp.replace('[','').replace(']','').strip()
                    arrtp = tp.replace(primtp,'').strip()
                    arg = f"{primtp} {vname} {arrtp}"
                else:
                    arg = f"{tp} {vname}"
            else:
                arg = f"{tp} {vname}"
            newargstr += arg + ","
        newargstr = "(" + newargstr[:-1] + ")"
        newdecl += newargstr
        return newdecl
    def staticTypeRewrite(self,errinfos):
        if self.tolang == "cpp":
            funcname = self.cfuncname
            formaltypes = self.cformaltypes
            oricode = self.oriccode
            cfg = self.ccfg
            rettype = self.crettype
            primitivevaluedic = CPRIMITIVEDEFAULTVALUE
            #arrdefs = {d[1]:d[2] for d in self.arrdefmap[self.tolang]}
            #bytecode = self.ccd
        else:
            return []
        changelist = []
        rewritefuncdecl = False
        formaltypedic = {vname:tp for tp,vname in formaltypes}
        for var,badtype,defaulttype in errinfos:
            if countCDimen(badtype) > 0 and countCDimen(defaulttype) > 0 and countCDimen(badtype) != countCDimen(defaulttype):
                changelist.extend(self.rewriteArrayDimen(var,self.cfgmap[self.frlang],self.cfgmap[self.tolang]))
            changeline = -1
            if var == "RET@":
                rettype = defaulttype
                rewritefuncdecl = True
            elif var in formaltypedic:
                formaltypedic[var] = defaulttype 
                rewritefuncdecl = True
            else:
                newcode = ""
                for node in cfg.nodelist:
                    for ud in node['UD']:
                        if ud[0] == var and (ud[1] == 'D' or ud[1] == 'RD'):
                            changeline = ud[2]
                            break
                    if changeline != -1:
                        break
                if changeline != -1:
                    changecode = getNlineCode(oricode,changeline)
                    
                    if countCDimen(badtype) > 0 and countCDimen(defaulttype) > 0 and countCDimen(badtype) != countCDimen(defaulttype):
                        frarrshape = [STMTTRANSPILE2PY[self.frlang](s) for s in self.arrshapeinfo[self.frlang][var] if s != '']
                        toarrshape = [STMTTRANSPILE2PY[self.tolang](s) for s in self.arrshapeinfo[self.tolang][var] if s != '']
                        changed = False
                        for c in self.changelist:
                            if c["line"] == -1 and c["changetype"] == "arrshape":
                                changed = True
                        if not changed:
                            changelist.append({"type":"add","line":-1,"content":str(frarrshape)+str(toarrshape),"changetype":"type"})
                            err = {"frarrshape":frarrshape,"toarrshape":toarrshape,"varname":var}
                            changelist.extend(self.rewriteArrayShape(err))
                        primt = getFirstTypeOfArray(badtype)
                        if primt != None:
                            newdecl = ""
                            if "<" in badtype:
                                newtype = ""
                                for i in range(0,len(frarrshape)):
                                    newtype = f"vector<{primt}>" if i == 0 else f"vector<{newtype}>"
                                if newtype != "":
                                    changelist.append({"type":"replace2","line":changeline,"old":badtype+var,"new":newtype + var,"changetype":"type"})
                            elif "*" in badtype:
                                newtype = primt 
                                for i in range(0,len(frarrshape)):
                                    newtype += "*"
                                changelist.append({"type":"replace2","line":changeline,"old":badtype+var,"new":newtype+var,"changetype":"type"})
                        
                    else:
                        if changecode.find('=') != -1:
                            newcode = defaulttype + " " + var + " = " + changecode.split("=")[1]
                        else:
                            newcode = defaulttype + " " + var
                            if defaulttype in primitivevaluedic:
                                newcode += " = " + primitivevaluedic[defaulttype]
                            newcode += ";"
                            
                if newcode != "":
                    changelist.append({"type":"add","line":changeline,"content":newcode,"changetype":"type"})
                    changelist.append({"type":"del","line":changeline,"changetype":"type"})
        if rewritefuncdecl:
            newdecl = self.generateFuncDecl(rettype,funcname,formaltypedic)
            declcode = getNlineCode(oricode,1)
            if declcode.count('{') != 0:
                newdecl += "{"
            changeline = 1
            changelist.append({"type":"add","line":changeline,"content":newdecl,"changetype":"type"})
            changelist.append({"type":"del","line":changeline,"changetype":"type"})
        return changelist
    def staticTypeCheck(self,frvartypemap,tovartypemap):
        changelist = []
        statictypemap = {}
        if self.frlang == "java" and self.tolang == "cpp":
            statictypemap = JVCTYPEMAP
            formaltypedic = formaltypedic = {vname:tp for tp,vname in self.jvformaltypes}
        tmpmap = {}
        for ke,va in frvartypemap.items():
            if ke in self.varmap:
                tmpmap[self.varmap[ke]] = va
            else:
                tmpmap[ke] = va
        frvartypemap = tmpmap
        errlist = []
        for var,frtype in frvartypemap.items():
            if frtype in statictypemap:
                mappedtype = statictypemap[frtype]
                if var not in tovartypemap:
                    #errlist.append((var,""))
                    pass
                else:
                    totype = tovartypemap[var]
                    if totype == "auto" or "iterator" in totype:
                        flg = True
                    else:
                        if type(mappedtype) == str:
                            flg = totype == mappedtype
                            defaulttype = mappedtype
                        elif type(mappedtype) == list:
                            defaulttype = mappedtype[0]
                            mappedtype = [removeBlank(t) for t in mappedtype]
                            flg = totype in mappedtype
                        else:
                            flg = True
                    if not flg:
                        errlist.append((var,totype,defaulttype))
                        changelist.append({"type":"add","line":-1,"content":var+" "+totype,"changetype":"type"})
                        Logger.cstwarning(f"type unpreserved: var: {var}, src:{frtype}, tgt: {totype}",0)
                    '''elif var in formaltypedic and frtype.find('[') != -1 and totype.find('vector') != -1:
                        errlist.append((var,totype,defaulttype))
                        changelist.append({"type":"add","line":-1,"content":var+" "+totype,"changetype":"type"})'''
        changelist.extend(self.staticTypeRewrite(errlist))
        return changelist
    
    def propagateJvFloatVar(self,line=-1):
        vartypemap = self.jvvartypemap
        uds = [ud for node in self.cfgmap['python'].nodelist for ud in node['UD']]
        varset = self.jvtyperewritevars
        while True:
            lastset = copy.deepcopy(varset)
            for ud in uds:
                if 'rv' in ud[3] or 'returnstmt' in ud[3]:
                    exp = ud[3]['rv'] if 'rv' in ud[3] else ud[3]['returnstmt']
                    lv = ud[0] if 'rv' in ud[3] else 'RET@'
                    expvars = extractVarInExp(exp)
                    if line != -1 and ud[2] == line:
                        varset.add(ud[0])
                    if lv not in varset:
                        if len(expvars & varset) != 0:
                            varset.add(lv)
                    else:
                        varset = varset | expvars
            varset = {v for v in varset if v in vartypemap and vartypemap[v] == 'int'}
            if lastset == varset:
                break
        self.jvtyperewritevars = varset
    def rewriteJvFloatVar(self):
        changelist = []
        jvtyperewriteformals = copy.deepcopy(self.jvformaltypes)
        jvtyperewriteformals = {vname:tp for tp,vname in jvtyperewriteformals}
        jvtyperewriteformals["RET@"] = self.jvrettype
        rewritedecl = False
        changelines = set()
        for v in self.jvtyperewritevars:
            if v in jvtyperewriteformals:
                if jvtyperewriteformals[v] == 'int':
                    jvtyperewriteformals[v] = 'double'
                    rewritedecl = True
            if v not in jvtyperewriteformals or v == "RET@":
                uds = [ud for node in self.cfgmap['java'].nodelist for ud in node['UD']]
                
                for ud in uds:
                    changeline = -1
                    if ud[0] == v and ud[1] == 'D':
                        changeline = int(ud[2])
                        code = self.jvcd.decode().split("\n")[changeline-1]
                        newcode = re.sub(f'int\s*{v}',f'double {v}',code)
                        newcode = re.sub('\(\s*int\s*\)','',newcode)
                    elif (ud[0] == v and ud[1] == 'RD') or (v == "RET@" and 'returnstmt' in ud[3]):
                        changeline = int(ud[2])
                        code = self.jvcd.decode().split("\n")[changeline-1]
                        newcode = re.sub('\(\s*int\s*\)','',code)
                        if newcode == code:
                            continue
                    if changeline != -1 and changeline not in changelines:
                        changelist.append({"type":"del","line":changeline,"changetype":"type_floatint"})
                        changelist.append({"type":"add","line":changeline,"content":newcode,"changetype":"type_floatint"})
                        changelines.add(changeline)       
        if rewritedecl:
            declcode = self.jvcd.decode().split("\n")[1]    
            newrettype = jvtyperewriteformals["RET@"]
            del jvtyperewriteformals["RET@"]       
            newdecl = self.generateFuncDecl(newrettype,self.jvfuncname,jvtyperewriteformals)   
            newdecl = newdecl + '{' if '{' in declcode else newdecl
            #Logger.debug(newdecl)
            changelist.append({"type":"del","line":2,"changetype":"type_decl"})
            changelist.append({"type":"add","line":2,"content":newdecl,"changetype":"type_decl"})  
        return changelist
    def omitListInArray(self):
        for lang,infodic in self.arrshapeinfo.items():
            if lang == "python":
                uds = [ud for node in self.cfgmap['python'].nodelist for ud in node['UD']]
                listv = {ud[0] for ud in uds if 'lv' in ud[3] and '[@]' in ud[3]['lv']}
                self.arrshapeinfo['python']= {v:info  for v,info in infodic.items() if v not in listv}
                arrdef = self.arrdefmap['python']
                self.arrdefmap['python'] = [df for df in arrdef if df[1] not in listv]              
    

    def initMValueMap(self):
        keywordlangmap = {
            "java":[["Integer.MAX_VALUE","Double.MAX_VALUE","LITERALMVALUE"],["Integer.MIN_VALUE","-Integer.MAX_VALUE-1","-Integer.MAX_VALUE","-LITERALMVALUE","Double.MIN_VALUE"]],
            "cpp":[["INT_MAX","LITERALMVALUE","std::numeric_limits<int>::max()"],["INT_MIN","-LITERALMVALUE","std::numeric_limits<int>::min()"]],
            "python":[["sys.maxsize","float('inf')",'float("inf")',"LITERALMVALUE"],["-sys.maxsize","-sys.maxsize-1","-float('inf')","float('-inf')",'-float("inf")','float("-inf")',"-LITERALMVALUE"]]
        }
        keywordmap = {}
        frkeywordliss = keywordlangmap[self.frlang]
        tokeywordliss = keywordlangmap[self.tolang]
        for frkwlis,tokwlis in zip(frkeywordliss,tokeywordliss):
            for frkw in frkwlis:
                keywordmap[frkw] = tokwlis
        return keywordmap
     
    def checkForSEStrip(self,startline,endline,startb,endb,tocode,tosplitline):
        startstrip_pre = False
        endstrip_post = False
        if checkStrip2(tocode[tosplitline[startline-2]+1:startb]):
            startstrip_pre = True
        if checkStrip2(tocode[endb:tosplitline[endline-1]]):
            endstrip_post = True
        return startstrip_pre,endstrip_post
    def changeJCFor(self,startstrip_pre,endstrip_post,startline,endline,startb,endb,tocode,tosplitline,newcode):
        changelist = []
        if startline == endline:
            changelist.append({"type":"replace","line":startline,"old":tocode[startb:endb],"new":newcode,"changetype":"for"})
        else:
            if startstrip_pre:
                changelist.append({"type":"del","line":startline,"changetype":"for"})
            else:
                changelist.append({"type":"replace","line":startline,"old":tocode[startb:tosplitline[startline-1]],"new":"","changetype":"for"})
            for line in range(startline+1,endline):
                changelist.append({"type":"del","line":line,"changetype":"for"})
            if endstrip_post:
                changelist.append({"type":"del","line":endline,"changetype":"for"})
            else:
                changelist.append({"type":"replace","line":endline,"old":tocode[tosplitline[endline-2]+1:endb],"new":newcode,"changetype":"for"})
        return changelist
    
    def getPyArrDefs(self):
        self.pyarrinitdefs = {}
        arrvarset = set()
        for item in self.jvlocaltypes:
            if item[0].count('[') > 0:
                arrvarset.add(item[1])
        for node in self.pycfg.nodelist:
            for ud in node['UD']:
                if ud[1] == 'D' and 'rv' in ud[3] and ud[0] in arrvarset and ud[0] not in self.pyarrinitdefs:
                    self.pyarrinitdefs[ud[0]] = (node['index'],ud[3]['rv'])
    def printCFG(self):
        for node in self.jvcfg.nodelist:
            Logger.debug(str(node['index']) + " " + str(node))
        for node in self.pycfg.nodelist:
            Logger.debug(str(node['index']) + " " + str(node))
    def initVarMap(self):
        if self.frlang not in self.cfgmap or self.tolang not in self.cfgmap:
            exit(-1)
        frcfg = self.cfgmap[self.frlang]
        tocfg = self.cfgmap[self.tolang]
        frvarset = set()
        for node in frcfg.nodelist:
            for ud in node['UD']:
                if ud[1] == 'RD' or ud[1] == 'D':
                    if type(ud[0]) == type([]):
                        for v in ud[0]:
                            frvarset.add(v)
                    else:
                        frvarset.add(ud[0])
        tovarset = set()
        for node in tocfg.nodelist:
            for ud in node['UD']:
                if ud[1] == 'RD' or ud[1] == 'D':
                    if type(ud[0]) == type([]):
                        for v in ud[0]:
                            tovarset.add(v)
                    else:
                        tovarset.add(ud[0])
        if len(frvarset) == len(tovarset):
            self.varmap = varmapping(frvarset,tovarset)
        else:
            self.varmap = {}
    def cfgnodeTypeCheck(self,cfg1,cfg2):
        if len(cfg1.nodelist) != len(cfg2.nodelist):
            return False
        for node1,node2 in zip(cfg1.nodelist,cfg2.nodelist):
            if node1["type"] != node2["type"]:
                looplist = ['for_init','while_init','do_init','enhanced_init']
                if node1["type"] not in looplist and node2["type"] not in looplist:
                    return False
        return True
    def evalArrIndexs(self,oriexpr,onetimedr):
        if '[' in oriexpr:
            _,subarrindexs = parseCArray(oriexpr)
            if subarrindexs == None:
                return None
            literallidexs = []
            for subind in subarrindexs:
                tmpdr = copy.deepcopy(onetimedr)
                vars = list(extractVarInExp(subind))
                vardrs = [list(tmpdr[d]) for d in vars if d in tmpdr]
                
                comb = list(itertools.product(*vardrs))
                maybevalues = []
                for drs in comb:
                    for i,dr in enumerate(drs):
                        tmpdr[vars[i]] = set([dr])

                    drevalexp = simplifyExpByDR(self.tovartypemap,"",subind,tmpdr,{},lang="cpp")
                    numres = None
                    try:
                        numres = eval(drevalexp.replace("/","//"))
                    except:
                        pass
                    if numres != None:
                        maybevalues.append(str(numres))
                if len(maybevalues) > 0:
                    literallidexs.append(maybevalues)
            if len(literallidexs) == len(subarrindexs):
                return literallidexs
        return None
    def rewriteArrayShape(self,err):
        arrdefdic = {df[1]:(df[0],df[2]) for df in self.arrdefmap[self.tolang]}
        frarrshape = err['frarrshape']
        toarrshape = err['toarrshape']
        vname = err['varname']
        changelist = []
        #changelist.append({"type":"add","line":-1,"content":vname,"changetype":"arrshape"})
        
        if self.tolang == "cpp":           
            bytecode = self.ccd
            splitlines = self.clineindex           
            if vname in arrdefdic:
                tp,definit = arrdefdic[vname]
                if '*' in tp:
                    if not(definit == None):
                        if type(definit) != list:
                            definit = [definit]
                        errindex = []
                        cnt = 0
                        for frsp,tosp in zip(frarrshape,toarrshape):
                            if frsp != tosp:
                                errindex.append(cnt)
                            cnt += 1
                        
                            
                        if len(errindex) > 0:
                            for i in range(0,len(definit)):
                                if i in errindex:
                                    errdefinit = definit[i]
                                    errdefinitcode = getToken(bytecode,errdefinit)
                                    line = getLinebyPlace(splitlines,errdefinit.start_byte)
                                    defsplit = errdefinitcode.split("=")
                                    orashape = frarrshape[i]
                                    if len(defsplit) == 2:
                                        newcode = defsplit[0] + " = " + f"new int [{orashape}]()"
                                        changelist.append({"type":"replace","line":line,"old":errdefinitcode,"new":newcode,"changetype":"arrshape"})
                        if len(frarrshape) > len(toarrshape):
                            line = -1
                            if len(definit) > 0:
                                line = getLinebyPlace(splitlines,definit[0].start_byte)
                            for i in range(len(toarrshape),len(frarrshape)):
                                curdimen = i
                                forstmt = ""
                                asignstmt = vname
                                primt = tp.replace("*","").strip()
                                pointernum = len(frarrshape) - 1 - i
                                newstmt = "new " + primt
                                for j in range(0,pointernum):
                                    newstmt += "*"
                                for fortime in range(0,curdimen):
                                    forstmt += f"for(int i{fortime} = 0;i{fortime} < {frarrshape[fortime]};i{fortime}++) "
                                    asignstmt += f"[i{fortime}]"
                                newstmt += f" [{frarrshape[curdimen]}]"
                                if pointernum == 0:
                                    newcode = forstmt + asignstmt + " = " + newstmt + "();"
                                else:
                                    newcode = forstmt + asignstmt + " = " + newstmt + ";"
                                changelist.append({"type":"add","line":line+1,"content":newcode,"changetype":"arrshape"})
                elif '[' in tp:
                    if type(definit) != None and type(definit) != list:
                        errdefinit = definit
                        errdefinitcode = getToken(bytecode,errdefinit)
                        line = getLinebyPlace(splitlines,errdefinit.start_byte)
                        frarrshapestr = ""
                        for s in frarrshape:
                            frarrshapestr += f"[{s}]"
                        defaultv = getDefaultValueofArray(tp)
                        if defaultv != None:
                            newcode = f"{vname} {frarrshapestr} = {{{defaultv}}}"
                            changelist.append({"type":"replace","line":line,"old":errdefinitcode,"new":newcode,"changetype":"arrshape"})
                            changelist.append({"type":"add","line":line+1,"content":f"memset({vname},0,sizeof({vname}));","changetype":"arrshape"})
                elif '<' in tp:
                    if type(definit) != None and type(definit) != list:
                        errdefinit = definit
                        errdefinitcode = getToken(bytecode,errdefinit)
                        line = getLinebyPlace(splitlines,errdefinit.start_byte)
                        defaultv = getDefaultValueofArray(tp)
                        primtp = getFirstTypeOfArray(tp)
                        if defaultv != None and primtp != None:
                            frarrshapestr = ""
                            for i in range(len(frarrshape)-1,-1,-1):
                                s = frarrshape[i]
                                if i == len(frarrshape)-1:
                                    frarrshapestr = f"({s},{defaultv})"
                                else:
                                    frarrshapestr = f"({s},vector<{primtp}>{frarrshapestr})"
                            newcode = f"{vname} {frarrshapestr}"
                            changelist.append({"type":"replace","line":line,"old":errdefinitcode,"new":newcode,"changetype":"arrshape"})

        elif self.tolang == "java":
            bytecode = self.jvcd
            splitlines = self.jvlineindex
            if vname in arrdefdic:
                tp,definit = arrdefdic[vname]
                errdefinit = definit
                errdefinitcode = getToken(bytecode,errdefinit)
                line = getLinebyPlace(splitlines,errdefinit.start_byte)
                primt = getFirstTypeOfArray(tp)
                if primt != None:
                    newstmt = f"{vname} = new {primt}" 
                    for s in frarrshape:
                        newstmt += f"[{s}]"
                    if vname in self.jvvartypemap and self.jvvartypemap[vname].count('[') != len(frarrshape):
                        news = ""
                        for _ in range(len(frarrshape)):
                            news += "[]"
                        newstmt = news + newstmt
                        for _ in range(self.jvvartypemap[vname].count('[')):
                            errdefinitcode = '[]' + errdefinitcode
                    changelist.append({"type":"replace2","line":line,"old":errdefinitcode,"new":newstmt,"changetype":"arrshape"})
        elif self.tolang == "python":
            bytecode = self.pycd
            splitlines = self.pylineindex
            if vname in arrdefdic:
                _,definit = arrdefdic[vname]
                errdefinitcode = getToken(bytecode,definit)
                line = getLinebyPlace(splitlines,definit.start_byte)
                newdef = "0"
                for s in frarrshape[::-1]:
                    newdef = f"[{newdef} for _ in range({s})]"
                changelist.append({"type":"replace2","line":line,"old":errdefinitcode,"new":newdef,"changetype":"arrshape"})
        if len(changelist) > 0:
            Logger.cstwarning(f"array unpreserved. src: {frarrshape}, tgt: {toarrshape}",line)
        return changelist
    def rewriteArrInit(self,errarrname,frinitv,arrdefs):
        arrdefdic = {df[1]:(df[0],df[2]) for df in arrdefs}
        if self.tolang == "cpp":
            arrshape,bytecode,splitline,cft = self.arrshapeinfo["cpp"],self.ccd,self.clineindex,self.ccft
        elif self.tolang == "java":
            arrshape,bytecode,splitline,cft = self.arrshapeinfo["java"],self.jvcd,self.jvlineindex,self.jvcft
        elif self.tolang == "python":
            arrshape,bytecode,splitline,cft = self.arrshapeinfo["python"],self.pycd,self.pylineindex,self.pycft
        changelist = []
        vname = errarrname
        changelist.append({"type":"add","line":-1,"content":vname,"changetype":"arrinit"})
        if vname in arrdefdic:
            tp,initdef = arrdefdic[vname]
            if not(initdef == None):
                if type(initdef) == list:
                    initdef = initdef[-1]
                    if initdef == None:
                        return changelist
                line = getLinebyPlace(splitline,initdef.start_byte)
                defcode = getToken(bytecode,initdef)
                newcode = ""
                if self.tolang == "cpp":
                    cutflg = False
                    if '[' in tp:
                        #defaultv = getDefaultValueofArray(tp)
                        defaultv = frinitv
                        if defaultv != None:
                            if "=" in defcode:
                                newcode = defcode.split("=")[0] + f" = {{{defaultv}}}"
                            else:
                                newcode = defcode + f" = {{{defaultv}}}"
                            changelist.append({"type":"add","line":line+1,"content":f"memset({vname},{defaultv},sizeof({vname}));","changetype":"arrinit"})
                            if not cutflg:
                                cutflg = True
                                for t in cft:
                                    if t['type'] in ["for_statement","enhanced_for_statement"] and 'tobecut' in t:
                                        startb = t['start']
                                        endb = t['end']
                                        oritocode = self.tocode
                                        tosplitline = self.clineindex
                                        _,startline,endline = getSELine(startb,endb,oritocode,tosplitline)
                                        startstrip_pre,endstrip_post = self.checkForSEStrip(startline,endline,startb,endb,oritocode,tosplitline)
                                        changelist.extend(self.changeJCFor(startstrip_pre,endstrip_post,startline,endline,startb,endb,oritocode,tosplitline,""))
                                
                    elif '*' in tp:                          
                        if "=" in defcode:
                            newcode = defcode + "()"
                            if tp.count('*') == 1:
                                if vname in arrshape and len(arrshape[vname]) == 1:
                                    shape = arrshape[vname][0]
                                    newcode = f" {vname} [{shape}]"
                                    #defaultv = getDefaultValueofArray(tp)
                                    defaultv = frinitv
                                    if defaultv != None:
                                        changelist.append({"type":"add","line":line+1,"content":f"memset({vname},{defaultv},sizeof({vname}));","changetype":"arrinit"})
                            
                elif self.tolang == "java":
                    defaultv = frinitv
                    if defaultv != None:
                        changelist.append({"type":"add","line":line+1,"content":f"  Arrays.fill({vname},{defaultv});","changetype":"arrinit"})
                elif self.tolang == "python":
                    defaultv = frinitv
                    if defaultv != None:
                        initflg = True
                        for s in arrshape[vname]:
                            if initflg:
                                newcode = f'({s}) * [{defaultv}]' 
                                initflg = False
                            else:
                                newcode = f'({s}) * [{newcode}]'
                if newcode != "":
                    changelist.append({"type":"replace","line":line,"old":defcode,"new":newcode,"changetype":"arrinit"})
        return changelist
    def checkArrayInit(self,cfg,errarrname,frinitv):
        arrdefs = self.arrdefmap[self.tolang]
        changelist = []
        dr1 = DefineReach(cfg,mode=0)
        onetimeDRINs = []
        for node in cfg.nodelist:
            onetimeDRINs.append(node['DRIN'])
            #Logger.debug(f"{node['type']} {node['DRIN']} {node['UD']} {node['start']} {node['end']}")
        dr1.resetUD()
        dr2 = DefineReach(cfg,mode=2)
        Dominate(cfg,mode=2)
        cfg.reduceDRbyDO()
        truedefset = set()
        defeles = set()
        defeledic = {errarrname:set()}
        errlist = []
        for i in range(0,len(cfg.nodelist)):
            node = cfg.nodelist[i]
            onetimedr = onetimeDRINs[i]
            defdic = {}
            for name,definfo in node['DRIN'].items():
                defdic[name] = {(d[1],d[2]) for d in definfo if not checkRvIsArray(d[2])}
            for ud in node['UD']:
                udname = ud[0]
                onetimedr,_ = dr2.inductUD(onetimedr,ud,[])
                if ud[1] != 'U':
                    if 'rv' in ud[3] and ud[1] == 'RD':
                        df = ud[3]['rv']
                        if udname in defdic:
                            defdic[udname].add((node['index'],df))
                        else:
                            defdic[udname] = set()
                            defdic[udname].add((node['index'],df))
                        if udname == errarrname:
                            '''lv = removeBlank(ud[3]['lv'])
                            arrindexs = self.evalArrIndexs(lv,onetimedr)
                            if arrindexs != None and node["deep"] == 0:
                                defeles.add(tuple(arrindexs))
                            else:
                                defeles = set()'''
                            lv = removeBlank(ud[3]['lv'])
                            '''if udname in onetimedr:
                                del onetimedr[udname]'''
                            arrindexs = self.evalArrIndexs(lv,onetimedr)                            
                            if arrindexs != None and node["deep"] == 0:
                                comb = list(itertools.product(*arrindexs))
                                for c in comb:
                                    defeledic[udname].add(tuple(c))
                            else:
                                defeledic[udname] = set()
                else:
                    if udname == errarrname:
                        if udname not in defdic:
                            errlist.append(udname)                                
                        else:
                            defs = defdic[udname]
                            flg = False
                            for nodeindex,df in defs:
                                if df != "" and df.count(udname+"[") <= 0:
                                    truedefset.add(node['index'])
                                    flg = True
                                    break
                                elif nodeindex in truedefset:
                                    flg = True
                                    break
                            if not flg and udname not in errlist:
                                errlist.append(udname)
                            else:
                                if 'expr' in ud[3]:
                                    arrexpr = removeBlank(ud[3]['expr'])
                                    '''arrindexs = self.evalArrIndexs(arrexpr,onetimedr)
                                    if arrindexs != None:
                                        if len(defeles) > 0 and tuple(arrindexs) not in defeles:
                                            errlist.append(udname)'''
                                    if udname in onetimedr:
                                        del onetimedr[udname]
                                    arrindexs = self.evalArrIndexs(arrexpr,onetimedr)
                                    if arrindexs != None:
                                        comb = list(itertools.product(*arrindexs))
                                        if udname in defeledic:
                                            defeles = defeledic[udname]
                                            if len(defeles) > 0:
                                                cnt = 0
                                                for c in comb:
                                                    if tuple(c) not in defeles:
                                                        cnt += 1
                                                if cnt == len(comb):
                                                    #errlist.append(udname)
                                                    1
        dr2.resetUD()
        if len(errlist) != 0:
            return self.rewriteArrInit(errarrname,frinitv,arrdefs)
        else:
            return []

    def condition_Div(self,node,exp):
        if not(node == None):
            info = []
            self.traverseBinary(node,info)
            for div in info:
                newdiv = div.replace('/','//')
                exp = exp.replace(div,newdiv)
        return exp
    def checkRedefineOfLoop(self,cond,cfg:CFG,cfgnode):
        if 'allcontent' in cfgnode:
            vars = extractVarInExp(cond)
            for ind in cfgnode['allcontent']:
                if ind == cfgnode['index']:
                    continue
                subnode = cfg.getNode(ind)
                for ud in subnode['UD']:
                    if ud[1] in ['D','RD'] and ud[0] in vars:
                        return True
        return False
    def replaceLen(self,exp,arrshapeinfo):
        vars = extractVarInExp(exp)
        for var in vars:
            if exp.count(f'len({var})') > 0:
                if arrshapeinfo != None and var in arrshapeinfo:
                    shape = arrshapeinfo[var]
                    if len(shape) >= 1:
                        targetexp = shape[0]
                        exp = exp.replace(f'len({var})',targetexp)
        return exp
    def reJudgeForCondErr2(self,err):
        if not (len(err['frcond']) == len(err['tocond']) and len(err['tocond']) == 1):
            return True
        if not(len(err['frinit']) == 1 and len(err['toinit']) == 1 and len(err['frupdate']) == 1 and len(err['toupdate']) == 1):
            return True
        if self.tolang == "cpp":
            # do not check iterators in cpp
            for init in err['toinit']:
                if 'begin' in init:
                    return True
            for cond in err['tocond']:
                if 'end' in cond:
                    return True
        def checkOnlyForError(err,fortp):
            return "detailtype" in err and len(err["detailtype"]) == 1 and fortp in err["detailtype"]
        
        tocfg = self.cfgmap[self.tolang]
        frcfg = self.cfgmap[self.frlang]
        DefineReach(frcfg)
        DefineReach(tocfg)
        if self.checkRedefineOfLoop(err['frcond'][0],frcfg,frcfg.getNodeByPlace(err['frplace'][0]+2)):
            return True
        frcstnode = frcfg.getNodeByPlace(err['frplace'][0]+1)
        node = tocfg.getNodeByPlace(err['toplace'][0]+1)
        frinit,frupdate,toinit,toupdate = err['frinit'][0],err['frupdate'][0],err['toinit'][0],err['toupdate'][0]
        tocond,frcond = removeBlank(err['tocond'][0]),removeBlank(err['frcond'][0])
        if "for_update" in err["detailtype"]:
            frupdate,toupdate = STMTTRANSPILE2PY[self.frlang](frupdate),STMTTRANSPILE2PY[self.tolang](toupdate)
            frupdate = renamevar(frupdate,self.varmap)
            if frupdate == toupdate:
                del err["detailtype"]["for_update"]
                if len(err["detailtype"]) == 0:
                    return True
        if "for_init" in err["detailtype"]:
            if checkOnlyForError(err,"for_init") and renamevar(frinit,self.varmap) == toinit:
                return True
            frinit,toinit = STMTTRANSPILE2PY[self.frlang](frinit),STMTTRANSPILE2PY[self.tolang](toinit)
            frinit = simplifyExpByDR(self.oracletypemap,"",frinit,frcstnode['DRIN'],frcstnode['CRIN']['CRSIBIN'] | frcstnode['CRIN']['CRPARIN'],self.frlang)
            toinit = simplifyExpByDR(self.oracletypemap,"",toinit,node['DRIN'],node['CRIN']['CRSIBIN'] | node['CRIN']['CRPARIN'],self.tolang)        
            frinit,toinit = replaceChar(frinit),replaceChar(toinit)
            frinit = renamevar(frinit,self.varmap)
            if frinit == toinit:
                del err["detailtype"]["for_init"]
                if len(err["detailtype"]) == 0:
                    return True
        if "for_cond" in err["detailtype"]:
            
            frcond = STMTTRANSPILE2PY[self.frlang](frcond)
            tocond = STMTTRANSPILE2PY[self.tolang](tocond)
            frcond = self.condition_Div(err["frcondition_node"],frcond)
            tocond = self.condition_Div(err["tocondition_node"],tocond)
            frcond,tocond = self.replaceLen(frcond,self.arrshapeinfo[self.frlang]),self.replaceLen(tocond,self.arrshapeinfo[self.tolang])
            frcond,tocond = replaceChar(frcond),replaceChar(tocond)
            '''if checkOnlyForError(err,"for_cond") and frcond == tocond:
                return True'''
            if checkOnlyForError(err,"for_cond") and renamevar(frcond,self.varmap) == tocond:
                return True
            comp = ExpExector("","",{},{},vartypemap=self.tovartypemap).compareLoop(
                STMTTRANSPILE2PY[self.frlang](removeBlank(frinit)),frcond,STMTTRANSPILE2PY[self.frlang](removeBlank(frupdate)),
                STMTTRANSPILE2PY[self.tolang](removeBlank(toinit)),tocond,STMTTRANSPILE2PY[self.tolang](removeBlank(toupdate))
                )
            if comp == True:
                return True
            frcstnode = frcfg.getNodeByPlace(err['frplace'][0]+1)
            node = tocfg.getNodeByPlace(err['toplace'][0]+1)
            frcond = simplifyExpByDR(self.oracletypemap,STMTTRANSPILE2PY[self.frlang](removeBlank(frinit)),frcond,frcstnode['DRIN'],frcstnode['CRIN']['CRSIBIN'] | frcstnode['CRIN']['CRPARIN'],self.frlang)
            tocond = simplifyExpByDR(self.tovartypemap,STMTTRANSPILE2PY[self.tolang](removeBlank(toinit)),tocond,node['DRIN'],node['CRIN']['CRSIBIN'] | node['CRIN']['CRPARIN'],self.tolang)
            '''if checkOnlyForError(err,"for_cond") and frcond == tocond:
                return True'''
            frcond = renamevar(frcond,self.varmap)
            if checkOnlyForError(err,"for_cond") and frcond == tocond:
                return True
        comp = ExpExector("","",{},{},vartypemap=self.tovartypemap).compareLoop(frinit,frcond,frupdate,toinit,tocond,toupdate)
        if comp == True:
            return True
            
        return False
    def reJudgeForCondErr(self,err):
        if not (len(err['frcond']) == len(err['tocond']) and len(err['tocond']) == 1):
            return True
        if not(len(err['frinit']) == 1 and len(err['toinit']) == 1 and len(err['frupdate']) == 1 and len(err['toupdate']) == 1):
            return True
        if self.tolang == "cpp":
            # do not check iterators in cpp
            for init in err['toinit']:
                if 'begin' in init:
                    return True
            for cond in err['tocond']:
                if 'end' in cond:
                    return True
        def checkOnlyForError(err,fortp):
            return "detailtype" in err and len(err["detailtype"]) == 1 and fortp in err["detailtype"]
        tocfg = self.cfgmap[self.tolang]
        frcfg = self.cfgmap[self.frlang]
        DefineReach(frcfg)
        DefineReach(tocfg)
        if self.checkRedefineOfLoop(err['frcond'][0],frcfg,frcfg.getNodeByPlace(err['frplace'][0]+2)):
            return True
        tocond = removeBlank(err['tocond'][0])
        frcond = removeBlank(err['frcond'][0])
        frcond = STMTTRANSPILE2PY[self.frlang](frcond)
        tocond = STMTTRANSPILE2PY[self.tolang](tocond)
        frcond = self.condition_Div(err["frcondition_node"],frcond)
        tocond = self.condition_Div(err["tocondition_node"],tocond)
        frcond,tocond = self.replaceLen(frcond,self.arrshapeinfo[self.frlang]),self.replaceLen(tocond,self.arrshapeinfo[self.tolang])
        frcond,tocond = replaceChar(frcond),replaceChar(tocond)
        if ("for_cond" in err and "for_init" not in err and "for_update" not in err) and frcond == tocond:
            return True
        frcond = renamevar(frcond,self.varmap)
        if ("for_cond" in err and "for_init" not in err and "for_update" not in err) and frcond == tocond:
            return True
        #Logger.debug(frcond)
        comp = ExpExector(tocond,frcond,{},{},vartypemap=self.tovartypemap).compareLoop(
                    STMTTRANSPILE2PY[self.frlang](replaceChar(removeBlank(err['frinit'][0]))),frcond,STMTTRANSPILE2PY[self.frlang](removeBlank(err['frupdate'][0])),
                    STMTTRANSPILE2PY[self.frlang](replaceChar(removeBlank(err['toinit'][0]))),tocond,STMTTRANSPILE2PY[self.frlang](removeBlank(err['toupdate'][0])) )
        #Logger.debug(comp)
        if comp == True:
            return True
        cntdic = {}
        frcstnode = frcfg.getNodeByPlace(err['frplace'][0]+1)
        node = tocfg.getNodeByPlace(err['toplace'][0]+1)
        frnewcond = frcond
        tonewcond = tocond
        #self.Logger.debugCFG()
        frnewcond = simplifyExpByDR(self.tovartypemap,STMTTRANSPILE2PY[self.frlang](removeBlank(err['frinit'][0])),frnewcond,frcstnode['DRIN'],frcstnode['CRIN']['CRSIBIN'] | frcstnode['CRIN']['CRPARIN'],self.frlang)
        tonewcond = simplifyExpByDR(self.tovartypemap,STMTTRANSPILE2PY[self.tolang](removeBlank(err['toinit'][0])),tonewcond,node['DRIN'],node['CRIN']['CRSIBIN'] | node['CRIN']['CRPARIN'],self.tolang)
        #Logger.debug(frnewcond)
        #Logger.debug(tonewcond)
        if ("for_cond" in err and "for_init" not in err and "for_update" not in err) and frnewcond == tonewcond:
            return True
        frnewcond = renamevar(frnewcond,self.varmap)
        if ("for_cond" in err and "for_init" not in err and "for_update" not in err) and frnewcond == tonewcond:
            return True
        if len(err['frinit']) == 1 and len(err['toinit']) == 1 and len(err['frupdate']) == 1 and len(err['toupdate']) == 1:
            comp = ExpExector("","",{},{},vartypemap=self.tovartypemap).compareLoop(
                STMTTRANSPILE2PY[self.frlang](replaceChar(removeBlank(err['frinit'][0]))),frnewcond,STMTTRANSPILE2PY[self.frlang](removeBlank(err['frupdate'][0])),
                STMTTRANSPILE2PY[self.frlang](replaceChar(removeBlank(err['toinit'][0]))),tonewcond,STMTTRANSPILE2PY[self.frlang](removeBlank(err['toupdate'][0]))
                )
            if comp == True:
                return True
        
        return False
    def reJudgeForInitUpdateErr(self,err):  
                    
        targetnode = ""
        err['frinit'] = [renamevar(i,self.varmap) for i in err['frinit']]
        err['frupdate'] = [renamevar(i,self.varmap) for i in err['frupdate']]
        frcfg = self.cfgmap[self.frlang]
        tocfg = self.cfgmap[self.tolang]
        DefineReach(frcfg)
        DefineReach(tocfg)
        if self.tolang == "cpp":
            for init in err['toinit']:
                if 'begin' in init:
                    return True
        cntdic = {}
        if "for_init" in err["detailtype"] and len(err['frinit']) == len(err['toinit']) and len(err['frinit']) == 1:
            frinit = err['frinit'][0]
            toinit = err['toinit'][0]
            for node in tocfg.nodelist:
                frcstnode = findCSTCFGNode(node,frcfg,cntdic)
                if 'condition' in node and len(node['condition']) == 1 and node['condition'][0] == err['tocond'][0] and node['type'] in ['for_init','while_init','do_init']:
                    try:
                        simpfrinit = simplifyExpByDR(self.tovartypemap,"",frinit,frcstnode['DRIN'],frcstnode['CRIN']['CRSIBIN'] | frcstnode['CRIN']['CRPARIN'],self.frlang)
                        simptoinit = simplifyExpByDR(self.tovartypemap,"",toinit,node['DRIN'],node['CRIN']['CRSIBIN'] | node['CRIN']['CRPARIN'],self.tolang)        
                        comp = ExpExector([simpfrinit],[simptoinit],{},{},vartypemap=self.tovartypemap).compareList()
                        if comp:
                            return True
                    except:
                        pass
                    break
        compressflg = False
        for dt,dtct in err['detailtype'].items():
            if dtct == "len":
                compressflg = True
                break
        frcfg = self.cfgmap[self.frlang]
        tocfg = self.cfgmap[self.tolang]
        if compressflg:
            for node in tocfg.nodelist:
                if node['start'] >= err['toplace'][0]:
                    targetnode = node
                    break
            
            if targetnode['type'] not in ["for_init" ,"while_init" , "do_init"]:
                return False
            
            if len(targetnode['UD']) > 0:
                initline = int(targetnode['UD'][0][2])
            else:
                
                return False
            targetud = None
            
            for ud in targetnode['UD']:
                if ud[1] == 'D' and ud[2] == initline + 1:
                    targetud = ud
            if targetud == None:
                return False
            newinitlv = targetud[3]['lv']
            newinitrv = removeBlank(targetud[3]['rv'])
            err['toinit'].append(removeBlank(newinitlv + '=' + newinitrv))
            if len(err['toinit']) != len(err['frinit']):
                return False
            oplist = extractVarandNumInExp(err['frupdate'][0])
            updatenum = 1
            var = ''
            for op in oplist:
                if op.isdigit():
                    updatenum = op
                else:
                    var = op
            if var == '':
                return False
            if newinitrv.find(var) == 0:
                token = '+'
            else:
                token = newinitrv[newinitrv.find(var)-1]
            newupdate = None
            pmflg = None
            if err['toupdate'][0].find('+') != -1:
                if token == '+':
                    pmflg = '+'
                elif token == '-':
                    pmflg = '-'
            elif err['toupdate'][0].find('-') != -1:
                if token == '+':
                    pmflg = '-'    
                elif token == '-':
                    pmflg = '+'
            
            if pmflg == None:
                return False
            if pmflg == '+':
                newupdate =  newinitlv + "++"  if updatenum == 1 else newinitlv + "=" + newinitlv + "+" + updatenum 
            elif pmflg == '-':
                newupdate =  newinitlv + "--"  if updatenum == 1 else newinitlv + "=" + newinitlv + "-" + updatenum 
            err['toupdate'].append(newupdate)
        comp = ExpExector(err['frinit'],err['toinit'],{},{},vartypemap=self.tovartypemap).compareList()
        #Logger.debug(comp)
        if comp == False:
            return False    
        if len(err['toupdate']) != len(err['toupdate']):
            return False
        for tu,fu in zip(err['toupdate'],err['frupdate']):
            if tu != fu:
                return False
        
        return True
    
    def conftrolStructCheck(self,jvstruct,pystruct):
        if len(jvstruct) != len(pystruct):
            return False
        for jvsut,pysut in zip(jvstruct,pystruct):
            if jvsut[0] != pysut[0]:
                return False
            if not self.conftrolStructCheck(jvsut[1],pysut[1]):
                return False
        return True
    def extractIfFromStruct(self,structlis,iflis):
        for item in structlis:
            tp = item[0]
            cont = item[1]
            if tp == 'if' or tp == 'elif':
                iflis.append(item)
            self.extractIfFromStruct(cont,iflis)
    def structcheck_If(self):
        #Logger.debug(self.jvpyvarmp)
        bankeyword = ['. get','. put','containsKey',"contains",". add","Stack","HashMap","switch"]
        if [self.orijvcode.find(k) for k in bankeyword] != [-1 for _ in bankeyword]:
            return []
        if self.frlang == 'java':
            friflis = self.jviflis
            toiflis = self.pyiflis
            frcode = jv2py(renamevar(self.orijvcode,self.varmap))
            tocode = self.oripycode
        else:
            friflis = self.pyiflis
            toiflis = self.jviflis
            frcode = renamevar(self.oripycode,self.varmap)
            tocode = jv2py(self.orijvcode)
        changelis = []
        bankeyword = ['get','put','in']
        for frifitem in friflis:
            if frifitem[0] == 'elif':
                continue
            frifdesc = frifitem[2]
            if 'condition' in frifdesc:
                frifcond = removeBlank(frifdesc['condition'])
                if self.frlang == 'java':
                    frifcond = jv2py(frifcond.replace('++',"").replace('--',""))
                frifcond = renamevar(frifcond,self.varmap)
                toifdesc = None
                for toifitem in toiflis:
                    desc = toifitem[2]
                    if 'condition' in desc:
                        toifcond = removeBlank(desc['condition'])
                        if self.tolang == "java":
                            toifcond = jv2py(toifcond.replace('++',"").replace('--',""))
                        if frifcond == toifcond:
                            toifdesc = desc
                            break
                if toifdesc == None:
                    if removeBlank(frifcond) not in removeBlank(tocode):
                        if 'max' not in frifcond and 'min' not in frifcond:
                            changelis.append({"type":"add","line":-1,"changetype":"lackif",'content':frifcond})
                else:
                    if 'else' in frifdesc and 'else' in toifdesc and frifdesc['else'] == True and toifdesc['else'] == False:
                        if 'return' in frifdesc and frifdesc['return'] == False:
                            changelis.append({"type":"add","line":-1,"changetype":"lackelse",'content':frifcond})
        for toifitem in toiflis:
            if toifitem[0] == 'elif':
                continue
            toifdesc = toifitem[2]
            if 'condition' in toifdesc:
                toifcond = removeBlank(toifdesc['condition'])
                if self.tolang == 'java':
                    toifcond = jv2py(toifcond.replace('++',"").replace('--',""))
                frif = None
                for frifitem in friflis:
                    frifdesc = frifitem[2]
                    if 'condition' in frifdesc:
                        frifcond = removeBlank(frifdesc['condition'])
                        if self.frlang == 'java':
                            frifcond = jv2py(frifcond.replace('++',"").replace('--',""))
                        frifcond = renamevar(frifcond,self.varmap)
                        if frifcond == toifcond:
                            frif = frifdesc
                            break
                if frif == None:
                    if removeBlank(toifcond) not in removeBlank(frcode):
                        changelis.append({"type":"add","line":-1,"changetype":"addif",'content':toifcond})
        return changelis
    def traverseReturn(self,node,cfg:CFG):
        if node.type == 'return_statement':
            cnt = 0
            cfg.addReturn(node.start_byte)
            for child in node.children:
                cnt += 1
            if cnt == 1:
                return False
            else:
                return True
        flg = True
        for child in node.children:
            flg = flg and self.traverseReturn(child,cfg)
        return flg
    def checkBoolVar(self,expset,vartypemap):
        for exp in expset:
            words = re.findall("[a-zA-Z_][0-9a-zA-Z_]+",exp)
            for word in words:
                if word in vartypemap:
                    if vartypemap[word].find('bool') == -1:
                        return False
        return True
    def normalizeExtracond(self,crin,cfgnode,vset,to=False):
        cc = ConditionComparar()
        extraconds = set()
        for extracond in crin:
            if to:
                extracond = renamevar(extracond,self.varmap)
            extracond = STMTTRANSPILE2PY[self.frlang](extracond.replace("//","/").replace('True','1').replace('False','0').replace("'","").replace('"',""))
            extracond = simplifyExpByDR({},"",extracond,cfgnode['DRIN'],crin)
            extracond = renameArr(extracond)
            #Logger.debug(extracond)
            extrav = extractVarInExp(extracond)
            extracond = cc.post2Func(cc.infix2postfix(extracond))[0]
            if len(extrav) > 0 and extrav.issubset(vset):
                extraconds.add(extracond)
        return extraconds
                
    def z3ProveEqual(self,frcond,tocond,vset,extracond1=None,extracond2=None):
        execcode = "s1,s2 = Solver(),Solver()\n"
        if '%' in frcond or '%' in tocond or '&' in frcond or '&' in tocond:
            defaulttp = 'Int'
        else:
            defaulttp = 'Real'
        
        if extracond1 != None:
            for cond in extracond1:
                if [cond.find(a+"(") for a in APIS] == [-1 for _ in APIS]:
                    frcond = f"And({frcond},{cond})"
        if extracond2 != None:
            for cond in extracond2:
                if [cond.find(a+"(") for a in APIS] == [-1 for _ in APIS]:
                    tocond = f"And({tocond},{cond})"

        for v in vset:
            if self.oracletypemap.get(v) in ["int","Integer"]:
                execcode += f"{v} = Int('{v}')\n"
            else:
                execcode += f"{v} = {defaulttp}('{v}')\n"
        judgecond1,judgecond2 = f"And({frcond},Not({tocond}))",f"And({tocond},Not({frcond}))"
        
        execcode += f"s1.add({judgecond1})\ns2.add({judgecond2})\n"
        execcode += f"res1,res2=s1.check(),s2.check()"
        Logger.debug(execcode+"\n---\n")
        localmap = {}
        try:
            exec(execcode,None,localmap)
            res1 = localmap["res1"]
            res2 = localmap["res2"]
            if res1 != unknown and res2 != unknown and not(res1 == unsat and res2 == unsat):
                return False
        except Exception as e:
            Logger.debug(e)
            Logger.debug("z3 condition error")
            Logger.debug(execcode)
            pass
        return True
    def judgeCondBySAT(self,frcond,tocond,frcfgnode,tocfgnode): 
        frcond = renamevar(frcond,self.varmap)
        frcrin = frcfgnode['CRIN']['CRSIBIN'] | frcfgnode['CRIN']['CRPARIN']
        tocrin = tocfgnode['CRIN']['CRSIBIN'] | tocfgnode['CRIN']['CRPARIN']
        frcond,tocond = replaceChar(frcond),replaceChar(tocond)
        cc1,cc2 = ConditionComparar(),ConditionComparar()
        s1 = cc1.post2Func(cc1.infix2postfix(frcond))
        s2 = cc2.post2Func(cc2.infix2postfix(tocond))    
        if self.tolang == "java" and cc2.normalized and not self.checkBoolVar(cc2.normalizedexp,self.jvvartypemap):
            return False           
        if len(s1) == 1 and len(s2) == 1:
            frcond,tocond = s1[0],s2[0]
            #orifrcond,oritocond = frcond,tocond
            nexp = cc1.normalizedexp | cc2.normalizedexp
            for e in nexp:
                frcond = f"And({frcond},Or({e}==1,{e}==0))" #bool variable can only be 0 or 1
                tocond = f"And({tocond},Or({e}==1,{e}==0))"
            frcond,tocond = STMTTRANSPILE2PY[self.frlang](frcond.replace("//","/").replace('True','1')).replace('False','0'),STMTTRANSPILE2PY[self.tolang](tocond.replace("//","/").replace('True','1')).replace('False','0')
            frcond,tocond = renameArr(frcond),renameArr(tocond)
            vset1,vset2 = extractVarInExp(frcond),extractVarInExp(tocond)
            vset = vset1 | vset2
            comp = self.z3ProveEqual(frcond,tocond,vset)
            if not comp:
                frcond = simplifyExpByDR(self.oracletypemap,"",frcond,frcfgnode['DRIN'],frcrin,bans=["len(","len ("])
                tocond = simplifyExpByDR(self.tovartypemap,"",tocond,tocfgnode['DRIN'],tocrin,bans=["len(","len ("]) 
                vset1,vset2 = extractVarInExp(frcond),extractVarInExp(tocond)
                vset = vset1 | vset2
                excond1 = self.normalizeExtracond(frcrin,frcfgnode,vset)
                excond2 = self.normalizeExtracond(tocrin,tocfgnode,vset,to=True)
                comp = self.z3ProveEqual(frcond,tocond,vset,extracond1=excond1,extracond2=excond2)
                if not comp:
                    return False
        return True
    def reJudgeIf(self,err):
        #change example:transcoder COUNT_POSSIBLE_DECODINGS_GIVEN_DIGIT_SEQUENCE_1 replace '',""/judge false for add variable
        frnode = err['frcond_node']
        tonode = err['tocond_node']
        frcond = err['frcond']
        tocond = err['tocond']
        frcfg,tocfg = self.cfgmap[self.frlang],self.cfgmap[self.tolang]
        frcode = self.frcode
        tocode = self.tocode
        #self.Logger.debugCFG()
        DefineReach(frcfg,mode=2)
        DefineReach(tocfg,mode=2)
        def getCall(code,node):
            bannodes = ['call','method_invocation','in','call_expression']
            methods= []
            flg = traverseBanNode(node,bannodes,lis=methods)
            newmethods = []
            for f in methods:
                callcode = code[f.start_byte:f.end_byte]
                if callcode == 'in':
                    continue
                if callcode.find(".") != -1:
                    callname = removeBlank(callcode[callcode.find(".")+1:callcode.find("(")])
                else:
                    callname = removeBlank(callcode[:callcode.find("(")])
                newmethods.append(callname)
            return flg,newmethods
        if not(frnode == None) and not(tonode == None):
            frcallflg,frmethods = getCall(frcode,frnode)
            tocallflg,tomethods = getCall(tocode,tonode)
            frcallflg = False if len(frmethods) == 1 and frmethods[0] == "charAt" else frcallflg
            tocallflg = False if len(tomethods) == 1 and tomethods[0] == "charAt" else tocallflg
            if not frcallflg and not tocallflg:
                frcfgnode = frcfg.getNodeByPlace(frnode.start_byte)
                tocfgnode = tocfg.getNodeByPlace(tonode.start_byte)
                return self.judgeCondBySAT(frcond,tocond,frcfgnode,tocfgnode)
        return True
    def addtype(self):
        curlocaltypedic = {}
        localarrinitdic = {}
        self.importstmt = "import math\nimport numpy as np\nfrom queue import Queue\nfrom queue import PriorityQueue\nimport numpy.typing as npt\nfrom typing import Union\nfrom typing import Any\n"
        for ts in self.jvlocaltypes:
            var = ts[1]
            if self.frlang == "java" and var in self.varmap:
                var = self.varmap[ts[1]]
            curlocaltypedic[var] = removeBlank(ts[0])
            localarrinitdic[var] = ts[2]
        asslis = []
        findAssignment(self.pycd,self.pytree.root_node,asslis)
        rewriterecode = []
        oripycode = rewriteFuncDecl(self.oripycode,self.jvrettype,self.jvformaltypes)
        oldassdic,newassdic = {},{}
        oldassdic,newassdic = {},{}
        changelist = []
        assigned = set()
        for _,v in self.jvformaltypes:
            assigned.add(v)
        for ass in asslis:
            assstmt,assstart = ass[0],ass[1]
            assline = 0
            blank = ""
            for i in range(0,len(self.pylineindex)):
                if self.pylineindex[i] > assstart:
                    assline = i + 1
                    for c in self.oripycode.split("\n")[i]:
                        if c in [" ","\t","\n"]:
                            blank += c
                        else:
                            break
                    break
            #Logger.debug(assline)
            oldassdic[assline] = assstmt
            newassigns = rewriteSingleAssign(assstmt,curlocaltypedic,localarrinitdic,changelist,assline,blank,assigned)
            if len(newassigns) > 1:
                rewriterecode.append({"oldplace":assline,"addline":len(newassigns)})
            newassdic[assline] = newassigns
        newpycode = self.importstmt + rewriteAssign(oripycode,oldassdic,newassdic)
        #Logger.debug(newpycode)
        with open(self.pytypedaddr,"w",encoding='UTF-8') as fptr:
            Logger.debug(self.pytypedaddr)
            fptr.write(newpycode)
        return rewriterecode,changelist

    def typeRewrite_Refactor(self,errinfo,oripycode,filename,currewriterec,importaddline):
        changelist = []
        if errinfo.find("Success") != -1:
            return changelist
        #Logger.debug(filename)
        errinfos = errinfo.split("\n")[:-2]
        linepycode = oripycode.split("\n")
        changelist = []
        for errinfo in errinfos:
            baseinfo = re.search("%s\.py\:(\d+): ([a-zA-Z]+):"%(filename),errinfo)
            line,errtype = int(baseinfo.group(1)),baseinfo.group(2)
            if errtype == "error":
                codeinfo = {}
                oriline = line - importaddline
                curline = oriline
                for rec in currewriterec:
                    preline = rec["oldplace"]
                    addline = rec["addline"]
                    if oriline + 1 - addline >= preline:
                        curline = curline - addline + 1
                code = linepycode[curline-1]
                node = self.pycfg.getNodeByLine(curline)
                incond = node['CRIN']['CRSIBIN'] | node['CRIN']['CRPARIN']
                if node['type'] in ['while_init','for_init']:
                    nodecond = node['condition'] if type(node['condition']) != type([]) else node['condition'][0]
                    incond = incond | set([nodecond])
                incond = set([removeBlank(c) for c in incond])
                codeinfo['code'],codeinfo['curline'],codeinfo['tolang'],codeinfo['incond'] = code,curline,self.tolang,incond
                rewriter = mypyRewriter(self)
                changes = rewriter.rewrite_dispense(errinfo,codeinfo)
                if any((change['type'] == 'del' and change["changetype"] in ["type_CallFloatint","type_RetFloatint","type_AssignFloatint"] and any((havechanged["type"] in ["del","replace","replace2"] and change["line"] == havechanged["line"]) for havechanged in self.changelist)) for change in changes):
                    continue
                changelist.extend(changes)
            elif errtype == "note":
                if 'type "str | int"' in errinfo and "Str" in changelist[-1]["changetype"]:
                    changelist = changelist[:-1]
                elif 'Both left and right operands are unions' in errinfo:
                    changelist = changelist[:-2]
        if self.tolang == "java":
            if len(self.jvtyperewritevars) != 0:
                changelist.extend(self.rewriteJvFloatVar())
        return changelist
    def pytypecheck(self,rewriterecord):
        try:
            result = subprocess.run(['mypy',"--allow-redefinition",self.pytypedaddr],capture_output=True,text=True,timeout=30)
        except Exception:
            result.stdout = "loop"
            result.stderr = ""
        mypyerr = result.stdout
        return self.typeRewrite_Refactor(mypyerr,self.oripycode,self.filename,rewriterecord,len(self.importstmt.split("\n"))-1),mypyerr
    
    def valueCheckRewritePy_arrG(self,frarrlengthinfo,toarrlengthinfo):
        def compArrShape(frshape,toshape):
            if len(frshape) != len(toshape) :
                return False
            else:
                if frshape != toshape:
                    for frs,tos in zip(frshape,toshape):
                        frs = renamevar(frs,self.varmap)
                        if frs != tos:
                            vars1 = extractVarInExp(frs)
                            vars2 = extractVarInExp(tos)
                            if vars1 == vars2:
                                execcode = "s = Solver()\n"
                                for v in vars1:
                                    execcode += f"{v} = Int('{v}')\n"
                                execcode += f"s.add({frs}<={tos})\n"
                                #execcode += f"s.add({frs}<={tos})\n"
                                execcode += f"res=s.check()"
                                localmap = {}
                                try:
                                    exec(execcode,None,localmap)
                                    res = localmap["res"]
                                    if res == unsat:
                                        return False
                                except Exception as e:
                                    Logger.debug(e)
                                    Logger.debug("z3 condition error")
                                    Logger.debug(execcode)
                            else:
                                return False
            return True

        if self.frlang not in self.cfgmap and self.tolang not in self.cfgmap:
            exit(-1)
        frcfg,tocfg = self.cfgmap[self.frlang],self.cfgmap[self.tolang]
        if len(frarrlengthinfo) == 0:
            return []
        jvnodetypecntdic = {}
        changelist = []
        badshapevar = set()
        for frnode in frcfg.nodelist:
            csttonode = findCSTCFGNode(frnode,tocfg,jvnodetypecntdic)
            if csttonode == None:
                continue
            
            for ud in frnode["UD"]:
                frvarname,frudtype,frstmtinfo = ud[0],ud[1],ud[3]
                #Logger.debug(ud)
                frvarname = renamevar(frvarname,self.varmap)
                if frvarname not in toarrlengthinfo:
                    continue
                if frvarname in frarrlengthinfo:
                    if frudtype == "D":
                        frarrshape = [removeBlank(s) for s in frarrlengthinfo[frvarname] if s != '']
                        if frvarname in self.arrvalueinfo[self.frlang]:
                            frinitv = self.arrvalueinfo[self.frlang][frvarname]
                            if frinitv != None and frinitv != 'Other':
                                toinitv = None
                                if frvarname in self.arrvalueinfo[self.tolang]:
                                    toinitv = self.arrvalueinfo[self.tolang][frvarname]
                                if frinitv != toinitv and toinitv != 'Other':
                                    changelist.extend(self.checkArrayInit(tocfg,frvarname,frinitv))
                                    #changelist.append({"type":"add","line":-1,"content":str(frvarname)+str(frinitv),"changetype":"arrinitv"})
                        for ud in csttonode['UD']:
                            udname,udkind,line = ud[0],ud[1],ud[2]
                            if udkind == 'D' and udname == frvarname:
                                toarrshape = [removeBlank(s) for s in toarrlengthinfo[frvarname] if s != '']
                                if len(frarrshape) != 0 and frarrshape != toarrshape:
                                    frarrshape = [STMTTRANSPILE2PY[self.frlang](s) for s in frarrshape]
                                    toarrshape = [STMTTRANSPILE2PY[self.tolang](s) for s in toarrshape]
                                    if not compArrShape(frarrshape,toarrshape):
                                        badshapevar.add(udname)
                                        changelist.append({"type":"add","line":-1,"content":str(frarrshape)+str(toarrshape),"changetype":"arrshape_no_equal"})
                                        err = {'frarrshape':frarrshape,'toarrshape':toarrshape,"varname":udname}
                                        changelist.extend(self.rewriteArrayShape(err))
                        
        return changelist
    def valueCheckRewritePy_maxminG(self):
        if self.frlang not in self.cfgmap and self.tolang not in self.cfgmap:
            exit(-1)
        frcfg,tocfg = self.cfgmap[self.frlang],self.cfgmap[self.tolang]
        frnodetypecntdic = {}
        changelist = []
        keywordmap = self.initMValueMap()
        for frnode in frcfg.nodelist:
            if frnode["type"] == "else_init":
                continue
            csttonode = findCSTCFGNode(frnode,tocfg,frnodetypecntdic)
            if csttonode == None:
                continue
            frcond = frnode["condition"]
            if not(frcond == None):
                frcond = removeBlank(frcond)
                frcond = renamevar(frcond,self.varmap)
                if frcond != "":
                    frkeyword,tokeywords = "",""
                    for mvkeyword in keywordmap.keys():
                        if frcond.find(mvkeyword) != -1:
                            frkeyword = mvkeyword
                            tokeywords = keywordmap[frkeyword]
                            break
                    if frkeyword != "":
                        blank = ""
                        for _ in range(csttonode["deep"]):
                            blank += "    "
                        tocond = removeBlank(csttonode["condition"])
                        if frcond.find(frkeyword) != -1 and [tocond.find(towd) for towd in tokeywords] == [-1 for _ in tokeywords]:
                            tokeyword = tokeywords[0]
                            if self.tolang == "python":
                                newstmt = csttonode["type"].split("_")[0] + " " + frcond.replace(frkeyword,tokeyword) + ":"
                                newstmt = newstmt.replace("&&"," and ").replace("||"," or ")
                            else:
                                newstmt = csttonode["type"].split("_")[0] + " (" + frcond.replace(frkeyword,tokeyword) + " ) {"
                                newstmt = newstmt.replace("and","&&").replace("or","||")
                            changelist.append({"type":"add","content":frnode["condition"],"line":-1,"changetype":"maxmin1"})
                            changelist.append({"type":"add","content":blank+newstmt,"line":csttonode["UD"][0][2],"changetype":"maxmin1"})
                            changelist.append({"type":"del","line":csttonode["UD"][0][2],"changetype":"maxmin1"})
                            Logger.cstwarning(f"extreme value unpreserved in condition: src: {frcond}, tgt: {tocond}",csttonode["UD"][0][2])

            defcntdic = {}
            reassdic = {}
            blank = ""
            for _ in range(csttonode["deep"]):
                blank += "    "
            for ud in frnode["UD"]:
                if "lv" in ud[3]:
                    varname = ud[0]
                    frasslv = ud[3]["lv"]
                    varname = renamevar(varname,self.varmap)
                    frasslv = renamevar(frasslv,self.varmap)
                    defcntdic[varname] = 1 if varname not in defcntdic else defcntdic[varname] + 1
                    rv = removeBlank(ud[3]["rv"])
                    rv = str2peakvalue(rv)
                    frkeyword,tokeywords = "",""
                    for mvkeyword in keywordmap.keys():
                        if rv == removeBlank(mvkeyword):
                            frkeyword = mvkeyword
                            tokeywords = keywordmap[frkeyword]
                            break
                    if frkeyword != "":
                        tocnt = 0
                        csttoud = None
                        for toud in csttonode["UD"]:
                            toudkind = toud[1]
                            tovarname = toud[0]
                            if (toudkind == "D" or toudkind == "RD") and tovarname == varname:
                                tocnt += 1
                            if tocnt == defcntdic[varname]:
                                csttoud = toud
                                break
                        if not(csttoud == None):
                            torv = removeBlank(csttoud[3]["rv"])       
                            oritorv = torv                     
                            torv = str2peakvalue(torv)
                            tolv = csttoud[3]['lv']
                            if torv not in tokeywords:
                                tocstword = tokeywords[0]
                                newstmt = blank + frasslv + " = " + tocstword
                                changeline = csttoud[2]
                                if changeline not in reassdic:
                                    reassdic[changeline] = [frasslv]
                                else:
                                    reassdic[changeline].append(frasslv)
                                '''if self.tolang == "java" or self.tolang == "cpp":
                                    newstmt = "int " + newstmt + ";"

                                changelist.append({"type":"add","content":newstmt,"line":changeline,"changetype":"maxmin2"})
                                changelist.append({"type":"del","line":changeline,"changetype":"maxmin2"})'''
                                changelist.append({"type":"add","line":-1,"content":ud[3]["lv"]+" "+ud[3]["rv"],"changetype":"maxmin2"})    
                                changelist.append({"type":"replace2","line":changeline,"old":oritorv,"new":tocstword,"changetype":"maxmin2"})
                                Logger.cstwarning(f"extreme value unpreserved in expression: src: {ud[3]['rv']}, tgt: {oritorv}",changeline)    
            if "returnstmt" in frnode and "returnstmt" in csttonode:
                returnexpr = removeBlank(frnode["returnstmt"].replace(";","").replace("return",""))
                returnexpr = renamevar(returnexpr,self.varmap)   
                frkeyword,tokeywords = "",""
                for mvkeyword in keywordmap.keys():
                    if frcond.find(mvkeyword) != -1:
                        frkeyword = mvkeyword
                        tokeywords = keywordmap[frkeyword]
                        break
                if frkeyword != "":
                    toexpr = removeBlank(csttonode["returnstmt"].replace("return",""))
                        #Logger.debug(expr)
                        #Logger.debug(returnexpr)
                    if [toexpr.find(kw) for kw in tokeywords] == [-1 for _ in tokeywords]:
                        changelist.append({"type":"add","line":-1,"content":frnode["returnstmt"],"changetype":"maxmin3"})   
                        changelist.append({"type":"add","content":blank+"return "+tokeywords[0],"line":csttonode['returnline'],"changetype":"maxmin3"})
                        changelist.append({"type":"del","line":csttonode['returnline'],"changetype":"maxmin3"})
                        Logger.cstwarning(f"extreme value unpreserved in expression: src: {frnode['returnstmt']}, tgt: {csttonode['returnstmt']}",csttonode['returnline'])    
        return changelist 
    
    def normalizeLongCompExp(self,frexp,toexp,frud,toud,frnode,tonode,retflg):
        #"( int ) num . charAt ( i ) - '0'"
        expmap = {}
        expmap[self.frlang] = (frexp,frud,frnode)
        expmap[self.tolang] = (toexp,toud,tonode)
        resexp = {}
        for lang,expinfo in expmap.items():
            exp,ud,node = expinfo[0],expinfo[1],expinfo[2]
            info = ud[3]
            if lang == "java":
                exp = jv2py(exp)
                exp = toPyDiv(info,exp)
                exp = toPyCast(ud,node,exp,lang,self.jvvartypemap)
                exp = replaceChar(exp)
                if retflg and self.jvrettype == "int":
                    exp = "int(" + exp + ")"
            elif lang == "python":
                exp = pyself(exp)
                exp = removeBlank(exp)
            elif lang == "cpp":
                exp = c2py(exp)
                exp = toPyDiv(info,exp)
                exp = toPyCast(ud,node,exp,lang)
                if retflg and self.crettype == "int":
                    exp = "int(" + exp + ")"
            if 'op' in info and info['op'] != '=':
                subop = info['op'].replace('=','')
                exp = f"{ud[3]['lv']} {subop} ({exp})"
            resexp[lang] = exp
        resexp[self.frlang] = renamevar(resexp[self.frlang],self.varmap)
        return resexp[self.frlang],resexp[self.tolang]
    def rejudgeLongComp(self,frexp,toexp):
        #math.pow sometimes differs with pow. int(a/b) sometimes differs with a//b.
        if 'math.pow' in frexp:
            frexp = frexp.replace('math.pow','pow')
            comp = ExpExector(frexp,toexp,{},{},vartypemap=self.oracletypemap).compare()
            if comp == True:
                return True
        elif 'math.pow' in toexp:
            toexp = toexp.replace('math.pow','pow')
            comp = ExpExector(frexp,toexp,{},{},vartypemap=self.oracletypemap).compare()
            if comp == True:
                return True
        if 'int(' in frexp:
            castsub = getMatchedBracket(frexp[frexp.find('int('):])
            if '/' in castsub and '//' not in castsub:
                newsub = castsub.replace('/','//')
                frexp = frexp.replace(castsub,newsub)
                comp = ExpExector(frexp,toexp,{},{},vartypemap=self.oracletypemap).compare()
                if comp == True:
                    return True
        elif 'int(' in toexp:
            castsub = getMatchedBracket(toexp[toexp.find('int('):])
            if '/' in castsub and '//' not in castsub:
                newsub = castsub.replace('/','//')
                toexp = toexp.replace(castsub,newsub)
                comp = ExpExector(frexp,toexp,{},{},vartypemap=self.oracletypemap).compare()
                if comp == True:
                    return True
        return False
    def longComp_div(self,cfg):
        exprset = set()
        for node in cfg.nodelist:
            for ud in node['UD']:
                if 'node' in ud[3]:
                    if 'returnstmt' in ud[3]:
                        expr = ud[3]['returnstmt']
                    elif 'rv' in ud[3]:
                        expr = ud[3]['rv']
                    else:
                        continue
                    if expr in exprset:
                        continue
                    exprset.add(expr)
                    info = []
                    self.traverseBinary(ud[3]['node'],info)
                    ud[3]['div'] = info
                    #Logger.debug(info)
    
    def valueCheckLongCompG(self):
        fr = self.frlang
        to = self.tolang
        frnodetypecntdic = {}
        if fr not in self.cfgmap or to not in self.cfgmap:
            return []
        frcfg,tocfg = self.cfgmap[fr],self.cfgmap[to]
        changelist = []
        dr1 = DefineReach(frcfg,mode=2)
        dr2 = DefineReach(tocfg,mode=2)
        for frnode in frcfg.nodelist:
            csttonode = findCSTCFGNode(frnode,tocfg,frnodetypecntdic)
            if csttonode == None:
                continue
            frcnt,tocnt = 0,0 
            exprset = set()
            defcntdic = {}
            frdr = frnode['DRIN']
            for ud in frnode['UD']:
                if 'rv' in ud[3] or 'returnstmt' in ud[3]:
                    varname = renamevar(ud[0],self.varmap) if 'rv' in ud[3] else '@RET'                        
                    unsupapivar = ['inf','sys','math','Math','sqrt',"'inf'","Integer","MIN_VALUE","MAX_VALUE","INT_MAX","INT_MIN","Arrays","PI","Character","System","out","Collections","String","deque","np","start"]                    
                    if ud[0] in unsupapivar:
                        continue
                    if ud[0] in self.arrshapeinfo[self.frlang] and ud[1] == 'D':
                        continue
                    defcntdic[varname] = 1 if varname not in defcntdic else defcntdic[varname] + 1
                    orifrexp = ud[3]['rv'] if 'rv' in ud[3] else ud[3]['returnstmt'].replace('return','').replace(';','').strip()
                    frdr,_ = dr1.inductUD(frdr,ud,[])
                    retflg = False if 'rv' in ud[3] else True
                    #Logger.debug(orifrexp)
                    frexp = orifrexp
                    if countOPInExp(frexp) > 3:
                    #if len(removeBlank(frexp)) >= 15:
                        if frexp in exprset:
                            continue
                        exprset.add(frexp)
                        frexp = removeBlank(frexp)
                        tocnt = 0
                        csttoud = None
                        csttodr = csttonode['DRIN']
                        for tud in csttonode['UD']:
                            if 'rv' in tud[3] or 'returnstmt' in tud[3]:
                                tovarname = tud[0] if 'rv' in tud[3] else '@RET'
                                toudkind = tud[1]
                                csttodr,_ = dr2.inductUD(csttodr,tud,[])
                                if (retflg or toudkind == "D" or toudkind == "RD") and tovarname == varname:
                                    
                                    tocnt += 1
                                if tocnt == defcntdic[varname]:
                                    csttoud = tud
                                    break
                        if csttoud == None:
                            continue
                        toexp = csttoud[3]['rv'] if 'rv' in csttoud[3] else csttoud[3]['returnstmt'].replace('return','').replace(';','')
                        oritoexp = toexp
                        frexp,toexp = self.normalizeLongCompExp(frexp,toexp,ud,csttoud,frnode,csttonode,retflg)
                        if ( frexp[1:-1] == toexp and frexp[0] == "(" )or (toexp[1:-1] == frexp and frexp[0] == "("):
                            comp = True
                        else:
                            comp = ExpExector(frexp,toexp,{},{},vartypemap=self.oracletypemap).compare()                       
                        if comp == "Unknown_var":
                            newfrexp,newtoexp = renameArr(frexp),renameArr(toexp)
                            newfrexp = simplifyExpByDR(self.oracletypemap,"",newfrexp,frdr,set())
                            newtoexp = simplifyExpByDR(self.tovartypemap,"",newtoexp,csttodr,set())
                            #Logger.debug(frexp,toexp)
                            comp = ExpExector(newfrexp,newtoexp,{},{},vartypemap=self.oracletypemap).compare()
                            if comp == "Unknown_var":
                                comp = False
                        #Logger.debug(comp)
                        if comp == False:
                            if not self.rejudgeLongComp(frexp,toexp):                            
                                blank = ""
                                #Logger.debug(cstpynode['deep'])
                                converfrexp = STMTCONVERT[(self.frlang,self.tolang)](frexp)
                                for _ in range(csttonode["deep"] + 1):
                                    blank += "    "
                                newstmt = blank
                                if 'rv' in csttoud[3]:
                                    newstmt += csttoud[3]['lv'] + "=" + converfrexp + ";"
                                else:
                                    newstmt += 'return ' + converfrexp + ';'
                                if self.tolang != "python":
                                    tp = (self.crettype if self.tolang == "cpp" else self.jvrettype) if 'returnstmt' in ud[3] else self.oracletypemap[ud[0]]
                                    if 'bool' in tp:
                                        cc = ConditionComparar() 
                                        converfrexp = cc.post2Func(cc.infix2postfix(converfrexp),lang=self.tolang)[0]
                                if self.tolang == "java":   
                                    if 'div' in csttoud[3]:
                                        for dexpr in csttoud[3]['div']:
                                            if dexpr in converfrexp:
                                                converfrexp = converfrexp.replace(dexpr,'(double)'+dexpr+"")
                                if 'op' in csttoud[3] and len(csttoud[3]['op']) >= 2:
                                    oritoexp = csttoud[3]['op'] + oritoexp
                                    converfrexp = "=" + converfrexp
                                changelist.append({"type":"add","line":-1,"content":oritoexp,"changetype":"longcomp"})
                                changelist.append({"type":"replace2","line":csttoud[2],"old":oritoexp,"new":' '+converfrexp,"changetype":"longcomp"})       
                                Logger.cstwarning(f"complicated expression unpreserved: src: {orifrexp}, tgt: {oritoexp}",csttoud[2])                                   
        return changelist
    
    def normalStmtCheck(self):
        errorinfo = []
        #self.Logger.debugCFG()
        changelist = []
        pair = (self.frlang,self.tolang)
        if pair in [("java","python"),("python","java")]:
            self.longComp_div(self.cfgmap["java"])
        frcfg = self.cfgmap[self.frlang]
        tocfg = self.cfgmap[self.tolang]
        if self.cfgnodeTypeCheck(frcfg,tocfg):
            Logger.debug("cfg consistent")
            changelist.extend(self.valueCheckLongCompG())
        ConditionReach(frcfg)
        ConditionReach(tocfg)
        #self.Logger.debugCFG()
        PyUDCheck(tocfg)
        if self.cfgnodeTypeCheck(frcfg,tocfg):
            changelist.extend(self.valueCheckRewritePy_maxminG())
            changelist.extend(self.valueCheckRewritePy_arrG(self.arrshapeinfo[self.frlang],self.arrshapeinfo[self.tolang]))
        else:
            self.controlnoequeal += 1
        return changelist
    def controlStmtCheck(self):
        errlist = []
        frcft = self.cftmap[self.frlang]
        tocft = self.cftmap[self.tolang]
        flg = cftCtetCheck(frcft,tocft,self.frcode,self.tocode,errlist,self.frlang,self.tolang)
        frcfg = self.cfgmap[self.frlang]
        tocfg = self.cfgmap[self.tolang]
        frstruct = frcfg.compressCFG()
        tostruct = tocfg.compressCFG()
        #self.Logger.debugCFG()
        structcomp1 = True
        structcomp1 = self.conftrolStructCheck(frstruct,tostruct)
        changelist = []
        if len(errlist) != 0:
            newerrlist = []
            for err in errlist:
                if err["type"] == "for" and self.reJudgeForCondErr2(err):    
                    continue
                elif (err["type"] == "if" or err["type"] == "while") and self.reJudgeIf(err):
                    continue
                newerrlist.append(err)
            errlist = newerrlist
            for err in errlist:
                if err["type"] == "for":
                    cl = self.rewriteFor(err,self.tolineindex)
                    changelist.extend(cl)
                elif err["type"] == "if":
                    cl = self.rewriteIf(err,self.tolineindex)
                    changelist.extend(cl)
                elif err["type"] == "while":
                    cl = self.rewriteWhile(err,self.tolineindex)
                    changelist.extend(cl)
        frstruct = frcfg.compressCFG()
        tostruct = tocfg.compressCFG()
        self.friflis = []
        self.toiflis = []
        self.extractIfFromStruct(frstruct,self.friflis)
        self.extractIfFromStruct(tostruct,self.toiflis)
        structcomp2 = self.conftrolStructCheck(frstruct,tostruct)
        structchangelist = []
        if not self.cfgnodeTypeCheck(frcfg,tocfg):
            return []
        else:
            changelist.extend(structchangelist)
            return changelist
    
    def totalcheck(self):
        if self.error:
            return self.oripycode,["ASTERROR!"],"ASTERROR!"
        self.changelist = []
        changelist = []
        cl1,cl2 = [],[]
        frcfg = self.cfgmap[self.frlang]
        tocfg = self.cfgmap[self.tolang]
        if not(self.cfgnodeTypeCheck(frcfg,tocfg)):
            if self.tolang == "cpp":
                self.reduceCCFG(frcfg)
            self.reduceJVCFG()
        #frcfg = self.cfgmap[self.frlang]
        #tocfg = self.cfgmap[self.tolang]
        #Logger.debug(self.cfgnodeTypeCheck(frcfg,tocfg))
        cl1 = self.normalStmtCheck()
        self.changelist.extend(cl1)
        cl2 = self.controlStmtCheck()
        self.changelist.extend(cl2)
        cl3,cl4,mypyerr = [],[],""
        if self.frlang == "python" or self.tolang == "python":
            rewriterec,cl3 = self.addtype()
            self.changelist.extend(cl3)
            cl4,mypyerr = self.pytypecheck(rewriterec)
            self.changelist.extend(cl4)
        elif self.frlang == "java" and self.tolang == "cpp":
            self.changelist.extend(self.staticTypeCheck(self.jvvartypemap,self.cvartypemap))
        #Logger.debug("total changelist:"+str(self.changelist))
        return self.changeline(self.changelist),self.changelist,mypyerr
    def changeline(self,changelist):
        code = self.tocode
        if self.tolang == "cpp":
            code = code.replace("True","true").replace("False","false")
            for newplace,st in self.creviselist:
                code = code[:newplace[0]] + st + code[newplace[1]:]     
        codesp = code.split("\n")
        newcode = ""
        changedic = {}
        for changeitem in changelist:
            line = changeitem["line"]
            if line not in changedic:
                changedic[line] = [changeitem]
            else:
                changedic[line].append(changeitem)
        for index,code in enumerate(codesp):
            line = index + 1
            if line in changedic:
                changelis = changedic[line]
                delflg = False
                addcontents = []
                repcode = code
                for changeitem in changelis:
                    if changeitem["type"] == "del":
                        delflg = True
                    elif changeitem["type"] == "add":
                        addcontents.append(changeitem["content"])
                    elif changeitem["type"] == "replace":
                        oricode = repcode
                        repcode = repcode.replace(changeitem["old"],changeitem["new"])
                        if repcode != oricode:
                            delflg = True
                    elif changeitem["type"] == "replace2":
                        oricode = repcode
                        s = changeitem['old']
                        pattern = blankPattern(s)
                        for m in re.findall(pattern,repcode):
                            repcode = repcode.replace(m,changeitem["new"])
                        if repcode != oricode:
                            delflg = True
                addcontents.sort(key=blankCount,reverse=True)
                for addcode in addcontents:
                    newcode += addcode + "\n"
                if changeitem["type"] in ["replace","replace2"] and repcode != oricode:
                    newcode += repcode + "\n"
                if not delflg:
                    newcode += code + "\n"
                
            else:
                newcode += code + "\n"
        
        
        if self.tolang == "java":
            newcode = newcode.replace("class shi1ro{\n","")
            newcode = newcode[:-3]
        return newcode
                    
class Process:
    extdic = {"java":".java","python":".py","cpp":".cpp"}
    cnt = 0
    changerec = {}
    controlequal = 0
    nocontrolequalset = []
    cnt = 1
    def __init__(self,mode,args):
        self.mode = mode
        self.args = args
    
    def mainProcess(self,args):
        frcodeaddr,tocodeaddr,typeaddr,repairaddr,frlang,tolang = args.src_code,args.tgt_code,args.typed_path,args.repair_path,args.src_lang,args.tgt_lang
        file = os.path.basename(frcodeaddr)
        filename,_ = os.path.splitext(file)
        '''if filename != "PROGRAM_CHECK_INPUT_INTEGER_STRING":
            return'''
        Logger.info(f'''task_index: {self.cnt}, src_code: {frcodeaddr}, tgt_code: {tocodeaddr}, typed_code: {typeaddr},repair_code: {repairaddr}''')
        
        cm = CheckManager(frcodeaddr,tocodeaddr,typeaddr,filename,frlang,tolang)
        if cm.parseerror:
            cd,changelis,mypyerr = cm.totalcheck()
            if cm.controlnoequeal == 0:
                self.controlequal += 1
            else:
                self.nocontrolequalset.append(filename)
            if len(changelis) != 0:
                #Logger.debug("need change!")
                #Logger.debug(changelis)
                lineset = set([dic["line"] for dic in changelis])
                if not(len(lineset) == 1 and -1 in lineset):                     
                    with open(repairaddr,"w",encoding='UTF-8') as fptr:
                        fptr.write(cd)
            self.changerec[filename] = {"change":changelis,"mypyoutput":mypyerr}
        else:
            self.changerec[filename] = {"change":["ASTERROR"],"mypyoutput":""}
        Logger.print_all()
    def traverseCheck(self):
        filearg = copy.deepcopy(self.args)
        frpath,topath = self.args.src_code,self.args.tgt_code
        pytypepath,repairpath = self.args.typed_path,self.args.repair_path
        for rs,ds,fs in os.walk(frpath):
            for f in fs:
                '''if cnt <=300:
                    continue'''
                filename,_ = os.path.splitext(f)
                filearg.src_code = os.path.join(frpath,f)
                filearg.tgt_code = os.path.join(topath,filename+self.extdic[self.args.tgt_lang])
                filearg.typed_path = os.path.join(pytypepath,filename+".py")
                filearg.repair_path = os.path.join(repairpath,filename+self.extdic[self.args.tgt_lang])
                self.mainProcess(filearg)
                self.cnt += 1
        
    def run(self):
        if self.mode == 1:
            self.mainProcess(self.args)
        elif self.mode == 2:
            self.traverseCheck()
        #Logger.debug(controlequal)
        '''for name in nocontrolequalset:
            Logger.debug(name)'''
        #Logger.debug(nocontrolequalset)
        if self.args.changelog != "":
            '''with open(os.path.dirname(self.args.changelog)+"/controlinequal","w",encoding='UTF-8') as fptr:
                json.dump(nocontrolequalset,fptr,indent=4)'''
            with open(self.args.changelog,"w",encoding='UTF-8') as fptr:
                json.dump(self.changerec,fptr,indent=4)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('--src_lang', type=str, required=True,help='source language')
    parser.add_argument('--tgt_lang', type=str, required=True,help='target language')
    parser.add_argument('--src_code', type=str, required=True,help='path of source code')
    parser.add_argument('--tgt_code', type=str, required=True,help='path of target code')
    parser.add_argument('--typed_path', type=str, help='an output path, type Python with Java/C equivalent type')
    parser.add_argument('--changelog', type=str, help='path of change log')
    parser.add_argument('--repair_path', type=str, required=True,help='an output path, output the fixed code')
    args = parser.parse_args()
    direction = (args.src_lang,args.tgt_lang)
    supportdirect = [("java","python"),("python","java"),("java","cpp")]
    if direction not in supportdirect:
        Logger.debug(f"transpilation direction {direction[0]}->{direction[1]} not support")
        Logger.print_all()
        sys.exit(1)
    if (direction[0] == "python" or direction[1] == "python"):
        if args.typed_path is None:
            Logger.debug("require a path to output typed Python")
            Logger.print_all()
            sys.exit(1)
        outputPaths = [args.typed_path, args.repair_path]
    else:
        outputPaths = [args.repair_path]
    args.changelog = "" if args.changelog is None else args.changelog
    if args.changelog != "":
        ensureParentDirsExist([args.changelog])
    inputPaths = [args.src_code, args.tgt_code]
    arePathsExist(inputPaths)
    mode = 0
    if isAllFiles(inputPaths + outputPaths):
        ensureParentDirsExist(outputPaths)
        mode = 1
    elif isAllDirs(inputPaths + outputPaths):
        ensureDirsExist(outputPaths)
        mode = 2
    else:
        Logger.debug("must be all files or all dirs")
        Logger.print_all()
        sys.exit(1)
    Logger._debug_enabled = False
    p = Process(mode,args).run()

    