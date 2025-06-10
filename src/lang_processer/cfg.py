import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from common.util import getToken,dumpAST,removeBlank,normalizeJavaComp,getCode,checkStrip,splitLineAST,normalizaUpdate,ridType,rewriteOpAssExpr,ConditionComparar,Logger,STMTTRANSPILE2PY,PRIMITIVETYPE
from common.traverse import unfoldParenthe,findError,CDefUseTvs,getNthChild,checkArrayInitInLoop,pyDefUseTvs,copyKeyStmt

import re
import copy
tmpset = set()
def JavaCftConstruct(code,node):
    if node.type == "if_statement":
        cnt = 0
        ifdesc = {"type":node.type,"condition":None,"else":[],"start":node.start_byte,"end":node.end_byte,"ternary_flg":False}
        elseflg = False
        returnflg = False
        for child1 in node.children:
            if cnt == 1:
                cond = getToken(code,child1)
                if child1.type == "parenthesized_expression":
                    cond = cond[1:-1]
                ifdesc["condition"] = cond
                ifdesc["condition_node"] = child1
            elif cnt == 2:
                returnflg = False
                desc = JavaCftConstruct(code,child1)
                ifdesc["start_content"] = child1.start_byte
                ifdesc["content"] = [desc] if type(desc) != type([]) and desc != None else desc
            elif cnt == 3 and child1.type == "else":
                elseflg = True
            elif cnt == 4 and elseflg:
                elsedesc = JavaCftConstruct(code,child1)   
                if child1.type == "if_statement":
                    if elsedesc == None:
                        ifdesc["else"].append({"type":"else_statement","content":None,"start":child1.start_byte,"start_content":child1.start_byte,"end":child1.end_byte})
                    else:
                        elselist = elsedesc["else"]
                        if elselist == None:
                            elselist = []
                        neweliflist = [{"type":"elif_statement","condition":elsedesc["condition"],"condition_node":elsedesc["condition_node"],"content":elsedesc["content"],"start":elsedesc["start"],"start_content":elsedesc["start_content"],"end":elsedesc["end"]}]
                        neweliflist.extend(elselist)
                        ifdesc["else"] = neweliflist
                else:
                    if elsedesc != None and type(elsedesc) != type([]):
                        elsedesc = [elsedesc]
                    ifdesc['else'] = [{"type":"else_statement","content":elsedesc,"start":child1.start_byte,"start_content":child1.start_byte,"end":child1.end_byte}]
            cnt += 1
        if len(ifdesc['else']) == 0:
            ifdesc['else'] = None
        return ifdesc
    elif node.type == "for_statement":
        cnt = 0
        fordesc = {"type":node.type,"init":[],"condition":[],"update":[],"content":None,"start":node.start_byte,"end":node.end_byte}
        omitflg,key = checkArrayInitInLoop(code,node)
        #Logger.debug(omitflg,key)
        if omitflg:
            fordesc['defomit'] = key
        stmtflg = False
        blockflg = False
        compnode = None
        for child1 in node.children:
            if child1.type == ";":
                stmtflg = True
            elif child1.type == ")":
                blockflg = True
                stmtflg = False
                #fordesc['end'] = child1.end_byte
            elif child1.type == "block" or blockflg:              
                desc = JavaCftConstruct(code,child1)
                fordesc["start_content"] = child1.start_byte
                fordesc["content"] = [desc] if type(desc) != type([]) and desc != None else desc
            elif not stmtflg and (child1.type == "local_variable_declaration" or child1.type == "assignment_expression"): 
                initst = getToken(code,child1).replace(";","")
                initlis = []
                initsgst = ""
                spflg = True
                for c in initst:
                    if c == "(":
                        spflg = False
                    elif c == ")":
                        spflg = True
                    if c == "," and spflg:
                        initlis.append(initsgst)
                        initsgst = ""
                    else:
                        initsgst += c
                if initsgst != "" and initsgst not in initlis:
                    initlis.append(initsgst)
                fordesc["init"] = initlis
            elif child1.type == "binary_expression":
                compstmt = normalizeJavaComp(code,child1)
                compnode = child1
                fordesc["condition"].append(compstmt)
                #fordesc["condition"].append(child1)
            elif child1.type == "parenthesized_expression":
                for child2 in child1.children:
                    if child2.type not in ['(',')']:
                        compnode = child2
                        fordesc["condition"].append(normalizeJavaComp(code,child2))
            elif stmtflg and child1.type != ")" and child1.type != ";" and child1.type != ",":
                updates = removeBlank(getToken(code,child1))
                updates = normalizaUpdate(updates)
                fordesc["update"].append(updates)
                #fordesc["update"].append(child1)
            
            cnt += 1
        if not compnode == None:
            fordesc['condition_node'] = compnode    
        return fordesc
    elif node.type == "enhanced_for_statement":
        fordesc = {"type":"enhanced_for_statement","iter":None,"collection":None,"content":None,"start":node.start_byte,"end":node.end_byte}
        splitchar = ":"
        flg = None
        iterstr = ""
        coltstr = ""
        blockflg = None
        for child1 in node.children:
            if child1.type == "(":
                flg = True
            elif child1.type == ")":
                flg = None
                blockflg = True
                #fordesc['end'] = child1.end_byte
            elif child1.type == splitchar:
                flg = False
            elif flg == True:
                iterstr += getToken(code,child1)
            elif flg == False:
                coltstr += getToken(code,child1)
            elif blockflg:
                desc = JavaCftConstruct(code,child1)
                fordesc["start_content"] = child1.start_byte
                fordesc["content"] = [desc] if type(desc) != type([]) and desc != None else desc
                break
        return fordesc
    elif node.type == "ternary_expression":
        ifdesc = {"type":"if_statement","else":[{"type":"else_statement","content":None,"start":node.start_byte,"end":node.end_byte}],"content":None,"start":node.start_byte,"end":node.end_byte,"ternary_flg":True,"ternary_code":getToken(code,node)}
        lasttoken = ""
        for child1 in node.children:
            if child1.type == "?":
                ifdesc["condition"] = lasttoken
                ifdesc["start_content"] = child1.end_byte+1
            elif child1.type == ":":
                ifdesc["else"][0]["start"] = child1.end_byte
                ifdesc["else"][0]["start_content"] = child1.end_byte + 1
                break
            lasttoken = getToken(code,child1)
            '''if child1.type == "binary_expression":
                ifdesc["condition"] = getToken(code,child1)
            elif child1.type == "parenthesized_expression":
                ifdesc["condition"] = getToken(code,child1)[1:-1]
                break'''
        return ifdesc
    elif node.type == "while_statement" or node.type == "do_statement":
        whiledesc = {"type":node.type,"condition":None,"content":None,"start":node.start_byte,"end":node.end_byte}
        blockflg = False
        for child1 in node.children:
            if child1.type == "block" or blockflg:
                blockdesc = JavaCftConstruct(code,child1)
                whiledesc["start_content"] = child1.start_byte
                whiledesc["content"] = [blockdesc] if type(blockdesc) != type([]) and blockdesc != None else blockdesc
                break
            elif child1.type == "condition" or child1.type == "parenthesized_expression":
                if child1.type == "parenthesized_expression":
                    cond = getToken(code,child1)[1:-1]
                else:
                    cond = getToken(code,child1)
                whiledesc["condition"] = cond
                whiledesc["condition_node"] = child1
                blockflg = True
            
        return whiledesc
    else:   
        lis = []
        for child in node.children:
            desc = JavaCftConstruct(code,child)
            if desc != None:
                lis.append(desc)
        if len(lis) == 0:
            return None
        elif len(lis) == 1:
            return lis[0]
        else:
            return lis

