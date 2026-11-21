import json,os,urllib.request,random
E=os.getenv("MAKEFUN_ENV_URL")
_r=random.Random(99)
Z=[[_r.getrandbits(64) for _ in range(64)] for _ in range(15)]
ZS=_r.getrandbits(64)
ZC=[_r.getrandbits(64) for _ in range(16)]
V=(0,100,320,330,500,900,0)
def D(x):return[ord(c)-48 for c in x]
PR=D("0005:DS0")
NT=D(" (.33.( ")
BT=D("'-1331-'")
RT=D("033333>0");RF=D("-012210-")
QT=D(")-/11/-)")
KMR=D("<81)#");KMF=D(">@3++3@>")
KET=D("%.55.%")
PS={1:(PR,PR),2:(NT,NT),3:(BT,BT),4:(RT,RF),5:(QT,QT)}
KN=tuple((df,dr) for df in(-2,-1,1,2) for dr in(-2,-1,1,2) if abs(df)+abs(dr)==3)
K8=((-1,-1),(-1,1),(1,-1),(1,1),(-1,0),(1,0),(0,-1),(0,1))
BD=K8[:4];RD=K8[4:]
INF=10**7;MATE=1000000;CRR={0:-3,7:-2,56:-9,63:-5}
B=[0]*64;SD=0;CA=0;EP=-1;HF=0;KEY=0
TT={};KILL={};HH={};NODES=0;LIMIT=40000;STOP=False;KS=[4,60]
HIST=set()


def A(s,by):
 f0=s&7;r0=s>>3
 for dx,pc in((-9,1),(-7,1))if by==0 else((7,9),(9,9)):
  x=s+dx
  if 0<=x<64 and abs((x&7)-f0)==1 and B[x]==pc:return True
 nw,kw=(2,6) if by==0 else (10,14)
 for D,W in((KN,(nw,)),(K8,(kw,))):
  for df,dr in D:
   ff,rr=f0+df,r0+dr
   if 0<=ff<8 and 0<=rr<8 and B[rr*8+ff] in W:return True
 f=s&7;r=s>>3
 for df,dr in K8:
  W=(3,5) if df and dr else(4,5)
  ff,rr=f+df,r+dr
  while 0<=ff<8 and 0<=rr<8:
   p=B[rr*8+ff]
   if p:
    if (p<8)==(by==0) and (p&7) in W:return True
    break
   ff+=df;rr+=dr
 return False

def G(co=False):
 ms=[];w=SD==0
 for s in range(64):
  p=B[s]
  if not p or (p<8)!=w:continue
  t=p&7;f=s&7;r=s>>3
  if t==1:
   d=8 if w else -8;home=1 if w else 6;last=6 if w else 1
   for df in(-1,0,1):
    if df and not(0<=f+df<8):continue
    to=s+d+df;q=B[to]
    if df==0:
     if q:continue
     if r==last:
      for pr in(5,4,3,2):ms.append((s,to,pr))
     elif not co:
      ms.append((s,to,0))
      if r==home and not B[s+2*d]:ms.append((s,s+2*d,0))
    elif(q and(q<8)!=w)or to==EP:
     if r==last:
      for pr in(5,4,3,2):ms.append((s,to,pr))
     else:ms.append((s,to,0))
  else:
   D=KN if t==2 else BD if t==3 else RD if t==4 else K8
   for df,dr in D:
    ff,rr=f+df,r+dr
    while 0<=ff<8 and 0<=rr<8:
     to=rr*8+ff;q=B[to]
     if q:
      if (q<8)!=w:ms.append((s,to,0))
      break
     if not co:ms.append((s,to,0))
     if t in(2,6):break
     ff+=df;rr+=dr
 if not co and not A(KS[SD],1-SD):
  for bit,fr,to,emp,saf in((1,4,6,(5,6),(5,6)),(2,4,2,(1,2,3),(2,3)),(4,60,62,(61,62),(61,62)),(8,60,58,(57,58,59),(58,59)))[SD*2:SD*2+2]:
   if CA&bit and all(not B[x] for x in emp) and all(not A(x,1-SD) for x in saf):ms.append((fr,to,0))
 return ms

