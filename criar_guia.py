#!/usr/bin/env python3
"""Guia Visual Completo - Corumbas Sistemas - PDF"""
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm, cm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable)
import os

output_path = "/opt/projects/Guia_Visual_Corumba_Sistemas.pdf"
doc = SimpleDocTemplate(output_path, pagesize=A4, rightMargin=2*cm, leftMargin=2*cm, topMargin=2*cm, bottomMargin=2*cm)

CP = colors.HexColor("#0b1a30")
CD = colors.HexColor("#84cc16")
CF = colors.HexColor("#f8fafc")
CB = colors.HexColor("#e2e8f0")
CW = colors.white
CR = colors.HexColor("#ef4444")

styles = getSampleStyleSheet()

def add_style(name, **kw):
    styles.add(ParagraphStyle(name=name, **kw))
    return styles[name]

ST = add_style('T', fontSize=22, leading=28, alignment=TA_CENTER, textColor=CP, spaceBefore=6*mm, spaceAfter=4*mm, fontName='Helvetica-Bold')
SS = add_style('S', fontSize=13, leading=18, textColor=CP, spaceBefore=4*mm, spaceAfter=2*mm, fontName='Helvetica-Bold')
SB = add_style('SB', fontSize=10.5, leading=14, textColor=CP, spaceBefore=3*mm, spaceAfter=1.5*mm, fontName='Helvetica-Bold')
SC = add_style('SC', fontSize=9, leading=13.5, textColor=colors.HexColor('#334155'), spaceAfter=2*mm, fontName='Helvetica', alignment=TA_JUSTIFY)
SCD = add_style('SCD', fontSize=7.5, leading=10.5, textColor=colors.HexColor('#1e293b'), fontName='Courier', spaceAfter=1*mm, backColor=colors.HexColor('#f1f5f9'), borderWidth=0.5, borderColor=CB, borderPadding=3*mm)
SD = add_style('SD', fontSize=8.5, leading=12.5, textColor=colors.HexColor('#1e40af'), fontName='Helvetica', leftIndent=3*mm, backColor=colors.HexColor('#eff6ff'), borderWidth=0.5, borderColor=colors.HexColor('#bfdbfe'), borderPadding=3*mm, spaceAfter=2*mm)
SI = add_style('SI', fontSize=9, leading=13, textColor=colors.HexColor('#334155'), fontName='Helvetica', leftIndent=5*mm, spaceAfter=0.5*mm)
Scenter = add_style('Scenter', fontSize=8, leading=11, textColor=CB, alignment=TA_CENTER, fontName='Helvetica')

def hr(): return HRFlowable(width='100%', thickness=1, color=CB, spaceAfter=2*mm, spaceBefore=1*mm)
def sp(h=3*mm): return Spacer(1, h)

def tmake(data, cols):
    t = Table(data, colWidths=cols)
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,0), CP), ('TEXTCOLOR',(0,0),(-1,0), CW),
        ('FONTNAME',(0,0),(-1,0),'Helvetica-Bold'), ('FONTSIZE',(0,0),(-1,-1), 8),
        ('ALIGN',(0,0),(-1,0),'CENTER'), ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
        ('GRID',(0,0),(-1,-1), 0.5, CB),
        ('ROWBACKGROUNDS',(0,1),(-1,-1), [CW, CF]),
        ('TOPPADDING',(0,0),(-1,-1), 5), ('BOTTOMPADDING',(0,0),(-1,-1), 5),
        ('LEFTPADDING',(0,0),(-1,-1), 6), ('RIGHTPADDING',(0,0),(-1,-1), 6),
    ]))
    return t

story = []
C = story.append

# === CAPA ===
C(sp(3*cm))
C(Paragraph("GUIA VISUAL COMPLETO", ST))
C(Paragraph("Corumba Sistemas", add_style('ST2', fontSize=20, leading=26, alignment=TA_CENTER, textColor=CD, spaceAfter=3*mm, fontName='Helvetica-Bold')))
C(Paragraph("SaltoGestao + MesaPronta - Guia para Iniciantes", add_style('ST3', fontSize=11, leading=16, alignment=TA_CENTER, textColor=colors.HexColor('#64748b'), fontName='Helvetica')))
C(sp(8*mm))
tr = [["Sistema","Tecnologia","Tipo","Arquivos de estilo"],
      ["SaltoGestao","Next.js + Tailwind CSS","Web (navegador)","globals.css + page.tsx"],
      ["MesaPronta","JavaFX + FXML","Desktop (Java)","LoginView.fxml + PrincipalView.fxml"]]
C(tmake(tr, [3*cm, 3.5*cm, 3*cm, 7*mm]))
C(sp(5*mm))
C(Paragraph("Como usar: Cada secao explica ONDE esta o arquivo, QUAL cor mudar e O QUE editar - passo a passo para quem esta comecando.", SD))
C(PageBreak())