def CPPCftConstruct(code,node):
    if node.type == "if_statement":
        cnt = 0
        ifdesc = {"type":node.type,"condition":None,"else":[],"start":node.start_byte,"end":node.end_byte,"ternary_flg":False}
        returnflg = False
        for child1 in node.children:
            if cnt == 1:
                child = unfoldParenthe(child1)
                cond = getToken(code,child)
                ifdesc["condition"] = cond
                ifdesc["condition_node"] = child
            elif cnt == 2:
                returnflg = False
                desc = CPPCftConstruct(code,child1)
                ifdesc["start_content"] = child1.start_byte
                ifdesc["content"] = [desc] if type(desc) != type([]) and desc != None else desc
            elif cnt == 3 and child1.type == "else_clause":
                elsedesc = CPPCftConstruct(code,child1)   
                if elsedesc == None:
                    startcontent = getNthChild(child1,1).start_byte
                    ifdesc["else"].append({"type":"else_statement","content":None,"start":child1.start_byte,"end":child1.end_byte,"start_content":startcontent})
                else:
                    if type(elsedesc) == type({}) and elsedesc["type"] == "if_statement" and not elsedesc["ternary_flg"]:
                        elselist = elsedesc["else"]
                        if elselist == None:
                            elselist = []
                        neweliflist = [{"type":"elif_statement","condition":elsedesc["condition"],"condition_node":elsedesc["condition_node"],"content":elsedesc["content"],"start":elsedesc["start"],"start_content":elsedesc["start_content"],"end":elsedesc["end"]}]
                        neweliflist.extend(elselist)
                        ifdesc["else"] = neweliflist
                    else:
                        if elsedesc != None and type(elsedesc) != type([]):
                            elsedesc = [elsedesc]
                        startcontent = getNthChild(child1,1).start_byte
                        ifdesc['else'] = [{"type":"else_statement","content":elsedesc,"start":child1.start_byte,"start_content":startcontent,"end":child1.end_byte}]
            cnt += 1
        if len(ifdesc['else']) == 0:
            ifdesc['else'] = None
        return ifdesc
    elif node.type == "for_statement":
        cnt = 0
        fordesc = {"type":node.type,"init":[],"condition":[],"update":[],"content":None,"start":node.start_byte,"end":node.end_byte}
        omitflg,key = checkArrayInitInLoop(code,node)
        #Logger.debug(omitflg,key)
        if omitflg:
            fordesc['defomit'] = key
            if 'initcall' in key:
                fordesc['tobecut'] = True
        stmtflg = False
        blockflg = False
        compnode = None
        for child1 in node.children:
            if child1.type == ";":
                stmtflg = True
            elif child1.type == ")":
                blockflg = True
                stmtflg = False
                #fordesc['end'] = child1.end_byte
            elif child1.type == "compound_statement" or blockflg:
                fordesc["start_content"] = child1.start_byte              
                desc = CPPCftConstruct(code,child1)
                fordesc["content"] = [desc] if type(desc) != type([]) and desc != None else desc
            elif not stmtflg and (child1.type == "declaration" or child1.type == "assignment_expression"): 
                initst = getToken(code,child1).replace(";","")
                initlis = []
                initsgst = ""
                spflg = True
                for c in initst:
                    if c == "(":
                        spflg = False
                    elif c == ")":
                        spflg = True
                    if c == "," and spflg:
                        initlis.append(initsgst)
                        initsgst = ""
                    else:
                        initsgst += c
                if initsgst != "" and initsgst not in initlis:
                    initlis.append(initsgst)
                fordesc["init"] = initlis
            elif child1.type == "binary_expression":
                compstmt = normalizeJavaComp(code,child1)
                compnode = child1
                fordesc["condition"].append(compstmt)
                #fordesc["condition"].append(child1)
            elif child1.type == "parenthesized_expression":
                for child2 in child1.children:
                    if child2.type not in ['(',')']:
                        compnode = child2
                        fordesc["condition"].append(normalizeJavaComp(code,child2))
            elif stmtflg and child1.type != ")" and child1.type != ";" and child1.type != ",":
                updates = removeBlank(getToken(code,child1))
                if ',' in updates:
                    updates = updates.split(',')
                    updates = [normalizaUpdate(u) for u in updates]
                else:
                    updates = [normalizaUpdate(updates)]
                
                fordesc["update"].extend(updates)
                #fordesc["update"].append(child1)
            
            cnt += 1
        if not compnode == None:
            fordesc['condition_node'] = compnode    
        return fordesc
    elif node.type == "for_range_loop":
        fordesc = {"type":"enhanced_for_statement","iter":None,"collection":None,"content":None,"start":node.start_byte,"end":node.end_byte}
        cutflg,_ = checkArrayInitInLoop(code,node)
        if cutflg:
            fordesc['tobecut'] = True
        splitchar = ":"
        flg = None
        iterstr = ""
        coltstr = ""
        blockflg = None
        for child1 in node.children:
            if child1.type == "(":
                flg = True
            elif child1.type == ")":
                flg = None
                blockflg = True
                #fordesc['end'] = child1.end_byte
            elif child1.type == splitchar:
                flg = False
            elif flg == True:
                iterstr += getToken(code,child1)
            elif flg == False:
                coltstr += getToken(code,child1)
            elif blockflg:
                desc = CPPCftConstruct(code,child1)
                fordesc["start_content"] = child1.start_byte       
                fordesc["content"] = [desc] if type(desc) != type([]) and desc != None else desc
                break
        return fordesc
    elif node.type == "conditional_expression":
        ifdesc = {"type":"if_statement","else":[{"type":"else_statement","content":None,"start":node.start_byte,"end":node.end_byte}],"content":None,"start":node.start_byte,"end":node.end_byte,"ternary_flg":True,"ternary_code":getToken(code,node)}
        lasttoken = ""
        for child1 in node.children:
            if child1.type == "?":
                ifdesc["condition"] = lasttoken
                ifdesc["start_content"] = child1.end_byte+1
            elif child1.type == ":":
                ifdesc["else"][0]["start"] = child1.end_byte
                ifdesc["else"][0]["start_content"] = child1.end_byte + 1
                break
            lasttoken = getToken(code,child1)
            '''if child1.type == "binary_expression":
                ifdesc["condition"] = getToken(code,child1)
            elif child1.type == "parenthesized_expression":
                ifdesc["condition"] = getToken(code,child1)[1:-1]
                break'''
        return ifdesc
    elif node.type == "while_statement" or node.type == "do_statement":
        whiledesc = {"type":node.type,"condition":None,"content":None,"start":node.start_byte,"end":node.end_byte}
        blockflg = False
        parseblock = False
        for child1 in node.children:
            if child1.type == "compound_statement" or blockflg:
                blockdesc = CPPCftConstruct(code,child1)
                whiledesc["start_content"] = child1.start_byte       
                whiledesc["content"] = [blockdesc] if type(blockdesc) != type([]) and blockdesc != None else blockdesc
                parseblock = True
                if not (whiledesc["condition"] == None):
                    break

            elif child1.type == "condition_clause" or child1.type == "parenthesized_expression":
                child = unfoldParenthe(child1)
                cond = getToken(code,child)
                whiledesc["condition"] = cond
                whiledesc["condition_node"] = child1
                if parseblock:
                    break
                blockflg = True
        return whiledesc
    else:   
        lis = []
        for child in node.children:
            desc = CPPCftConstruct(code,child)
            if desc != None:
                global tmpset
                lis.append(desc)
        if len(lis) == 0:
            return None
        elif len(lis) == 1:
            return lis[0]
        else:
            return lis

