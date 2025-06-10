from common.util import getToken,removeBlank,blankPattern,dumpAST,Logger
import re
import copy
def getNthChild(node,n):
    cnt = 0
    for child in node.children:
        if cnt == n:
            return child
        cnt += 1
    return None
def traverseArrInit(code,defnode,arrname,lenginfo,cfg,cft,defaultvalue=None):
    curcfgnode,nextcfgnode = None,None
    parnode,defstmtnode = defnode,None
    arrinitvalue = defaultvalue
    while not(parnode == None):
        if parnode.parent.type == "block" or parnode.parent.type == "compound_statement":
            defstmtnode = parnode
            break
        parnode = parnode.parent
    if parnode == None:
        return arrinitvalue
    '''for i in range(len(cfg.nodelist)):
        Logger.debug(cfg.nodelist[i])'''
    for i in range(len(cfg.nodelist)):
        c = cfg.nodelist[i]
        if defstmtnode.start_byte >= c['start'] and defstmtnode.end_byte <= c['end']:
            curcfgnode = c
            if i != len(cfg.nodelist) - 1:
                nextcfgnode = cfg.nodelist[i+1]
                if 'defomit' in nextcfgnode and nextcfgnode['defomit'] == 'new':
                    maxindex = max(nextcfgnode['allcontent'])
                    if maxindex < len(cfg.nodelist):
                        nextcfgnode = cfg.nodelist[maxindex]
            break
    if curcfgnode == None:
        return arrinitvalue
    if nextcfgnode != None and nextcfgnode['type'] == 'for_init' and 'defomit' in nextcfgnode:
        if 'literal' in nextcfgnode['defomit']:
            literalinfo = nextcfgnode['defomit'].split('literal_')[1].split('_')
            initarr,value,initlength = literalinfo[0],literalinfo[-1],literalinfo[1:-1]
            if initarr == arrname and (initlength == lenginfo or initlength == [arrname+".length"]):
                arrinitvalue = value
                for c in cft:
                    if 'defomit' in c and c['defomit'] == nextcfgnode['defomit']:
                        c['defomit'] = 'literal'
                        break
                return arrinitvalue
        elif 'initcall' in nextcfgnode['defomit']:
            literalinfo = nextcfgnode['defomit'].split('initcall_')[1].split('_')
            initarr,value = literalinfo[0].split('[')[0],literalinfo[1]
            if initarr == arrname:
                arrinitvalue = value
                for c in cft:
                    if 'defomit' in c and c['defomit'] == nextcfgnode['defomit']:
                        c['defomit'] = 'literal'
                        break
                return arrinitvalue
    nextnode = defstmtnode.next_sibling
    while not(nextnode == None) and nextnode.end_byte <= curcfgnode['end']:
        #dumpAST(code,nextnode)
        stmtstr = removeBlank(getToken(code,nextnode))
        if 'Arrays.fill' in stmtstr: #java fill
            argnode = getNthChild(getNthChild(nextnode,0),3)
            fillarr = getToken(code,getNthChild(argnode,2*1-1))
            value = getToken(code,getNthChild(argnode,2*2-1))
            if arrname in fillarr:
                return value
        elif "memset" in stmtstr:
            argnode = getNthChild(getNthChild(nextnode,0),1)
            fillarr = getToken(code,getNthChild(argnode,2*1-1))
            value = getToken(code,getNthChild(argnode,2*2-1))
            if arrname in fillarr:
                return value                           
        elif "fill" in stmtstr: # c fill
            argnode = getNthChild(getNthChild(nextnode,0),1)
            fillarr = getToken(code,getNthChild(argnode,2*1-1))
            value = getToken(code,getNthChild(argnode,2*3-1))
            if arrname in fillarr:
                return value
        nextnode = nextnode.next_sibling
    return arrinitvalue
    
def traverseDiv(code,node,divinfo):
    if node.type == "binary_expression" or node.type == "augmented_assignment" or node.type == "binary_operator":
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
        op = getToken(code,op)
        if op == "/" or op == "/=":
            divinfo.append((removeBlank(getToken(code,lnode)),removeBlank(getToken(code,rnode))))
    for child in node.children:
        traverseDiv(code,child,divinfo)
def traverseCast(code,node,lis):
    if node.type == "cast_expression":
        cflg = False
        for child in node.children:
            if child.type == ")":
                cflg = True
            elif cflg:             
                caste = getToken(code,child)
                lis.append(removeBlank(caste))
    for child in node.children:
        traverseCast(code,child,lis)
def traverseBanNode(node,bannodetypes,lis=None):
    if node.type in bannodetypes:
        if lis != None:
            lis.append(node)
        return True
    for child in node.children:
        if traverseBanNode(child,bannodetypes,lis):
            return True
    return False
def unfoldParenthe(node):
    if node.type == "parenthesized_expression" or node.type == "condition_clause":
        child = getNthChild(node,1)
        return unfoldParenthe(child)
    else:
        return node
def unfoldCompound(node):
    if node.type == "compound_statement":
        child = getNthChild(node,1)
        return unfoldCompound(child)
    else:
        return node
def getChildNum(node):
    cnt = 0
    for c in node.children:
        cnt += 1
    return cnt