# === INDICE ===
C(Paragraph("INDICE", ST))
C(hr())
for item in ["1. PARTE 1 - SALTOGESTAO (Web)","   1.1 Paleta de Cores","   1.2 globals.css (Estilo Global)","   1.3 Como Mudar as Cores do Sistema","   1.4 Pagina de Login do Cliente","   1.5 Dashboard do Cliente","   1.6 Login do Administrador","   1.7 Dashboard do Admin","   1.8 Lista de Clientes","   1.9 Cadastro de Cliente","   1.10 Classes Tailwind Mais Usadas","","2. PARTE 2 - MESAPRONTA (Desktop)","   2.1 Paleta de Cores","   2.2 Diferenca: CSS vs FXML","   2.3 Tela de Login","   2.4 Tela Principal","   2.5 Como Mudar Cores no JavaFX","","3. REFERENCIA RAPIDA","   3.1 Tabela de Cores Completas","   3.2 Localizacao dos Arquivos","   3.3 Comandos para Rebuild"]:
    C(Paragraph(item, SI) if item else sp(2*mm))
C(PageBreak())

# === PARTE 1: SALTOGESTAO ===
C(Paragraph("=============================", Scenter))
C(Paragraph("PARTE 1 - SALTOGESTAO", add_style('p1', fontSize=26, leading=32, alignment=TA_CENTER, textColor=CP, fontName='Helvetica-Bold')))
C(Paragraph("Sistema Web - Next.js + Tailwind CSS", add_style('p1s', fontSize=12, leading=17, alignment=TA_CENTER, textColor=CD, fontName='Helvetica-Bold')))
C(Paragraph("=============================", Scenter))
C(sp(4*mm))
C(Paragraph("O SaltoGestao e um sistema web acessado pelo navegador. Ele usa Next.js com Tailwind CSS para estilizacao. As cores sao controladas por classes Tailwind nos arquivos .tsx e no globals.css global.", SC))

C(Paragraph("1.1 - Paleta de Cores do SaltoGestao", SS))
C(hr())
C(Paragraph("Estas sao as principais cores do sistema. Mude os codigos hex abaixo para personalizar:", SC))
C(sp(2*mm))
cores = [
    ["Cor","Hex","Onde Usar"],
    ["Azul Escuro","#0b1a30","Headers, titulos, texto principal"],
    ["Verde Limao","#84cc16","Botoes, links, destaques, foco de inputs"],
    ["Verde Escuro","#65a30d","Hover dos botoes verdes"],
    ["Cinza Fundo","#f8fafc","Fundo das paginas"],
    ["Cinza Borda","#e2e8f0","Bordas de cards, inputs, tabelas"],
    ["Cinza Texto","#64748b","Textos secundarios, descricoes"],
    ["Branco","#ffffff","Fundo de cards e inputs"],
    ["Verde Sucesso","#22c55e","Mensagens de sucesso, status Ativo"],
    ["Vermelho Erro","#ef4444","Mensagens de erro, status Inadimplente"],
    ["Amarelo Aviso","#f59e0b","Alertas e avisos"],
]
C(tmake(cores, [3.5*cm, 3*cm, 10*mm]))
C(sp(3*mm))
C(Paragraph("DICA: Para mudar a cor principal, procure #0b1a30 nos arquivos e substitua. Para mudar a cor de destaque, procure #84cc16.", SD))

C(PageBreak())
C(Paragraph("1.2 - Arquivo globals.css (Estilo Global)", SS))
C(hr())
C(Paragraph("O globals.css define estilos para TODAS as paginas. Fica em:", SC))
C(Paragraph("/opt/projects/SaltoGestao/frontend-web/app/globals.css", SD))
C(sp(2*mm))
C(Paragraph("Conteudo atual:", SB))
C(Paragraph('@import "tailwindcss";\n\n:root {\n  --background: #ffffff;\n  --foreground: #0b1a30;\n}\n\n@theme inline {\n  --color-background: var(--background);\n  --color-foreground: var(--foreground);\n}\n\n/* Forcar light mode */\n@media (prefers-color-scheme: dark) {\n  :root { --background: #ffffff; --foreground: #0b1a30; }\n}\n\nbody {\n  background: #ffffff;\n  color: #0b1a30;\n  font-family: Arial, Helvetica, sans-serif;\n}\n\ninput, select, textarea {\n  color: #0b1a30 !important;\n  background-color: #ffffff !important;\n}\n\nlabel { color: #0b1a30 !important; }', SCD))
C(sp(2*mm))
C(Paragraph("O que cada parte faz:", SB))
C(tmake([
    [":root","Define variaveis CSS. --background=fundo, --foreground=texto"],
    ["@theme inline","Configura tema do Tailwind com cores customizadas"],
    ["@media (dark)","Forca light mode mesmo com dark mode do SO"],
    ["body","Corpo da pagina: fundo branco, texto azul escuro, fonte Arial"],
    ["input,select,textarea","Garante texto escuro em campos de formulario"],
    ["label","Garante labels visiveis em azul escuro"],
], [3.5*cm, 13*mm]))