def PythonCftConstruct(code,node):
    if node.type == "if_statement":
        cnt = 0
        ifdesc = {"type":node.type,"condition":None,"else":[],"start":node.start_byte,"end":node.end_byte,"conditional_exp":False}
        for child1 in node.children:
            if cnt == 1:
                cond = getToken(code,child1)
                if child1.type == "parenthesized_expression":
                    cond = cond[1:-1]
                ifdesc["condition"] = cond
                ifdesc["condition_node"] = child1
            elif cnt == 3:
                desc = PythonCftConstruct(code,child1)
                ifdesc["start_content"] = child1.start_byte
                ifdesc["content"] = [desc] if type(desc) != type([]) and desc != None else desc
            elif child1.type == "elif_clause" or child1.type == "else_clause":
                cnt1 = 0
                typename = "elif_statement" if child1.type == "elif_clause" else "else_statement"
                elsedesc = {"type":typename,"condition":None,"content":None,"start":child1.start_byte,"end":child1.end_byte} if child1.type == "elif_clause" else {"type":typename,"content":None,"start":child1.start_byte,"end":child1.end_byte}
                for child2 in child1.children:
                    if child2.type == ":":
                        continue
                    if cnt1 == 1 and child1.type == "elif_clause":
                        elsecond = getToken(code,child2)
                        if child2.type == "parenthesized_expression":
                            elsecond = elsecond[1:-1]
                        elsedesc["condition"] = elsecond
                        elsedesc["condition_node"] = child2
                    elif child2.type == "block":
                        desc = PythonCftConstruct(code,child2)
                        elsedesc["start_content"] = child2.start_byte
                        elsedesc["content"] = [desc] if type(desc) != type([]) and desc != None else desc
                    cnt1 += 1
                ifdesc["else"].append(elsedesc)
            cnt += 1
        if len(ifdesc['else']) == 0:
            ifdesc['else'] = None
        return ifdesc
    elif node.type == "conditional_expression":
        ifdesc = {"type":"if_statement","else":[{"type":'else_statement',"content":None,"start":node.start_byte,"end":node.end_byte}],"content":None,"start_content":node.start_byte,"end":node.end_byte,"conditional_exp":True,"conditional_exp_code":getToken(code,node)}
        ifflg = False
        elseflg = False
        for child1 in node.children:
            if child1.type == "if":
                ifflg = True
            elif ifflg:
                cond = getToken(code,child1)
                if child1.type == "parenthesized_expression":
                    cond = cond[1:-1]
                ifdesc["condition"] = cond
                ifdesc["start"] = child1.start_byte
                ifflg = False
            elif child1.type == "else":
                elseflg = True
                ifdesc["else"][0]["start"] = child1.start_byte
            elif elseflg:
                ifdesc["start"] = node.start_byte
                ifdesc["else"][0]["start_content"] = child1.start_byte 
                ifdesc["else"][0]["end"] = node.end_byte
        return ifdesc
    elif node.type == "for_statement":
        fordesc = {"type":"for_statement","init":[],"condition":[],"content":None,"start":node.start_byte,"end":node.end_byte}
        inflg = False
        forflg = False
        for child1 in node.children:
            if child1.type == "for":
                forflg = True
            elif child1.type == "in":
                inflg = True
            elif inflg:
                cond = getToken(code,child1)
                fordesc['condition'] = [getToken(code,child1)]
                rangeargs = []
                if cond.find("zip") != -1:
                    fordesc['update'] = ""
                elif cond.find("range") != -1:
                    for child2 in child1.children:
                        if child2.type == "argument_list":
                            for child3 in child2.children:
                                if child3.type not in ["(",",",")"]:
                                    arg = getToken(code,child3)
                                    if child3.type == "parenthesized_expression":
                                        arg = arg[1:-1]
                                    rangeargs.append(removeBlank(arg))
                    itr = fordesc['init'][0]
                    if len(rangeargs) == 0:
                        fordesc['init'] = [""]
                        fordesc['condition'] = [""] 
                        fordesc['update'] = [""]
                    else:
                        boundst = rangeargs[0] if len(rangeargs) == 1 else rangeargs[1]
                        #boundst = boundst.replace("math","Math")
                        ''' if boundst.find("and") != -1:
                            boundst = boundst.replace("and","&&")
                            boundst = '(' + boundst + ')'
                        elif boundst.find("or") != -1:
                            boundst = boundst.replace("or","||")
                            boundst = '(' + boundst + ')
                        f = re.findall('len\([a-zA-Z0-9]*\)',boundst)
                        for matched in f:
                            m = re.match('len\(([a-zA-Z0-9]*)\)',matched)
                            boundst = boundst.replace(matched,m[1]+".length()")'''
                        speckeywords = ["if","and","or",">","<","!=","=="]
                        if [boundst.find(w) for w in speckeywords] != [-1 for _ in speckeywords]:
                            boundst = "(" + boundst + ")"
                        if len(rangeargs) == 1:
                            fordesc['init'] = [itr + "=0"]
                            fordesc['condition'] = [itr + "<" + boundst] 
                            fordesc['update'] = [itr + "++"]
                        elif len(rangeargs) == 2:
                            fordesc['init'] = [itr + "=" + rangeargs[0]]
                            fordesc['condition'] = [itr + "<" + boundst] 
                            fordesc['update'] = [itr + "++"]
                        elif len(rangeargs) == 3:
                            updatev = rangeargs[2]
                            try:
                                updatev = int(updatev)
                            except Exception:
                                updatev = None
                            if updatev != None and updatev < 0:
                                if updatev == -1:
                                    fordesc['update'] = [itr + "--"]
                                else:
                                    fordesc['update'] = [itr + "=" + itr + str(updatev)]
                                fordesc['condition'] = [itr + ">" + boundst] 
                            else:
                                if rangeargs[2] == "1":
                                    fordesc['update'] = [itr + "++"]
                                else:
                                    fordesc['update'] = [itr + "=" + itr + "+" + rangeargs[2]]
                                fordesc['condition'] = [itr + "<" + boundst] 
                            fordesc['init'] = [itr + "=" + rangeargs[0]]
                        else:
                            fordesc['init'] = ["Unknown"]
                            fordesc['condition'] = ["Unknown"]
                            fordesc['update'] = ["Unknown"]
                            Logger.debug("range arguments error")
                    fordesc['range'] = True
                elif cond.find("enumerate") != -1:
                    fordesc['update'] = ""
                    '''args = []
                    for child2 in child1.children:
                        if child2.type == "argument_list":
                            for child3 in child2.children:
                                if child3.type not in ["(",",",")"]:
                                    args.append(removeBlank(getToken(code,child3)))
                    itr = removeBlank(fordesc['init'].split(',')[0])
                    fordesc['init'] = [itr + "=0"]
                    fordesc['condition'] = [itr + "<" + args[0]] 
                    fordesc['update'] = [itr + "++"]'''
                else:
                    fordesc['update'] = ""  
                inflg = False
            elif forflg:
                initst = getToken(code,child1).replace(";","")
                fordesc["init"].extend(initst.split(","))
                forflg = False
            elif node.type == "for_statement" and child1.type == "block":
                desc = PythonCftConstruct(code,child1)
                fordesc["start_content"] = child1.start_byte
                fordesc["content"] = [desc] if type(desc) != type([]) and desc != None else desc
        return fordesc
    elif node.type == "while_statement":
        whiledesc = {"type":node.type,"condition":None,"content":None,"start":node.start_byte,"end":node.end_byte}
        whileflg = False
        for child1 in node.children:
            if child1.type == "while":
                whileflg = True
            elif whileflg:
                
                cond = getToken(code,child1)
                whiledesc["condition"] = getToken(code,unfoldParenthe(child1))
                whiledesc["condition_node"] = child1
                whileflg = False
            elif child1.type == "block":
                desc = PythonCftConstruct(code,child1)
                whiledesc["start_content"] = child1.start_byte
                whiledesc["content"] = [desc] if type(desc) != type([]) and desc != None else desc
        return whiledesc
    else:
        lis = []
        for child in node.children:
            desc = PythonCftConstruct(code,child)
            if desc != None:
                lis.append(desc)
        if len(lis) == 0:
            return None
        elif len(lis) == 1:
            return lis[0]
        else:
            return lis

