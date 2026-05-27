from PIL import Image, ImageDraw, ImageFont
import os

DIR = "/opt/projects/arquivos/screenshots"
os.makedirs(DIR, exist_ok=True)
FP = "/usr/share/fonts/truetype/dejavu/"

def gf(name, size):
    try: return ImageFont.truetype(FP+name, size)
    except: return ImageFont.load_default()

B24=gf("DejaVuSans-Bold.ttf",24); B20=gf("DejaVuSans-Bold.ttf",20)
B16=gf("DejaVuSans-Bold.ttf",16); B14=gf("DejaVuSans-Bold.ttf",14)
B12=gf("DejaVuSans-Bold.ttf",12); B11=gf("DejaVuSans-Bold.ttf",11)
B10=gf("DejaVuSans-Bold.ttf",10)
R12=gf("DejaVuSans.ttf",12); R11=gf("DejaVuSans.ttf",11)
R10=gf("DejaVuSans.ttf",10); R9=gf("DejaVuSans.ttf",9)
M11=gf("DejaVuSansMono.ttf",11)

P=(11,26,48); P20=(155,181,208); P5=(226,232,240); BG=(245,247,250); W=(255,255,255)
T=(11,26,48); T80=(60,74,94); T60=(109,122,142); T40=(158,170,190)
BORDA=(226,232,240); OK=(34,197,94); ER=(239,68,68)
AL=(245,158,11); INFO=(59,130,246)
PD=(155,181,208)

def rr(d,xy,r,fill,outline=None):
    d.rounded_rectangle(xy,radius=r,fill=fill,outline=outline,width=1 if outline else 0)

def sc(d,xy,r):
    x1,y1,x2,y2=xy
    d.rounded_rectangle([x1,y1+2,x2,y2+2],radius=r,fill=(220,225,235))

