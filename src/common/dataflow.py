import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from common.util import removeBlank,extractVarInExp,simplifyExpByDR,Logger
import copy
from lang_processer.cfg import CFG
class DataFlowAnalysis:
    def __init__(self,cfg:CFG):
        self.cfg = cfg
        self.reverse = False
        '''for node in self.cfg.nodelist:
            node['IN'] = []
            node['OUT'] = []'''
        self.tmpudmap = {}
        for index,node in enumerate(self.cfg.nodelist):
            newud = []
            packvar = []
            changeflg = False
            for ud in node['UD']:
                
                if 'lv' in ud[3] and ud[3]['lv'].find(",") != -1:
                    varlist = []
                    for var in ud[3]['lv'].split(","):
                        changeflg = True
                        var = var.strip()
                        varlist.append(var)
                    if packvar == varlist:
                        continue
                    else:
                        ud1 = (varlist,ud[1],ud[2],ud[3])
                        packvar = copy.deepcopy(varlist)
                        
                        newud.append(ud1)
                else:
                    newud.append(ud)
            if changeflg:
                self.tmpudmap[index] = node['UD']
                node['UD'] = newud
    
    def printINOUT(self):
        for node in self.cfg.nodelist:
            Logger.debug("index:"+str(node["index"])+"in:"+str(node["IN"])+",out:"+str(node["OUT"]))
    def resetUD(self):
        for i,udlis in self.tmpudmap.items():
            self.cfg.nodelist[i]['UD'] = udlis
    def traverse(self,mode):
        #Logger.debug(self.cfg.dataflow)

        if self.reverse == False:
            beginnode = self.cfg.nodelist[0]
            nextguide = "succ"
        else:
            beginnode = self.cfg.nodelist[-1]
            nextguide = "pred"
        if mode <= 1:
            self.cfg.initTraState()
            self.DFS(beginnode,nextguide)
        elif mode >= 2:
            while not self.checkSame():
                self.cfg.initTraState()
                self.DFS_2(beginnode,nextguide)
    def checkSame(self):
        raise NotImplementedError    
    def nodeInduct(self,node,guide):
        raise NotImplementedError
    def union(self,node,outs):
        #Logger.debug("union " + str(node['index']))
        raise NotImplementedError
    def DFS_2(self,node,nextguide):
        lastguide = 'pred' if nextguide == 'succ' else 'succ'
        node['trastate'] = 'grey'
        self.union(node,node[lastguide])
        self.nodeInduct(node)
        for nextnodeind in node[nextguide]:
            nextnode = self.cfg.getNode(nextnodeind)
            if nextnode['trastate'] != 'white':
                continue
            self.DFS(nextnode,nextguide)
        node['trastate'] = 'black'
    def DFS(self,node,nextguide):
        #Logger.debug('enter:'+str(node['index']))
        lastguide = 'pred' if nextguide == 'succ' else 'succ'
        reunionflg = False
        for lastnodeind in node[lastguide]:
            if 'allcontent' in node and lastnodeind in node['allcontent']:
                reunionflg = True
                continue
            lastnode = self.cfg.getNode(lastnodeind)
            if lastnode['trastate'] == 'white':
                #Logger.debug('exit:'+str(node['index']))
                return
        #Logger.debug('firstunion')
        node['trastate'] = 'grey'
        self.union(node,node[lastguide])
        self.nodeInduct(node)
        firnodes = []
        secnodes = []
        if reunionflg:
            for nextnodeind in node[nextguide]:
                if nextnodeind in node['allcontent']:
                    firnodes.append(nextnodeind)
                else:
                    secnodes.append(nextnodeind)
        else:
            firnodes = node[nextguide]
        for nextnodeind in firnodes:
            nextnode = self.cfg.getNode(nextnodeind)
            if nextnode['trastate'] != 'white':
                continue
            self.DFS(self.cfg.getNode(nextnodeind),nextguide)
        if len(secnodes) != 0:
            
            if len(firnodes) != 0:
                #Logger.debug('reunion')
                self.union(node,node[lastguide])
                self.nodeInduct(node)
            
            for nextnodeind in secnodes:
                nextnode = self.cfg.getNode(nextnodeind)
                if nextnode['trastate'] != 'white':
                    continue
                self.DFS(self.cfg.getNode(nextnodeind),nextguide)
        '''traversednodes = []
        for nextnodeind in node[nextguide]:
            nextnode = self.cfg.getNode(nextnodeind)
            if nextnode['trastate'] == 'grey':
                continue
            if type(reunionflg) == type(True) and reunionflg and 'content' in node and nextnodeind in node['content']:
                traversednodes.append(nextnodeind)
            elif type(reunionflg) == type(True) and 'content' in node and set(traversednodes) == set(node['content']):
                self.union(node,node[lastguide])
                reunionflg = None
            if reunionflg and 'allcontent' in node and nextnodeind not in node['allcontent']:
                #Logger.debug("reunion")
                #Logger.debug(nextnodeind)
                self.union(node,node[lastguide])
                reunionflg = False
            self.DFS(nextnode,nextguide)'''
        node['trastate'] = 'black'  