def cftCtetCheck(jvcft,pycft,jvcode,pycode,errlist,frlang,tolang):
    if (jvcft == None) and (pycft == None):
        return True
    if (jvcft == None) ^ (pycft == None):
        Logger.debug("key stmt inequal")
        return False
    if len(jvcft) != len(pycft):
        Logger.debug("key stmt inequal")
        return False
    flg = True
    checker = CFTNodeChecker() 
    for jvsubcft,pysubcft in zip(jvcft,pycft):
        checkflg = checker.manager(jvsubcft,pysubcft,jvcode,pycode,errlist,frlang,tolang)
        flg = flg and checkflg
    return flg

class CFTNodeChecker:
    CFTCheckerDic = {}
    def __init_subclass__(cls):
        super().__init_subclass__()
        cls.CFTCheckerDic[cls.stmt] = cls
    def check(self,frcft,tocft,frcode,tocode,errlist,frlang,tolang):
        raise NotImplementedError
    def manager(self,frdesc,todesc,frcode,tocode,errlist,frlang,tolang):
        if frdesc['type'] in self.CFTCheckerDic and frdesc['type'] != todesc['type']:
            return False
        for stmt,cls in self.CFTCheckerDic.items():
            if stmt == frdesc['type']:
                checker = cls()
                flg = checker.check(frdesc,todesc,frcode,tocode,errlist,frlang,tolang)
                '''if not flg:
                    Logger.debug(stmt)
                    Logger.debug(jvdesc)
                    Logger.debug(pydesc)'''
                return flg
        return True
class CFGWhileChecker(CFTNodeChecker):
    stmt = "while_statement"
    def checkField(self,frcft,tocft,key,frcode,tocode,errlist,frlang,tolang):
        if (frcft[key] == None) ^ (tocft[key] == None):
            return False
        if frcft[key] == None and tocft[key] == None:
            return True
        if len(frcft[key]) != len(tocft[key]):
            return False
        flg = True
        for fr,to in zip(frcft[key],tocft[key]):
            flg = self.manager(fr,to,frcode,tocode,errlist,frlang,tolang) and flg
        return flg
    def check(self,frdesc,todesc,frcode,tocode,errlist,frlang,tolang):
        flg = self.checkField(frdesc,todesc,'content',frcode,tocode,errlist,frlang,tolang)
        tocond = removeBlank(STMTTRANSPILE2PY[tolang](todesc['condition']))
        frcond = removeBlank(STMTTRANSPILE2PY[frlang](frdesc['condition']))
        finalflg = True
        if type(frcond) == str and type(tocond) == str and tocond != frcond:
            finalflg = False
        if not finalflg:
            errlist.append({
                "type":"while",
                "frcond":frcond,
                "tocond":tocond,
                "frcond_node":frdesc['condition_node'] if 'condition_node' in frdesc else None,
                "tocond_node":todesc['condition_node'] if 'condition_node' in todesc else None,
                "frplace":(frdesc["start"],frdesc["end"]),
                "toplace":(todesc["start"],todesc["end"]),
                "towhileplace":(todesc["start"],todesc.get("start_content")),
            })
        finalflg = finalflg and flg
        return finalflg
        return flg
#change: transcoder MINIMUM_NUMBER_OF_JUMPS_TO_REACH_END_OF_A_GIVEN_ARRAY_2 check condition of elif
class CFGElifChecker(CFTNodeChecker):
    stmt = "elif_statement"
    def checkField(self,frcft,tocft,key,frcode,tocode,errlist,frlang,tolang):
        if (frcft[key] == None) ^ (tocft[key] == None):
            return False
        if frcft[key] == None and tocft[key] == None:
            return True
        if len(frcft[key]) != len(tocft[key]):
            return False
        flg = True
        for fr,to in zip(frcft[key],tocft[key]):
            flg = self.manager(fr,to,frcode,tocode,errlist,frlang,tolang) and flg
        return flg
    def check(self,frdesc,todesc,frcode,tocode,errlist,frlang,tolang):
        flg = self.checkField(frdesc,todesc,'content',frcode,tocode,errlist,frlang,tolang)
        tocond = removeBlank(STMTTRANSPILE2PY[tolang](todesc['condition']))
        frcond = removeBlank(STMTTRANSPILE2PY[frlang](frdesc['condition']))
        finalflg = True
        if type(frcond) == str and type(tocond) == str and tocond != frcond:
            finalflg = False
        if not finalflg:
            errlist.append({
                "type":"if",
                "frcond":frcond,
                "tocond":tocond,
                "frcond_node":frdesc['condition_node'] if 'condition_node' in frdesc else None,
                "tocond_node":todesc['condition_node'] if 'condition_node' in todesc else None,
                "jvplace":(frdesc["start"],frdesc["end"]),
                "pyplace":(todesc["start"],todesc["end"]),
            })
        finalflg = finalflg and flg
        return finalflg
