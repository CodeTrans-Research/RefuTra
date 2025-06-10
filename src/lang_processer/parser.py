import tree_sitter as ts
from common.util import getToken,removeBlank,parseCArray,checkCArray,Logger
from common.traverse import findJavaLocalVar,getNthChild,findTokenWithType,parseList_Node
class JavaParser:
    def __init__(self,code) -> None:
        self.code,self.tree = self.getAST(code)
        #dumpAST(self.code,self.tree.root_node)
    def getAST(self,input):
        lib_path = "src/tree-sitter/java.so"
        LAN = ts.Language(lib_path,"java")    
        parser = ts.Parser()
        parser.set_language(LAN)
        code = bytes(input, "utf8")
        tree = parser.parse(code)
        return code,tree
    def getFunctions(self):
        lis = []
        self.traverseJavaFunctions(self.code,self.tree.root_node,lis)
        return lis
    def traverseJavaFunctions(self,code,node,funclis):
        for child in node.children:
            if child.type == "function_definition" or child.type == "method_declaration":
                name = ""
                funcnamenode = None
                blocknode = None
                cnt = 0
                for child2 in child.children:
                    cnt += 1
                    if cnt == 1:
                        rettype = getToken(code,child2)
                    elif cnt == 2:
                        funcname = getToken(code,child2)
                    elif child2.type == "block":
                        blocknode = child2
                        locallis1 = []
                        findJavaLocalVar(code,child2,locallis1)
                        #Logger.debug(locallis1)
                        locallis2 = []
                        for local in locallis1:
                            if local[1] != "":
                                locallis2.append(local)
                    elif child2.type == "formal_parameters":
                        formaltypedic = []
                        for child3 in child2.children:
                            if child3.type == "formal_parameter":
                                tp = ""
                                name = ""
                                for child4 in child3.children:
                                    if child4.type != "identifier":
                                        tp += (getToken(code,child4) + " ")
                                    else:
                                        name = getToken(code,child4)
                                tp = tp[:-1]
                                formaltypedic.append((tp,name))
                if name != "__init__" and name != "main":
                    funclis.append((rettype,formaltypedic,locallis2,child.start_byte,child.end_byte,funcname))
            self.traverseJavaFunctions(code,child,funclis)
class PythonParser:
    def __init__(self,code) -> None:
        self.code,self.tree = self.getAST(code)
    def getAST(self,input):
        lib_path = "src/tree-sitter/python.so"
        LAN = ts.Language(lib_path,"python")    
        parser = ts.Parser()
        parser.set_language(LAN)
        code = bytes(input, "utf8")
        tree = parser.parse(code)
        return code,tree
    def getFunctions(self):
        lis = []
        self.traversePyFunctions(lis,self.code,self.tree.root_node)
        return lis
    def traversePyStr(self,code,node,strset):
        if node.type in ["comparison_operator","binary_operator","augmented_assignment"]:
            lvnode = getNthChild(node,0)
            rvnode = getNthChild(node,2)
            varnode = None
            if lvnode.type == "string":
                varnode = rvnode
            elif rvnode.type == "string":
                varnode = lvnode
            if not(varnode == None) :
                if varnode.type == "identifier":
                    strset.add(getToken(code,varnode))
                elif varnode.type == "subscript":
                    strset.add(getToken(code,getNthChild(varnode,0)))
                return "str"
            return "Unknown"
        elif node.type == "string":
            return "str"
        elif node.type == "assignment":
            lvnode = getNthChild(node,0)
            rvnode = getNthChild(node,2)
            strtype = "Unknown"
            if rvnode.type != "expression_list":
                strtype = self.traversePyStr(code,rvnode,strset)
                if strtype == "str":
                    if lvnode.type == "identifier":
                        strset.add(getToken(code,lvnode))
            else:
                lvnodes = parseList_Node(code,lvnode)
                rvnodes = parseList_Node(code,rvnode)
                for lvnode,rvnode in zip(lvnodes,rvnodes):
                    strtype = self.traversePyStr(code,rvnode,strset)
                    if strtype == "str":
                        if lvnode.type == "identifier":
                            strset.add(getToken(code,lvnode))
            return strtype
        for child in node.children:
            self.traversePyStr(code,child,strset)
        return "Unknown"
    def traversePyFunctions(self,funclis,code,node):
        for child in node.children:
            if child.type == "function_definition" or child.type == "method_declaration":
                start = child.start_byte
                end = child.end_byte
                name = ""
                cnt = 0
                flg = False
                pmt = []
                strset = set()
                for child2 in child.children:
                    cnt += 1
                    if cnt == 2:
                        name = getToken(code,child2)
                        if name == "f_gold" or name == "f_filled":
                            flg = True
                    elif child2.type == "block":
                        self.traversePyStr(code,child2,strset)
                    '''elif child2.type == "parameters":
                        for child3 in child2.children:
                            if child3.type not in ["(",",",")"]:
                                pmt.append(getToken(code,child3))'''
                if flg:
                    funclis.append({"start":start,"end":end,"strset":strset})
                    return
            if len(funclis) == 0:
                self.traversePyFunctions(funclis,code,child)
            else:
                return
