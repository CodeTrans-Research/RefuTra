import re
#from math import *
import math
import ast
import os
import sys
import copy
import random
JVPYKEYWORDMAP = {
    "true":"True",
    #"F":"",
    "false":"False",
    "length":"len",
    "size()":"len",
    "Math.max":"max",
    "Math.min":"min",
    "Math.abs":"abs",
    "Math.sqrt":"math.sqrt",
    "Math.pow":"math.pow",
    "Math.log":"math.log",
    "Math.PI":"math.pi",
    "Math.floor":"math.floor",
    "Math.ceil":"math.ceil",
    "Integer.max":"max",
    "Integer.min":"min",
    "&&":" and ",
    "||":" or ",
    "(float)":"float",
    "(int)":"int",
    "(double)":"float",
    "(char)":"chr",
    "null":"None",
    "Integer.MAX_VALUE":"float('inf')",
    "Integer.MIN_VALUE":"float('-inf')",
    "NO_OF_CHARS":"256"
}
PYJVKEYWORDMAP = {
    "True":"true",
    "False":"false",
    "math.pi":"Math.PI",
    "//":"/",
    "and":"&&",
    "for":"@",
    "ord":"(int)",
    "or":"||",
    "not":"!",
    "@":"for",
    "None":"null",
    "int(":"(int)(",
    "float(":"(float)(",
    "float('inf')":"Integer.MAX_VALUE"
}
CPYKEYWORDMAP = {
    "true":"True",
    "false":"False",
    "length":"len",
    "&&":" and ",
    "||":" or ",
    "strlen":"len",
    "size()":"len()",
    "(float)":"float",
    "(int)":"int",
    "NULL":"None",
    ".sqrt":"Sqrt",
    "sqrt":"math.sqrt",
    "Sqrt":".sqrt",
    "ceil":"math.ceil",
    "log10":"math.log",
    "log":"math.log",
    "floor":"math.floor",
    "std::min":"min",
    "std::max":"max",
    "M_PI":"math.pi",
    "INT_MAX":"float('inf')",
    "INT_MIN":"float('-inf')"
}
JVPRIMITIVETYPE = ['int','char','double','boolean','Boolean','float','long','String','Integer']
CPRIMITIVETYPE = ['int','char','double','bool','float','long','string','std::string']
JVCTYPEMAP = {
    "int":["int","unsigned int","unsigned","size_t"],
    "char":"char",
    "boolean":"bool",
    "Boolean":"bool",
    "double":"double",
    "float":"float",
    "long":["long long","unsigned long","long","uint32_t","long int"],
    "String":["string","char*","const string&","string&","const char *"],
    "HashSet<Integer>":["set<int>","unordered_set<int>"],
    "Set<Integer>":["set<int>","unordered_set<int>"],
    "HashMap<Integer,Integer>":["unordered_map<int,int>","map<int,int>"],
    "Map<Integer,Integer>":["unordered_map<int,int>","map<int,int>"],
    "HashMap<String,Integer>":"unordered_map<string,int>",
    "int[][]":["vector<vector<int>>","int**","int[][]","vector<vector<int>>&"],
    "boolean[][]":["vector<vector<bool>>","bool**","bool[][]"],
    "Queue<Integer>":"queue<int>",
    "Stack<Integer>":"stack<int>",
    "boolean[]":["vector<bool>","bool*","bool[]"],
    "long[][]":["vector<vector<long>>","long**","long[][]","long long[][]","vector<vector<long long>>"],
    "Stack<Character>":"stack<char>",
    "char[]":["vector<char>","char*","char[]"],
    "Vector<Long>":"vector<long>",
    "PriorityQueue<Integer>":["priority_queue<int,vector<int>,greater<int>>","priority_queue<int>"],
    "String[]":["vector<string>","string*","string[]"],
    "double[]":["vector<double>","double*","double[]"],
    "ArrayList<Integer>":["int[]","vector<int>","int*"],
    "List<Integer>":["int[]","vector<int>","int*"],
    "int[]":["int[]","vector<int>","int*","vector<int>&","int32_t[]"],
    "LinkedHashSet<Integer>":"set<int>",
    "Integer":"int",
    "Integer[]":["int[]","vector<int>","int*"],
    "long[]":["longlong[]","vector<long>","long*","long[]"],
    "double[][]":["double[][]","vector<vector<double>>","double**"],
    "char[][]":["vector<vector<char>>","char**","char[][]"],
    "int[][][]":["vector<vector<vector<int>>>","int***","int[][][]"],
    "StringBuffer":"string"
}
TYPEMAP = {
    "int":"int",
    "char":"Union[str|int]",
    "boolean":"bool",
    "Boolean":"bool",
    "double":"float",
    "float":"float",
    "long":"int",
    "String":"str",
    "HashSet<Integer>":"set[int]",
    "Set<Integer>":"set[int]",
    "HashMap<Integer,Integer>":"dict[int,int]",
    "Map<Integer,Integer>":"dict[int,int]",
    "HashMap<String,Integer>":"dict[str,int]",
    "int[][]":"list[list[int]]",
    "boolean[][]":"list[list[bool]]",
    #"Queue<Integer>":"Queue[int]",
    #"Stack<Integer>":"list[int]",
    "boolean[]":"list[bool]",
    "long[][]":"list[list[int]]",
    "Stack<Character>":"list[str]",
    "char[]":"list[Union[str|int]]",
    "Vector<Long>":"list[int]",
    #"PriorityQueue<Integer>":"PriorityQueue[int]",
    "String[]":"list[str]",
    "double[]":"list[float]",
    "ArrayList<Integer>":"list[int]",
    "List<Integer>":"list[int]",
    "int[]":"list[int]",
    "LinkedHashSet<Integer>":"set[int]",
    "Integer":"int",
    "Integer[]":"list[int]",
    "long[]":"list[int]",
    "double[][]":"list[list[float]]",
    "char[][]":"list[list[str]]",
    "int[][][]":"list[list[list[int]]]"
}
ARRTYPEINITMAP = {
    "int[][]":"[[0 for _ in range(#)] for _ in range(#)]",
    "boolean[][]":"[[False for _ in range(#)] for _ in range(#)]",
    "boolean[]":"[False for _ in range(#)]",
    "char[]":"[\" \" for _ in range(#)]",
    "long[][]":"[[0 for _ in range(#)] for _ in range(#)]",
    "String[]":"[\"\" for _ in range(#)]",
    "double[]":"[0.0 for _ in range(#)]",
    "int[]":"[0 for _ in range(#)]",
    "Integer[]":"[0 for _ in range(#)]",
    "long[]":"[0 for _ in range(#)]",
    "double[][]":"[[0.0 for _ in range(#)] for _ in range(#)]",
    "char[][]":"[[\" \" for _ in range(#)] for _ in range(#)]",
    "int[] [] []":"[[[0 for _ in range(#)] for _ in range(#)] for _ in range(#)]"
}
CPRIMITIVEDEFAULTVALUE = {
    "int":"0",
    "bool":"false",
    "float":"0.0",
    "long long":"0",
    "long":"0",
    "char":"' '",
    "string":'""',
    "char*":'""'
}
LITERALMVALUE = 9999