class CFGElseChecker(CFTNodeChecker):
    stmt = "else_statement"
    def check(self,frcft,tocft,frcode,tocode,errlist,frlang,tolang):
        if frcft['content'] == None and tocft['content'] == None:
            return True
        if (frcft['content'] == None) ^ (tocft['content'] == None):
            return False
        flg = True
        for fr,to in zip(frcft['content'],tocft['content']):
            flg = self.manager(fr,to,frcode,tocode,errlist,frlang,tolang) and flg
        return flg
class CFTIfChecker(CFTNodeChecker):
    stmt = "if_statement"
    def checkField(self,frcft,tocft,key,frcode,tocode,errlist,frlang,tolang):
        if (frcft[key] == None) ^ (tocft[key] == None):
            return False
        if frcft[key] == None and tocft[key] == None:
            return True
        if len(frcft[key]) != len(tocft[key]):
            return False
        flg = True
        for fr,to in zip(frcft[key],tocft[key]):
            res = self.manager(fr,to,frcode,tocode,errlist,frlang,tolang)
            flg = flg and res
        return flg
    def check(self,frcft,tocft,frcode,tocode,errlist,frlang,tolang):
        flg = self.checkField(frcft,tocft,'else',frcode,tocode,errlist,frlang,tolang) and self.checkField(frcft,tocft,'content',frcode,tocode,errlist,frlang,tolang)
        tocond = removeBlank(STMTTRANSPILE2PY[tolang](tocft['condition']))
        frcond = removeBlank(STMTTRANSPILE2PY[frlang](frcft['condition']))
        finalflg = True
        if type(frcond) == str and type(tocond) == str and tocond != frcond:
            finalflg = False
        if not finalflg:
            errlist.append({
                "type":"if",
                "frcond":frcond,
                "tocond":tocond,
                "frcond_node":frcft['condition_node'] if 'condition_node' in frcft else None,
                "tocond_node":tocft['condition_node'] if 'condition_node' in tocft else None,
                "frplace":(frcft["start"],frcft["end"]),
                "toplace":(tocft["start"],tocft["end"]),
            })
        finalflg = finalflg and flg
        return finalflg
class CFTForChecker(CFTNodeChecker):
    stmt = "for_statement"
    def rewritePyCFT(self,pycft):
        cond = pycft['condition']
        if cond.find('range') != -1:
            rangeargs = cond[cond.find('(') + 1: cond.find(')')]
            rangeargs = rangeargs.split(',')
            newargs = []
            for arg in rangeargs:
                newargs.append(removeBlank(arg))
            rangeargs=newargs
            itr = pycft['init']
            if len(rangeargs) == 1:
                pycft['init'] = itr + "=0"
                pycft['condition'] = [itr + "<" + rangeargs[0]] 
                pycft['update'] = [itr + "++"]
            elif len(rangeargs) == 2:
                pycft['init'] = itr + "=" + rangeargs[0]
                pycft['condition'] = [itr + "<" + rangeargs[1]] 
                pycft['update'] = [itr + "++"]
            elif len(rangeargs) == 3:
                pycft['init'] = itr + "=" + rangeargs[0]
                pycft['condition'] = [itr + "<" + rangeargs[1]] 
                pycft['update'] = [itr + "=" + itr + "+" + rangeargs[2]]
            else:
                Logger.debug("range arguments error")
                return False
        else:
            pycft['update'] = ""
        #Logger.debug(pycft)
        return pycft
    def check(self,frcft,tocft,frcode,tocode,errlist,frlang,tolang):
        #Logger.debug(tocft)
        finalflg = True
        if (frcft['content'] == None) ^ (tocft['content'] == None):
            finalflg = False
        if frcft['content'] != None and tocft['content'] != None:
            for fr,to in zip(frcft['content'],tocft['content']):
                finalflg = self.manager(fr,to,frcode,tocode,errlist,frlang,tolang) and finalflg
        tocond = tocft['condition']
        frcond = frcft['condition']
        toupdate = tocft['update']
        frupdate = frcft['update']
        toinit = tocft['init']
        frinit = frcft['init']

        if toupdate == "":
            return True
        frinitnum = -1
        toinitnum = -1
        if type(toinit) == type([]):
            toinit = ridType(toinit,PRIMITIVETYPE[tolang],STMTTRANSPILE2PY[tolang])
            toinitnum = len(toinit)
        if type(frinit) == type([]):
            frinit = ridType(frinit,PRIMITIVETYPE[frlang],STMTTRANSPILE2PY[frlang])
            frinitnum = len(frinit)
        if frinitnum != -1 and toinitnum != -1 and frinitnum != toinitnum:
            return True
        if type(frupdate) == type([]):
            newfrupdate = [rewriteOpAssExpr(STMTTRANSPILE2PY[frlang](removeBlank(it))) for it in frupdate]
            frupdate = newfrupdate
        if type(toupdate) == type([]):
            newtoupdate = [rewriteOpAssExpr(STMTTRANSPILE2PY[tolang](removeBlank(it))) for it in toupdate]
            toupdate = newtoupdate
        finalflg = True
        detailtype = {}
        if len(tocond) != len(frcond):
            '''Logger.debug("cond len ineuqal")
            Logger.debug(tocond)
            Logger.debug(frcond)
            detailtype["for_cond"] = "len"
            finalflg =  False'''
            1
        else:
            if len(tocond) == 1:
                '''if frcond[0][0] == "(" and frcond[0][-1] == ")":
                    frcond[0] = frcond[0][1:-1]'''
                #frcond[0] = STMTTRANSPILE2PY[frlang](removeBlank(frcond[0]))
                #tocond[0] = STMTTRANSPILE2PY[tolang](removeBlank(tocond[0]))
                if tocond[0] != frcond[0]:
                    #if not deepcomp(tocond[0],frcond[0]):
                    finalflg =  False
                    excepts = ['zip','enumerate']
                    for e in excepts:
                        if (tocond[0].find(e) != -1 or (tocond[0].find("<") == -1 and tocond[0].find(">") == -1 and tocond[0].find("<=") == -1 and tocond[0].find(">=") == -1)) or (frcond[0].find(e) != -1 or (frcond[0].find("<") == -1 and frcond[0].find(">") == -1 and frcond[0].find("<=") == -1 and frcond[0].find(">=") == -1)):
                            Logger.debug("cond content inequal, but contains exception api")
                            return True
                    Logger.debug("cond content ineuqal,to:%s,fr:%s" %(tocond[0],frcond[0]))
                    detailtype["for_cond"] = "content"
        if toupdate != "" and type(toinit) == type([]):             
            '''if len(toupdate) != len(frupdate):
                detailtype["for_update"] = "len"
                Logger.debug("update len ineuqal")
                finalflg = False
            else:'''
            if len(toupdate) == 1 and len(toupdate) == len(frupdate):
                #frupdate[0] = fr2to(frupdate[0])
                #if not deepcomp(toupdate[0],frupdate[0]):
                if toupdate[0] != frupdate[0]:
                    Logger.debug("update content ineuqal,to:%s,fr:%s" %(toupdate[0],frupdate[0]))
                    finalflg = False
                    detailtype["for_update"] = "content"
        if toinit != "" and type(toinit) == type([]):         
            '''if len(toinit) != len(frinit):
                detailtype["for_init"] = "len"
                Logger.debug("init len ineuqal")
                finalflg = False
            else:'''
            if len(toinit) == 1 and (len(toinit) == len(frinit)):
                #frinit[0] = fr2to(frinit[0]) 
                #if not deepcomp(toinit[0],frinit[0]):
                if toinit[0] != frinit[0]:
                    Logger.debug("init content ineuqal,to:%s,fr:%s" %(toinit[0],frinit[0]))
                    finalflg = False
                    detailtype["for_init"] = "content"
        if not finalflg:
            frcondition_node = frcft['condition_node'] if 'condition_node' in frcft else None
            tocondition_node = tocft['condition_node'] if 'condition_node' in tocft else None
            errlist.append({
                "type":"for",
                "frcond":copy.deepcopy(frcond),
                "tocond":copy.deepcopy(tocond),
                "frupdate":frupdate,
                "toupdate":toupdate,
                "frinit":frinit,
                "toinit":toinit,
                "frplace":(frcft["start"],frcft["end"]),
                "toplace":(tocft["start"],tocft["end"]),
                "toforplace":(tocft["start"],tocft["start_content"]),
                "frcondition_node":frcondition_node,
                "tocondition_node":tocondition_node,
                "detailtype":detailtype,
            })
        
        return finalflg