def findError(node):
    if node.type == "ERROR":
        return True
    for child in node.children:
        childflg = findError(child)
        if childflg:
            return True
    return False
def findAssignment(code,node,lis):
    if node == None:
        return
    if node.type == "assignment":
        #dumpAST(code,node)
        name = getToken(code,node)         
        lis.append((name,node.start_byte))
    for child in node.children:
        findAssignment(code,child,lis)
def findImport(code,node,importlis):
    if node == None:
        return
    if node.type == "import_from_statement" or node.type == "import_statement":
        #dumpAST(code,node)
        name = getToken(code,node)         
        importlis.append(name)
    for child in node.children:
        findImport(code,child,importlis)
def findCall(code,node,funcname,calllis):
    #Logger.debug(node.type)
    if node == None:
        return
    if node.type == "call" or node.type == "method_invocation":
        #dumpAST(code,node)
        callnode = None
        for child2 in node.children:
            if child2.type == "attribute":
                node = child2
            break
        for child2 in node.children:
            if child2.type == "identifier":
                name = getToken(code,child2)
                #Logger.debug(name)
                if name == funcname:
                    calllis.append(child2)
                    break
    for child in node.children:
        '''elif child.type == "class_definition" and "class!" not in lis:
            lis.append("class!")'''
        findCall(code,child,funcname,calllis)
def getSeqLoopVar(code,node):
    n = getNthChild(node,5)
    c = getNthChild(node,3)
    v,bound = None,None
    if not(n == None):
        updtoken = removeBlank(getToken(code,n))
        pats = [r'([a-zA-Z_]\w*)=\1\+1',r'([a-zA-Z_]\w*)\+\+',r'\+\+([a-zA-Z_]\w*)']
        for p in pats:
            m = re.match(p,updtoken)
            if m != None:
                v = m[1]
                break
    if v != None:
        condstr = removeBlank(getToken(code,c))
        if v + '<' in condstr:
            bound = condstr.replace(v+'<','')
    return v,bound

def checkArrayInitInLoop(code,node,mode=0,loopvs=None):
    if loopvs == None:
        loopvs = []
    #loopstmts = ["for_statement","while_statement","do_statement","for_range_loop"]
    loopstmts = ["for_statement","for_range_loop"]
    key = ""
    if node.type in loopstmts:
        loopv,bound = getSeqLoopVar(code,node)
        if node.type != "for_range_loop" and (loopv == None or bound == None):
            return False,key
        loopvs.append((loopv,bound))            
        blockflg = False
        for child in node.children:
            if child.type == ")":
                blockflg = True
            elif blockflg:
                targetstmt = []
                if child.type == "compound_statement" or child.type == "block":
                    for cchild in child.children:
                        if cchild.type not in ["{","}"]:
                            targetstmt.append(cchild)
                else:
                    targetstmt = [child]
                stmtflg = False
                for stmt in targetstmt:
                    if stmt.type in loopstmts:
                        stmtflg,subkey = checkArrayInitInLoop(code,stmt,loopvs=loopvs)
                        key += "_" + subkey
                    else:
                        if stmt.type == "expression_statement":
                            stmt = getNthChild(stmt,0)
                            if stmt.type == "assignment_expression":
                                stmtcode = getToken(code,stmt)
                                stmtsplit = stmtcode.split("=")
                                if len(stmtsplit) == 2:
                                    if '[' in stmtsplit[0]:
                                        if 'new' in stmtsplit[1]:
                                            stmtflg = True
                                            key += "_new"
                                        elif "literal" in getNthChild(stmt,2).type or (getNthChild(stmt,2).type == 'unary_expression' and 'literal' in getNthChild(getNthChild(stmt,2),1).type):
                                            lv = stmtsplit[0]
                                            if lv.count('[') == lv.count(']'):
                                                lvsp = removeBlank(lv).replace(']','').split('[')
                                                indexs = lvsp[1:]
                                                arrn = lvsp[0]
                                                loopvars = [v[0] for v in loopvs]
                                                bounds = [v[1] for v in loopvs]
                                                if indexs == loopvars:
                                                    stmtflg = True
                                                    key += "_literal_"+ arrn + "_"+"_".join(bounds)+"_"+removeBlank(stmtsplit[1])
                            elif stmt.type == "delete_expression":
                                stmtflg = True
                                key += "_delete"
                            #elif mode == 1 and stmt.type == "call_expression":
                            elif stmt.type == "call_expression":
                                callname = getToken(code,getNthChild(stmt,0))
                                argnode = getNthChild(stmt,1)
                                if callname == "memset":
                                    arrname = getToken(code,getNthChild(argnode,2*1-1))
                                    literal = getToken(code,getNthChild(argnode,2*2-1))
                                    stmtflg = True
                                    key += f"_initcall_{arrname}_{literal}"                           
                                elif "fill" in callname:
                                    arrname = getToken(code,getNthChild(argnode,2*1-1))
                                    literal = getToken(code,getNthChild(argnode,2*3-1))
                                    stmtflg = True
                                    key += f"_initcall_{arrname}_{literal}"
                    if not stmtflg:
                        return False,""
                    elif key[0] == "_":
                        key = key[1:]
                return True,key
    return False,key            
                