def getToken(code,node):
    bsnippet = code[node.start_byte : node.end_byte].strip(b" ")
    snippet = bsnippet.decode("utf8")
    return snippet
def getCode(code,start,end):
    bsnippet = code[start : end].strip(b" ")
    snippet = bsnippet.decode("utf8")
    return snippet
def dumpAST(code,node,indent=0):
    prefix = str(indent)
    for i in range(0,indent):
        prefix = prefix + " "
    output = prefix + " token:" + getToken(code,node) + ",type:" + node.type
    Logger.debug(output)
    for child in node.children:
        dumpAST(code,child,indent + 1)
def removeBlank(st):
    newst = ""
    for c in st:
        if c  != " ":
            newst += c
    return newst
def normalizeArrValue(v):
    valuemap = {'None':None,'Other':'Other','False':'0','True':'1','false':'0','true':'1'}
    newv = None
    if v in valuemap:
        newv = valuemap[v]
    else:
        try:
            float(v)
            newv = v
        except:
            newv = "Other"
    return newv
def blankPattern(s):
    pattern = ''
    for char in s:
        if char in '[]':
            pattern += re.escape(char) + r'\s*'
        elif char == '-':
            pattern += r'\-' + r'\s*'
        else:
            pattern += re.escape(char) + r'\s*'
    return pattern
def checkStrip(st):
    if len(st) == 0:
        return True
    for c in st:
        if c not in ["\n"," ","\t","{","}"]:
            return False
    return True
def checkStrip2(st):
    if len(st) == 0:
        return True
    for c in st:
        if c not in ["\n"," ","\t"]:
            return False
    return True
def normalizaUpdate(updates):
    patterns = [(['\+\+([a-zA-Z0-9]+)','([a-zA-Z0-9]+)=([a-zA-Z0-9]+)\+1'],'1++')
                ,(['--([a-zA-Z0-9]+)','([a-zA-Z0-9]+)=([a-zA-Z0-9]+)-1'],'1--')
                ,(['([a-zA-Z0-9]+)(\+)=([a-zA-Z0-9]+)','([a-zA-Z0-9]+)(-)=([a-zA-Z0-9]+)'],'1=123')           
                ]
    updates = updates.replace("+=1","++").replace("-=1","--")
    for p in patterns:
        pts = p[0]
        re_p = p[1]
        for pt in pts:
            m = re.match(pt,updates)
            if m != None:
                updates = ""
                for c in re_p:
                    try:
                        index = int(c)
                        updates += m[index]
                    except Exception:
                        updates += c
                break
    return updates

def normalizeJavaComp(code,child1):
    from common.traverse import traverseCast
    cnt2 = 0
    comtype,lftv,rgtv = "","",""
    for child2 in child1.children:
        cnt2 += 1
        if cnt2 == 1:
            lftv = removeBlank(getToken(code,child2))
        elif cnt2 == 2:
            comtype = child2.type
        elif cnt2 == 3:
            rgtv = removeBlank(getToken(code,child2))
            castlis = []
            traverseCast(code,child2,castlis)
            castlis.reverse()
            for caste in castlis:
                rgtv = rgtv.replace(caste,"("+caste+")")
            '''if child2.type == "cast_expression":
                cflg = False
                for child in child2.children:
                    if child.type == ")":
                        cflg = True
                    elif cflg:             
                        caste = getToken(code,child)
                rgtv = rgtv.replace(caste,"("+caste+")")'''

    if comtype == "<=":
        intrgtv = None
        try:
            intrgtv = int(rgtv)
        except Exception:
            pass
        if intrgtv != None:
            newcompstmt = lftv+"<"+str(intrgtv+1)
        else:
            m = re.match('([a-zA-Z-9\+-]*)([\+-])([0-9]+)',rgtv)
            if m != None:
                rgtv = m[1]
                op = m[2]
                v = int(m[3])
                if op == "+":
                    if v + 1 != 0:
                        newcompstmt = lftv + "<" + rgtv + op + str(v+1)
                    else:
                        newcompstmt = lftv + "<" + rgtv
                else:
                    if v - 1 != 0:
                        newcompstmt = lftv + "<" + rgtv + op + str(v-1)
                    else:
                        newcompstmt = lftv + "<" + rgtv
            else:
                if rgtv.find("sqrt") == -1 and rgtv.find("log") == -1:
                    newcompstmt = lftv+"<"+rgtv+"+1"
                else:
                    newcompstmt = lftv + "<=" + rgtv   
                    
    elif comtype == ">=":
        intrgtv = None
        try:
            intrgtv = int(rgtv)
        except Exception:
            pass
        if intrgtv != None:
            newcompstmt = lftv+">"+str(intrgtv-1)
        else:
            m = re.match('([a-zA-Z-9\+-]*)([\+-])([0-9]*)',rgtv)
            if m != None:
                rgtv = m[1]
                op = m[2]
                v = int(m[3])
                if op == "+":
                    if v - 1 != 0:
                        newcompstmt = lftv + ">" + rgtv + op + str(v-1)
                    else:
                        newcompstmt = lftv + ">" + rgtv
                else:
                    if v + 1 != 0:
                        newcompstmt = lftv + ">" + rgtv + op + str(v+1)
                    else:
                        newcompstmt = lftv + ">" + rgtv
            else:
                if rgtv.find("sqrt") == -1 and rgtv.find("log") == -1 and lftv.find("sqrt") == -1 and lftv.find("log") == -1:
                    newcompstmt = lftv+">"+rgtv+"-1"    
                else:
                    newcompstmt = lftv + ">=" + rgtv   
    else:
        #newcompstmt = removeBlank(getToken(code,child1))
        newcompstmt = lftv+comtype+rgtv
    return newcompstmt
def parseCArray(ctype):
    eles = []
    if ctype.count('[') > 0:
        flg = False
        ele = ""
        for c in ctype:
            if c == "[":
                if flg:
                    return None,None
                flg = True
            elif c == "]":
                flg = False
                if ele != "":
                    eles.append(ele)
                ele = ""
            elif flg:
                ele += c
        for ele in eles:
            ctype = ctype.replace(f"[{ele}]","[]")
    return ctype,eles
def checkJVArray(tp):
    return tp.count('[') > 0
def checkCArray(tp):
    return "vector" in tp or "*" in tp or "[" in tp
def str2peakvalue(exp):
    numexp = exp.replace("L","").replace("F","")
    try:
        num = float(numexp)
        if num >= LITERALMVALUE:
            exp = "LITERALMVALUE"
        elif num <= -LITERALMVALUE:
            exp = "-LITERALMVALUE"
    except:
        pass
    return exp
def splitLineAST(code,rootnode):
    token = getToken(code,rootnode)
    linelis = []
    cnt = 0
    for ch in token:
        if ch == "\n":
            linelis.append(cnt)
        cnt += 1
    if token[-1] != "\n":
        linelis.append(cnt)
    return linelis
    