C(Paragraph("1.3 - Como Mudar as Cores (3 Metodos)", SS))
C(hr())
C(Paragraph("METODO 1: Mudar no globals.css (afeta todo o sistema)", SB))
C(Paragraph('/* Mudar fundo de branco para escuro */\nbody {\n  background: #1a1a2e;\n  color: #ffffff;\n}', SCD))
C(sp(2*mm))
C(Paragraph("METODO 2: Mudar classes Tailwind nos .tsx", SB))
C(Paragraph('/* ANTES: header azul escuro */\n<header className="bg-[#0b1a30] text-white px-8 py-5">\n\n/* DEPOIS: header vermelho */\n<header className="bg-[#dc2626] text-white px-8 py-5">\n\n/* DEPOIS: header roxo */\n<header className="bg-[#7c3aed] text-white px-8 py-5">', SCD))
C(sp(2*mm))
C(Paragraph("METODO 3: Usar nomes praticais do Tailwind", SB))
C(tmake([
    ["Classe","Cor","Hex Equivalente"],
    ["bg-blue-900","Azul escuro","#1e3a8a"],
    ["bg-blue-600","Azul medio","#2563eb"],
    ["bg-green-500","Verde","#22c55e"],
    ["bg-green-600","Verde escuro","#16a34a"],
    ["bg-red-500","Vermelho","#ef4444"],
    ["bg-red-600","Vermelho escuro","#dc2626"],
    ["bg-purple-600","Roxo","#7c3aed"],
    ["bg-yellow-500","Amarelo","#eab308"],
    ["bg-gray-100","Cinza claro","#f3f4f6"],
    ["bg-gray-900","Cinza escuro","#111827"],
    ["bg-white","Branco","#ffffff"],
    ["text-white","Texto branco","#ffffff"],
    ["text-gray-600","Texto cinza","#4b5563"],
], [4*cm, 3*cm, 6*mm]))

C(PageBreak())
C(Paragraph("1.4 - Pagina de Login do Cliente", SS))
C(hr())
C(Paragraph("Arquivo: frontend-web/app/login/page.tsx", SD))
C(sp(2*mm))
C(tmake([
    ["Elemento","Classe CSS","O que faz"],
    ["Fundo pagina","bg-gray-50","Cinza claro ao redor do card"],
    ["Card login","bg-white rounded-xl shadow-lg","Caixa branca com sombra"],
    ["Campo input","border border-gray-300 focus:ring-[#84cc16]","Borda cinza, verde ao clicar"],
    ["Botao Entrar","bg-[#84cc16] hover:bg-[#65a30d]","Verde limao, escurece no hover"],
    ["Mensagem erro","bg-red-50 border-red-200 text-red-700","Caixa vermelha clara"],
], [3.5*cm, 6*cm, 7*mm]))
C(sp(3*mm))
C(Paragraph("Mudar cor do botao de login:", SB))
C(Paragraph('/* ANTES */\nclassName="... bg-[#84cc16] text-[#0b1a30] hover:bg-[#65a30d] ..."\n\n/* AZUL */\nclassName="... bg-[#3b82f6] text-white hover:bg-[#2563eb] ..."\n\n/* ROXO */\nclassName="... bg-[#8b5cf6] text-white hover:bg-[#7c3aed] ..."', SCD))
C(sp(2*mm))
C(Paragraph("Mudar fundo da pagina:", SB))
C(Paragraph('/* ANTES */\n<div className="... bg-gray-50">\n\n/* ESCURO */\n<div className="... bg-[#0b1a30]">\n\n/* GRADIENTE */\n<div style={{background:"linear-gradient(135deg,#0b1a30,#1e3a5f)"}}>', SCD))
C(sp(2*mm))
C(Paragraph("Mudar card de login:", SB))
C(Paragraph('/* ANTES: branco */\n<div className="... bg-white rounded-xl shadow-lg ...">\n\n/* ESCURO */\n<div className="... bg-[#1a1a2e] rounded-xl shadow-2xl text-white ...">', SCD))

C(PageBreak())
C(Paragraph("1.5 - Dashboard do Cliente", SS))
C(hr())
C(Paragraph("Arquivo: frontend-web/app/dashboard/page.tsx", SD))
C(sp(2*mm))
C(tmake([
    ["Elemento","Classe CSS","Descricao"],
    ["Fundo","bg-gray-50 min-h-screen","Cinza claro, tela toda"],
    ["Header","bg-[#0b1a30] text-white","Barra azul escuro no topo"],
    ["Card produto","bg-white rounded-xl shadow-sm border","Card branco com sombra leve"],
    ["Status Ativo","bg-green-50 text-green-700 border-green-200","Badge verde claro"],
    ["Status Inadimplente","bg-red-50 text-red-700 border-red-200","Badge vermelho claro"],
    ["Botao acao","bg-[#84cc16] hover:bg-[#65a30d]","Verde limao"],
], [3.5*cm, 6*cm, 7*mm]))
C(sp(3*mm))
C(Paragraph("Mudar header do dashboard:", SB))
C(Paragraph('/* ANTES */\n<header className="bg-[#0b1a30] text-white ...">\n\n/* ROXO */\n<header className="bg-[#581c87] text-white ...">\n\n/* GRADIENTE */\n<header style={{background:"linear-gradient(90deg,#0b1a30,#1e3a5f)"}} ...>', SCD))