def findTokenWithType(code,node,lis,tp):
    if node == None or len(lis) > 0:
        return
    if type(tp) == type(""):
        if node.type == tp:
            #dumpAST(code,node)
            name = getToken(code,node)         
            lis.append(name)
    elif type(tp) == type([]):
        if node.type in tp:
            name = getToken(code,node)         
            lis.append(name)
    for child in node.children:
        findTokenWithType(code,child,lis,tp)
        if len(lis) > 0:
            break
def parseJavaVarDecl(code,node,tp,lis):
    namelis = []
    dmlis = []
    arrinitarg = []
    declstr = getToken(code,node)
    findTokenWithType(code,node,namelis,"identifier")
    findTokenWithType(code,node,dmlis,"dimensions")
    if len(namelis) != 0:
        name = namelis[0]
    else:
        name = ""      
    #Logger.debug(tp)  
    if len(dmlis) != 0:
        tp += (" " + dmlis[0])
    if tp.find("[") != -1:
        declasssp = declstr.split("=")
        
        if len(declasssp) == 2:
            rv = declasssp[1]
            if rv.find("toCharArray") != -1:
                arrinitarg.append('nan')
            elif rv.find("new") != -1:
                arg = ""
                argflg = False
                for c in rv:
                    if c == "[":
                        argflg = True
                    elif c == "]":
                        argflg = False
                        arrinitarg.append(arg)
                        arg = ""
                    if argflg and c not in ["]","["]:
                        arg += c
            elif rv.find('{') != -1:#REMAINDER_7_LARGE_NUMBERS
                arrinitarg.append(str(-(rv.count(',')+1)))
    #Logger.debug(arrinitarg)
    lis.append((tp,name,arrinitarg,node))
def findJavaLocalVar(code,node,lis):
    if node == None:
        return
    if node.type == "local_variable_declaration":
        declstr = getToken(code,node)
        #dumpAST(code,node)
        cnt = 0
        spflg = False
        for child in node.children:
            cnt += 1
            if cnt == 1:
                tp = getToken(code,child)
            elif child.type == "variable_declarator":
                parseJavaVarDecl(code,child,tp,lis)
    for child in node.children:
        findJavaLocalVar(code,child,lis)

def copyKeyStmt(keystmt):
    if 'node' in keystmt:
        nd = keystmt['node']
        del keystmt['node']
        newkeystmt = copy.deepcopy(keystmt)
        newkeystmt['node'] = nd
    else:
        newkeystmt = copy.deepcopy(keystmt)
    return newkeystmt