class CPPParser:
    def __init__(self,code) -> None:
        self.code,self.tree = self.getAST(code)
    def getAST(self,input):
        lib_path = "src/tree-sitter/cpp.so"
        LAN = ts.Language(lib_path,"cpp")    
        parser = ts.Parser()
        parser.set_language(LAN)
        code = bytes(input, "utf8")
        tree = parser.parse(code)
        return code,tree
    def getFunctions(self):
        lis = []
        self.traverseCPPFunctions(self.code,self.tree.root_node,lis)
        return lis
    def arrInitParse(self,code,node,knowndimen=False):
        arginfo = {"length":[],"value":None}
        singlearg = False
        if node.type == "argument_list" or node.type == "parameter_list":  
            cnt = 0
            for child in node.children:
                if child.type in ["(",")",","]:
                    continue
                if child.type == "call_expression" or (cnt == 1 and child.type == "parameter_declaration" and 'vector' in getToken(code,child)):
                    if child.type == "call_expression":
                        argnode = getNthChild(child,1)
                    else:
                        argnode = getNthChild(getNthChild(child,1),0)
                    subinfo = self.arrInitParse(code,argnode)
                    #subinfo["caller"] = caller
                    arginfo["length"].extend(subinfo["length"])
                    arginfo["value"] = subinfo["value"]
                else:   
                    if cnt == 0:
                        arginfo["length"] = [getToken(code,child)] + arginfo["length"]
                        singlearg = True
                    elif cnt == 1:
                        arginfo["value"] = getToken(code,child)
                        singlearg = False
                    else:
                        arginfo["unknown"+str(cnt)] = getToken(code,child)
                cnt += 1
            if singlearg and not (arginfo == None):
                #arginfo["value"] = "default"
                arginfo["value"] = "0"
        elif node.type == "new_expression":
            dimen = getToken(code,getNthChild(getNthChild(node,2),1))
            arginfo["length"] = [dimen] + arginfo["length"] 
            if not(getNthChild(node,3) == None):
                # and getToken(code,getNthChild(node,3)) == "()"
                #arginfo["value"] = "default"
                arginfo["value"] = "0"
        elif node.type == "call_expression":
            if 'c_str' in getToken(code,node):
                arginfo["value"] = "Other"
        elif node.type == "initializer_list":
            if not knowndimen:
                cnt = 1
                otherflg = False
                for child in node.children:
                    if child.type == ",":
                        cnt += 1
                    elif child.type in ["{","}"]:
                        continue
                arginfo["length"] = [str(cnt)] + arginfo["length"]
            initlisstr = removeBlank(getToken(code,node)).replace('{','').replace('}','')
            if ',' not in initlisstr and ('0' in initlisstr or 'false' in initlisstr):
                arginfo["value"] = '0'
            else:
                arginfo["value"] = "Other"
        elif node.type == "assignment_expression":
            idlis = []
            lvnode = getNthChild(node,0)
            findTokenWithType(code,lvnode,idlis,"identifier")
            if idlis == 0:
                return None
            lv = idlis[0]
            rvnode = getNthChild(node,2)
            if rvnode.type == "new_expression":
                dimen = getToken(code,lvnode).count('[')
                info = self.arrInitParse(code,rvnode)
                info["def"] = node
                return (dimen,lv,info)
            else:
                return None
        else:
            arginfo = {}
            Logger.debug("unknown arr init approach")
        return arginfo
    def parseMemCall(self,code,node):
        cnt = 0
        argnode = getNthChild(node,1)
        id,v,sz = None,None,None
        for child in argnode.children:
            if child.type in ["(",",",")"]:
                continue
            if cnt == 0:
                id = getToken(code,child)
            elif cnt == 1:
                v = getToken(code,child)
            elif cnt == 2:
                sz = getToken(code,child)
            cnt += 1
        return id,v,sz

    def varParse(self,code,node):
        firstnode = getNthChild(node,0)
        varlis = []
        if firstnode.type == "type_qualifier":
            type1 = getToken(code,firstnode) + " "+ getToken(code,getNthChild(node,1))
            nxtindex = 1
        else:
            type1 = getToken(code,firstnode) 
            nxtindex = 0
        nxtnode = getNthChild(node,nxtindex)
        while not nxtnode == None:
            if nxtnode.type == ";":
                break
            nxtindex += 1
            namenode = getNthChild(node,nxtindex)
            initnode = None
            defnode = namenode
            if namenode.type == "init_declarator" or namenode.type == "function_declarator":
                if namenode.type == "init_declarator":
                    
                    initnode = getNthChild(namenode,1)
                    if initnode.type == "=":
                        initnode = getNthChild(namenode,2)
                elif namenode.type == "function_declarator":
                    initnode = getNthChild(namenode,1)
                namenode = getNthChild(namenode,0)
            
            namelis = []
            findTokenWithType(code,namenode,namelis,"identifier")
            id = namelis[0]
            tp2 = removeBlank(getToken(code,namenode).replace(id,""))
            tp = removeBlank(type1 + tp2)
            initinfo = {}
            if checkCArray(tp):
                #Logger.debug(id,tp)
                initinfo = {"length":[],"value":None}
                ele = None
                if "[" in tp:
                    tp,ele = parseCArray(tp)
                    if not (ele == None) and len(ele) > 0:
                        initinfo["length"] = ele
                if not(initnode == None):
                    if initnode.type == "new_expression" and '*' not in tp:
                        initinfo = {"length":[],"value":None}
                    else:
                        if not (ele == None):
                            if len(ele) > 0:
                                subinfo = self.arrInitParse(code,initnode,knowndimen=True)
                                initinfo["value"] = subinfo["value"]
                            else:
                                initinfo = self.arrInitParse(code,initnode)
                        else:
                            initinfo = self.arrInitParse(code,initnode)
                initinfo["def"] = defnode
            varlis.append((tp,id,initinfo)) 
            nxtindex += 1
            nxtnode = getNthChild(node,nxtindex)
        return varlis
    def findCPPLocal(self,code,node,varlis,memlis):
        if node == None:
            return
        if node.type == "declaration":
            varlis.extend(self.varParse(code,node))
        elif node.type == "assignment_expression":
            arrinitinfo = self.arrInitParse(code,node)
            if not(arrinitinfo == None):
                varlis.append((arrinitinfo[0],arrinitinfo[1],arrinitinfo[2]))
        elif node.type == "call_expression":
            funcname = getToken(code,getNthChild(node,0))
            argnode = getNthChild(node,1)
            #if funcname in ["memset","std::fill","fill","strcpy"]:
            if funcname in ["strcpy"]:
                memlis.append(getToken(code,getNthChild(argnode,1)))
            elif funcname in ["copy","std::copy","Arrays.copyOfRange"]:
                memlis.append(getToken(code,getNthChild(argnode,5)))
        for child in node.children:
            self.findCPPLocal(code,child,varlis,memlis)        

    def sumupArrInit(self,vartypelis):
        #('int**', 'T', {'length': 'c + 1'}),  (1, 'T', {'length': 'n + 1'})
        deflist = []
        dupmap = {}
        for info in vartypelis:
            name = info[1]
            if name in dupmap:
                if info not in dupmap[name]:
                    dupmap[name].append(info)
            else:
                dupmap[name] = [info]
        newvartypelis = []
        for _,infos in dupmap.items():
            if len(infos) == 1:
                newvartypelis.append(infos[0])
            else:
                base = None
                arrinitinfo = {}
                subs = []
                for info in infos:
                    if type(info[0]) == str:
                        base = info
                    else:
                        subs.append(info)
                if not(base == None):
                    subs.sort()
                    initinfo = base[2]
                    flg = True
                    for i in range(0,len(subs) - 1):
                        if subs[i][0] == subs[i+1][0]:
                            flg = False
                    if not flg:
                        initinfo = {"length":[],"value":None}
                    else:
                        for _,_,sub in subs:
                            initinfo["length"].extend(sub["length"])
                            if type(initinfo["def"]) != list:
                                initinfo["def"] = [initinfo["def"]]
                                initinfo["def"].append(sub.get("def"))
                            else:
                                initinfo["def"].append(sub.get("def"))
                            if initinfo["value"] == None and not (sub["value"] == None):
                                initinfo["value"] = sub["value"]  
                    newvartypelis.append((base[0],base[1],initinfo))
                    '''lastsub = initinfo

                    for sub in subs:
                        lastsub["value"] = {"length":sub[2]["length"]}
                        lastsub = lastsub["value"]
                    if len(subs) > 0 and "value" in subs[-1][2]:
                        lastsub["value"] = subs[-1][2]["value"]
                    newvartypelis.append((base[0],base[1],initinfo))'''
        newvartypelis_,initvaluelis = [],[]
        for tp,name,info in newvartypelis:
            #Logger.debug(tp,name,info)
            if type(tp) != str:
                continue
            if info == {}:
                newvartypelis_.append((tp,name,[]))
            else:
                newvartypelis_.append((tp,name,info.get("length")))
                initvaluelis.append((tp,name,info.get("value")))                  
                deflist.append((tp,name,info.get("def")))
        return newvartypelis_,initvaluelis,deflist
    def updateMemInit(self,vinit1,vinit2):
        newvinit = []
        for tp,name,v in vinit1:
            if name in vinit2:
                newvinit.append((tp,name,"initcall"))
            else:
                newvinit.append((tp,name,v))
        return newvinit    
    def parseFuncArg(self,code,child2):
        funcname = getToken(code,getNthChild(child2,0))
        pmtlis = getNthChild(child2,1)
        formaltypelis = []
        for child3 in pmtlis.children:
            if child3.type == "parameter_declaration":
                '''tp = ""
                name = ""
                for child4 in child3.children:
                    if child4.type != "identifier":
                        tp += (getToken(code,child4) + " ")
                    else:
                        name = getToken(code,child4)
                tp = tp[:-1]'''
                for tp,name,_ in self.varParse(code,child3):
                    formaltypelis.append((tp,name))
        return funcname,formaltypelis
    def traverseCPPFunctions(self,code,node,funclis):
        for child in node.children:
            if child.type == "function_definition" or child.type == "method_declaration":
                cnt = 0
                for child2 in child.children:
                    cnt += 1
                    if cnt == 1:
                        rettype = getToken(code,child2)
                    elif child2.type == "compound_statement":
                        locallis1 = []
                        memlis = []
                        self.findCPPLocal(code,child2,locallis1,memlis)
                        locallis2 = []
                        for local in locallis1:
                            if local[1] != "":
                                locallis2.append(local)
                    elif child2.type == "pointer_declarator":
                        rettype += getToken(code,getNthChild(child2,0))
                        funcname,formaltypelis = self.parseFuncArg(code,getNthChild(child2,1))
                    elif child2.type == "function_declarator":
                        funcname,formaltypelis = self.parseFuncArg(code,child2)
                locallis2,arrvalueinitlis,arrdeflis = self.sumupArrInit(locallis2)
                arrvalueinitlis = self.updateMemInit(arrvalueinitlis,memlis)
                if funcname != "main":
                    #funclis.append((rettype,formaltypelis,locallis2))
                    funclis.append((rettype,formaltypelis,locallis2,child.start_byte,child.end_byte,arrvalueinitlis,arrdeflis,funcname))

            self.traverseCPPFunctions(code,child,funclis)