C(Paragraph("1.6 - Login do Administrador", SS))
C(hr())
C(Paragraph("Arquivo: frontend-web/app/admin/login/page.tsx", SD))
C(sp(2*mm))
C(Paragraph("A pagina de login do admin segue o mesmo padrao da do cliente. Mesmas regras se aplicam.", SC))
C(Paragraph("Exemplo: Mudar todo esquema de cores do admin:", SB))
C(Paragraph('bg-gray-50  ->  bg-slate-900     /* fundo escuro */\nbg-[#0b1a30]  ->  bg-slate-800   /* header cinza */\nbg-[#84cc16]  ->  bg-blue-600    /* botao azul */\nfocus:ring-[#84cc16]  ->  focus:ring-blue-500  /* foco azul */', SCD))

C(Paragraph("1.7 - Dashboard do Administrador", SS))
C(hr())
C(Paragraph("Arquivo: frontend-web/app/admin/dashboard/page.tsx", SD))
C(sp(2*mm))
C(tmake([
    ["Elemento","Classe CSS","Descricao"],
    ["Cards stat","bg-white rounded-xl border p-6","Cards brancos com numeros"],
    ["Numero","text-3xl font-extrabold text-[#0b1a30]","Valor em azul escuro"],
    ["Stat verde","text-3xl font-extrabold text-green-600","Numero verde (ativos)"],
    ["Stat vermelho","text-3xl font-extrabold text-red-600","Numero vermelho (inadimplentes)"],
    ["Tabela","bg-white rounded-xl border overflow-hidden","Tabela com bordas arredondadas"],
], [3*cm, 6.5*cm, 7*mm]))

C(PageBreak())
C(Paragraph("1.8 - Lista de Clientes (Admin)", SS))
C(hr())
C(Paragraph("Arquivo: frontend-web/app/admin/clientes/listar/page.tsx", SD))
C(sp(2*mm))
C(tmake([
    ["Elemento","Classe CSS","Descricao"],
    ["Header","bg-[#0b1a30] text-white","Barra azul escuro"],
    ["Botao Novo Cliente","bg-[#84cc16] text-[#0b1a30] font-bold","Verde limao"],
    ["Campo busca","border border-gray-300 focus:ring-[#84cc16]","Input com foco verde"],
    ["Select status","border border-gray-300 bg-white","Dropdown de filtro"],
    ["Linha tabela","hover:bg-gray-50","Highlight ao passar mouse"],
    ["Badge Ativo","bg-green-50 text-green-700 border-green-200","Verde claro"],
    ["Badge Inadimplente","bg-red-50 text-red-700 border-red-200","Vermelho claro"],
], [3.5*cm, 6*cm, 7*mm]))
C(sp(3*mm))
C(Paragraph("Mudar botao Novo Cliente:", SB))
C(Paragraph('/* ANTES */\nclassName="bg-[#84cc16] text-[#0b1a30] ... hover:bg-[#65a30d] hover:text-white"\n\n/* AZUL */\nclassName="bg-blue-600 text-white ... hover:bg-blue-700"\n\n/* ROXO */\nclassName="bg-purple-600 text-white ... hover:bg-purple-700"\n\n/* OUTLINE */\nclassName="border-2 border-[#84cc16] text-[#84cc16] ... hover:bg-[#84cc16] hover:text-white"', SCD))

C(Paragraph("1.9 - Cadastro de Cliente (Admin)", SS))
C(hr())
C(Paragraph("Arquivo: frontend-web/app/admin/clientes/criar/page.tsx", SD))
C(sp(2*mm))
C(tmake([
    ["Elemento","Classe CSS","Descricao"],
    ["Header","bg-[#0b1a30] text-white","Barra azul escuro"],
    ["Card formulario","bg-white rounded-xl border-gray-200 p-6","Card branco"],
    ["Label campos","text-xs font-bold text-[#0b1a30] uppercase","Rotulo azul escuro"],
    ["Input","border-gray-300 focus:ring-[#84cc16]","Campo com foco verde"],
    ["Card produto (nao selec.)","border-gray-200 hover:border-gray-300","Borda cinza"],
    ["Card produto (selec.)","border-[#84cc16] bg-green-50","Borda verde, fundo verde claro"],
    ["Botao Cadastrar","bg-[#84cc16] hover:bg-[#65a30d] hover:text-white","Verde limao"],
    ["Botao Cancelar","border-gray-300 text-gray-700 hover:bg-gray-50","Borda cinza"],
    ["Msg sucesso","bg-green-50 border-green-200 text-green-700","Verde claro"],
    ["Msg erro","bg-red-50 border-red-200 text-red-700","Vermelho claro"],
], [3.5*cm, 6*cm, 7*mm]))
C(sp(3*mm))
C(Paragraph("Mudar cor dos cards de selecao de produtos:", SB))
C(Paragraph('/* ANTES: verde */\n? \'border-[#84cc16] bg-green-50\' : \'border-gray-200\'\n\n/* AZUL */\n? \'border-blue-500 bg-blue-50\' : \'border-gray-200\'\n\n/* ROXO */\n? \'border-purple-500 bg-purple-50\' : \'border-gray-200\'', SCD))