class ConditionReach(DataFlowAnalysis):
    def __init__(self, cfg: CFG,mode=1):
        super().__init__(cfg)
        if str(type(self)) in self.cfg.dataflow:
            if self.cfg.dataflow[str(type(self))] == mode:
                return
        self.cfg.dataflow[str(type(self))] = mode
        self.mode = mode
        for node in self.cfg.nodelist:
            #Logger.debug(node)
            node['CRIN'] = {'CRSIBIN':set(),'CRPARIN':set()}
            node['CROUT'] = {'CRSIBOUT':set(),'CRPAROUT':set()}     
        self.traverse(mode)        
    def union(self,node,outs):
        '''if node['trastate'] == 'grey':
            return'''
        if len(node['CROUT']['CRSIBOUT'])+len(node['CROUT']['CRPAROUT']) > 0:
            return
        #Logger.debug("union " + str(node['index']))
        indic = {}
        pars = []
        sibs = []
        if node['index'] == 4:
            1
        firstchild = None
        if node['index'] in self.cfg.pardic:
            parnode = self.cfg.getNode(self.cfg.pardic[node['index']])
            pars.append(parnode['CROUT']['CRPAROUT'])
        for outind in outs:
            outnode = self.cfg.getNode(outind)
            #pars.append(outnode['CROUT']['CRPAROUT'])
            '''if node['index'] in self.cfg.pardic and outind == self.cfg.pardic[node['index']]:
                pars.append(outnode['CROUT']['CRPAROUT'])
                cnt = 0
                for cont in outnode['content']:
                    contnode = self.cfg.getNode(cont)
                    if contnode['trastate'] != 'white':
                        cnt += 1
                if cnt == 1:
                    firstchild = True
                else:
                    firstchild = False'''
            if node['deep'] == outnode['deep']:
                sibs.append(outnode['CROUT']['CRSIBOUT'])
            '''if outind == self.cfg.pardic[node['index']]:
                node['CRIN']['CRPARIN'] |= outnode['CROUT']['CRPAROUT']
            elif outind in self.cfg.sibdic[node['index']]:
                node['CRIN']['CRSIBIN'] |= outnode['CROUT']['CRSIBOUT']
            elif node['index'] == self.cfg.pardic[outind]:
                node['CRIN']['CRSIBIN'] |= outnode['CROUT']['CRSIBOUT']'''
        #node['firstchild'] = firstchild
        parin,sibin = set(),set()
        for par in pars:
            parin |= par
        for sib in sibs:
            sibin |= sib
        
        node['CRIN'] = {'CRPARIN':parin,"CRSIBIN":sibin}
    def inferForExtraCond(self,node):
        newcond = []
        if node['type'] == "for_init":
            inits,updates = node['init'],node['update']
            initdic,updatedic = {},{}
            for it in inits:
                if "=" in it:
                    lv = it.split("=")[0].strip().replace('int ','').replace('float ','').strip()
                    rv = it.split("=")[1].strip()
                    initdic[lv] = rv
            for udt in updates:
                vars = extractVarInExp(udt,True)
                if len(vars) > 0:
                    udtv = vars[0]
                    if '+' in udt:
                        updatedic[udtv] = '+'
                    elif '-' in udt:
                        updatedic[udtv] = '-'
                    else:
                        updatedic[udtv] = "Unknown"
            
            for lv,rv in initdic.items():
                if lv in updatedic:
                    if updatedic[lv] == '+':
                        newcond.append(f"{lv}>={rv}")
                    elif updatedic[lv] == '-':
                        newcond.append(f"{lv}<={rv}")
        return newcond
    def nodeInduct(self,node):
        if node['index'] == 4:
            1
        '''if node['trastate'] == 'grey':
            return'''
        if len(node['CROUT']['CRSIBOUT'])+len(node['CROUT']['CRPAROUT']) > 0:
            return
        parinconds = copy.deepcopy(node['CRIN']['CRPARIN'])
        sibinconds =  copy.deepcopy(node['CRIN']['CRSIBIN'])
        nodecond = set()
        if 'condition' in node:
            if type(node['condition']) == type([]):
                if node["type"] == "for_init":
                    conds = node['condition'] + self.inferForExtraCond(node)
                else:
                    conds = node['condition']
                nodecond = set(conds)
            else:
                if node['condition'] != None and node['condition'] != '':
                    nodecond = set([node['condition']])
            parinconds |= nodecond
        #node['CRIN']['CRPARIN'] = node['CRIN']['CRPARIN'] - nodecond
        #node['CRIN']['CRSIBIN'] = node['CRIN']['CRSIBIN'] - nodecond
        for ud in node['UD']:
            if ud[1] == 'D' or ud[1] == 'RD':
                defvar = []
                if type(ud[0]) != type([]):
                    defvar.append(ud[0])
                else:
                    defvar = ud[0]
                for dev in defvar:
                    if node['index'] in self.cfg.pardic and self.cfg.pardic[node['index']] != -1:
                        partype = self.cfg.getNode(self.cfg.pardic[node['index']])
                        if partype in ['if_init','elif_init','else_init']:
                            parinconds = set([cond for cond in parinconds if dev not in extractVarInExp(removeBlank(cond))])
                    sibinconds = set([cond for cond in sibinconds if dev not in extractVarInExp(removeBlank(cond))])
        #if 'condition' in node and node['condition'] != "" and 'return' in node and node['return'] == True:
        if 'condition' in node and node['condition'] != "" and node['type'] in ['if_init','elif_init']:    
            sibinconds |= set(["Not("+node['condition']+")"])
        node['CROUT']['CRPAROUT'] = parinconds
        '''if 'firstchild' in node and node['firstchild'] == True:
            node['CROUT']['CRSIBOUT'] = (parinconds | sibinconds) - nodecond
        else:'''
        node['CROUT']['CRSIBOUT'] = sibinconds