def MK(m):
 global SD,CA,EP,HF,KEY
 s,to,pr=m;p=B[s];t=p&7;w=p<8
 cap=B[to];ecs=-1
 if t==1 and to==EP and not cap:
  ecs=to-8 if w else to+8;cap=B[ecs]
 undo=(cap,CA,EP,HF,KEY,ecs)
 KEY^=Z[p][s]^ZC[CA]
 if ecs>=0:KEY^=Z[cap][ecs];B[ecs]=0
 elif cap:KEY^=Z[cap][to]
 B[s]=0
 np=(pr if w else pr+8) if pr else p
 B[to]=np;KEY^=Z[np][to]
 if t==6:KS[0 if w else 1]=to
 if t==6 and abs(to-s)==2:
  rf,rt=((7,5) if to>s else (0,3))
  if s>7:rf+=56;rt+=56
  rp=B[rf];B[rf]=0;B[rt]=rp;KEY^=Z[rp][rf]^Z[rp][rt]
 if t==6:CA&=-4 if w else -13
 for x in(s,to):CA&=CRR.get(x,-1)
 EP=-1
 if t==1 and abs(to-s)==16:EP=(s+to)//2
 KEY^=ZC[CA]^ZS
 HF=0 if t==1 or cap else HF+1
 SD=1-SD
 return undo

def UM(m,undo):
 global SD,CA,EP,HF,KEY
 s,to,pr=m;cap,CA,EP,HF,KEY,ecs=undo
 SD=1-SD;w=SD==0
 p=B[to]
 if pr:p=1 if w else 9
 B[s]=p;B[to]=0
 if (p&7)==6:KS[0 if w else 1]=s
 if ecs>=0:
  B[ecs]=9 if w else 1
 elif cap:
  B[to]=cap
 if (p&7)==6 and abs(to-s)==2:
  rf,rt=((7,5) if to>s else (0,3))
  if s>7:rf+=56;rt+=56
  B[rf]=B[rt];B[rt]=0

def EV():
 s=0;ph=0;bp=[0,0];pf=[[],[]];ps=[[],[]];kg=[0,0]
 for sq in range(64):
  p=B[sq]
  if not p:continue
  t=p&7;w=p<8;r=sq>>3;f=sq&7;i=0 if w else 1
  if t<6:ph+=1 if t in(2,3) else 2 if t==4 else 4
  rr=r if w else 7-r
  if t==6:kg[i]=(KMR[rr]+KMF[f],KET[rr]+KET[f])
  else:
   a,b=PS[t];v=V[t]+a[rr]+b[f];s+=v if w else -v
 if ph>24:ph=24
 for i in(0,1):
  mg,eg=kg[i];kv=(mg*ph+eg*(24-ph))//24
  s+=kv if i==0 else -kv
 return s if SD==0 else -s

def CK():
 global NODES,STOP
 if STOP:return 1
 NODES+=1
 if NODES>LIMIT:STOP=True;return 1
 return 0