C(PageBreak())
C(Paragraph("1.10 - Classes Tailwind CSS Mais Usadas", SS))
C(hr())
C(Paragraph("Resumo das classes que voce maisvai encontrar e modificar:", SC))
C(sp(2*mm))
C(tmake([
    ["Classe","O que faz","Exemplo"],
    ["bg-[#cor]","Cor de fundo personalizada","bg-[#0b1a30] = azul escuro"],
    ["bg-white","Fundo branco","Cards, inputs"],
    ["bg-gray-50","Fundo cinza claro","Paginas, header tabela"],
    ["text-white","Texto branco","Texto sobre fundo escuro"],
    ["text-[#cor]","Cor de texto personalizada","text-[#0b1a30]"],
    ["font-bold","Texto negrito","Titulos, botoes"],
    ["font-extrabold","Extra negrito","Numeros grandes"],
    ["text-xs/sm/lg/xl","Tamanho texto","xs=pequeno lg=grande"],
    ["rounded-md/xl","Bordas arredondadas","md=medio xl=bem redondo"],
    ["border border-gray-200","Borda cinza claro","Cards, inputs"],
    ["shadow-sm/lg/xl","Sombra","sm=leve lg=forte xl=muito forte"],
    ["p-4/p-6/p-8","Padding interno","4=medio 6=grande 8=muito"],
    ["px-8 py-4","Padding X=lateral Y=vertical","Botoes, headers"],
    ["flex","Layout flexbox","Alinhar elementos"],
    ["items-center","Centralizar vertical","Header, cards"],
    ["justify-between","Espacar entre","Header com logo e botao"],
    ["gap-4/gap-8","Espaco entre filhos","4=medio 8=grande"],
    ["grid grid-cols-2","Grade de 2 colunas","Formularios"],
    ["hover:bg-[#cor]","Cor ao passar mouse","Botoes, linhas tabela"],
    ["transition-all","Animacao suave","Botoes, hover effects"],
    ["w-full","Largura 100%","Inputs, botoes full-width"],
    ["min-h-screen","Altura minima = tela toda","Paginas principais"],
    ["max-w-4xl","Largura maxima","Containers centralizados"],
    ["mx-auto","Centralizar horizontal","Containers"],
    ["overflow-hidden","Esconder overflow","Cards com bordas arredondadas"],
], [4*cm, 5*cm, 8*mm]))

C(PageBreak())

# === PARTE 2: MESAPRONTA ===
C(Paragraph("=============================", Scenter))
C(Paragraph("PARTE 2 - MESAPRONTA", add_style('p2', fontSize=26, leading=32, alignment=TA_CENTER, textColor=CP, fontName='Helvetica-Bold')))
C(Paragraph("Sistema Desktop - JavaFX + FXML", add_style('p2s', fontSize=12, leading=17, alignment=TA_CENTER, textColor=colors.HexColor("#e94560"), fontName='Helvetica-Bold')))
C(Paragraph("=============================", Scenter))
C(sp(4*mm))
C(Paragraph("O MesaPronta e um sistema desktop Java. Ele usa JavaFX com FXML para a interface. Diferente do SaltoGestao (CSS/Tailwind), aqui o visual e definido por atributos style diretamente nas tags FXML.", SC))

C(Paragraph("2.1 - Paleta de Cores do MesaPronta", SS))
C(hr())
C(tmake([
    ["Cor","Hex","Onde Usar"],
    ["Fundo escuro","#0f0f23","Fundo principal da tela"],
    ["Header","#16213e","Barra superior (topo)"],
    ["Sidebar","#1a1a2e","Painel lateral direito (pedido)"],
    ["Rosa/Vermelho","#e94560","Logo, botao sair, destaques"],
    ["Verde agua","#4ecca3","Botao adicionar, status livre, total"],
    ["Azul claro","#00b4d8","Botao fechar pedido"],
    ["Laranja","#f77f00","Botao pagamento"],
    ["Cinza claro","#a0a0b0","Textos secundarios, subtitulos"],
    ["Cinza medio","#c0c0d0","Labels de campos"],
], [3.5*cm, 3*cm, 10*mm]))