def pyself(st):
    st = st.replace('\\\n','')
    mathAPIs = ["sqrt","pow","log","pi","floor","ceil"]
    for api in mathAPIs:
        if api in st and len(re.findall(f"math\s*\.{api}\s*\(",st)) == 0:
            st = st.replace(api+"(","math."+api+"(")    
    return st
def jv2py(st,varmap=None):
    st = removeBlank(st)
    for ke,va in JVPYKEYWORDMAP.items():
        if ke == "length" and varmap != None and ke in varmap:
            continue
        st = st.replace(ke,va)
    if st.find("len") != -1:
        mt1 = re.findall("([a-zA-Z_][a-zA-Z0-9_\[\]]*)\.len\(\)",st)
        mt2 = re.findall("([a-zA-Z_][a-zA-Z0-9_\[\]]*)\.len",st)
        for var in mt1:
            oldexpr = var+".len()"
            newexpr = "len("+var+")"
            st = st.replace(oldexpr,newexpr)
        for var in mt2:
            oldexpr = var+".len"
            newexpr = "len("+var+")"
            st = st.replace(oldexpr,newexpr)
    floatmt = None
    floatmt = re.findall("[0-9\.]+F",st)
    for fmt in floatmt:
        if st.count(f"0x{fmt}") == 0:
            st = st.replace(fmt,fmt[:-1])
    while st.find(".charAt") != -1:
        arg = getMatchedBracket(st[st.find(".charAt")+7:])[1:-1]
        oldexp = ".charAt(" + arg + ")"
        newexp = "[" + arg + "]"
        st = st.replace(oldexp,newexp)
    return st
def c2py(st):
    st = removeBlank(st)
    for ke,va in CPYKEYWORDMAP.items():
        st = st.replace(ke,va)
    if st.find("len") != -1:
        mt1 = re.findall("([a-zA-Z_][a-zA-Z0-9_\[\]]*)\.len\(\)",st)
        mt2 = re.findall("([a-zA-Z_][a-zA-Z0-9_\[\]]*)\.len",st)
        for var in mt1:
            oldexpr = var+".len()"
            newexpr = "len("+var+")"
            st = st.replace(oldexpr,newexpr)
        for var in mt2:
            oldexpr = var+".len"
            newexpr = "len("+var+")"
            st = st.replace(oldexpr,newexpr)
    floatmt = None
    floatmt = re.findall("[0-9\.]+F",st)
    for fmt in floatmt:
        if st.count(f"0x{fmt}") == 0:
            st = st.replace(fmt,fmt[:-1])
    while st.find(".at") != -1:
        arg = getMatchedBracket(st[st.find(".charAt")+3:])[1:-1]
        oldexp = ".at(" + arg + ")"
        newexp = "[" + arg + "]"
        st = st.replace(oldexp,newexp)
    return st
def jv2c(st):
    st = st.replace("Math.","").replace(".length",".length()")
    return st
APIS = ["max","min","sqrt","pow","log","floor","ceil","abs"]
def py2jv(st,jvvartypemap=None):
    maskmap,maskcnt = {},0
    if jvvartypemap != None:
        for v in jvvartypemap:
            if any(k in v for k in ["and","not","or"]):
                maskmap[v] = f'#{maskcnt}'
                st = st.replace(v,f'#{maskcnt}')
                maskcnt += 1
    for w1,w2 in PYJVKEYWORDMAP.items():
        st = st.replace(w1,w2)
    for w1,w2 in maskmap.items():
        st = st.replace(w2,w1)
    
    pt = "([a-zA-Z_][a-zA-Z0-9_]*\s*)\[(.+?)\]"
    mt = re.findall(pt,st)
    for arr,index in mt:
        if index.count('[') != index.count(']'):
            index += ']'
        oriexpr = arr + "[" + index + "]"
        arr = removeBlank(arr)
        if arr in jvvartypemap and jvvartypemap[arr] == "String":
            st = st.replace(oriexpr,f"{arr}.charAt({index})")
    for i,api in enumerate(APIS):
        pt1 = blankPattern("math."+api+'(')
        pt2 = blankPattern(api+'(')
        st = re.sub(pt1,f"@MATHAPI{i}",st)
        st = re.sub(pt2,f"@MATHAPI{i}",st)
    for i,api in enumerate(APIS):
        st = st.replace(f"@MATHAPI{i}",f"Math.{api}(")
    mt1 = re.findall("len\(([a-zA-Z_][a-zA-Z0-9_\[\]]*)\)",st)
    for m in mt1:
        words = re.findall("[a-zA-Z_]+",m)
        if jvvartypemap != None and len(words) > 0 and words[0] in jvvartypemap and '[' in jvvartypemap[words[0]]:
            st = st.replace(f"len({m})",f"{m}.length")
        else:
            st = st.replace(f"len({m})",f"{m}.length()")
    #"Math.abs":    "abs",
    #"Math.sqrt":"math.sqrt",
    #"Math.pow":"math.pow",
    #"Math.log":"math.log",
    #"Math.PI":"math.pi",
    #"Math.floor":"math.floor",
    #"Math.ceil":"math.ceil",
    return st
PRIMITIVETYPE = {"java":JVPRIMITIVETYPE,"cpp":CPRIMITIVETYPE,"python":[]}
STMTTRANSPILE2PY = {"java":jv2py,"cpp":c2py,"python":pyself}
STMTCONVERT = {("java","python"):jv2py,("java","cpp"):jv2c,("python","java"):py2jv}

def toPyCast(ud,node,exp,lang,varmap=None):
    cast = set()
    for uud in node['UD']:
        if uud[2] == ud[2] and uud[1] == 'U':
            if 'cast' in uud[3]:
                cast.add(STMTTRANSPILE2PY[lang](removeBlank(uud[3]['cast'])))
    if len(cast) != 0:
        for c in cast:
            words = re.findall("[a-zA-Z_][a-zA-Z0-9_]*",exp.replace('int',''))
            exp = exp.replace(c,"("+c+")")
            for v in words:
                if varmap != None and v in varmap and (varmap[v] == "char[]" or varmap[v] == "String"):
                    exp = exp.replace(f"int({c})",f"ord({c})")
                    break
            
    return exp

def toPyDiv(dic,exp):
    if 'div' in dic:
        for divexpr in dic['div']:
            divexpr = jv2py(removeBlank(divexpr))
            newdivexpr = divexpr.replace("/","//")
            exp = exp.replace(divexpr,newdivexpr)
    return exp
def ridType(exp,types,convert):
    if type(exp) == type([]):
        newexp = []
        for e in exp:
            for t in types:
                e = e.replace(t,'')
            newexp.append((removeBlank(convert(e))))
        return newexp
    elif type(exp) == type(""):
        for t in types:
            exp = exp.replace(t,'')
        return convert(exp)
    else:
        return exp
    
def exec_with_timeout(code,localmap, timeout=10):
    import signal
    def handler(signum, frame):
        raise Exception("Exec timeout")
    signal.signal(signal.SIGALRM, handler)
    signal.alarm(timeout)  
    try:
        #Logger.debug(code,localmap)
        exec(code,None,localmap)
    except Exception as e:
        #Logger.debug(f"Exec failed: {e}")
        return f"{e}"
    finally:
        signal.alarm(0) 
    return localmap