class CFG:
    index = 0
    nodelist = []
    splitlines = None
    def __init__(self,spl,lang):
        self.lang = lang
        self.splitlines = spl
        self.defs = set()
        self.nodelist = []
        self.sibdic = {}
        self.pardic = {}
        self.dataflow = {}
        self.firstlayer = set()
        self.nodenamemap = {"while_init":"for","for_init":"for","enhanced_init":"for","do_init":"for","if_init":"if","elif_init":"elif","else_init":"else"}
        self.omitplace = []
    def reduceDRinFor(self):
        for node in self.nodelist:
            if node["type"] == "for_init":
                udi = -1
                for i in range(len(node['UD'])-1,-1,-1):
                    ud = node['UD'][i]
                    if ud[1] == 'RD':
                        udi = i
                        break
                if udi != -1:
                    del node['UD'][udi]
    def reduceDRbyDO(self):
        for node in self.nodelist:
            if 'DRIN' in node and 'DOIN' in node:
                drin = node['DRIN']
                newdrin = {}
                if node["index"] == 25:
                    1
                for v,defs in drin.items():
                    newdefs = set()
                    for definfo in defs:
                        fromindex = definfo[1]
                        fromnode = self.getNode(fromindex)
                        fromdoin = fromnode['DOIN']
                        if not(fromindex == node['index'] or node['index'] in fromdoin):
                            newdefs.add(definfo)
                    if len(newdefs) > 0:
                        newdrin[v] = newdefs
                node['DRIN'] = newdrin

    def addReturn(self,place):
        node = self.getNodeByPlace(place)
        if node != None:
            node['return'] = True
            if node['type'] == 'normal':
                par = self.pardic[node['index']]
                if par != -1:
                    parnode = self.getNode(par)
                    if parnode['type'] in ['if_init','elif_init','else_init']:
                        parnode['return'] = True
    def sumupSibandPar(self):
        for i in self.firstlayer:
            self.sibdic[i] = self.firstlayer - set([i])
            self.pardic[i] = -1
        for node in self.nodelist:
            if 'content' in node:
                for i in node['content']:
                    self.sibdic[i] = set(node['content']) - set([i])
                    self.pardic[i] = node['index']
        #Logger.debug(self.sibdic)
        #Logger.debug(self.pardic)
    def sumupContent(self,node):
        desc = {}
        cond = None
        elseflg = None
        if 'condition' in node:
            cond = node['condition'] 
            if type(cond) == type([]):
                if len(cond) > 0:
                    cond = cond[0]
                else:
                    cond = ""
            desc['condition'] = cond
        if 'else' in node:
            elseflg = node['else']
            desc['else'] = elseflg
        if 'return' in node:
            desc['return'] = node['return']
        if 'content' in node:
            lis = []
            node['content'].sort()
            for contindex in node['content']:
                ct = self.sumupContent(self.getNode(contindex))
                if ct != None:
                    lis.append(ct)
            return self.nodenamemap[node['type']],lis,desc
        else:
            if node['type'] in self.nodenamemap:
                return self.nodenamemap[node['type']],[],desc
            else:
                return None
    def getNodeByPlace(self,place):
        for node in self.nodelist:
            if node['start'] <= place and node['end'] >= place:
                return node
        return None
    def getNodeByLine(self,line):
        place = self.splitlines[line-1]
        return self.getNodeByPlace(place)

    def compressCFG(self):
        lis = []
        contindexlis = []
        for node in self.nodelist:
            if 'content' in node and node['index'] not in contindexlis:
                contlis = self.sumupContent(node)
                lis.append(contlis)
                contindexlis.extend(node['allcontent'])
            elif node['index'] not in contindexlis and node['type'] in self.nodenamemap:
                if self.nodenamemap[node['type']] != 'for':
                    desc = {}
                    if 'condition' in node:
                        cond = node['condition'] 
                        if type(cond) == type([]):
                            cond = cond[0]
                        desc['condition'] = cond
                    if 'else' in node:
                        desc['else'] = node['else']
                    if 'return' in node:
                        desc['return'] = node['return']
                    lis.append((self.nodenamemap[node['type']],[],desc))
        return lis
    def getNode(self,index):
        return self.nodelist[index-1]
    def extractPyArr(self):
        arrinfo = { }
        for node in self.nodelist:
            for ud in node['UD']:
                if ud[1] == 'D':
                    vname = ud[0]
                    if 'arrinfo' in ud[3]:
                        arrinfo[vname] = ud[3]['arrinfo']
                        arrinfo[vname]['node'] = ud[3]['node']
                        del ud[3]['arrinfo']
        return arrinfo
    def initTraState(self):
        for node in self.nodelist:
            node['trastate'] = 'white'
    def compressCont(self,index):
        node = self.nodelist[index-1]
        #Logger.debug(node)
        
        if "content" in node:
            #Logger.debug(node)
            if len(node['content']) == 1:
                contnode = self.nodelist[node['content'][0]-1]
                #Logger.debug(contnode)
                if contnode['type'] == "if_init":
                    
                    #Logger.debug(node['succ'])
                    #Logger.debug(contnode['index'])
                    try:
                        node['succ'].remove(contnode['index'])
                        contnode['pred'].remove(node['index'])
                    except:
                        return False
                    if "content" in contnode:
                        node["content"] = contnode["content"]
                        #Logger.debug(contnode["content"])
                        node['succ'].append(contnode["content"][0])
                        self.getNode(contnode["content"][0])['pred'].append(node['index'])
                    else:
                        node.pop("content")
                    node["end"] = contnode["end"]
                    contnode['type'] = "discard"
                    node["condition"][0] = node["condition"][0] + "and" + removeBlank(contnode["condition"])
                    #Logger.debug(node)
                    return True
        return False
              
    def cleanUD(self):
        for node in self.nodelist:
            node['UD'] = []
    def createNode(self,tp,st,ed,dp,cond,succ=None,pred=None):
        self.index += 1
        node = {"type":tp,"start":st,"end":ed,"pred":[],"succ":[],"index":self.index,"deep":dp,"UD":[],"trastate":"white","defs":[],"condition":cond}
        if succ != None:
            node['succ'] = succ
        if pred != None:
            node['pred'] = pred
        self.nodelist.append(node)
        return node
    def appendDefUse(self,ud,st,end,keystmt):
        line = -1
        #Logger.debug(ud,st,end,keystmt)
        #Logger.debug(self.splitlines)
        for omitstart,omitend in self.omitplace:
            if omitstart <= end and end <= omitend:
                return
        newkeystmt = copyKeyStmt(keystmt)
        keystmt = newkeystmt
        for i in range(0,len(self.splitlines)):
            if end-1 < self.splitlines[i]:
                line = i+1
                break
        '''if self.lang == "java":
            line -= 1'''
        if ud[1] == 'U' and 'func' in keystmt and keystmt['func'] == 'append':
            ud = (ud[0],'RD')
            keystmt = {'lv':ud[0]+'[@]','rv':keystmt['arg'][1:-1]}
        if ud[1] == 'U':
            try:
                del keystmt["rv"]
                del keystmt["lv"]
                del keystmt["op"]
            except:
                pass
        for node in self.nodelist:
            if st >= node["start"] and end <= node["end"]:
                '''udlist = node["UD"]
                kind = ud[1]
                id = ud[0]
                flg = None
                if kind == "U":
                    for i in range(len(udlist)-1,-1,-1):
                        if udlist[i][1] == 'D' and udlist[i][0] == id:
                            flg = 'D'
                            break
                        elif udlist[i][1] == 'U' and udlist[i][0] == id:
                            flg = 'U'
                            break
                    if flg == None or flg == 'D':
                        udlist.append((ud[0],ud[1],line))
                else:'''
                if ud[0] != '_':
                    vname = ud[0]
                    kd = ud[1]
                    if ud[1] == 'D' or ud[1] == 'RD':
                        if vname in self.defs and ud[1] == 'D':
                            kd = 'RD'
                        self.defs.add(vname)
                    #Logger.debug((vname,kd,line,keystmt))
                    if node['type'] == 'for_init' and (ud[1] == 'D' or ud[1] == 'RD'):
                        if 'rv' in keystmt and 'lv' in keystmt:
                            del keystmt['rv']
                            del keystmt['lv']
                    node["UD"].append((vname,kd,line,keystmt))
    def getStart(self):
        for node in self.nodelist:
            if node["type"] == "start":
                return node
        return None