C(Paragraph("2.2 - Diferenca: CSS/Tailwind vs FXML", SS))
C(hr())
C(Paragraph("No SaltoGestao, voce usa classes CSS. No MesaPronta, usa atributos style diretamente:", SC))
C(sp(2*mm))
C(Paragraph('<!-- SALTOGESTAO (Tailwind) -->\n<header className="bg-[#0b1a30] text-white px-8 py-5">\n  <h1 className="text-2xl font-bold">Titulo</h1>\n</header>\n\n<!-- MESAPRONTA (FXML/JavaFX) -->\n<HBox style="-fx-background-color: #16213e; -fx-padding: 10 20;">\n  <Label text="Titulo"\n    style="-fx-font-size: 20px; -fx-font-weight: bold;\n           -fx-text-fill: #e94560;"/>\n</HBox>', SCD))
C(sp(2*mm))
C(Paragraph("A principal diferenca: CSS usa background-color, JavaFX usa -fx-background-color. Em vez de classes, voce coloca o estilo no atributo style.", SD))

C(PageBreak())
C(Paragraph("2.3 - Tela de Login (LoginView.fxml)", SS))
C(hr())
C(Paragraph("Arquivo: coruba-food/src/main/resources/view/LoginView.fxml", SD))
C(sp(2*mm))
C(tmake([
    ["Elemento","Atributo style","Descricao"],
    ["Fundo","-fx-background-color: #1a1a2e","Fundo azul bem escuro"],
    ["Titulo","-fx-font-size: 28px; -fx-text-fill: #e94560","Texto rosa grande"],
    ["Subtitulo","-fx-text-fill: #a0a0b0","Texto cinza claro"],
    ["Label campos","-fx-text-fill: #c0c0d0","Labels cinza claro"],
    ["TextField","-fx-font-size: 14px","Campo de texto simples"],
    ["Botao ENTRAR","-fx-background-color: #e94560; -fx-text-fill: white","Botao rosa"],
    ["Mensagem","-fx-font-size: 12px","Texto de erro/sucesso"],
], [3*cm, 6.5*cm, 7*mm]))
C(sp(3*mm))
C(Paragraph("Mudar cor de fundo da tela de login:", SB))
C(Paragraph('<!-- ANTES -->\n<AnchorPane style="-fx-background-color: #1a1a2e;">\n\n<!-- MAIS ESCURO -->\n<AnchorPane style="-fx-background-color: #0a0a1a;">\n\n<!-- ROXO -->\n<AnchorPane style="-fx-background-color: #1a0a2e;">', SCD))
C(sp(2*mm))
C(Paragraph("Mudar cor do botao ENTRAR:", SB))
C(Paragraph('<!-- ANTES -->\n<Button style="-fx-background-color: #e94560; -fx-text-fill: white;">\n\n<!-- VERDE -->\n<Button style="-fx-background-color: #4ecca3; -fx-text-fill: #0f0f23;">\n\n<!-- AZUL -->\n<Button style="-fx-background-color: #00b4d8; -fx-text-fill: white;">\n\n<!-- LARANJA -->\n<Button style="-fx-background-color: #f77f00; -fx-text-fill: white;">', SCD))
C(sp(2*mm))
C(Paragraph("Mudar cor do titulo:", SB))
C(Paragraph('<!-- ANTES -->\n<Label style="-fx-text-fill: #e94560;">\n\n<!-- VERDE -->\n<Label style="-fx-text-fill: #4ecca3;">\n\n<!-- DOURADO -->\n<Label style="-fx-text-fill: #fbbf24;">', SCD))