def CDefUseTvs(code,node,cfg,flg,info,keystmt):
    if node.type == "using_declaration":
        return
    elif node.type == "function_declarator":
        for child in node.children:
            if child.type == "parameter_list":
                CDefUseTvs(code,child,cfg,'D',info,keystmt)
    elif node.type == "function_definition":
        for child in node.children:
            if child.type == "function_declarator":
                CDefUseTvs(code,child,cfg,'D',info,keystmt)
            elif child.type == "compound_statement":
                CDefUseTvs(code,child,cfg,'U',info,keystmt)
            elif child.type == "pointer_declarator":
                CDefUseTvs(code,getNthChild(child,1),cfg,'D',info,keystmt)
    elif node.type == "declaration":
        for child in node.children:
            if child.type == "function_declarator":
                for child2 in child.children:
                    CDefUseTvs(code,child2,cfg,'D',info,keystmt)
            else:
                CDefUseTvs(code,child,cfg,'D',info,keystmt)
        rv,lv = arrayCopy(getToken(code,node))
        if lv != None and rv != None:
            cfg.appendDefUse((lv,'RD'),node.start_byte,node.end_byte,{'lv':lv,'rv':rv,"op":"="})
    elif node.type == "init_declarator":
        cnt = 0
        assflg = False
        lv,rv = "",""
        rvchild = None
        ind = 1
        defs = []
        for child in node.children:
            if child.type == "=":
                assflg = True
            elif not assflg:
                lv = getToken(code,child)
            else:
                rvchild = child
                rv = getToken(code,child)
        defchild = None
        for child in node.children:
            if cnt == 0:
                defchild = child              
            else:
                CDefUseTvs(code,child,cfg,'U',info,keystmt)
            cnt += 1
        if assflg:
            if rv.find("/") != -1:
                CDefUseTvs(code,defchild,cfg,'D',info,{"lv":lv,"rv":rv,"node":rvchild,"op":"="})
            else:
                CDefUseTvs(code,defchild,cfg,'D',info,{"lv":lv,"rv":rv,"op":"="})
        else:
            CDefUseTvs(code,defchild,cfg,'D',info,keystmt)
    elif node.type == "cast_expression":
        cflg = False
        #Logger.debug(keystmt)
        for child in node.children:
            if child.type == ")":
                cflg = True
            elif cflg:
                newkeystmt = copyKeyStmt(keystmt)
                newkeystmt['cast'] = getToken(code,child)
                if child.type.find("literal") != -1:
                    cfg.appendDefUse(("LITERALNUMBER",'U'),child.start_byte,child.end_byte,newkeystmt)
                CDefUseTvs(code,child,cfg,flg,info,newkeystmt)
    elif node.type == "update_expression":
        #starchat COUNT_WAYS_BUILD_STREET_GIVEN_CONSTRAINTS longcomp
        cnt = 0
        for child in node.children:
            if cnt == 0:
                lv = getToken(code,child)
            elif cnt == 1:
                op = getToken(code,child)
            cnt += 1
        if lv == "++" or lv == "--":
            tmp = lv
            lv = op
            op = tmp
        if op == "++":
            rv = lv + " + 1"
        elif op == "--":
            rv = lv + " - 1"
        for child in node.children:
            CDefUseTvs(code,child,cfg,'U',info,{})
        for child in node.children:
            CDefUseTvs(code,child,cfg,'RD',info,{'lv':lv,'rv':rv,'op':op})
        #cfg.appendDefUse((lv,'U'),node.start_byte,node.end_byte,{})
        #cfg.appendDefUse((lv,'RD'),node.start_byte,node.end_byte,{'lv':lv,'rv':rv,'op':op})
    elif node.type == "assignment_expression":
        cnt = 0
        assflg = False
        lv,rv = "",""
        rvchild = None
        for child in node.children:
            if child.type.find("=") != -1:
                assflg = True
                op = getToken(code,child)
            elif not assflg:
                lv = getToken(code,child)
            else:
                rvchild = child
                rv = getToken(code,child)
        defnode = None
        for child in node.children:
            if cnt == 0:
                defnode = child
                #if len(rv) >= 20 and rv.find("/") != -1:
                if op != "=":
                    CDefUseTvs(code,child,cfg,'U',info,keystmt)
                '''if rv.find("/") != -1:
                    CDefUseTvs(code,child,cfg,'RD',info,{"lv":lv,"rv":rv,"node":rvchild,"op":op})
                else:
                    CDefUseTvs(code,child,cfg,'RD',info,{"lv":lv,"rv":rv,"op":op})'''
            else:
                CDefUseTvs(code,child,cfg,'U',info,keystmt)
            cnt += 1
        if rv.find("=") != -1 and rv.find("==") == -1:
            rv = rv.split("=")[-1].strip()
        if rv.find("/") != -1:
            CDefUseTvs(code,defnode,cfg,'RD',info,{"lv":lv,"rv":rv,"node":rvchild,"op":op})
        else:
            CDefUseTvs(code,defnode,cfg,'RD',info,{"lv":lv,"rv":rv,"op":op})
    elif node.type == "subscript_expression":
        if flg in ["D","RD"]:
            cnt = 0
            for child in node.children:
                if cnt == 0:
                    CDefUseTvs(code,child,cfg,'RD',info,keystmt)
                else:
                    CDefUseTvs(code,child,cfg,'U',info,keystmt)
                cnt += 1
        else:
            if "expr" not in keystmt:
                newkeystmt = copyKeyStmt(keystmt)
                newkeystmt["expr"] = getToken(code,node)
                keystmt = newkeystmt
            for child in node.children:
                CDefUseTvs(code,child,cfg,'U',info,keystmt)
    elif node.type == "call_expression":
        funcnode = None
        argnode = None
        cnt = 0
        #Logger.debug(getToken(code,node))
        rv,lv = arrayCopy(getToken(code,node))
        if lv != None and rv != None:
            cfg.appendDefUse((lv,'RD'),node.start_byte,node.end_byte,{'lv':lv,'rv':rv,"op":"="})
        for child in node.children:
            if cnt == 0:
                funcnode = child
            elif cnt == 1:
                argnode = child
            cnt += 1
        functoken = getToken(code,funcnode)
        if not('memset' in functoken or 'fill' in functoken):
            if funcnode.type == "field_expression":
                CDefUseTvs(code,getNthChild(funcnode,0),cfg,'U',info,keystmt)
            for child in argnode.children:
                CDefUseTvs(code,child,cfg,'U',info,keystmt)

    elif node.type == "for_range_loop":
        splitflg = False
        cnt = 0
        for child in node.children:
            if child.type == ":":
                splitflg = True
            elif child.type in ["(","for",")"]:
                continue
            elif not splitflg:
                if cnt != 0:
                    CDefUseTvs(code,child,cfg,'D',info,keystmt)
                else:
                    CDefUseTvs(code,child,cfg,'U',info,keystmt)
            elif splitflg:
                CDefUseTvs(code,child,cfg,'U',info,keystmt)
            cnt += 1
    elif node.type == "return_statement":
        for child in node.children:
            if child.type == "return":
                continue
            returnexpr = getToken(code,child)
            if len(returnexpr) >= 12 and returnexpr.find("/") != -1:
                CDefUseTvs(code,child,cfg,'U',info,{"returnstmt":getToken(code,node),"node":child})
            else:
                CDefUseTvs(code,child,cfg,'U',info,{"returnstmt":getToken(code,node)})
    elif node.type == "identifier":
        name = getToken(code,node)
        cfg.appendDefUse((name,flg),node.start_byte,node.end_byte,keystmt)
    else:
        for child in node.children:
            CDefUseTvs(code,child,cfg,flg,info,keystmt)