def tc(d,y,text,font,fill,w,x0=0):
    bb=d.textbbox((0,0),text,font=font); tw=bb[2]-bb[0]
    d.text((x0+(w-tw)//2,y),text,font=font,fill=fill)

def sidebar(d,items,active_idx):
    d.rectangle([0,0,220,720],fill=P)
    rr(d,[16,14,48,46],8,W)
    d.text((54,16),"Sistema",font=B11,fill=W)
    d.text((54,32),"v2.0",font=R9,fill=P20)
    ny=76
    for i,(label,active) in enumerate(items):
        if i==active_idx:
            rr(d,[8,ny-4,212,ny+28],12,W)
            d.text((20,ny),label,font=B14,fill=P)
        else:
            d.text((20,ny),label,font=R12,fill=P20)
        ny+=36
    d.text((20,690),"(c) 2026",font=R9,fill=P20)
    d.line([(220,0),(220,720)],fill=BORDA)

def topbar(d,title,subtitle):
    d.rectangle([221,0,1280,56],fill=W)
    d.line([(221,56),(1280,56)],fill=BORDA)
    d.text((240,12),title,font=B20,fill=T)
    d.text((240,36),subtitle,font=R11,fill=T60)

def stat_cards(d,stats,cx,cy):
    for label,val,col in stats:
        sc(d,[cx-1,cy+2,cx+179,cy+82],12)
        rr(d,[cx,cy,cx+180,cy+80],12,W)
        cc=(col[0]//4,col[1]//4,col[2]//4)
        rr(d,[cx+12,cy+12,cx+40,cy+40],8,cc)
        d.text((cx+48,cy+14),label,font=R11,fill=T60)
        d.text((cx+12,cy+38),val,font=B20,fill=T)
        cx+=192

# ===== 1. SALTO GESTAO LOGIN =====
img=Image.new('RGB',(1280,720),BG); d=ImageDraw.Draw(img)
for y in range(720):
    p=y/720
    d.line([(0,y),(1280,y)],fill=(int(245+10*p),int(247+8*p),int(250+5*p)))
sc(d,[438,88,842,600],16)
rr(d,[440,90,840,598],16,W)
d.ellipse([576,130,704,258],fill=P)
tc(d,158,"SG",B24,W,128,576)
tc(d,280,"SaltoGestao",B20,P,400,440)
tc(d,312,"Sistema de Gestao Empresarial",R12,T60,400,440)
fy=350
for label,hint in [("Usuario","Digite seu usuario"),("Senha","Digite sua senha")]:
    d.text((470,fy),label,font=B10,fill=T60)
    fy+=16
    sc(d,[468,fy+2,812,fy+42],12)
    rr(d,[470,fy,810,fy+40],12,W,outline=BORDA)
    d.text((486,fy+12),hint,font=R12,fill=T40)
    fy+=54
sc(d,[468,fy+2,812,fy+48],12)
rr(d,[470,fy,810,fy+46],12,P)
tc(d,fy+12,"Entrar",B14,W,340,470)
tc(d,620,"Corumba Sistemas (c) 2026",R9,T40,1280)
img.save(os.path.join(DIR,"1-sg-login.png"))
print("OK: 1-sg-login.png")

# ===== 2. SALTO GESTAO DASHBOARD =====
img=Image.new('RGB',(1280,720),BG); d=ImageDraw.Draw(img)
sidebar(d,[("Dashboard",True),("Clientes",False),("Produtos",False),("Vendas",False),("Teste 100",False)],0)
topbar(d,"Dashboard","Bem-vindo, Admin!")
stat_cards(d,[("Clientes","142",P),("Produtos","87",INFO),("Vendas","326",OK),("Faturamento","R$ 48.2k",AL)],240,72)
d.line([(240,170),(1260,170)],fill=BORDA)
d.text((240,178),"Resumo do Negocio",font=B12,fill=T60)
ty=200
rr(d,[240,ty,1260,ty+24],0,(245,247,250),outline=BORDA)
d.text((252,ty+6),"DESCRICAO",font=B10,fill=T60)
d.text((600,ty+6),"STATUS",font=B10,fill=T60)
d.text((750,ty+6),"VALOR",font=B10,fill=T60)
ty+=24
for i,(desc,status,val) in enumerate([
    ("Venda #001 - Mercado Central","Concluida","R$ 45.90"),
    ("Venda #002 - Super Silva","Concluida","R$ 128.50"),
    ("Venda #003 - Joao da Feira","Pendente","R$ 32.00"),
]):
    ry=ty+i*36
    rr(d,[240,ry,1260,ry+36],0,W if i%2==0 else BG)
    d.line([(240,ry+36),(1260,ry+36)],fill=BORDA)
    d.text((252,ry+10),desc,font=R12,fill=T)
    sc2=OK if status=="Concluida" else AL
    rr(d,[600,ry+8,680,ry+26],12,(sc2[0]//4,sc2[1]//4,sc2[2]//4))
    tc(d,ry+10,status,B10,sc2,80,600)
    d.text((750,ry+10),val,font=M11,fill=OK)
img.save(os.path.join(DIR,"2-sg-dashboard.png"))
print("OK: 2-sg-dashboard.png")

# ===== 3. SALTO GESTAO CLIENTES =====
img=Image.new('RGB',(1280,720),BG); d=ImageDraw.Draw(img)
sidebar(d,[("Dashboard",False),("Clientes",True),("Produtos",False),("Vendas",False),("Teste 100",False)],1)
topbar(d,"Clientes","Gerencie seus clientes")
rr(d,[1020,14,1130,44],10,P)
tc(d,16,"Novo Cliente",B12,W,110,1020)
# Search
sc(d,[239,70,1261,112],12); rr(d,[240,72,1260,110],12,W)
d.text((256,82),"Buscar...",font=R12,fill=T40)
# Form
fy=124; d.text((240,fy),"Formulario",font=B14,fill=T); fy+=20
for l1,h1,l2,h2 in [("Nome completo","Ex: Joao Silva","CPF/CNPJ","000.000.000-00"),("E-mail","email@exemplo.com","Telefone","(62) 99999-9999")]:
    d.text((240,fy),l1,font=B10,fill=T60)
    sc(d,[239,fy+16,583,fy+52],12); rr(d,[240,fy+18,582,fy+50],12,W,outline=BORDA)
    d.text((256,fy+26),h1,font=R12,fill=T40)
    d.text((600,fy),l2,font=B10,fill=T60)
    sc(d,[599,fy+16,943,fy+52],12); rr(d,[600,fy+18,942,fy+50],12,W,outline=BORDA)
    d.text((616,fy+26),h2,font=R12,fill=T40)
    fy+=64
rr(d,[240,fy,340,fy+36],12,P); d.text((272,fy+10),"Salvar",font=B12,fill=W)
rr(d,[356,fy,456,fy+36],12,W,outline=BORDA); d.text((378,fy+10),"Limpar",font=R12,fill=P)
# Table
fy+=52; d.text((240,fy),"5 clientes cadastrados",font=R10,fill=T60); fy+=16
rr(d,[240,fy,1260,fy+22],0,(245,247,250),outline=BORDA)
d.text((252,fy+5),"NOME",font=B10,fill=T60)
d.text((480,fy+5),"CPF/CNPJ",font=B10,fill=T60)
d.text((640,fy+5),"TELEFONE",font=B10,fill=T60); fy+=22
for i,(nome,cpf,tel) in enumerate([("Joao Silva","123.456.789-00","(62) 99999-9999"),("Maria Santos","987.654.321-00","(11) 98888-8888"),("Pedro Costa","111.222.333-44","(21) 97777-7777")]):
    ry=fy+i*36
    rr(d,[240,ry,1260,ry+36],0,W if i%2==0 else BG)
    d.line([(240,ry+36),(1260,ry+36)],fill=BORDA)
    rr(d,[240,ry+2,272,ry+34],16,P)
    d.text((248,ry+10),nome[0],font=B12,fill=W)
    d.text((280,ry+4),nome,font=R12,fill=T)
    d.text((280,ry+18),cpf,font=R11,fill=T60)
    d.text((480,ry+4),tel,font=R12,fill=T80)
    rr(d,[900,ry+4,932,ry+30],8,(226,232,240))
    d.text((906,ry+10),"Editar",font=R10,fill=T60)
    rr(d,[940,ry+4,972,ry+30],8,(239//4,68//4,68//4))
    d.text((946,ry+10),"Excluir",font=R10,fill=ER)
img.save(os.path.join(DIR,"3-sg-clientes.png"))
print("OK: 3-sg-clientes.png")

# ===== 4. CORUBA FOOD DASHBOARD =====
img=Image.new('RGB',(1280,720),BG); d=ImageDraw.Draw(img)
sidebar(d,[("Dashboard",True),("Mesas",False),("Pedidos",False),("Cardapio",False),("Delivery",False)],0)
topbar(d,"Dashboard","Ola, Garcom!")
stat_cards(d,[("Pedidos","28",P),("Vendas","14",OK),("Faturamento","R$ 2.847",AL),("Ticket Medio","R$ 203",INFO)],240,72)
d.line([(240,170),(1260,170)],fill=BORDA)
d.text((240,178),"Status das Mesas",font=B12,fill=T60)
for i in range(12):
    col,row=i%4,i//3
    mx,my=240+col*158,202+row*72
    st="Livre" if i%3!=2 else "Ocupada"
    c=OK if st=="Livre" else ER
    sc(d,[mx-1,my+2,mx+147,my+66],12)
    rr(d,[mx,my,mx+148,my+64],12,W)
    d.text((mx+10,my+10),"Mesa "+str(i+1),font=B12,fill=T)
    d.ellipse([mx+126,my+12,mx+138,my+24],fill=c)
    d.text((mx+10,my+32),st,font=R10,fill=c)
img.save(os.path.join(DIR,"4-cf-dashboard.png"))
print("OK: 4-cf-dashboard.png")

# ===== 5. CORUBA FOOD CARDAPIO =====
img=Image.new('RGB',(1280,720),BG); d=ImageDraw.Draw(img)
sidebar(d,[("Dashboard",False),("Mesas",False),("Pedidos",False),("Cardapio",True),("Delivery",False)],3)
topbar(d,"Cardapio","Produtos do restaurante")
cx2=240
for label,active in [("Todos",True),("Lanches",False),("Porcoes",False),("Bebidas",False),("Sobremesas",False)]:
    w=len(label)*7+20
    rr(d,[cx2,68,cx2+w,92],12,P if active else P5)
    tc(d,72,label,B10 if active else R10,W if active else T60,w,cx2)
    cx2+=w+6

prods=[("X-Burger","R$ 22.90","La",P),("X-Tudo","R$ 28.90","La",P),("Picanha","R$ 52.00","Po",OK),("Batata Frita","R$ 15.90","Po",OK),("Coca-Cola","R$ 9.90","Be",INFO),("Suco Natural","R$ 12.00","Be",INFO),("Pudim","R$ 10.00","So",AL),("Acai 500ml","R$ 18.90","So",AL)]
for i,(nome,preco,abrev,col) in enumerate(prods):
    px,py=240+(i%4)*220,108+(i//4)*150
    sc(d,[px-1,py+2,px+207,py+142],12)
    rr(d,[px,py,px+208,py+140],12,W)
    rr(d,[px+8,py+8,px+200,py+72],12,(col[0]//5,col[1]//5,col[2]//5))
    tc(d,py+28,abrev,B16,col,192,px+8)
    d.text((px+10,py+82),"Em estoque",font=R9,fill=T40)
    d.text((px+10,py+96),nome,font=B16,fill=T)
    d.text((px+10,py+116),preco,font=B14,fill=OK)
img.save(os.path.join(DIR,"5-cf-cardapio.png"))
print("OK: 5-cf-cardapio.png")

print("\n=== SCREENSHOTS GERADOS ===")
for f in sorted(os.listdir(DIR)):
    sz=os.path.getsize(os.path.join(DIR,f))
    print("  "+f+" ("+str(sz//1024)+" KB)")