def extractVarInExp(exp:str,ordered=False):
    newexp = exp
    if 'for' in exp:
        newexp = newexp.replace('for',' ')
        newexp = newexp.replace('in',' ')
    if 'if' in newexp and 'else' in newexp:
        newexp = newexp.replace('if',"").replace('else','')
    vars = []
    baseopkeyword = ['**','*','//','/','%','++','--','+','-','(',')',',','!','~','and','ord','char','chr','or','isnot','not','&&','||','&','|','int','float','<=','>=','<','>','=',';',"Not","And","Or","False","True","true","false"]
    for op in baseopkeyword:
        newexp = newexp.replace(op,' ')
    
    words = set(['new','min','max','sqrt','math','len','pow','ceil'])
    
    for item in newexp.split():
        if item != "" and not item.isdigit() and item.find('.') == -1 and item.find("'") == -1 and item.find('"') == -1 and not item[0].isdigit():
            if item in words:
                if exp.count(item+"(") == 0 and exp.count(item+".") == 0:
                    vars.append(item)
            else:
                vars.append(item)
    #return varset-mathfuncs
    if ordered:
        return vars
    else:
        return set(vars)
def countOPInExp(exp:str):
    baseop = ['**','*','//','/','%','++','--','+','-','(',')',',','!','~','and','ord','char','chr','or','not','&&','||','int','float','<=','>=','<','>','=',';']
    opcnt = 0
    for op in baseop:
        if op not in ['(',')']:
            opcnt += exp.count(op)
        exp = exp.replace(op,' ')
    newexp = exp.replace('math','').replace(".","")
    mathfuncs = ['min','max','sqrt','len','log']
    for item in newexp.split():
        if item != "" and not item.isdigit() and item.find('.') == -1:
            if item in mathfuncs:
                if not (exp.count(item+"(") == 0 and exp.count(item+".") == 0):
                    opcnt += 1
    return opcnt
def extractVarandNumInExp(exp:str):
    
    baseop = ['**','*','//','/','%','++','--','+','-','(',')',',','and','or','not','&&','||','if','else','<=','>=','<','>','=',';']
    for op in baseop:
        exp = exp.replace(op,' ')
    
    mathfunc = set(['min','max','sqrt','math','int','float','len'])
    varset = set()
    for item in exp.split():
        if item != "":
            varset.add(item)
    #Logger.debug(varset-mathfunc)
    return varset-mathfunc
def getMatchedBracket(exp):
    #Logger.debug("here")
    #Logger.debug(exp)
    cnt = 0
    newexp = ""
    for c in exp:
        if c == "(":
            cnt += 1
            newexp += "("
        elif c == ")":
            cnt -= 1
            newexp += ")"
            if cnt <= 0:
                break
        elif cnt > 0:
            newexp += c
    return newexp 
def splitArg(exp):
    bccnt = 0
    splitplace = set()
    for index,c in enumerate(exp):
        if c == '(':
            bccnt += 1
        elif c == ')':
            bccnt -= 1
        elif c == ',':
            splitplace.add(index)
    arglis = []
    for index,p in enumerate(splitplace):
        if index == 0:
            arglis.append(exp[:p])
        if index == len(splitplace) - 1:
            arglis.append(exp[p+1:])
        if index > 0 and index < len(splitplace) - 1:
            arglis.append(exp[p+1:splitplace[index+1]])
    return arglis
def rewriteOpAssExpr(expr):
    ops = ["-=","+=","*=","/="]
    curop = None
    for candop in ops:
        if expr.find(candop) != -1:
            curop = candop
            break
    if curop == None:
        return expr
    vars = expr.split(candop)
    if len(vars) != 2:
        return expr
    
    if curop == '-=':
        return vars[0] + "=" + vars[0] + "-" + vars[1]
    elif curop == '+=':
        return vars[0] + "=" + vars[0] + "+" + vars[1]
    elif curop == "*=":
        return vars[0] + "=" + vars[0] + "*" + vars[1]
    elif curop == "/=":
        return vars[0] + "=" + vars[0] + "/" + vars[1]
def tokenizeSingleCompExpr(expr):
    compop = ['<',">","<=",">=","=="]
    op = None
    for candop in compop:
        if expr.find(candop) != -1:
            op = candop
    if op == None:
        return None
    var = expr.split(op)
    if op == '<':
        return (var[0],var[1])
    elif op == '<=':
        return (var[0],var[1] + "+1")
    elif op == ">":
        return (var[1],var[0])
    elif op == ">=":
        return (var[1],var[0]+"+1")
    else:
        return(var[0],var[1])
def renameArr(exp):
    while exp.count('[') > 0 != exp.count('[') > 0:
        mt = re.findall("([a-zA-Z_][a-zA-Z0-9_]*)\[(.+?)\]",exp)
        if len(mt) == 0:
            break
        for mapv in mt:
            arr = mapv[0]
            ind = mapv[1]
            iteind = ind
            if ind.count('(') == 1 and ind[-1] == ')' and ind[0] == '(':
                iteind = ind[1:-1]
            newind = ""
            for c in iteind.replace("//","/"):
                if c.isdigit() or c.islower() or c.isupper():
                    newind += c
                else:
                    newind += str(abs(hash(c)))[0]
            oriv = f"{arr}[{ind}]"
            newv = arr + "___" + newind
            exp = exp.replace(oriv,newv)
    return exp
def getNlineCode(code,line):
    return code.split("\n")[line-1]
def countCDimen(tp):
    if 'queue' in tp or 'stack' in tp:
        return 0
    if tp.count('[') > 0:
        return tp.count('[')
    elif tp.count('<') > 0:
        return tp.count('<')
    else:
        return 0
def getLinebyPlace(splitline,place):
    for i in range(0,len(splitline)):
        if place <= splitline[i]:
            return i+1
    return -1
def getFirstTypeOfArray(arrtp):
    for k in CPRIMITIVEDEFAULTVALUE.keys():
        if arrtp.count(k) > 0:
            return k
    return None
def getDefaultValueofArray(arrtp):
    primt = getFirstTypeOfArray(arrtp)
    if primt != None:
        defaultv = CPRIMITIVEDEFAULTVALUE[primt]
        return defaultv
    else:
        return None
def getSELine(startb,endb,oritocode,tosplitline):
    startline,endline = -1,-1
    blank = ""
    codesp = oritocode.split("\n")
    for i in range(0,len(tosplitline)):
        if startb <= tosplitline[i] and startline == -1:
            startline = i + 1
            linecode = codesp[i]
            for c in linecode:
                if c in [" "," \t","\n"]:
                    blank += c
                else:
                    break
        if endb <= tosplitline[i] and endline == -1:
            endline = i + 1
            break
    if endline == -1:
        endline = len(tosplitline)
    return blank,startline,endline