def arrayCopy(exp,lv=None):
    patterns = [
        r"Arrays\s*\.\s*copyOfRange\s*\((?P<rv>.+)\s*,\s*.+\s*,\s*.+\)",
        r"(?P<rv>.+)\s*\.\s*toCharArray",
        r"(std::)?copy\s*\(\s*(?P<rv>.+)\s*,\s*.+\s*,\s*(?P<lv>.+)\s*\)",
        r"vector\s*<.+>\s*(?P<lv>[a-zA-Z_][a-zA-Z0-9_]*)\s*\(\s*(?P<rv>[a-zA-Z_][a-zA-Z0-9_]*)\s*,\s*[a-zA-Z_][a-zA-Z0-9_]*\s*\+.+\)" 
    ]
    newrv,newlv = None,None
    for p in patterns:
        m = re.search(p,exp)
        if m:
            newrv = m.groupdict().get('rv')
            newlv = m.groupdict().get('lv')
    if newrv == None:
        return exp,lv
    else:
        if lv != None:
            if lv == newrv:
                return exp,lv
            else:
                return f"{newrv}.@copy()",lv
        else:
            return f"{newrv}.@copy()",newlv 
def jvDefUseTvs(code,node,cfg,flg,info,keystmt):
    if node.type == "class_declaration":
        for child in node.children:
            if child.type == "class_body":
                jvDefUseTvs(code,child,cfg,'U',info,keystmt)
    elif node.type == "method_declaration":
        for child in node.children:
            if child.type == "formal_parameters":
                jvDefUseTvs(code,child,cfg,'D',info,keystmt)
            elif child.type == "block":
                jvDefUseTvs(code,child,cfg,'U',info,keystmt)
    elif node.type == "variable_declarator":
        cnt = 0
        assflg = False
        lv,rv = "",""
        rvchild = None
        for child in node.children:
            if child.type == "=":
                assflg = True
            elif not assflg:
                lv = getToken(code,child)
            else:
                rvchild = child
                rv = getToken(code,child)
        rv,lv = arrayCopy(rv,lv=lv)
        defchild = None
        for child in node.children:
            if cnt == 0:
                defchild = child
                '''if assflg:
                
                #if len(rv) >= 20 and rv.find("/") != -1:
                    if rv.find("/") != -1:
                        jvDefUseTvs(code,child,cfg,'D',info,{"lv":lv,"rv":rv,"node":rvchild,"op":"="})
                    else:
                        jvDefUseTvs(code,child,cfg,'D',info,{"lv":lv,"rv":rv,"op":"="})
                else:
                    jvDefUseTvs(code,child,cfg,'D',info,keystmt)'''
                    
            else:
                jvDefUseTvs(code,child,cfg,'U',info,keystmt)
            cnt += 1
        if assflg:
            if rv.find("/") != -1:
                jvDefUseTvs(code,defchild,cfg,'D',info,{"lv":lv,"rv":rv,"node":rvchild,"op":"="})
            else:
                jvDefUseTvs(code,defchild,cfg,'D',info,{"lv":lv,"rv":rv,"op":"="})
        else:
            jvDefUseTvs(code,defchild,cfg,'D',info,keystmt)
    elif node.type == "cast_expression":
        cflg = False
        #Logger.debug(keystmt)
        for child in node.children:
            if child.type == ")":
                cflg = True
            elif cflg:
                newkeystmt = copyKeyStmt(keystmt)
                newkeystmt['cast'] = getToken(code,child)
                if child.type.find("literal") != -1:
                    cfg.appendDefUse(("LITERALNUMBER",'U'),child.start_byte,child.end_byte,newkeystmt)
                jvDefUseTvs(code,child,cfg,flg,info,newkeystmt)
    elif node.type == "update_expression":
        #starchat COUNT_WAYS_BUILD_STREET_GIVEN_CONSTRAINTS longcomp
        cnt = 0
        for child in node.children:
            if cnt == 0:
                lv = getToken(code,child)
            elif cnt == 1:
                op = getToken(code,child)
            cnt += 1
        if lv == "++" or lv == "--":
            tmp = lv
            lv = op
            op = tmp
        if op == "++":
            rv = lv + " + 1"
        elif op == "--":
            rv = lv + " - 1"
        cfg.appendDefUse((lv,'U'),node.start_byte,node.end_byte,{})
        cfg.appendDefUse((lv,'RD'),node.start_byte,node.end_byte,{'lv':lv,'rv':rv,'op':op})
    elif node.type == "assignment_expression":
        cnt = 0
        assflg = False
        lv,rv = "",""
        rvchild = None
        for child in node.children:
            if child.type.find("=") != -1:
                assflg = True
                op = getToken(code,child)
            elif not assflg:
                lv = getToken(code,child)
            else:
                rvchild = child
                rv = getToken(code,child)
        defnode = None
        for child in node.children:
            if cnt == 0:
                defnode = child
                #if len(rv) >= 20 and rv.find("/") != -1:
                if op != "=":
                    jvDefUseTvs(code,child,cfg,'U',info,keystmt)
                '''if rv.find("/") != -1:
                    jvDefUseTvs(code,child,cfg,'RD',info,{"lv":lv,"rv":rv,"node":rvchild,"op":op})
                else:
                    jvDefUseTvs(code,child,cfg,'RD',info,{"lv":lv,"rv":rv,"op":op})'''
            else:
                jvDefUseTvs(code,child,cfg,'U',info,keystmt)
            cnt += 1
        if rv.find("=") != -1 and rv.find("==") == -1:
            rv = rv.split("=")[-1].strip()
        rv,lv = arrayCopy(rv,lv=lv)
        if rv.find("/") != -1:
            jvDefUseTvs(code,defnode,cfg,'RD',info,{"lv":lv,"rv":rv,"node":rvchild,"op":op})
        else:
            jvDefUseTvs(code,defnode,cfg,'RD',info,{"lv":lv,"rv":rv,"op":op})
    elif node.type == "array_access":
        if flg in ["D","RD"]:
            cnt = 0
            for child in node.children:
                if cnt == 0:
                    jvDefUseTvs(code,child,cfg,'RD',info,keystmt)
                else:
                    jvDefUseTvs(code,child,cfg,'U',info,keystmt)
                cnt += 1
        else:
            if "expr" not in keystmt:
                newkeystmt = copyKeyStmt(keystmt)
                newkeystmt["expr"] = getToken(code,node)
                keystmt = newkeystmt
            for child in node.children:
                jvDefUseTvs(code,child,cfg,'U',info,keystmt)
    elif node.type == "method_invocation":
        #"caller":caller,"func":func,"arg":arg
        attrflg = False
        arg = ""
        funcflg = False
        func = ""
        if not ".fill" in removeBlank(getToken(code,node)):
            for child in node.children:
                if child.type == ".":
                    attrflg = True
                    funcflg = True
                elif child.type == "argument_list":
                    jvDefUseTvs(code,child,cfg,'U',info,keystmt)
                elif funcflg:
                    funcflg = False
                    func = getToken(code,child)
                    arg = getToken(code,child)
            for child in node.children:
                if attrflg:
                    #jvDefUseTvs(code,child,cfg,'U',info,{"caller":getToken(code,child),"func":func,"arg":arg})
                    jvDefUseTvs(code,child,cfg,'U',info,keystmt)
                    break
                else:
                    break
    elif node.type == "enhanced_for_statement":
        splitflg = False
        cnt = 0
        for child in node.children:
            if child.type == ":":
                splitflg = True
            elif child.type in ["(","for",")"]:
                continue
            elif not splitflg:
                if cnt != 0:
                    jvDefUseTvs(code,child,cfg,'D',info,keystmt)
                else:
                    jvDefUseTvs(code,child,cfg,'U',info,keystmt)
            elif splitflg:
                jvDefUseTvs(code,child,cfg,'U',info,keystmt)
            cnt += 1
    elif node.type == "return_statement":
        for child in node.children:
            if child.type == "return":
                continue
            returnexpr = getToken(code,child)
            if len(returnexpr) >= 12 and returnexpr.find("/") != -1:
                jvDefUseTvs(code,child,cfg,'U',info,{"returnstmt":getToken(code,node),"node":child})
            else:
                jvDefUseTvs(code,child,cfg,'U',info,{"returnstmt":getToken(code,node)})
    elif node.type == "identifier":
        name = getToken(code,node)
        cfg.appendDefUse((name,flg),node.start_byte,node.end_byte,keystmt)
    else:
        for child in node.children:
            jvDefUseTvs(code,child,cfg,flg,info,keystmt)               