def addEdge(nodesA,nodesB):
    '''Logger.debug("addA")
    Logger.debug([i["index"] for i in nodesA])
    Logger.debug("addB")
    Logger.debug([i["index"] for i in nodesB])'''
    for node in nodesA:
        nodes = []
        for nodeb in nodesB:
            if nodeb['index'] != node['index']:
                nodes.append(nodeb['index'])
        node["succ"].extend(nodes)
        node['succ'] = list(set(node['succ']))
    for node in nodesB:
        nodes = []
        for nodea in nodesA:
            if nodea['index'] != node['index']:
                nodes.append(nodea['index'])
        node["pred"].extend(nodes)
        node['pred'] = list(set(node['pred']))
def contentcfg(endnodes,code,deep,cfg,startbyte,nextstartbyte,pycft):
    newcontnode = []
    nextnodes = endnodes
    allcontentnodes = []
    if pycft["content"] == None:
        endbyte = nextstartbyte
    else:
        cont = pycft["content"][0]
        if type(cont) == type([]):
            cont = cont[0]
        endbyte = cont["start"]
    begincode = getCode(code,startbyte,endbyte)
    if not checkStrip(begincode):
        startnode = cfg.createNode("normal",startbyte,endbyte,deep,"")
        addEdge(endnodes,[startnode])
        newcontnode.append(startnode["index"])
        allcontentnodes.append(startnode["index"])
        endnodes = [startnode]
    if not(pycft["content"] == None):
        for index,cont in enumerate(pycft["content"]):
            if type(cont) == type([]):
                cont = cont[0]
            newnextstartbyte = cont["end"]
            newnodes,nextlayernode,allcontentnode = cft2cfg(code,cont,endnodes,newnextstartbyte,deep,cfg)
            newcontnode.extend(nextlayernode)
            allcontentnodes.extend(allcontentnode)
            #Logger.debug("placeG")
            

            #addEdge(endnodes,newnodes)
            endnodes = newnodes
            #Logger.debug(endnodes)
            midstart = cont["end"]
            if index + 1 == len(pycft["content"]):
                midend = nextstartbyte
            else:
                cft = pycft["content"][index+1]
                if type(cft) == type([]):
                    cft = cft[0]
                midend = cft["start"]
            midst = getCode(code,midstart,midend)
            #Logger.debug(midst)
            if not checkStrip(midst):
                midnode = cfg.createNode("normal",midstart,midend,deep,"")
                newcontnode.append(midnode["index"])
                allcontentnodes.append(midnode["index"])
                #Logger.debug("placeD")
                addEdge(newnodes,[midnode])
                endnodes = [midnode]
    return endnodes,newcontnode,allcontentnodes