def simplifyExpByDR(vartypemap,init,exp,DRIN,CRIN,lang="python",bans=[]):
        '''if self.frlang == "java" and jv == False:
            vartypemap = {}
            for v,tp in self.jvvartypemap.items():
                newv = v
                if v in self.varmap:
                    newv = self.varmap[v]
                vartypemap[newv] = tp
        elif self.frlang == "python" and jv == False:
            vartypemap = {}
            jvpyvarmap = {va:ke for ke,va in self.varmap.items()}
            for v,tp in self.jvvartypemap.items():
                newv = v
                if v in jvpyvarmap:
                    newv = jvpyvarmap[v]
                vartypemap[newv] = tp
        else:
            vartypemap = self.jvvartypemap'''
        newdrin = {}
        
        initvar = extractVarInExp(init)
        for var,descset in DRIN.items():
            if var in initvar:
                continue
            if len(descset) != 1:
                continue
            desc = list(descset)[0]
            drexp = str(desc[2])
            drexp = STMTTRANSPILE2PY[lang](drexp)
            '''if "Arrays.copyOfRange(" in drexp:
                drexp = drexp[drexp.find("(")+1:drexp.find(",")]
                exp = exp.replace(var+"___",drexp+"___")'''
            if drexp != '' and var not in extractVarInExp(drexp):
                newdrin[var] = drexp
        #newdrin["copyA"] = "A" 
        #newdrin["copyB"] = "B" 
        #newdrin["v"] = "arr.@copy()"         
        if exp.count('min(') > 0:
            mexp = getMatchedBracket(exp[exp.find('min('):])[1:-1]
            args = splitArg(mexp)
            if len(args) == 2:
                res = None
                for cond in CRIN:
                    var = tokenizeSingleCompExpr(cond)
                    if var != None:
                        if args[0] in var[0] and args[1] in var[1]:
                            res = args[0]
                        elif args[0] in var[1] and args[1] in var[0]:
                            res = args[1]
                if res != None:
                    exp = exp.replace(f"min({mexp})",res)
        expset = set()
        usedrvar = set()
        while True:
            #Logger.debug(exp)
            vars = extractVarInExp(exp)
            newvars = set()
            for v in vars:
                if v.find("___") != -1:
                    newvars.add(v[:v.find("___")])
                else:
                    newvars.add(v)
            vars = newvars
            if len(vars & newdrin.keys()) == 0:
                break
            newexp = exp
            for var in vars & newdrin.keys():
                if var not in usedrvar:
                    if var in vartypemap and (vartypemap[var].count('[') > 0 or vartypemap[var].count('*') > 0):
                        if exp.count(f'len({var})') > 0:
                            targetexp = None
                            arrinitpatterns = [
                                '\[.+?\]\*(.+?)',
                                'new.+?\[(.+?)\]',
                                'for.+?inrange\((.+?)\)',
                            ]
                            drexp = newdrin[var]
                            #Logger.debug(drexp)
                            targetexp = None
                            for pt in arrinitpatterns:
                                mt = re.findall(pt,drexp)
                                if len(mt) > 1:
                                    targetexp = mt[-1]
                                    break
                                elif len(mt) == 1:
                                    targetexp = mt[0]
                                    break
                            '''if targetexp == None:
                                arrinitcopypatterns = [
                                    '(.+?)\.toCharArray\(\)'
                                ]
                                for pt in arrinitcopypatterns:
                                    mt = re.findall(pt,drexp)
                                    if len(mt) == 1:
                                        targetexp = mt[0]
                                        break
                                if not(targetexp == None):
                                    targetexp = f"len({targetexp})"'''
                            if not (targetexp == None):
                                newexp = newexp.replace(f'len({var})',targetexp)
                        if newdrin[var].count(".@copy") > 0:
                            drin = newdrin[var].replace(".@copy()","")
                            newexp = newexp.replace(var,drin)

                    else:
                        if [newdrin[var].find(b) for b in bans] == [-1 for _ in bans]:
                            newexp = newexp.replace(var+"___",newdrin[var].replace(".@copy()","")+"___") 
                            tmpmap = {}
                            cnt = 0
                            words = sorted(re.findall("[a-zA-Z_][a-zA-Z0-9_]*",newexp), key=len,reverse=True)
                            for v in words:
                                if v != var and var in v:
                                    newexp = newexp.replace(v,f"@{cnt}")
                                    tmpmap[v] = f"@{cnt}"
                                    cnt += 1
                            if newexp.find("=") != -1 and newexp.find("==") == -1 and newexp.find("!=") == -1:
                                sp = newexp.split("=")
                                newexp = sp[0] + "=" + sp[1].replace(var,"("+newdrin[var]+")")
                            else:
                                newexp = newexp.replace(var,"("+newdrin[var]+")")
                            #newexp = newexp.replace(var,newdrin[var])
                            for old,new in tmpmap.items():  
                                newexp = newexp.replace(new,old)
                            
                    usedrvar.add(var)
            if newexp in expset:
                break
            else:
                expset.add(newexp)
                exp = newexp
        return exp
def replaceChar(exp):
    pt = "['\"].['\"]"
    ms = re.findall(pt,exp)
    for m in ms:
        ch = m[1:-1]
        exp = exp.replace(f"ord({m})",str(ord(ch))).replace(m,str(ord(ch)))
    return exp

def isSingleVariable(expr):
    try:
        tree = ast.parse(expr, mode='eval')
        return isinstance(tree.body, ast.Name)
    
    except Exception as e:
        return False

def checkRvIsArray(rv):
    if 'for' in rv or 'new' in rv:
        return True
    try:
        tree = ast.parse(rv)
        for node in ast.walk(tree):  # 遍历 AST
            if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Mult) and (isinstance(node.left, ast.List) or isinstance(node.right, ast.List)):
                return True
    except SyntaxError:
        return False
    return False
def subvarcomp(st1,st2):
    dp = [[0 for _ in range(len(st2))] for _ in range(len(st1))]
    mx = -1
    for i,c1 in enumerate(st1):
        for j,c2 in enumerate(st2):
            
            if c1 == c2:
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    foremax = -1
                    for i0 in range(0,i):
                        for j0 in range(0,j):
                            if dp[i0][j0] > foremax:
                                foremax = dp[i0][j0]
                    dp[i][j] = foremax + 1
                if dp[i][j] > mx:
                    mx = dp[i][j]
            else:
                dp[i][j] = 0
    return mx
def deepcomp(st1,st2):
    st1 = removeBlank(st1)
    st2 = removeBlank(st2)
    mt1 = re.search("[a-zA-Z_][a-zA-Z0-9_]*",st1)
    mt2 = re.search("[a-zA-Z_][a-zA-Z0-9_]*",st2)
    cnt = 0
    while mt1 != None and mt2 != None:
        st1 = st1.replace(mt1[0],"@"+str(cnt))
        st2 = st2.replace(mt2[0],"@"+str(cnt))
        mt1 = re.search("[a-zA-Z_][a-zA-Z0-9_]*",st1)
        mt2 = re.search("[a-zA-Z_][a-zA-Z0-9_]*",st2)
    #Logger.debug(st1,st2)
    return st1==st2