def parseList_Str(code,node):
    lis = []
    for child in node.children:
        if child.type not in [",","(",")","[","]"]:
            lis.append(removeBlank(getToken(code,child)))
    return lis
def parseList_Node(code,node):
    lis = []
    for child in node.children:
        if child.type not in [",","(",")","[","]"]:
            lis.append(child)
    return lis
def parsePyArray(code,node):
    arrinfo = {"length":[],"value":None}
    if node.type == "call":
        funcname = getToken(code,getNthChild(node,0))
        if removeBlank(funcname) == "np.zeros":
            argnode = getNthChild(node,1)
            firstarg = getNthChild(argnode,1)
            if not (firstarg == None) and firstarg.type == "tuple":
                for child in firstarg.children:
                    if child.type not in ['(',',',')']:
                        arrinfo["length"].append(getToken(code,child))
                arrinfo["value"] = "0"
    elif node.type == "list_comprehension":
        vnode = getNthChild(node,1)
        fornode = getNthChild(node,2)
        subinfo = parsePyArray(code,vnode)
        if not(subinfo == None):
            arrinfo["length"] = subinfo["length"]
            arrinfo["value"] = subinfo["value"]
        else:
            arrinfo["value"] = getToken(code,vnode)
        if fornode.type == "for_in_clause":
            rangenode = getNthChild(fornode,3)
            if rangenode.type == "call" and "range" in getToken(code,rangenode):
                rangeargnode = getNthChild(rangenode,1)
                rangearglist = []
                for child in rangeargnode.children:
                    if child.type not in ['(',',',')']:
                        rangearglist.append(getToken(code,child))
                if len(rangearglist) >= 2:
                    if rangearglist[0] == "0":
                        arrinfo["length"] = [rangearglist[1]] + arrinfo["length"]
                    else:
                        arrinfo["length"] = [rangearglist[1] + "-" + rangearglist[0]] + arrinfo["length"]
                elif len(rangearglist) == 1:
                    arrinfo["length"] = [rangearglist[0]] + arrinfo["length"]
    elif node.type == "binary_operator":
        operator = getToken(code,getNthChild(node,1))
        operand1 = getNthChild(node,0)
        operand2 = getNthChild(node,2)
        if operator == "*":
            lengthnode = None
            listnode = None
            if operand1.type in ["list_comprehension","list"]:
                lengthnode,listnode = operand2,operand1
            elif operand2.type in ["list_comprehension","list"]:
                lengthnode,listnode = operand1,operand2
            if not(lengthnode == None):
                subinfo = parsePyArray(code,listnode)
                lengthnode = unfoldParenthe(lengthnode)
                if not(subinfo == None):
                    sublength = subinfo["length"][-1]
                    arrinfo["length"] = subinfo["length"]
                    if sublength == "1":
                        arrinfo["length"][-1] = getToken(code,lengthnode)
                    else:
                        arrinfo["length"][-1] = arrinfo["length"][-1] + "*" + getToken(code,lengthnode)
                    arrinfo["value"] = subinfo["value"]
        elif operator == "+":
            lisinfo1 = parsePyArray(code,operand1)
            lisinfo2 = parsePyArray(code,operand2)
            if not(lisinfo1 == None) and not(lisinfo2 == None):
                arrinfo["length"],arrinfo["value"] = lisinfo1["length"],lisinfo1["value"]
                if len(arrinfo["length"]) > 0 and len(lisinfo2["length"]) > 0:
                    arrinfo["length"][0] =  arrinfo["length"][0] + "+" + lisinfo2["length"][0]
    elif node.type == "list":
        elenode = getNthChild(node,1)
        if elenode.type in ["binary_operator","list_comprehension"]:
            arrinfo = parsePyArray(code,elenode)
            if arrinfo != None:
                arrinfo["length"].append("1")
            else:
                return {"length":["Unknown"],"value":None}
        else:
            liststrs = parseList_Str(code,node)
            arrinfo["length"] = [str(len(liststrs))]
            if arrinfo["length"] == ["0"]:
                return None 
            arrinfo["value"] = removeBlank(getToken(code,elenode))
            if len(liststrs) > 1:
                arrinfo["value"] = "Other"
    if len(arrinfo["length"]) == 0:
        return None
    else:
        return arrinfo