def cft2cfg(code,pycft,startnodes,nextstartbyte,deep,cfg:CFG):
    nextlayernode = []
    allcontentnode = []
    if pycft["type"] in ["for_statement" ,"while_statement" , "enhanced_for_statement","do_statement","for_statement_fake"]:
        if not(pycft["content"] == None):
            #Logger.debug(pycft["content"])
            newnextstartbyte = pycft["content"][0]["start"]
        else:
            newnextstartbyte = nextstartbyte
        forcondstart = pycft["start"]
        forcondend = pycft["start_content"] if "start_content" in pycft else newnextstartbyte
        startcontent = forcondend
        cond = "" if "condition" not in pycft else pycft["condition"]
        forcondnode = cfg.createNode(pycft["type"].split("_")[0]+"_init",forcondstart,forcondend,deep,cond)
        addEdge(startnodes,[forcondnode])
        endnodes = [forcondnode]
        startnodes = [forcondnode]
        if 'range' in pycft:
            forcondnode['range'] = True
        if "init" in pycft:
            forcondnode['init'] = pycft['init']
        if "update" in pycft:
            forcondnode['update'] = pycft['update']
        if "defomit" in pycft:
            forcondnode['defomit'] = pycft['defomit']
        #Logger.debug("placeA")
        endnodes,contindexs,allcontindexs = contentcfg(endnodes,code,deep+1,cfg,startcontent,nextstartbyte,pycft)
        if pycft["type"] == "for_statement_fake":
            contindexs.append(2)
            cfg.firstlayer = set(contindexs)
        else:
            #Logger.debug("placeB")
            addEdge(endnodes,[forcondnode])
            nextlayernode.append(forcondnode["index"])
            allcontentnode.append(forcondnode["index"])
            try:
                contindexs.remove(forcondnode["index"])
            except:
                pass
            #nextlayernode.extend(contindexs)
            allcontentnode.extend(allcontindexs)
            if len(contindexs) > 0:
                forcondnode["content"] = contindexs
            if len(allcontentnode) > 0:
                forcondnode['allcontent'] = allcontentnode   
        endnodes = [forcondnode]
        return endnodes,list(set(nextlayernode)),list(set(allcontentnode))
    elif pycft["type"] == "if_statement":
        ifs = [{"type":"if_statement","condition":pycft["condition"],"content":pycft["content"],"start":pycft["start"],"end":pycft["end"],"start_content":pycft["start_content"]}]
        elseflg = False
        ifnode = None
        elsenode = None
        if pycft["else"] != None:
            ifs.extend(pycft["else"])
            ifs[0]["end"] = pycft["else"][0]["start"]
        finalendnodes = []
        ifscond = ""
        for i in range(0,len(ifs)):
            subif = ifs[i]
            if i < len(ifs) - 1 and ifs[i]["end"] > ifs[i+1]["start"]:
                ifs[i]["end"] = ifs[i+1]["start"]  
            if subif["type"] == "else_statement":
                elseflg = True
            tp = subif["type"].split("_")[0]
            cond = "" if "condition" not in subif else subif["condition"]
            if cond != "":
                ifscond += f" ({cond}) And"
            ifcondstart = subif["start"]
            ifcondend = subif["start_content"]
            if ifcondstart > ifcondend:
                ifcondstart,ifcondend = ifcondend,ifcondstart
            ifcondnode = cfg.createNode(tp+"_init",ifcondstart,ifcondend,deep,cond)
            if tp == "if":
                ifnode = ifcondnode
            if elseflg:
                elsenode = ifcondnode
            addEdge(startnodes,[ifcondnode])
            endnodes = [ifcondnode]
            startnodes = [ifcondnode]
            if subif["start"] > subif["start_content"]:
                endnodes,contindexs,allcontindexs = contentcfg(startnodes,code,deep+1,cfg,subif["start_content"],subif["start"],subif)
            else:
                endnodes,contindexs,allcontindexs = contentcfg(startnodes,code,deep+1,cfg,subif["start_content"],subif["end"],subif)
            try:
                contindexs.remove(ifcondnode["index"])
            except:
                pass
            if len(contindexs) > 0:
                ifcondnode["content"] = contindexs
            if len(allcontindexs) > 0:
                ifcondnode["allcontent"] = allcontindexs
                #nextlayernode.extend(contindexs)
            allcontentnode.extend(allcontindexs)
            finalendnodes.extend(endnodes)
            nextlayernode.append(ifcondnode["index"])
            allcontentnode.append(ifcondnode["index"])
        ifnode['else'] = elseflg
        if not elseflg:
            #finalendnodes.extend(startnodes)
            finalendnodes.append(ifcondnode)
        else:
            if elsenode != None:
                elsenode['condition'] = "Not("+ifscond[1:-3]+")"
        #Logger.debug("plaecF")
        #Logger.debug(finalendnodes)
        return finalendnodes,list(set(nextlayernode)),list(set(allcontentnode))
def CFGConstruct(code,pycft,funcinfo,cfg:CFG):
    if pycft == None:
        end = funcinfo["end"]
        cfg.createNode("start",0,end,0,"")
    elif len(pycft) == 0:
        cfg.createNode("start",0,0,0,"")
    else:
        end = pycft[0]["start"]
        startnodes = [cfg.createNode("start",0,0,0,"")]
        newpycft = {'type':'for_statement_fake',"content":pycft,"start":0,"end":funcinfo['end']}
        cft2cfg(code,newpycft,startnodes,funcinfo['end'],0,cfg)
        cfg.nodelist[1]["type"] = "normal"
    endnodes = []
    
    for c in cfg.nodelist:
        if len(c['succ']) == 0:
            endnodes.append(c['index'])
            c['succ'].append(len(cfg.nodelist)+1)
    cfg.createNode("end",0,0,0,"",succ=[],pred=endnodes)
    cfg.sumupSibandPar()
    '''for c in cfg.nodelist:
        Logger.debug(str(c['index']) + " " + str(c))'''

    #Logger.debug("\n")
def printCFG(cfg):
    for node in cfg.nodelist:
        #Logger.debug(str(node['index']) + " " + str(node['type'])+str(node['succ']) + str(node['pred']))
        Logger.debug(str(node['index']) + " " + str(node))
def findCSTCFGNode(nodea,cfgb,cntdic):
    nodetype = nodea["type"]
    cntdic[nodetype] = 1 if nodetype not in cntdic else cntdic[nodetype] + 1
    cstnodeb = None
    cnt = 0
    for nodeb in cfgb.nodelist:
        if nodeb["type"] == nodetype:
            cnt += 1
        if cnt == cntdic[nodetype]:
            cstnodeb = nodeb
            break
    return cstnodeb
def omitCFTbyCFG(cft,cfg,key):
    changeflg = False
    omitcfg = []
    if not(cft == None):
        newcft = []
        for c in cft:
            if "defomit" in c and key in c['defomit']:
                cfg.omitplace.append((c["start"],c["end"]))
                omitcfg.append(c)
                changeflg = True
            else:
                newcft.append(c)
        cft = newcft
        if len(cft) == 0:
            cft = None
    return cft,changeflg,omitcfg

def PyUDCheck(cfg:CFG):
    for node in cfg.nodelist:
        defs = []
        for preindex in node["pred"]:
            prenode = cfg.nodelist[preindex-1]
            for d in prenode["defs"]:
                if d not in defs:
                    defs.append(d)
        for ud in node["UD"]:
            if ud[1] == 'D':
                defs.append(ud[0])
            elif ud[1] == 'U':
                if ud[0] not in defs:
                    Logger.debug("%s use but not define in line %s" % (ud[0],ud[2]))
        node["defs"] = defs


if __name__ == "__main__":
    cc = ConditionComparar()
    t = cc.infix2postfix("(count_neg&1==0)andcount_neg!=0")
    Logger.debug(t)
    Logger.debug(cc.post2Func(t))          