def addDic(d,n):
    if n not in d:
        d[n] = 1
    else:
        d[n] = d[n] + 1
def blankCount(st):
    cnt = 0
    for c in st:
        if c in [" ","\n","\t"]:
            cnt += 1
        else:
            return cnt
    return cnt
def ridDup(lis):
    newlis = []
    for i in lis:
        if i not in newlis:
            newlis.append(i)
    return newlis
def renamevar(exp,varmap):
    varlis = sorted(varmap.items(),key=lambda x:len(x[0]),reverse=True)
    for index,v in enumerate(varlis):
        frv = v[0]
        tov = v[1]
        exp = exp.replace("."+frv,"@"+str(index))
        exp = exp.replace(frv+"(","#"+str(index))
        exp = exp.replace(frv,'$'+str(index))
    for index,v in enumerate(varlis):
        frv = v[0]
        tov = v[1]
        exp = exp.replace("@"+str(index),"."+frv)
        exp = exp.replace("#"+str(index),frv+"(")
        exp = exp.replace('$'+str(index),tov)
    return exp
def varmapping(varset1,varset2):
    
    diffset1 = varset1-varset2
    diffset2 = varset2-varset1
    mp = {}
    for var1 in diffset1:
        mappedvar = []
        for var2 in diffset2:
            
            substlen = subvarcomp(var1.lower(),var2.lower())
            requirelen = min(len(var1),len(var2)) if min(len(var1),len(var2)) < 3 else 3
            if substlen >= requirelen:
                mappedvar.append((substlen,var2))
            if len(mappedvar) == 1:
                mp[var1] = mappedvar[0][1]
            elif len(mappedvar) > 1:
                disset = set()
                for dis,v in mappedvar:
                    disset.add(dis)
                if len(disset) != 1:
                    mappedvar.sort()
                    mappedvar.reverse()
                    mp[var1] = mappedvar[0][1]
                else:
                    place = []
                    for _,var in mappedvar:
                        place1,place2 = sys.maxsize,sys.maxsize
                        if var1.find(var) != -1:
                            place1 = var1.find(var)
                        if var.find(var1) != -1:
                            place2 = var.find(var1)
                        place.append((min(place1,place2),var))
                    place.sort()
                    mp[var1] = place[0][1]
                
    return mp
class Logger:
    _logs = []  
    _debug_enabled = True
    @classmethod
    def debug(cls, msg):
        if cls._debug_enabled:
            cls._logs.append(f"[DEBUG] {msg}")
            
    @classmethod
    def info(cls, msg):
        cls._logs.append(f"[INFO] {msg}")
    
    @classmethod
    def cstwarning(cls, msg, line):
        cls._logs.append(f"\033[33m[WARNING] \033[0min line {line}: {msg}")
    
    @classmethod
    def csterror(cls, msg, line):
        cls._logs.append(f"\033[31m[ERROR] \033[0min line {line}: {msg}")

    @classmethod
    def print_all(cls):
        for log in cls._logs:
            print(log)
        cls._logs = []
def isAllFiles(paths):
    return all(os.path.isfile(p) for p in paths)

def isAllDirs(paths):
    return all(os.path.isdir(p) for p in paths)

def arePathsExist(paths):
    for path in paths:
        if not os.path.exists(path):
            Logger.debug(f"{path} does not exist")
            sys.exit(1)

def ensureDirsExist(paths):
    for path in paths:
        if not os.path.exists(path):
            Logger.debug(f"{path} does not exist, try to create...")
            try:
                os.makedirs(path)
            except Exception as e:
                Logger.debug(f"cannot create dir:{path}\n{e}")
                sys.exit(1)
        elif not os.path.isdir(path):
            Logger.debug(f"not reasonable path: {path}")
            sys.exit(1)

def ensureParentDirsExist(filePaths):
    for path in filePaths:
        parentDir = os.path.dirname(path)
        if parentDir and not os.path.exists(parentDir):
            Logger.debug(f"parent dir does not exist: {parentDir}")
            try:
                os.makedirs(parentDir)
            except Exception as e:
                Logger.debug(f"cannot create directory: {parentDir}\n{e}")
                sys.exit(1)

class ConditionComparar:
    def post2Func(self,expression,lang="z3"):
        num_stack = []
        for e in expression:
            if e not in self.op_priority:
                num_stack.append(self.normalizeOperand(e,lang))
            else:
                exp = ""
                if e == chr(2):
                    num1 = num_stack.pop(len(num_stack)-1)
                    num2 = num_stack.pop(len(num_stack)-1)
                    exp = self.formats[lang][e].format(num1=num1,num2=num2)
                elif e == chr(1):
                    num1 = num_stack.pop(len(num_stack)-1)
                    num2 = num_stack.pop(len(num_stack)-1)
                    exp = self.formats[lang][e].format(num1=num1,num2=num2)
                elif e == chr(3):
                    num1 = num_stack.pop(len(num_stack)-1)
                    exp = self.formats[lang][e].format(num1=num1)
                num_stack.append(exp)
        newstack = []
        for e in num_stack:
            newstack.append(e.replace("@","!=").replace(chr(4),"'('").replace(chr(5),"')'"))
        return newstack
    #def regularNoComp(self,exp):
    def normalizeOperand(self,exp,lang):
        tmpexp = exp.replace(">>","").replace("<<","")
        compop = set(['>','<',">=","<=","==","@","equal"])
        if not any(op in tmpexp for op in compop):
            self.normalizedexp.add(exp)
            #exp = self.formats[lang][chr(1)].format(num1=f"({exp})@0",num2=f"({exp})==1") 
            exp = f"({exp})@0"
            self.normalized = True
        return exp

    def regularPa(self,exp):
        pacnt = 0
        totalcnt = 0
        for i in range(len(exp)-1,-1,-1):
            if exp[i] == ")":
                pacnt += 1
                totalcnt += 1
            elif exp[i] == "(":
                pacnt -= 1
        if pacnt > 0:
            index = exp.rfind(')')
            if index != -1:
                exp = exp[:index] + exp[index+1:]
        elif pacnt == 0 and totalcnt == 1 and len(exp) >= 2 and exp[-1] == ")" and exp[0] == "(":
            exp = exp[1:-1]
        elif pacnt == -1:
            exp = exp + ")"
        return exp
    def infix2postfix(self,expression):
        expression = removeBlank(expression)
        output = []
        op_stack = []
        expression = expression.replace("&&",chr(2)).replace("and",chr(2)).replace("||",chr(1)).replace("divisor","divis").replace("or",chr(1)).replace("!=","@").replace("not",chr(3)).replace("!",chr(3)).replace("'('",chr(4)).replace("')'",chr(5))
        operandstr = ""
        for e in expression:
            
            if e == '(':
                op_stack.append(e)
                operandstr += "("
            elif e == ')':
                if op_stack[len(op_stack)-1] == '(':
                    op_stack = op_stack[:-1]
                    operandstr += ")"
                else:
                    if operandstr != "":
                        output.append(self.regularPa(operandstr))
                        operandstr = ""
                    while op_stack[len(op_stack)-1] != '(':
                        output.append(op_stack.pop(len(op_stack)-1))
                    op_stack.pop(len(op_stack)-1)
            elif e not in self.op_priority:
                operandstr += e
            else:
                if operandstr != "":
                    if operandstr[0] == "(":
                        operandstr = operandstr[1:]
                    if operandstr != "":
                        output.append(self.regularPa(operandstr))
                    operandstr = ""
                while not len(op_stack) == 0 and self.op_priority[op_stack[len(op_stack)-1]] >= self.op_priority[e]:
                    output.append(op_stack.pop(len(op_stack)-1))
                op_stack.append(e) 

        if operandstr != "":
            output.append(self.regularPa(operandstr))
        while not len(op_stack) == 0:
            output.append(op_stack.pop())

        return output
    
    def __init__(self):
        self.normalizedexp = set()
        self.op_priority = {chr(3):3,chr(2): 2, chr(1): 1, '(': 0, ')': 0}
        self.boolop = set([chr(1),chr(2),chr(3)])
        self.normalized = False
        self.formats = {
            "python":{chr(1):"({num1} or {num2})",chr(2):"({num1} and {num2})",chr(3):"not ({num1})"}
            ,"java": {chr(1):"({num1} || {num2})",chr(2):"({num1} && {num2})",chr(3):"!({num1})"}
            ,"cpp":  {chr(1):"({num1} || {num2})",chr(2):"({num1} && {num2})",chr(3):"!({num1})"}
            ,"z3":   {chr(1):"Or({num1},{num2})",chr(2):"And({num1},{num2})",chr(3):"Not({num1})"}
        }