class DefineReach(DataFlowAnalysis):
    def __init__(self, cfg: CFG,mode=1):
        super().__init__(cfg)
        self.banvar = ['inf','sys','math','Math','sqrt','min','max',"'inf'","Integer","MIN_VALUE","MAX_VALUE","Arrays","PI","Character","System","out","Collections","collections","reverse","length","String","deque","LITERALNUMBER","np","start","len"]
        self.definemap = {}
        self.useinfo = {}
        self.defnum = 0  
        if str(type(self)) in self.cfg.dataflow:
            if self.cfg.dataflow[str(type(self))] == mode:
                return
        self.cfg.dataflow[str(type(self))] = mode
        self.mode = mode
        for node in self.cfg.nodelist:
            node['DRIN'] = {}
            node['DROUT'] = {}
            for ud in node['UD']:
                if ud[1] == "D" or ud[1] == "RD":
                    self.definemap[id(ud)] = (len(self.definemap),node['index'])
                    if type(ud[0]) == type([]):
                        self.defnum += len(ud[0])
                    else:
                        if ud[0] not in self.banvar:
                            #Logger.debug(ud[0])
                            self.defnum += 1
                    #Logger.debug(ud)
                    #Logger.debug(self.definemap[id(ud)])
        self.defaultDR = self.summarizeDR()
        #Logger.debug(self.definemap)
        self.traverse(mode)
    def summarizeDR(self):
        info = {}
        for node in self.cfg.nodelist:
            info[node['index']] = {'DRIN':node['DRIN'],'DROUT':node['DROUT']}
        return info
    def checkSame(self):
        curdr = self.summarizeDR()
        if curdr == self.defaultDR:
            self.lastDR = curdr
            return False
        else:
            flg = self.lastDR == curdr
            self.lastDR = curdr
            return flg
    def getDefine(self,ud):
        return self.definemap.get(id(ud))
    def getDefNums(self):
        return self.defnum
    
    
    def checkRV(self,desc):
        if desc == None:
            return ""
        if type(desc) == type({}) and 'lv' in desc and 'rv' in desc:
            lv = desc['lv']
            rv = removeBlank(desc['rv'])
            '''if lv.count('[') > 0:
                return None'''
            '''if rv.count('new') > 0:
                return None,None'''
            if 'div' in desc:
                divexprs = desc['div']
                for divexpr in divexprs:
                    rv = rv.replace(divexpr,divexpr.replace('/','//'))
            return lv,rv
            #return rv
        else:
            return "",""
    def inductUD(self,defs,ud,newudlis):
        import copy
        rdin = copy.deepcopy(defs)
        if ud[1] == 'D' or ud[1] == 'RD':
            if type(ud[0]) == type([]):
                lv,rv = self.checkRV(ud[3])
                if rv != None:
                    newset = set()
                    d = self.getDefine(ud)
                    newset.add((d[0],d[1],rv))
                    for v in ud[0]:
                        defs[v] = newset
                        #defs[v] = set([self.getDefine(ud)])
            else:
                lv,rv = self.checkRV(ud[3])
                if rv != None:
                    newset = set()
                    d = self.getDefine(ud)
                    if self.mode == 0:
                        numres = None
                        try:
                            simprv = simplifyExpByDR({},"",rv,rdin,{})
                            numres = eval(simprv.replace("/","//"))
                        except:
                            pass
                        if numres != None:
                            rv = str(numres)
                    newset.add((d[0],d[1],rv))
                    defs[ud[0]] = newset

                '''rv = self.checkRV(ud[3])
                if rv != None:
                    defs[ud[0]] = (set([self.getDefine(ud)]),rv)'''
            newudlis.append(ud)
        else:
            if ud[0] not in self.banvar:
                if ud[0] in defs:
                    definfo = defs[ud[0]]
                else:
                    definfo = None
                newudlis.append((ud[0],ud[1],ud[2],ud[3],definfo))
        return defs,newudlis
    def nodeInduct(self,node):
        #raise NotImplementedError
        
        defs = copy.deepcopy(node['DRIN'])
        newudlis = []
        for ud in node['UD']:
            defs,newudlis = self.inductUD(defs,ud,newudlis)
        node['UD'] = newudlis
        node['DROUT'] = defs

    def union(self,node,outs):
        #Logger.debug("union " + str(node['index']))
        indic = {}
        for outind in outs:
            outnode = self.cfg.getNode(outind)
            #Logger.debug(str(outnode['index']) + str(outnode['DROUT']))
            for v,deflis in outnode['DROUT'].items():
                if v not in indic:
                    indic[v] = set(deflis)
                else:
                    indic[v] = set(deflis) | indic[v]
        node['DRIN'] = indic