C(PageBreak())
C(Paragraph("2.4 - Tela Principal (PrincipalView.fxml)", SS))
C(hr())
C(Paragraph("Arquivo: coruba-food/src/main/resources/view/PrincipalView.fxml", SD))
C(sp(2*mm))
C(tmake([
    ["Elemento","Atributo style","Descricao"],
    ["Fundo principal","-fx-background-color: #0f0f23","Fundo bem escuro"],
    ["Header (topo)","-fx-background-color: #16213e","Barra azul escuro"],
    ["Logo texto","-fx-text-fill: #e94560; -fx-font-size: 20px","Titulo MesaPronta"],
    ["Sidebar (direita)","-fx-background-color: #1a1a2e","Painel de pedido"],
    ["Mesa (livre)","-fx-background-color: #4ecca3","Botao verde"],
    ["Mesa (ocupada)","-fx-background-color: #e94560","Botao rosa"],
    ["Mesa (reservada)","-fx-background-color: #f77f00","Botao laranja"],
    ["Botao Adicionar","-fx-background-color: #4ecca3","Verde agua"],
    ["Botao Remover","-fx-background-color: #e94560","Rosa"],
    ["Botao Fechar","-fx-background-color: #00b4d8","Azul claro"],
    ["Botao Pagamento","-fx-background-color: #f77f00","Laranja"],
    ["Label Total","-fx-text-fill: #4ecca3; -fx-font-size: 22px","Verde agua grande"],
    ["Status bar","-fx-background-color: #16213e","Mesma cor do header"],
], [3.5*cm, 6*cm, 7*mm]))
C(sp(3*mm))
C(Paragraph("Mudar cores das mesas:", SB))
C(Paragraph('<!-- ANTES: mesa livre=verde, ocupada=rosa, reservada=laranja -->\n<!-- Estes sao controlados no codigo Java PrincipalController.java -->\n<!-- LIVRE=verde (#4ecca3), OCUPADA=rosa (#e94560), RESERVADA=laranja (#f77f00) -->\n\n/* Para mudar, edite as cores no metodo carregarMesas() do PrincipalController.java */\n/* Procure por: case LIVRE, case OCUPADA, case RESERVADA */', SCD))
C(sp(2*mm))
C(Paragraph("Mudar painel lateral (sidebar):", SB))
C(Paragraph('<!-- ANTES -->\n<VBox style="-fx-background-color: #1a1a2e; -fx-padding: 12;">\n\n<!-- MAIS CLARO -->\n<VBox style="-fx-background-color: #252547; -fx-padding: 12;">\n\n<!-- COM BORDA COLORIDA -->\n<VBox style="-fx-background-color: #1a1a2e; -fx-padding: 12;\n     -fx-border-color: #e94560; -fx-border-width: 0 0 0 3;">', SCD))
C(sp(2*mm))
C(Paragraph("Mudar header superior:", SB))
C(Paragraph('<!-- ANTES -->\n<HBox style="-fx-background-color: #16213e; -fx-padding: 10 20;">\n\n<!-- ESCURO TOTAL -->\n<HBox style="-fx-background-color: #0a0a1a; -fx-padding: 10 20;">\n\n<!-- ROXO -->\n<HBox style="-fx-background-color: #1e1b4b; -fx-padding: 10 20;">\n\n<!-- COM BORDA INFERIOR -->\n<HBox style="-fx-background-color: #16213e; -fx-padding: 10 20;\n     -fx-border-color: #e94560; -fx-border-width: 0 0 2 0;">', SCD))

C(PageBreak())
C(Paragraph("2.5 - Guia Completo: Cores JavaFX (propriedades -fx-)", SS))
C(hr())
C(Paragraph("No JavaFX/FXML, cada propriedade de estilo tem o prefixo -fx-. Referencia completa:", SC))
C(sp(2*mm))
C(tmake([
    ["Propriedade FXML","Equivalente CSS","Exemplo"],
    ["-fx-background-color","background-color","-fx-background-color: #1a1a2e"],
    ["-fx-text-fill","color","-fx-text-fill: #ffffff"],
    ["-fx-font-size","font-size","-fx-font-size: 14px"],
    ["-fx-font-weight","font-weight","-fx-font-weight: bold"],
    ["-fx-padding","padding","-fx-padding: 10 20"],
    ["-fx-border-color","border-color","-fx-border-color: #333"],
    ["-fx-border-width","border-width","-fx-border-width: 1"],
    ["-fx-border-radius","border-radius","-fx-border-radius: 8"],
    ["-fx-background-radius","border-radius","-fx-background-radius: 8"],
    ["-fx-cursor","cursor","-fx-cursor: hand"],
    ["-fx-opacity","opacity","-fx-opacity: 0.8"],
    ["-fx-alignment","text-align","-fx-alignment: center"],
    ["-fx-effect","box-shadow","-fx-effect: dropshadow(...)"],
], [4.5*cm, 4*cm, 8*mm]))
C(sp(3*mm))
C(Paragraph("Exemplo: Criar tema roxo para o MesaPronta", SB))
C(Paragraph('/* Substitua as cores em ambos os FXMLs */\n\n/* Fundo principal */\n-fx-background-color: #0f0f23  ->  #1a0a2e\n\n/* Header e status bar */\n-fx-background-color: #16213e  ->  #2e1b4b\n\n/* Sidebar */\n-fx-background-color: #1a1a2e  ->  #2d1b4e\n\n/* Destaques (logo, botoes) */\n-fx-text-fill: #e94560  ->  #a855f7\n-fx-background-color: #e94560  ->  #a855f7\n\n/* Mesa livre */\n-fx-background-color: #4ecca3  ->  #86efac', SCD))
C(sp(3*mm))
C(Paragraph("Adicionar efeitos visuais (sombra e hover):", SB))
C(Paragraph('<!-- Botao com sombra colorida -->\n<Button style="-fx-background-color: #e94560;\n  -fx-effect: dropshadow(gaussian, #e94560, 10, 0, 0, 0);"/>\n\n<!-- Hover via codigo Java no controller -->\n// No PrincipalController.java:\nbtn.setOnMouseEntered(e ->\n  btn.setStyle("-fx-background-color: #ff6b8a;"));\nbtn.setOnMouseExited(e ->\n  btn.setStyle("-fx-background-color: #e94560;"));', SCD))

C(PageBreak())

# === PARTE 3: REFERENCIA ===
C(Paragraph("=============================", Scenter))
C(Paragraph("PARTE 3 - REFERENCIA RAPIDA", add_style('p3', fontSize=26, leading=32, alignment=TA_CENTER, textColor=CP, fontName='Helvetica-Bold')))
C(Paragraph("=============================", Scenter))
C(sp(4*mm))