class ExpExector:
    
    def sampleVar(self,varset,x=1,y=None):
        varmap = {}
        if y == None:
            y = self.max
        for v in varset:
            if v.count("___") > 0:
                base = v.split("___")[0]
            else:
                base = v
            if self.oracletypemap != None and base in self.oracletypemap and self.oracletypemap[base] in ["String","char[]"]:#int[]?
                if v.count("___") > 0:
                    varmap[v] = chr(random.randint(33, 126))
                else:
                    varmap[v] = "".join([chr(random.randint(33, 126)) for _ in range(0,self.sampleOne(x,y))])
            else:
                if v not in self.specv:
                    self.specv[v] = True
                    varmap[v] = y
                else:
                    varmap[v] = self.sampleOne(x,y)
        return varmap
    def detokenize(self,exp):
        exp = exp.replace("or"," or ").replace("flo or ","floor").replace("and"," and ")
        exp = exp.replace("if"," if ").replace("else"," else ")
        return exp
    def compareLoop(self,inita,conda,updatea,initb,condb,updateb):
        initastmt = ""
        if inita != None:
            inita = self.rename(removeBlank(inita))
        else:
            inita = ""
        if initb != None:
            initb = self.rename(removeBlank(initb))
        else:
            initb = ""
        updatea = self.rename(removeBlank(updatea))
        updateb = self.rename(removeBlank(updateb))
        conda = self.rename(removeBlank(conda))
        condb = self.rename(removeBlank(condb))
        #Logger.debug(conda,condb)
        upaflg = True
        if updatea.find("++") != -1:
                updatea = updatea.replace("++","")
                updatea += "=" + updatea + "+1"
        elif updatea.find("--") != -1:
            updatea = updatea.replace("--","")
            updatea += "=" + updatea + "-1"
        if updatea.count('+') > 0:
            upaflg = True
        elif updatea.count('-') > 0:
            upaflg = False
        upbflg = True
        if updateb.find("++") != -1:
                updateb = updateb.replace("++","")
                updateb += "=" + updateb + "+1"
        elif updateb.find("--") != -1:
            updateb = updateb.replace("--","")
            updateb += "=" + updateb + "-1"
        if updateb.count('+') > 0:
            upbflg = True
        elif updateb.count('-') > 0:
            upbflg = False
        if upaflg:
            ainitlowerbound = 0
            ainitupperbound = 10
            acondlowerbound = 1000
            acondupperbound = 10000
        else:
            ainitlowerbound = 1000
            ainitupperbound = 10000
            acondlowerbound = 0
            acondupperbound = 10
        if upbflg:
            binitlowerbound = 0
            binitupperbound = 10
            bcondlowerbound = 1000
            bcondupperbound = 10000
        else:
            binitlowerbound = 1000
            binitupperbound = 10000
            bcondlowerbound = 0
            bcondupperbound = 10
        varinitseta = set()
        varinitsetb = set()
        varmap = {}
        initarv = inita.split("=")[1]
        initbrv = initb.split("=")[1]
        sampletime = 0
        self.loopvaluename = "loopvalue"
        if not initarv.isdigit():
            varinitseta = extractVarInExp(initarv)
            
        if not initbrv.isdigit():
            varinitsetb = extractVarInExp(initbrv)
        condseta = extractVarInExp(conda) - varinitseta
        condsetb = extractVarInExp(condb) - varinitsetb
        Logger.debug(condseta)
        Logger.debug(condsetb)
        if condseta != condsetb or varinitseta != varinitsetb:
            if not((condseta | varinitseta) == (condsetb | varinitsetb)):
                return "Unknown1"
        samplemax = 200
        truetime = 0
        looptime = 0
        while True:
            if sampletime == samplemax//2:
                if upaflg:
                    acondlowerbound *= 10
                    acondupperbound *= 10
                else:
                    ainitlowerbound *= 10
                    ainitupperbound *= 10
                if upbflg:
                    bcondlowerbound *= 10
                    bcondupperbound *= 10
                else:
                    binitlowerbound *= 10
                    bcondlowerbound *= 10
            elif sampletime == samplemax:
                #return "Unknown3"
                return True
            loopa = f'''{self.detokenize(inita)}
while {self.detokenize(conda)}:
    {self.loopvaluename} += 1
    {updatea}
'''
            loopb =  f'''{self.detokenize(initb)}
while {self.detokenize(condb)}:
    {self.loopvaluename} += 1
    {updateb}
'''
            
            varmap = {**self.sampleVar(varinitseta,ainitlowerbound,ainitupperbound),**self.sampleVar(condseta,acondlowerbound,acondupperbound)}
            #Logger.debug(varmap)
            varmap[self.loopvaluename] = 0
            varmapb = copy.deepcopy(varmap)
            resa = exec_with_timeout(loopa,varmap,1)
            if type(resa) == type(""):
                if resa.find("timeout") != -1:
                    sampletime += 1
                    looptime += 1
                    Logger.debug(f"loopa test timeout!init:{inita},cond:{conda},ud:{updatea},map:{varmap},script:\n{loopa}")
                    if looptime < samplemax / 10:
                        continue
                    else:
                        return False
                else:
                    Logger.debug(f"loopa test RunError!init:{inita},cond:{conda},ud:{updatea},map:{varmap},script:\n{loopa}")
                    return "Unknown2"
            resb = exec_with_timeout(loopb,varmapb,1)
            if type(resb) == type(""):
                if resb.find("timeout") != -1:
                    sampletime += 1
                    Logger.debug(f"loopb test timeout!init:{initb},cond:{condb},ud:{updateb}")
                    if sampletime < samplemax:
                        continue
                    else:
                        return False
                else:
                    Logger.debug(f"loopb test RunError!init:{initb},cond:{condb},ud:{updateb},map:{varmapb},script:\n{loopb}")
                    return "Unknown2"
            if resa[self.loopvaluename] == resb[self.loopvaluename]:
                if resa[self.loopvaluename] == 0:
                    sampletime += 1
                    continue
                else:
                    truetime += 1
                    if truetime >= samplemax//20:
                        return True
            else:
                return False
    
    def rename(self,exp):
        exp = exp.replace("or"," or ").replace("flo or ","floor").replace(" or d","ord").replace("and"," and ")
        exp = exp.replace("if"," if ").replace("else"," else ")
        self.renamemap = {'len':'length'}
        for ke,va in self.renamemap.items():
            if exp.find(va) != -1:
                exp = exp.replace(va,ke+"_var")
            elif exp.find(ke) != -1:
                exp = exp.replace(ke,ke+"_var")
            exp = exp.replace(ke+"_var(",ke+"(")
        #Logger.debug(exp)
        exp = renameArr(exp)
        return exp
    def sampleOne(self,x=1,y=None):
        if y == None:
            y = self.max
        return random.randint(x,y)
    def evalExp(self,exp,varmap):
        return eval(exp,None,varmap)
    def addDict(self,dica,dicb):
        for ke,va in dicb.items():
            dica[ke] = va
        return dica
    def evalAssign(self,exp,varmap):
        if exp.find('=') != -1:
            lv,rv = exp.split('=')[0],exp.split('=')[1]
            vara = extractVarInExp(rv)
            for var in vara:
                if var not in varmap:
                    if var not in self.samplemap:
                        self.samplemap[var] = self.sampleOne()
                    varmap[var] = self.samplemap[var]
            ans = None
            try:
                ans = self.evalExp(rv,varmap)
            except:
                pass
            if ans != None:
                varmap[lv] = ans
        return ans,varmap      
    def compareList(self,keyvars=set()):
        expalis = self.expa
        expblis = self.expb
        expalis = [self.rename(e) for e in expalis]
        expblis = [self.rename(e) for e in expblis]
        for expa in expalis:
            if '[' in expa:
                return "Unknown1"
        for expb in expblis:
            if '[' in expb:
                return "Unknown1"
        varmapa = self.varmapa
        varmapb = self.varmapb
        sampletime = 0
        while sampletime < self.sample:
            self.samplemap = {}
            for expa in expalis:
                if expa.find("=") != -1:
                    resa,varmapa = self.evalAssign(expa,varmapa)
                else:
                    try:
                        resa = self.evalExp(expa,varmapa)
                    except:
                        resa = None
            for expb in expblis:
                if expb.find("=") != -1:
                    resb,varmapb = self.evalAssign(expb,varmapb)
                else:
                    try:
                        resb = self.evalExp(expb,varmapb)
                    except:
                        resb = None
            #Logger.debug(expalis,resa,varmapa)
            #Logger.debug(expblis,resb,varmapb)
            if varmapa != varmapb:
                if len(keyvars) == 0:
                    return False
                else:
                    valueseta = set()
                    valuesetb = set()
                    for var in keyvars:
                        if var not in varmapa or var not in varmapb:
                            return False
                        valueseta.add(varmapa[var])
                        valuesetb.add(varmapb[var])
                    
                    if valueseta != valuesetb:
                        return False
            sampletime += 1
        return True
    def tryEval(self,exp,varset,vmap):
        samplevarset = varset - set(vmap.keys())
        samplemap = self.sampleVar(samplevarset)
        vmap2 = copy.deepcopy(vmap)
        try:
            vmap2 = self.addDict(vmap2,samplemap)
            self.evalExp(exp,vmap2)
        except OverflowError:
            pass
        except BaseException:
            return False
        return True
    def compare(self):
        if self.expa == self.expb:
            return True
        self.expa = self.rename(self.expa)
        self.expb = self.rename(self.expb)
        if '[' in self.expa or '[' in self.expb:
            #slice in arr expression,not support
            return True
        vara = extractVarInExp(self.expa)
        varb = extractVarInExp(self.expb)
        
        if not self.tryEval(self.expa,vara,self.varmapa) or not self.tryEval(self.expb,varb,self.varmapb):
            return True
        if len(vara - set(self.varmapa.keys())) > len(varb - set(self.varmapb.keys())):
            return 'Unknown_var'
        elif vara - set(self.varmapa.keys()) != varb - set(self.varmapb.keys()):
            return 'Unknown_var'
        self.expa = self.expa.replace("or"," or ").replace("flo or ","floor").replace(" or d","ord").replace("and"," and ")
        self.expb = self.expb.replace("or"," or ").replace("flo or ","floor").replace(" or d","ord").replace("and"," and ")
        self.expa = self.expa.replace("if"," if ").replace("else"," else ")
        self.expb = self.expb.replace("if"," if ").replace("else"," else ")
        samplevarset = vara - set(self.varmapa.keys())
        sampletime = 0
        ans = set()
        addsample = self.sample
        
        while sampletime < self.sample:
            #Logger.debug(sampletime)
            resa = None
            resb = None
            samplemap = self.sampleVar(samplevarset)
            #Logger.debug(samplemap)
            vmapa = copy.deepcopy(self.varmapa)
            vmapb = copy.deepcopy(self.varmapb)
            try:
                vmapa = self.addDict(vmapa,samplemap)
                resa = self.evalExp(self.expa,vmapa)
            except OverflowError:
                if self.max >= 10:
                    self.max /= 10
                continue
            except BaseException:
                return 'Unknown_base'
            try:
                vmapb = self.addDict(vmapb,samplemap)
                resb = self.evalExp(self.expb,vmapb)
            except OverflowError:
                if self.max >= 10:
                    self.max /= 10
                continue
            except BaseException:
                #pass
                return 'Unknown_base' #starchat py->jv PRODUCT_NODES_K_TH_LEVEL_TREE_REPRESENTED_STRING
            #
            if type(resa) == float or type(resb) == float:
                sub = -1
                try:
                    sub = abs(resa-resb)
                except:
                    return False
                if sub > 0.1:
                    return False 
            
            elif resa != resb:
                Logger.debug(self.expa)
                Logger.debug(self.expb)
                return False
            if type(resa) == type(True):
                ans.add(resa)
            if sampletime == self.sample - 1 and ((True in ans and False not in ans) or (False in ans and True not in ans)):
                self.sample += addsample
                if self.sample > 10 * addsample:
                    return True
            sampletime += 1
        return True
    def __init__(self,expa,expb,varmapa,varmapb,sample=100,vartypemap=None):
        self.specv = {}
        self.expa = expa
        self.expb = expb
        self.varmapa = varmapa
        self.varmapb = varmapb
        self.sample = sample
        self.max = 1000
        self.oracletypemap = vartypemap