def pyDefUseTvs(code,node,cfg,flg,info,keystmt):
    #Logger.debug(getToken(code,node))
    if node.type == "import_statement":
        aliasimport = None
        for child in node.children:
            if child.type == "aliased_import":
                aliasimport = child
        if aliasimport == None:
            for child in node.children:
                pyDefUseTvs(code,child,cfg,'D',info,keystmt)
        else:
            spflg = False
            for child in aliasimport.children:
                if child.type == "as":
                    spflg = True
                elif spflg:
                    pyDefUseTvs(code,child,cfg,'D',info,keystmt)
                    break
    elif getToken(code,node) == "\'inf\'":
        cfg.appendDefUse(("\'inf\'",flg),node.start_byte,node.end_byte,keystmt)
    elif node.type == "function_definition":
        for child in node.children:
            if child.type == "parameters":
                pyDefUseTvs(code,child,cfg,'D',info,keystmt)
            elif child.type == "block":
                pyDefUseTvs(code,child,cfg,'U',info,keystmt)
    elif node.type == "for_statement":
        flg = 'D'
        defchild = None
        rangeflg = False
        for child in node.children:
            if child.type == "in":
                flg = 'U'
            else:
                if flg == 'D':
                    defchild = child
                elif flg == 'U':
                    if child.type == ":":
                        1
                        '''if rangeflg:
                            pyDefUseTvs(code,defchild,cfg,'U',info,{})
                            pyDefUseTvs(code,defchild,cfg,'D',info,{})'''
                    elif 'range' in getToken(code,child):
                        rangeflg = True
                pyDefUseTvs(code,child,cfg,flg,info,keystmt)
    elif node.type == "for_in_clause":
        flg = 'D'
        for child in node.children:
            if child.type == "in":
                flg = 'U'
            else:
                pyDefUseTvs(code,child,cfg,flg,info,keystmt)
    elif node.type == "augmented_assignment":
        cnt = 0
        for child in node.children:
            if cnt == 0:
                lv = getToken(code,child)
            elif cnt == 1:
                op = getToken(code,child)
            elif cnt == 2:
                rv = getToken(code,child)
            cnt += 1
        cnt = 0
        defchild = None
        for child1 in node.children:
            if cnt == 0:
                defchild = child1
                pyDefUseTvs(code,child1,cfg,'U',info,keystmt)
                
            elif cnt == 2:
                pyDefUseTvs(code,child1,cfg,'U',info,keystmt)
            cnt += 1
        pyDefUseTvs(code,defchild,cfg,'D',info,{"lv":lv,"rv":rv,"op":op})
    elif node.type == "assignment":
        ptflg = False
        assflg = False
        explis = []
        arrinfolis = []
        assflg = False
        rvnode = None
        lv,rv = "",""
        nodelis = []
        for child in node.children:
            if child.type == "=":
                assflg = True
            elif not assflg:
                lv = getToken(code,child)
            else:
                rv = getToken(code,child)
                rvnode = child
                rvarrinfo = parsePyArray(code,child)
        for child1 in node.children:
            if child1.type == "pattern_list":
                ptflg = True
                ptlis = parseList_Str(code,child1)
                #ptlis = [i.split("[")[0] for i in ptlis]
            elif child1.type == "=":
                assflg = True
            elif ptflg and (child1.type == "expression_list" or assflg):
                if child1.type == "expression_list":
                    explis = parseList_Str(code,child1)
                    nodelis = parseList_Node(code,child1)
                    for nd in nodelis:
                        arrinfolis.append(parsePyArray(code,nd))
                elif assflg:
                    explis = [removeBlank(getToken(code,child1))]
        if ptflg and len(ptlis) != len(explis):
            Logger.debug("assignment inagree")
            info.append({"type":"assignment","leftvalue":ptlis,"rightvalue":explis,"start":node.start_byte,"end":node.end_byte})
        cnt = 0
        defchild = None
        for child1 in node.children:
            cnt += 1
            if cnt == 1:
                defchild = child1
            elif cnt == 3:
                pyDefUseTvs(code,child1,cfg,'U',info,keystmt)
        if not(defchild == None):
            if rv.find("=") != -1 and rv.find("==") == -1:
                rv = rv.split("=")[-1].strip()
            if ptflg:
                cnt = 0
                for child1 in node.children:
                    if child1.type == "pattern_list":
                        for child2 in child1.children:
                            if child2.type != ",":
                                if cnt < len(explis):
                                    lv = getToken(code,child2)
                                    newkeystmt = {"lv":lv,"rv":explis[cnt],"op":"="}
                                    if cnt < len(arrinfolis) and not(arrinfolis[cnt] == None):
                                        newkeystmt["arrinfo"] = arrinfolis[cnt]
                                        newkeystmt["node"] = nodelis[cnt]
                                    elif lv in info and cnt < len(nodelis):
                                        newkeystmt["arrinfo"] = {"length":["Unknown"],"value":None}
                                        newkeystmt["node"] = nodelis[cnt]
                                    pyDefUseTvs(code,child2,cfg,'D',info,newkeystmt)
                                    cnt += 1
            else:
                newkeystmt = {"lv":lv,"rv":rv,"op":"="}
                if not(rvarrinfo == None):
                    newkeystmt["arrinfo"] = rvarrinfo
                    newkeystmt["node"] = rvnode
                elif lv in info:
                    newkeystmt["arrinfo"] = {"length":["Unknown"],"value":None}
                    newkeystmt["node"] = rvnode
                pyDefUseTvs(code,defchild,cfg,'D',info,newkeystmt)
    elif node.type == "call":
        func,arg,caller = "","",""
        cnt = 0
        for child in node.children:
            if cnt == 0:
                if child.type == "attribute":
                    attflg = False
                    for child2 in child.children:
                        if child2.type == ".":
                            attflg = True
                        elif not attflg:
                            caller = getToken(code,child2)
                        elif attflg:
                            func = getToken(code,child2)
                else:
                    func = getToken(code,child)
                cnt += 1
            elif child.type == "argument_list":
                arg = getToken(code,child)
        for child in node.children:
            if child.type == "attribute":
                for child2 in child.children:
                    pyDefUseTvs(code,child2,cfg,'U',info,{"caller":caller,"func":func,"arg":arg})
                    break
            if child.type == "argument_list":
                pyDefUseTvs(code,child,cfg,'U',info,keystmt)
    elif node.type == "attribute":
        for child in node.children:
            if child.type == ".":
                break
            pyDefUseTvs(code,child,cfg,'U',info,keystmt)
    elif node.type == "return_statement":
        for child in node.children:
            if getToken(code,child) == "return":
                continue
            #Logger.debug(getToken(code,node))
            pyDefUseTvs(code,child,cfg,'U',info,{"returnstmt":getToken(code,node)})
    elif node.type == "subscript":
        splitflg = False
        
        dnodes = []
        unodes = []
        for child in node.children:
            if child.type == "[":
                splitflg = True
            elif not splitflg:
                if flg == "D":
                    dnodes.append(child)
                else:
                    unodes.append(child)           
            elif splitflg:
                unodes.append(child)
        if len(unodes) > 0 and "expr" not in keystmt:
            newkeystmt = copyKeyStmt(keystmt)
            newkeystmt["expr"] = getToken(code,node)
            keystmt = newkeystmt
        for child in unodes:
            pyDefUseTvs(code,child,cfg,'U',info,keystmt)
        for child in dnodes:
            pyDefUseTvs(code,child,cfg,'D',info,keystmt)
    elif node.type == "identifier":
        name = getToken(code,node)
        cfg.appendDefUse((name,flg),node.start_byte,node.end_byte,keystmt)
    else:
        for child in node.children:
            pyDefUseTvs(code,child,cfg,flg,info,keystmt)