def Q(a,b,ply):
 if CK():return 0
 if HF>=100:return 0
 inch=A(KS[SD],1-SD)
 if inch:
  ms=G()
 else:
  st=EV()
  if st>=b:return st
  if st>a:a=st
  ms=G(True)
 ms.sort(key=lambda m:-(V[B[m[1]]&7]*10-V[B[m[0]]&7]//10))
 best=-INF
 for m in ms:
  u=MK(m)
  if A(KS[1-SD],SD):
   UM(m,u);continue
  v=-Q(-b,-a,ply+1)
  UM(m,u)
  if v>best:best=v
  if v>a:a=v
  if a>=b:break
 if best==-INF:
  return -MATE+ply if inch else EV()
 return best

def S(d,a,b,ply):
 global SD,EP,HF,KEY
 if CK():return 0
 e=TT.get(KEY)
 if e and ply>0 and e[0]>=d:
  if e[2]==0:return e[1]
  if e[2]==1 and e[1]>=b:return e[1]
  if e[2]==2 and e[1]<=a:return e[1]
 inch=A(KS[SD],1-SD)
 if d<=0:return Q(a,b,ply)
 if not inch and ply>0 and d>=3 and EV()>=b and any((p&7)>1 and (p&7)<6 and (p<8)==(SD==0) for p in B):
  u=(EP,KEY);KEY^=ZS;EP=-1;HF+=1;SD=1-SD
  v=-S(d-3,-b,-b+1,ply+1)
  EP,KEY=u;SD=1-SD;HF-=1
  if v>=b:return v
 ms=G()
 tm=e[3] if e else None
 L=sorted(((10**10 if m==tm else 10**8+(B[m[1]]&7)*10-(B[m[0]]&7) if B[m[1]] else 10**7 if m==KILL.get(ply) else HH.get(m,0)),m) for m in ms)
 best=-INF;bm=None;aa=a;i=0
 for sc,m in reversed(L):
  u=MK(m);q0=not u[0] and not m[2]
  if A(KS[1-SD],SD):
   UM(m,u);continue
  if KEY in HIST or HF>=100:v=0
  else:
   HIST.add(KEY)
   quiet=q0
   if i==0:
    v=-S(d-1,-b,-a,ply+1)
   else:
    rd=d-2 if d>=3 and quiet and not inch and i>2 else d-1
    v=-S(rd,-a-1,-a,ply+1)
    if v>a and rd<d-1:v=-S(d-1,-a-1,-a,ply+1)
    if a<v<b:v=-S(d-1,-b,-a,ply+1)
   HIST.discard(KEY)
  UM(m,u)
  i+=1
  if v>best:best=v;bm=m
  if v>a:a=v
  if a>=b:
   if q0:KILL[ply]=m;HH[m]=HH.get(m,0)+d*d
   break
 if bm is None:
  return -MATE+ply if inch else 0
 fl=0 if aa<best<b else 1 if best>=b else 2
 if not STOP:TT[KEY]=(d,best,fl,bm)
 return best

def RT():
 global NODES,STOP
 TT.clear();HH.clear();KILL.clear()
 ms=G()
 legal=[]
 for m in ms:
  u=MK(m)
  if not A(KS[1-SD],SD):legal.append(m)
  UM(m,u)
 if not legal:return None
 best=legal[0];NODES=0;STOP=False
 d=1
 while NODES<=LIMIT:
  bb=-INF;bm=best
  for m in legal:
   u=MK(m);HIST.add(KEY)
   v=-S(d-1,-INF,INF,1)
   HIST.discard(KEY);UM(m,u)
   if v>bb:bb=v;bm=m
  if STOP:break
  best=bm
  if bb>MATE-1000:break
  d+=1
 return best

B0=[4,2,3,5,6,3,2,4]+[1]*8+[0]*32+[9]*8+[12,10,11,13,14,11,10,12]
def HK(moves):
 global B,SD,CA,EP,HF,KEY
 B=list(B0);SD=0;CA=15;EP=-1;HF=0;KS[0]=4;KS[1]=60;KEY=0
 for sq in range(64):
  if B[sq]:KEY^=Z[B[sq]][sq]
 KEY^=ZC[15]
 ks=[KEY]
 for u in moves:
  s=(ord(u[0])-97)+(ord(u[1])-49)*8;to=(ord(u[2])-97)+(ord(u[3])-49)*8
  pr="nbrq".index(u[4])+2 if len(u)>4 else 0
  MK((s,to,pr));ks.append(KEY)
 return ks

def UC(m):
 s,to,pr=m
 return chr((s&7)+97)+chr((s>>3)+49)+chr((to&7)+97)+chr((to>>3)+49)+("nbrq"[pr-2] if pr else"")

def PO(path,body):
 req=urllib.request.Request(E+path,json.dumps(body).encode(),{"content-type":"application/json"})
 with urllib.request.urlopen(req) as res:return json.load(res)

def MN2():
 while True:
  g=PO("/game",{})
  if g["status"]=="done":break
  while g["status"]=="your_move":
   global HIST
   HIST=set(HK(g["moves"]))
   m=RT()
   u=UC(m) if m else ""
   mv=u if u in g["legal_moves"] else g["legal_moves"][0]
   g=PO("/move",{"game":g["game"],"move":mv})

if __name__=="__main__":
 MN2()