C(Paragraph("3.1 - Tabela de Cores Completas", SS))
C(hr())
C(Paragraph("Copie os codigos abaixo para usar nos dois sistemas:", SC))
C(sp(2*mm))
C(tmake([
    ["Nome","Hex","Uso sugerido"],
    ["Azul escuro","#0b1a30","Cor principal SaltoGestao"],
    ["Azul medio","#16213e","Headers secundarios"],
    ["Azul claro","#00b4d8","Botoes informativos"],
    ["Verde limao","#84cc16","Botoes principais SaltoGestao"],
    ["Verde escuro","#65a30d","Hover botoes SaltoGestao"],
    ["Verde agua","#4ecca3","Sucesso, mesas livres"],
    ["Verde sucesso","#22c55e","Status ativo, msgs OK"],
    ["Rosa","#e94560","Destaques MesaPronta, logo"],
    ["Vermelho","#ef4444","Erros, inadimplencia"],
    ["Laranja","#f77f00","Pagamentos, reservas"],
    ["Amarelo","#f59e0b","Avisos"],
    ["Cinza fundo","#f8fafc","Fundo de paginas"],
    ["Cinza borda","#e2e8f0","Bordas de cards"],
    ["Cinza texto","#64748b","Textos secundarios"],
    ["Branco","#ffffff","Fundo de cards"],
    ["Escuro fundo","#0f0f23","Fundo MesaPronta"],
    ["Escuro header","#16213e","Header MesaPronta"],
    ["Escuro sidebar","#1a1a2e","Sidebar MesaPronta"],
], [3.5*cm, 3*cm, 10*mm]))

C(Paragraph("3.2 - Onde Cada Arquivo Fica", SS))
C(hr())
C(tmake([
    ["Sistema","Arquivo","Caminho completo"],
    ["SaltoGestao","globals.css","frontend-web/app/globals.css"],
    ["SaltoGestao","Login cliente","frontend-web/app/login/page.tsx"],
    ["SaltoGestao","Dashboard cliente","frontend-web/app/dashboard/page.tsx"],
    ["SaltoGestao","Login admin","frontend-web/app/admin/login/page.tsx"],
    ["SaltoGestao","Dashboard admin","frontend-web/app/admin/dashboard/page.tsx"],
    ["SaltoGestao","Lista clientes","frontend-web/app/admin/clientes/listar/page.tsx"],
    ["SaltoGestao","Criar cliente","frontend-web/app/admin/clientes/criar/page.tsx"],
    ["SaltoGestao","Layout global","frontend-web/app/layout.tsx"],
    ["MesaPronta","Login FXML","src/main/resources/view/LoginView.fxml"],
    ["MesaPronta","Principal FXML","src/main/resources/view/PrincipalView.fxml"],
    ["MesaPronta","persistence.xml","src/main/resources/META-INF/persistence.xml"],
    ["MesaPronta","LoginController","src/...controller/LoginController.java"],
    ["MesaPronta","PrincipalController","src/...controller/PrincipalController.java"],
], [2.5*cm, 4*cm, 10*mm]))

C(Paragraph("3.3 - Comandos para Aplicar Mudancas", SS))
C(hr())
C(Paragraph("Apos editar qualquer arquivo, use estes comandos:", SC))
C(sp(2*mm))
C(Paragraph(
   '# === SALTOGESTAO (Web) ===\n'
   'cd /opt/projects/SaltoGestao/frontend-web\n'
   'npm run build\n'
   '# Acesse: http://191.252.210.235:3000\n\n'
   '# === MESAPRONTA (Desktop) ===\n'
   'cd /opt/projects/coruba-food\n'
   'mvn clean compile\n'
   'mvn exec:java -Dexec.mainClass="com.corumbasistemas.corubafood.CorubaFoodApp"\n\n'
   '# === ENVIAR PARA GITHUB ===\n'
   'cd /opt/projects/coruba-food  (ou SaltoGestao)\n'
   'git add -A\n'
   'git commit -m "mudancas visuais"\n'
   'git push', SCD))

C(sp(6*mm))
C(Paragraph("=============================", Scenter))
C(Paragraph("FIM DO GUIA", add_style('end2', fontSize=14, leading=20, alignment=TA_CENTER, textColor=CP, fontName='Helvetica-Bold')))
C(Paragraph("Corumba Sistemas - SaltoGestao + MesaPronta", add_style('end3', fontSize=9, leading=13, alignment=TA_CENTER, textColor=colors.HexColor('#64748b'), fontName='Helvetica')))
C(Paragraph("Gerado por OWL - Hermes Agent", add_style('end4', fontSize=7.5, leading=10, alignment=TA_CENTER, textColor=colors.HexColor('#94a3b8'), fontName='Helvetica')))
C(Paragraph("=============================", Scenter))

doc.build(story)
size = os.path.getsize(output_path)
print(f"PDF criado: {output_path}")
print(f"Tamanho: {size} bytes ({size//1024} KB)")
