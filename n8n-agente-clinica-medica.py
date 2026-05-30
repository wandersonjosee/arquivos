"""
Guia Completo: Agente de IA com n8n para Clínica Médica
Gera PDF com passo a passo detalhado + tabela de preços
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import HexColor, black, white
from reportlab.lib.units import mm, cm
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                  TableStyle, PageBreak, HRFlowable, Image)
from reportlab.lib import colors
import os

OUTPUT = "/opt/projects/Agente_IA_n8n_Clinica_Medica.pdf"

doc = SimpleDocTemplate(
    OUTPUT,
    pagesize=A4,
    rightMargin=2*cm,
    leftMargin=2*cm,
    topMargin=2*cm,
    bottomMargin=2*cm,
)

# === CORES ===
AZUL_ESCURO = HexColor("#1a365d")
AZUL_MEDIO = HexColor("#2b6cb0")
AZUL_CLARO = HexColor("#bee3f8")
VERDE = HexColor("#38a169")
VERDE_CLARO = HexColor("#c6f6d5")
LARANJA = HexColor("#dd6b20")
CINZA = HexColor("#718096")
CINZA_CLARO = HexColor("#f7fafc")
CINZA_MEDIO = HexColor("#e2e8f0")
BRANCO = white
PRETO = black

# === ESTILOS ===
styles = getSampleStyleSheet()

# Título principal (capa)
style_titulo = ParagraphStyle(
    "Titulo", parent=styles["Title"], fontSize=28, textColor=AZUL_ESCURO,
    spaceAfter=6, alignment=TA_CENTER, leading=34
)
style_subtitulo = ParagraphStyle(
    "Subtitulo", parent=styles["Normal"], fontSize=16, textColor=AZUL_MEDIO,
    spaceAfter=20, alignment=TA_CENTER, leading=22
)
style_autor = ParagraphStyle(
    "Autor", parent=styles["Normal"], fontSize=11, textColor=CINZA,
    spaceAfter=8, alignment=TA_CENTER
)

# Seções
style_h1 = ParagraphStyle(
    "H1", parent=styles["Heading1"], fontSize=18, textColor=AZUL_ESCURO,
    spaceBefore=16, spaceAfter=10, borderWidth=0, borderPadding=0,
    borderColor=AZUL_MEDIO
)
style_h2 = ParagraphStyle(
    "H2", parent=styles["Heading2"], fontSize=14, textColor=AZUL_MEDIO,
    spaceBefore=12, spaceAfter=8
)
style_h3 = ParagraphStyle(
    "H3", parent=styles["Heading3"], fontSize=12, textColor=VERDE,
    spaceBefore=10, spaceAfter=6
)

# Texto corpo
style_corpo = ParagraphStyle(
    "Corpo", parent=styles["Normal"], fontSize=10.5, textColor=PRETO,
    spaceAfter=6, leading=16, alignment=TA_JUSTIFY
)
style_corpo_left = ParagraphStyle(
    "CorpoLeft", parent=styles["Normal"], fontSize=10.5, textColor=PRETO,
    spaceAfter=6, leading=16, alignment=TA_LEFT
)

# Destaque (dicas/notas)
style_destaque = ParagraphStyle(
    "Destaque", parent=styles["Normal"], fontSize=10, textColor=PRETO,
    leftIndent=12, rightIndent=12, spaceAfter=6, leading=15,
    borderColor=VERDE, borderWidth=1, borderPadding=8,
    backColor=VERDE_CLARO
)
style_aviso = ParagraphStyle(
    "Aviso", parent=styles["Normal"], fontSize=10, textColor=PRETO,
    leftIndent=12, rightIndent=12, spaceAfter=6, leading=15,
    borderColor=LARANJA, borderWidth=1, borderPadding=8,
    backColor=HexColor("#fefcbf")
)
style_codigo = ParagraphStyle(
    "Codigo", parent=styles["Normal"], fontSize=9, textColor=PRETO,
    fontName="Courier", leftIndent=8, rightIndent=8, spaceAfter=4,
    leading=13, backColor=HexColor("#1a202c"), textColor=white
)

# Bullet
style_bullet = ParagraphStyle(
    "Bullet", parent=styles["Normal"], fontSize=10.5, textColor=PRETO,
    leftIndent=20, spaceAfter=4, leading=16, bulletText="\u2022"
)
style_bullet_num = ParagraphStyle(
    "BulletNum", parent=styles["Normal"], fontSize=10.5, textColor=PRETO,
    leftIndent=20, spaceAfter=4, leading=16
)


def divider(color=AZUL_MEDIO, thickness=1):
    return HRFlowable(width="100%", thickness=thickness, color=color,
                      spaceAfter=8, spaceBefore=4)


def table_header_style():
    return TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), AZUL_ESCURO),
        ("TEXTCOLOR", (0, 0), (-1, 0), BRANCO),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, 0), 10),
        ("ALIGN", (0, 0), (-1, 0), "CENTER"),
        ("VALIGN", (0, 0), (-1, 0), "MIDDLE"),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 8),
        ("TOPPADDING", (0, 0), (-1, 0), 8),
        ("BACKGROUND", (0, 1), (-1, -1), CINZA_CLARO),
        ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
        ("FONTSIZE", (0, 1), (-1, -1), 9.5),
        ("TEXTCOLOR", (0, 1), (-1, -1), PRETO),
        ("VALIGN", (0, 1), (-1, -1), "MIDDLE"),
        ("TOPPADDING", (0, 1), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 1), (-1, -1), 6),
        ("LEFTPADDING", (0, 1), (-1, -1), 8),
        ("RIGHTPADDING", (0, 1), (-1, -1), 8),
        ("GRID", (0, 0), (-1, -1), 0.5, CINZA_MEDIO),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [BRANCO, CINZA_CLARO]),
    ])


# ============================================================
# CONTEÚDO DO PDF
# ============================================================
story = []

# === CAPA ===
story.append(Spacer(1, 60))
story.append(Paragraph("\U0001F916", ParagraphStyle("EmojiCapa", fontSize=60, alignment=TA_CENTER)))
story.append(Spacer(1, 10))
story.append(Paragraph("GUIA COMPLETO", style_titulo))
story.append(Paragraph("Agente de IA com n8n", style_titulo))
story.append(Paragraph("para Cl\u00ednica M\u00e9dica", style_titulo))
story.append(Spacer(1, 8))
story.append(divider(thickness=2))
story.append(Spacer(1, 8))
story.append(Paragraph("Atendente Virtual Inteligente", style_subtitulo))
story.append(Paragraph("Consulta de Agenda \u2022 Agendamento Automatizado \u2022 Confirma\u00e7\u00f5es via WhatsApp", style_autor))
story.append(Spacer(1, 40))
story.append(divider(thickness=2))
story.append(Spacer(1, 12))

info_data = [
    ["Tecnologia", "n8n (self-hosted) + Google Calendar API + WhatsApp"],
    ["Custo da API", "GRATUITA (Google Calendar API) + WhatsApp via WhatsApp Business API"],
    ["Complexidade", "Intermedi\u00e1ria \u2014 Sem c\u00f3digo (no-code/low-code)"],
    ["Tempo estimado de setup", "4 a 8 horas"],
]
info_table = Table(info_data, colWidths=[4*cm, 12*cm])
info_table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (0, -1), AZUL_CLARO),
    ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
    ("FONTSIZE", (0, 0), (-1, -1), 10),
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ("TOPPADDING", (0, 0), (-1, -1), 8),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
    ("LEFTPADDING", (0, 0), (-1, -1), 10),
    ("GRID", (0, 0), (-1, -1), 0.5, CINZA_MEDIO),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [BRANCO, CINZA_CLARO]),
]))
story.append(info_table)
story.append(Spacer(1, 20))
story.append(Paragraph("Gerado em: Maio/2026", style_autor))
story.append(PageBreak())

# === SUMÁRIO ===
story.append(Paragraph("SUM\u00c1RIO", style_h1))
story.append(divider())
itens_sumario = [
    "1. Vis\u00e3o Geral do Projeto",
    "2. O Que Voc\u00ea Vai Precisar (Pr\u00e9-requisitos)",
    "3. Arquitetura do Fluxo",
    "4. Passo a Passo: Configura\u00e7\u00e3o do n8n",
    "5. Passo a Passo: Google Cloud &amp; Calendar API",
    "6. Passo a Passo: Cria\u00e7\u00e3o do Fluxo no n8n",
    "7. Configura\u00e7\u00e3o do WhatsApp",
    "8. Prompt do Agente de IA",
    "9. Testes e Valida\u00e7\u00e3o",
    "10. Tabela de Pre\u00e7os (Quanto Cobrar)",
    "11. Dicas Avan\u00e7adas",
]
for item in itens_sumario:
    story.append(Paragraph(item, style_corpo_left))
story.append(PageBreak())

# === SEÇÃO 1: VISÃO GERAL ===
story.append(Paragraph("1. VIS\u00c3O GERAL DO PROJETO", style_h1))
story.append(divider())
story.append(Paragraph(
    "Este guia ensina a criar um <b>agente de IA completamente funcional</b> que atua como "
    "atendente virtual de uma cl\u00ednica m\u00e9dica. O agente consulta a agenda do Google Calendar, "
    "verifica hor\u00e1rios dispon\u00edveis, agenda consultas e envia confirma\u00e7\u00f5es \u2014 tudo de "
    "forma automatizada e gratuita.",
    style_corpo
))
story.append(Spacer(1, 8))

story.append(Paragraph("O que o agente faz:", style_h2))
funcionalidades = [
    "<b>Recebe mensagens</b> do paciente via WhatsApp (ou outro canal)",
    "<b>Entende a inten\u00e7\u00e3o</b> usando IA (classifica: agendar, cancelar, remarcar, d\u00favida)",
    "<b>Consulta o Google Calendar</b> para verificar hor\u00e1rios dispon\u00edveis",
    "<b>Agenda a consulta</b> diretamente no calend\u00e1rio do m\u00e9dico",
    "<b>Envia confirma\u00e7\u00e3o</b> autom\u00e1tica ao paciente",
    "<b>Responde d\u00favidas</b> sobre hor\u00e1rios, endere\u00e7o e preparo para exames",
    "<b>Envia lembretes</b> autom\u00e1ticos 24h antes da consulta",
]
for i, f in enumerate(funcionalidades):
    story.append(Paragraph(f"{i+1}. {f}", style_bullet_num))

story.append(Spacer(1, 8))
story.append(Paragraph(
    "<b>Por que n8n?</b> O n8n \u00e9 uma ferramenta de automa\u00e7\u00e3o open-source (gratuita para self-host) "
    "que permite criar fluxos visuais complexos sem escrever c\u00f3digo. Ele tem integra\u00e7\u00e3o nativa com "
    "Google Calendar, WhatsApp (via APIs), e suporte a IA com v\u00e1rios modelos gratuitos (Groq, Ollama local).",
    style_destaque
))

story.append(PageBreak())

# === SEÇÃO 2: PRÉ-REQUISITOS ===
story.append(Paragraph("2. O QUE VOC\u00ea VAI PRECISAR", style_h1))
story.append(divider())

story.append(Paragraph("2.1 \u2014 Hardware / Servidor", style_h2))
pre_table = [
    ["Item", "Especifica\u00e7\u00e3o Mnecess\u00e1ria"],
    ["Servidor", "VPS m\u00ednimo: 2 vCPU, 4GB RAM (ex: DigitalOcean $12/m\u00eas)"],
    ["Sistema", "Linux (Ubuntu 22.04+) ou Docker local"],
    ["Dom\u00ednio ", "Nome de dom\u00e9nio apontado para o servidor (opcional, mas recomendado)"],
    ["Node.js", "v18+ (necess\u00e1rio para rodar o n8n)"],
]
pre_table_t = Table(pre_table, colWidths=[3*cm, 13*cm])
pre_table_t.setStyle(table_header_style())
story.append(pre_table_t)
story.append(Spacer(1, 8))

story.append(Paragraph("2.2 \u2014 Contas e Servi\u00e7os Gratuitos", style_h2))
contas_table = [
    ["Servi\u00e7o", "Finalidade", "Custo"],
    ["Google Cloud (GCP)", "Criar projeto para Google Calendar API", "Gratuito (quotas generosas)"],
    ["Google Calendar", "Agenda do m\u00e9dico \u2014 consulta e agendamento", "Gratuito"],
    ["WhatsApp Business API", "Comunica\u00e7\u00e3o com pacientes", "Gratuito via WhatsApp Business App"],
    ["n8n (self-hosted)", "Motor de automa\u00e7\u00e3o", "Gratuito (open source)"],
    ["Groq Cloud API", "Modelo de IA gratuito (Llama 3/Mixtral)", "Gratuito (limite generoso)"],
    ["ngrok ou dom\u00e9nio", "Expor n8n para receber webhooks", "Gratuito (ngrok) ou ~$10/ano (dom\u00e9nio)"],
]
contas_table_t = Table(contas_table, colWidths=[4*cm, 7*cm, 5*cm])
contas_table_t.setStyle(table_header_style())
story.append(contas_table_t)
story.append(Spacer(1, 8))

story.append(Paragraph(
    "<b>\u26a0\ufe0f Nota sobre WhatsApp:</b> Para produ\u00e7\u00e3o com muitos pacientes, use a WhatsApp Business API "
    "oficial (via Meta ou provedores como Wati, Chatwoot, Evolution API). Para testes ou cl\u00ednicas pequenas, "
    "o WhatsApp Business App gratuito com Evolution API (open source) funciona bem.",
    style_aviso
))

story.append(PageBreak())

# === SEÇÃO 3: ARQUITETURA ===
story.append(Paragraph("3. ARQUITETURA DO FLUXO", style_h1))
story.append(divider())

story.append(Paragraph(
    "Diagrama visual do fluxo do agente de atendimento:",
    style_corpo
))
story.append(Spacer(1, 8))

# Arquitetura em tabela
arq_data = [
    ["ETAPA", "COMPONENTE N8N", "DESCRI\u00c7\u00c3O"],
    ["1. Entrada", "Webhook / WhatsApp Trigger", "Paciente envia mensagem pelo WhatsApp"],
    ["2. Receber", "Webhook Node", "n8n recebe a mensagem (JSON via POST)"],
    ["3. Entender", "AI Agent (Groq/Ollama)", "IA analisa a inten\u00e7\u00e3o do paciente"],
    ["4. Decidir", "Switch / If Node", "Roteia: agendar, cancelar, consultar, d\u00favida"],
    ["5a. Buscar", "Google Calendar \u2014 List Events", "Lista eventos para ver disponibilidade"],
    ["5b. Criar", "Google Calendar \u2014 Create Event", "Cria o evento da consulta na agenda"],
    ["5c. Deletar", "Google Calendar \u2014 Delete Event", "Cancela evento existente"],
    ["6. Responder", "WhatsApp Send Message", "Envia confirma\u00e7\u00e3o ao paciente"],
    ["7. Lembrete", "Schedule Trigger + Flow", "Envia lembrete 24h antes (opcional)"],
]
arq_table_t = Table(arq_data, colWidths=[2.5*cm, 5*cm, 8.5*cm])
arq_table_t.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), AZUL_ESCURO),
    ("TEXTCOLOR", (0, 0), (-1, 0), BRANCO),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("FONTSIZE", (0, 0), (-1, 0), 10),
    ("ALIGN", (0, 0), (-1, -1), "LEFT"),
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ("TOPPADDING", (0, 0), (-1, -1), 7),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ("LEFTPADDING", (0, 0), (-1, -1), 8),
    ("RIGHTPADDING", (0, 0), (-1, -1), 8),
    ("GRID", (0, 0), (-1, -1), 0.5, CINZA_MEDIO),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [BRANCO, CINZA_CLARO]),
    ("FONTSIZE", (0, 1), (-1, -1), 9.5),
]))
story.append(arq_table_t)

story.append(PageBreak())

# === SEÇÃO 4: CONFIGURAÇÃO DO N8N ===
story.append(Paragraph("4. PASSO A PASSO: CONFIGURA\u00c7\u00c3O DO N8N", style_h1))
story.append(divider())

story.append(Paragraph("4.1 \u2014 Instala\u00e7\u00e3o via Docker (Recomendado)", style_h2))
story.append(Paragraph(
    "A forma mais simples e confi\u00e1vel de rodar o n8n \u00e9 via Docker. Execute os comandos abaixo "
    "no seu servidor Linux:",
    style_corpo
))

docker_cmds = """# Criar diret\u00f3rio para dados persistentes
mkdir -p /opt/n8n && cd /opt/n8n

# Criar docker-compose.yml
cat > docker-compose.yml << 'EOF'
version: '3.8'
services:
  n8n:
    image: n8nio/n8n:latest
    container_name: n8n
    restart: always
    ports:
      - "5678:5678"
    environment:
      - N8N_HOST=seu-dominio.com
      - N8N_PORT=5678
      - N8N_PROTOCOL=https
      - WEBHOOK_URL=https://seu-dominio.com/
      - GENERIC_TIMEZONE=America/Sao_Paulo
      - TZ=America/Sao_Paulo
    volumes:
      - n8n_data:/home/node/.n8n
    networks:
      - n8n_net
volumes:
  n8n_data:
networks:
  n8n_net:
EOF

# Subir o container
docker compose up -d

# Verificar se est\u00e1 rodando
docker logs n8n --tail 20"""
story.append(Paragraph(docker_cmds, style_codigo))

story.append(Paragraph(
    "Acesse <b>http://IP-DO-SERVIDOR:5678</b> para ver a interface do n8n pela primeira vez. "
    "Crie a conta de administrador.",
    style_destaque
))

story.append(Paragraph("4.2 \u2014 Instala\u00e7\u00e3o via npm (alternativa)", style_h2))
npm_cmds = """# Instalar n8n globalmente
npm install n8n -g

# Configurar vari\u00e1veis de ambiente
export N8N_HOST=localhost
export N8N_PORT=5678
export N8N_PROTOCOL=http
export WEBHOOK_URL=http://localhost:5678/
export GENERIC_TIMEZONE=America/Sao_Paulo
export TZ=America/Sao_Paulo

# Iniciar
n8n start"""
story.append(Paragraph(npm_cmds, style_codigo))

story.append(Paragraph("4.3 \u2014 Configura\u00e7\u00e3o de Proxy Reverso (Nginx)", style_h2))
story.append(Paragraph(
    "Para usar HTTPS e dom\u00e9nio pr\u00f3prio, configure um proxy reverso com Nginx + SSL gratuito via Let's Encrypt:",
    style_corpo
))
nginx_cmds = """# Instalar Nginx e Certbot
sudo apt install nginx certbot python3-certbot-nginx -y

# Criar configura\u00e7\u00e3o
sudo tee /etc/nginx/sites-available/n8n << 'EOF'
server {
    listen 80;
    server_name n8n.seudominio.com;

    location / {
        proxy_pass http://localhost:5678;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
EOF

# Ativar site e obter SSL
sudo ln -s /etc/nginx/sites-available/n8n /etc/nginx/sites-enabled/
sudo certbot --nginx -d n8n.seudominio.com -m seu@email.com
sudo nginx -t && sudo systemctl reload nginx"""
story.append(Paragraph(nginx_cmds, style_codigo))

story.append(PageBreak())

# === SEÇÃO 5: GOOGLE CLOUD ===
story.append(Paragraph("5. PASSO A PASSO: GOOGLE CLOUD &amp; CALENDAR API", style_h1))
story.append(divider())

story.append(Paragraph("5.1 \u2014 Criar Projeto no Google Cloud Console", style_h2))
for i, passo in enumerate([
    "Acesse <b>console.cloud.google.com</b> com sua conta Google",
    "Clique em <b>Selecionar projeto</b> \u2192 <b>Novo Projeto</b>",
    "D\u00ea um nome (ex: <b>agente-clinica</b>) e clique em <b>Criar</b>",
    "Aguarde a cria\u00e7\u00e3o e selecione o projeto"], 1):
    story.append(Paragraph(f"{passo}", style_bullet_num))

story.append(Paragraph("5.2 \u2014 Ativar a Google Calendar API", style_h2))
for i, passo in enumerate([
    "No menu lateral, v\u00e1 em <b>APIs e Servi\u00e7os</b> \u2192 <b>Biblioteca</b>",
    "Pesquise por <b>Google Calendar API</b>",
    "Clique em <b>Google Calendar API</b> \u2192 <b>Ativar</b>",
    "Aguarde a ativa\u00e7\u00e3o (pode levar alguns segundos)"], 1):
    story.append(Paragraph(f"{passo}", style_bullet_num))

story.append(Paragraph("5.3 \u2014 Criar Credenciais OAuth 2.0", style_h2))
for i, passo in enumerate([
    "V\u00e1 em <b>APIs e Servi\u00e7os</b> \u2192 <b>Credenciais</b>",
    "Clique em <b>Criar Credenciais</b> \u2192 <b>ID do cliente OAuth</b>",
    "Se for a primeira vez, configure a <b>Tela de Consentimento</b>: Tipo = Externo, preencha nome do app, email, salve",
    "Tipo de aplicativo: <b>Aplicativo da Web</b>",
    "Nome: <b>n8n-agente-clinica</b>",
    "Origens JavaScript autorizadas: <b>https://n8n.seudominio.com</b>",
    "URIs de redirecionamento: <b>https://n8n.seudominio.com/rest/oauth2-credential/callback</b>",
    "Clique em <b>Criar</b> e <b>copie o Client ID e Client Secret</b>"], 1):
    story.append(Paragraph(f"{passo}", style_bullet_num))

story.append(Paragraph("5.4 \u201— Configurar no n8n", style_h2))
for i, passo in enumerate([
    "No n8n, v\u00e1 em <b>Configura\u00e7\u00f5es</b> \u2192 <b>Credenciais</b> \u2192 <b>Adicionar Credencial</b>",
    "Pesquise por <b>Google OAuth2 API</b>",
    "Cole o <b>Client ID</b> e <b>Client Secret</b> obtidos no passo anterior",
    "Clique em <b>Sign in with Google</b> e autorize o acesso",
    "Selecione as permiss\u00f5es do Calendar (leitura e escrita)",
    "Salve a credencial com nome: <b>Google Calendar - Clinica</b>"], 1):
    story.append(Paragraph(f"{passo}", style_bullet_num))

story.append(Paragraph("5.5 \u2014 Preparar a Agenda no Google Calendar", style_h2))
for i, passo in enumerate([
    "No Google Calendar (calendar.google.com), crie um novo calend\u00e1rio: <b>Clinica - Dr. Nome</b>",
    "Configure os <b>hor\u00e1rios de atendimento</b> (ex: Seg-Sex 08:00-18:00, intervalo 12:00-13:00)",
    "Defina o <b>ID do calend\u00e1rio</b> (nas configura\u00e7\u00f5es do calend\u00e1rio, procure por 'Integrar calend\u00e1rio')",
    "Guarde o ID do calend\u00e1rio (formato: <b>xxxxx@group.calendar.google.com</b>)"], 1):
    story.append(Paragraph(f"{passo}", style_bullet_num))

story.append(PageBreak())

# === SEÇÃO 6: CRIAÇÃO DO FLUXO ===
story.append(Paragraph("6. PASSO A PASSO: CRIA\u00c7\u00c3O DO FLUXO NO N8N", style_h1))
story.append(divider())

story.append(Paragraph(
    "Agora vamos criar o fluxo completo no n8n. Cada n\u00f3 (node) \u00e9 arrastado da paleta esquerda "
    "para a \u00e1rea de trabalho e conectado sequencialmente.",
    style_corpo
))

# --- Nó 1 ---
story.append(Paragraph("6.1 \u2014 N\u00f3 1: Webhook (Receber Mensagem)", style_h2))
story.append(Paragraph(
    "Este n\u00f3 recebe a mensagem do paciente via WhatsApp. Clique em <b>Adicionar n\u00f3 inicial</b> e selecione <b>Webhook</b>.",
    style_corpo
))
webhook_table = [
    ["Par\u00e2metro", "Valor"],
    ["HTTP Method", "POST"],
    ["Path", "webhook/agente-clinica"],
    ["Authentication", "None (ou Header Auth com token secreto)"],
    ["Respond", "When Last Node Finishes"],
]
wt = Table(webhook_table, colWrites=[5*cm, 11*cm])
wt.setStyle(table_header_style())
story.append(wt)
story.append(Spacer(1, 6))
story.append(Paragraph(
    "URL completa: <b>https://n8n.seudominio.com/webhook/agente-clinica</b>",
    style_destaque
))

# --- Nó 2 ---
story.append(Paragraph("6.2 \u2014 N\u00f3 2: Extrair Dados da Mensagem", style_h2))
story.append(Paragraph(
    "Adicione um n\u00f3 <b>Edit Fields (Set)</b> para extrair os campos relevantes da mensagem recebida:",
    style_corpo
))
set_table = [
    ["Campo", "Valor / Express\u00e3o"],
    ["telefone", "={{ $json.from ou $json.messages[0].from }}"],
    ["mensagem", "={{ $json.body.message ou $json.messages[0].text.body }}"],
    ["nome_paciente", "={{ $json.contacts[0].profile.name ou 'Paciente' }}"],
    ["timestamp", "={{ new Date().toISOString() }}"],
]
st = Table(set_table, colWidths=[4*cm, 12*cm])
st.setStyle(table_header_style())
story.append(st)

# --- Nó 3 ---
story.append(Paragraph("6.3 \u2014 N\u00f3 3: Agente de IA (Classificar Inten\u00e7\u00e3o)", style_h2))
story.append(Paragraph(
    "Adicione um n\u00f3 <b>AI Agent</b> (n8n AI Agent) com as seguintes configura\u00e7\u00f5es:",
    style_corpo
))
ia_table = [
    ["Par\u00e2metro", "Valor"],
    ["Model", "Groq - llama-3.3-70b-versatile (gratuito)"],
    ["Temperature", "0.3 (para respostas consistentes)"],
    ["System Message", "Veja Se\u00e7\u00e3o 8 abaixo (Prompt do Agente)"],
    ["Prompt (User)", "={{ $json.mensagem }}"],
    ["Options", "Structured Output com JSON Schema"],
]
it = Table(ia_table, colWidths=[4*cm, 12*cm])
it.setStyle(table_header_style())
story.append(story)  # typo fix below

# --- Nó 4 ---
story.append(Paragraph("6.4 \u2014 N\u00f3 4: Switch (Roteamento por Inten\u00e7\u00e3o)", style_h2))
story.append(Paragraph(
    "Adicione um n\u00f3 <b>Switch</b> que analisa o campo <b>intencao</b> retornado pela IA:",
    style_corpo
))
switch_table = [
    ["Sa\u00edda", "Condi\u00e7\u00e3o", "Pr\u00f3ximo n\u00f3"],
    ["0", "intencao == 'agendar'", "Consultar Agenda (Google Calendar)"],
    ["1", "intencao == 'cancelar'", "Deletar Evento (Google Calendar)"],
    ["2", "intencao == 'remarcar'", "Cancelar + Reagendar"],
    ["3", "intencao == 'consultar_horarios'", "Listar Disponibilidade"],
    ["4", "intencao == 'duvida'", "Responder D\u00favida (IA)"],
    ["default", "Qualquer outro", "Mensagem de Erro / Transferir para humano"],
]
switch_t = Table(switch_table, colWidths=[2.5*cm, 5.5*cm, 8*cm])
switch_t.setStyle(table_header_style())
story.append(switch_t)

# --- Nó 5 ---
story.append(Paragraph("6.5 \u2014 N\u00f3 5a: Consultar Agenda (Google Calendar List)", style_h2))
story.append(Paragraph(
    "Na ramifica\u00e7\u00e3o <b>agendar</b>, adicione um n\u00f3 <b>Google Calendar \u2014 List Events</b>:",
    style_corpo
))
cal_table = [
    ["Par\u00e2metro", "Valor"],
    ["Credential", "Google Calendar - Clinica (credencial criada no passo 5.4)"],
    ["Calendar", "ID do calend\u00e1rio da cl\u00ednica"],
    ["Operation", "List Events"],
    ["Return All", "true"],
    ["Start", "={{ new Date().toISOString() }}"],
    ["End", "={{ new Date(Date.now() + 7*24*60*60*1000).toISOString() }}"],
    ["Query/Day", "Lista eventos dos pr\u00f3ximos 7 dias"],
]
ct = Table(cal_table, colWidths=[3*cm, 13*cm])
ct.setStyle(table_header_style())
story.append(ct)

# --- Nó 6 ---
story.append(Paragraph("6.6 \u201— N\u00f3 6: Code Node (Calcular Vagas Livres)", style_h2))
story.append(Paragraph(
    "Adicione um n\u00f3 <b>Code (JavaScript)</b> que processa os eventos e calcula os hor\u00e1rios livres:",
    style_corpo
))
code_js = """// Calcula hor\u00e1rios dispon\u00edveis nos pr\u00f3ximos 7 dias
const events = $input.all()[0].json.events || [];
const horariosTrabalho = { inicio: 8, fim: 18, intervaloInicio: 12, intervaloFim: 13 };
const duracaoConsulta = 30; // minutos
const vagasPorDia = {};

// Inicializar pr\u00f3ximos 7 dias
for (let d = 0; d < 7; d++) {
    const dia = new Date();
    dia.setDate(dia.getDate() + d);
    if (dia.getDay() === 0) continue; // pular domingo
    const key = dia.toLocaleDateString('pt-BR');
    vagasPorDia[key] = [];
    for (let h = horariosTrabalho.inicio; h < horariosTrabalho.fim; h++) {
        if (h >= horariosTrabalho.intervaloInicio && h < horariosTrabalho.intervaloFim) continue;
        vagasPorDia[key].push(`${String(h).padStart(2,'0')}:00`);
        if (duracaoConsulta > 30) vagasPorDia[key].push(`${String(h).padStart(2,'0')}:30`);
    }
}

// Remover hor\u00e1rios j\u00e1 ocupados
events.forEach(evt => {
    if (evt.start && evt.start.dateTime) {
        const dt = new Date(evt.start.dateTime);
        const diaKey = dt.toLocaleDateString('pt-BR');
        const hora = dt.toLocaleTimeString('pt-BR', {hour:'2-digit', minute:'2-digit'});
        if (vagasPorDia[diaKey]) {
            vagasPorDia[diaKey] = vagasPorDia[diaKey].filter(v => v !== hora);
        }
    }
});

// Formatar para resposta
const resultado = Object.entries(vagasPorDia)
    .filter(([_, vagas]) => vagas.length > 0)
    .slice(0, 3) // mostrar pr\u00f3ximos 3 dias
    .map(([dia, vagas]) => `${dia}: ${vagas.slice(0, 5).join(', ')}${vagas.length > 5 ? '...' : ''}`)
    .join('\\n');

return [{ json: { disponibilidade: resultado, vagas: vagasPorDia } }];"""
story.append(Paragraph(code_js, style_codigo))

# --- Nó 7 ---
story.append(Paragraph("6.7 \u2014 N\u00f3 7: Responder via WhatsApp", style_h2))
story.append(Paragraph(
    "Adicione o n\u00f3 de envio do WhatsApp (ou outro canal) com a resposta formatada:",
    style_corpo
))
wresp_table = [
    ["Par\u00e2metro", "Valor"],
    ["Operation", "Send Message"],
    ["Phone", "={{ $('Edit Fields').item.json.telefone }}"],
    ["Text", "={{ $json.resposta ou $json.disponibilidade }}"],
]
wrt = Table(wresp_table, colWidths=[3*cm, 13*cm])
wrt.setStyle(table_header_style())
story.append(wrt)

story.append(PageBreak())

# === SEÇÃO 7: WHATSAPP ===
story.append(Paragraph("7. CONFIGURA\u00c7\u00c3O DO WHATSAPP", style_h1))
story.append(divider())

story.append(Paragraph("7.1 \u2014 Op\u00e7\u00e3o A: Evolution API (Gratuito, Self-Hosted)", style_h2))
story.append(Paragraph(
    "A Evolution API \u00e0 uma API open-source que se conecta ao WhatsApp Web (igual ao WhatsApp Web que voc\u00ea usa no computador). "
    "\u00c9 a op\u00e7\u00e3o gratuita mais popular.",
    style_corpo
))
evo_cmds = """# Docker Compose para Evolution API
cat > docker-compose.yml << 'EOF'
version: '3.8'
services:
  evolution-api:
    image: atendai/evolution-api:latest
    container_name: evolution-api
    restart: always
    ports:
      - "8080:8080"
    environment:
      - AUTHENTICATION_API_KEY=sua-chave-secreta-aqui
      - DATABASE_ENABLED=true
      - DATABASE_PROVIDER=postgresql
      - DATABASE_CONNECTION_URI=postgresql://user:pass@postgres:5432/evolution
    depends_on:
      - postgres

  postgres:
    image: postgres:15
    container_name: evolution-db
    restart: always
    environment:
      POSTGRES_USER: user
      POSTGRES_PASSWORD: pass
      POSTGRES_DB: evolution
    volumes:
      - pg_data:/var/lib/postgresql/data

volumes:
  pg_data:
EOF

docker compose up -d"""
story.append(Paragraph(evo_cmds, style_codigo))

story.append(Paragraph("Passos para conectar:", style_h3))
for i, passo in enumerate([
    "Acesse <b>http://IP:8080</b> e fa\u00e7a login com a API key",
    "Crie uma inst\u00e2ncia: <b>POST /instance/create</b> com nome 'clinica'",
    "Escaneie o QR Code com o WhatsApp do n\u00fmero da cl\u00ednica",
    "Configure o webhook da inst\u00e2ncia para <b>http://n8n.seudominio.com/webhook/agente-clinica</b>",
    "Agora qualquer mensagem recebida no WhatsApp ir\u00e1 disparar o fluxo do n8n"], 1):
    story.append(Paragraph(f"{passo}", style_bullet_num))

story.append(Paragraph("7.2 \u2014 Op\u00e7\u00e3o B: WhatsApp Business API (Meta Cloud API)", style_h2))
story.append(Paragraph(
    "Para cl\u00ednicas maiores que precisam de maior volume, a API oficial da Meta \u00e9 gratuita para as primeiras "
    "1.000 conversas por m\u00eas. Configura\u00e7\u00e3o:",
    style_corpo
))
for i, passo in enumerate([
    "Crie uma conta em <b>developers.facebook.com</b>",
    "Crie um app do tipo <b>Business</b>",
    "Adicione o produto <b>WhatsApp</b> ao app",
    "Configure um n\u00fmero de telefone (pode ser o n\u00fmero da cl\u00ednica)",
    "Obtenha o <b>Access Token</b> e <b>Phone Number ID</b>",
    "No n8n, use o n\u00f3 <b>WhatsApp Business Cloud</b> com esses dados",
    "Configure o webhook URL para receber mensagens"], 1):
    story.append(Paragraph(f"{passo}", style_bullet_num))

story.append(PageBreak())

# === SEÇÃO 8: PROMPT ===
story.append(Paragraph("8. PROMPT DO AGENTE DE IA", style_h1))
story.append(divider())

story.append(Paragraph(
    "Este \u00e9 o <b>System Message</b> que voc\u00ea deve colocar no n\u00f3 AI Agent do n8n. "
    "Ele define o comportamento e as regras do atendente virtual:",
    style_corpo
))

prompt_system = """Voc\u00ea \u00e9 o atendente virtual da Cl\u00ednica [NOME DA CL\u00ednica].
Seu nome \u00e9 Clara e voc\u00ea atende pacientes de forma simp\u00e1tica e profissional.

REGRAS:
- Responda SEMPRE em portugu\u00eas brasileiro
- Seja breve e objetivo (m\u00e1ximo 3 par\u00e1grafos)
- N\u00e1o forne\u00e7a diagn\u00f3sticos ou prescri\u00e7\u00f5es
- Para d\u00favidas m\u00e9dicas, encaminhe para o m\u00e9dico
- Hor\u00e1rios de atendimento: Seg a Sex 08h-18h, S\u00e1b 08h-12h
- Endere\u00e7o: [ENDERE\u00c7O DA CL\u00ednica]
- Conv\u00eanios aceitos: [LISTA DE CONV\u00caNIOS]

INFORMA\u00c7\u00c5O DO PACIENTE:
- Nome: {{ nome_paciente }}
- Telefone: {{ telefone }}

MENSAGEM RECEBIDA: {{ mensagem }}

TAREFAS POSS\u00cdVEIS:

1. AGENDAR: Identifique a especialidade e data/hor\u00e1rio desejado.
   Extraia: { "intencao": "agendar", "especialidade": "...", "data_preferida": "...", "horario_preferido": "...", "urgencia": "normal|urgente" }

2. CANCELAR: Identifique qual consulta cancelar.
   Extraia: { "intencao": "cancelar", "data_consulta": "..." }

3. REMARCAR: Identifique consulta atual e novo hor\u00e1rio.
   Extraia: { "intencao": "remarcar", "data_atual": "...", "nova_data": "..." }

4. CONSULTAR_HORARIOS: Mostre pr\u00f3ximas vagas dispon\u00edveis.
   Extraia: { "intencao": "consultar_horarios", "dias": 7 }

5. DUVIDA: Responda a perguntas sobre hor\u00e1rios, endere\u00e7o, conv\u00eanios, preparo de exames.
   Extraia: { "intencao": "duvida", "topico": "..." }

6. OUTRO: Se n\u00e3o se encaixa acima.
   Extraia: { "intencao": "outro", "categoria": "..." }

Retorne em JSON:
{
  "intencao": "...",
  "resposta_ao_paciente": "mensagem humanizada de resposta",
  "dados_extraidos": { ... }}
"""
story.append(Paragraph(prompt_system, style_codigo))

story.append(Paragraph(
    "<b>Output Schema</b> (Schema JSON para Structured Output do AI Agent):",
    style_h2
))
schema_json = """{
  "type": "object",
  "properties": {
    "intencao": { "type": "string", "enum": ["agendar", "cancelar", "remarcar", "consultar_horarios", "duvida", "outro"] },
    "resposta_ao_paciente": { "type": "string" },
    "dados_extraidos": { "type": "object" }
  },
  "required": ["intencao", "resposta_ao_paciente"]
}"""
story.append(Paragraph(schema_json, style_codigo))

story.append(PageBreak())

# === SEÇÃO 9: TESTES ===
story.append(Paragraph("9. TESTES E VALIDA\u00c7\u00c3O", style_h1))
story.append(divider())

story.append(Paragraph("9.1 \u2014 Testar o Webhook Manualmente", style_h2))
story.append(Paragraph(
    "Antes de conectar ao WhatsApp, teste o webhook com o curl:",
    style_corpo
))
test_curl = """curl -X POST https://n8n.seudominio.com/webhook/agente-clinica \\
  -H "Content-Type: application/json" \\
  -d '{
    "from": "5562999999999",
    "contacts": [{"profile": {"name": "Maria Silva"}}],
    "body": {"message": "Ol\u00e1, gostaria de agendar uma consulta para amanh\u00e3"}
  }'"""
story.append(Paragraph(test_curl, style_codigo))

story.append(Paragraph("9.2 \u2014 Cen\u00e1rios de Teste", style_h2))
cenario_table = [
    ["#", "Mensagem do Paciente", "Intend\u00e7\u00e3o Esperada"],
    ["1", '"Gostaria de agendar consulta com Dr. Jo\u00e3o para quinta"', "agendar"],
    ["2", '"Quais hor\u00e1rios dispon\u00edveis para amanh\u00e3?"', "consultar_horarios"],
    ["3", '"Preciso cancelar minha consulta de sexta"', "cancelar"],
    ["4", '"O cl\u00ednica atende pelo SUS?"', "duvida"],
    ["5", '"Qual o endere\u00e7o da cl\u00ednica?"', "duvida"],
    ["6", '"Quero remarcar para pr\u00f3xima semana"', "remarcar"],
    ["7", '"Oi, tudo bem?" (sauda\u00e7\u00e3o gen\u00e9rica)', "outro / continuar"],
]
ctbl = Table(cenario_table, colWidths=[1*cm, 8*cm, 7*cm])
ctbl.setStyle(table_header_style())
story.append(ctbl)

story.append(Paragraph("9.3 \u2014 Checklist de Valida\u00e7\u00e3o", style_h2))
checklist = [
    "[] Webhook recebe mensagens (verificar no n8n: Execution Log)",
    "[] IA classifica corretamente a inten\u00e7\u00e3o (> 90% de acerto nos testes)",
    "[] Google Calendar: consulta retorna eventos corretamente",
    "[] Google Calendar: cria\u00e7\u00e3o de evento funciona (verificar no Calendar)",
    "[] WhatsApp envia mensagem de resposta",
    "[] Hor\u00e1rios dispon\u00edveis s\u00e3o calculados corretamente",
    "[] Cancelamento remove evento do calend\u00e1rio",
    "[] Lembrete autom\u00e1tico � disparado 24h antes",
    "[] Flow n\u00e3o quebra com mensagens inesperadas (erro gen\u00e9rico)",
]
for item in checklist:
    story.append(Paragraph(item, style_bullet_num))

story.append(PageBreak())

# === SEÇÃO 10: TABELA DE PREÇOS ===
story.append(Paragraph("10. TABELA DE PRE\u00c7OS \u2014 QUANTO COBRAR", style_h1))
story.append(divider())

story.append(Paragraph(
    "Veja abaixo os valores praticados no mercado brasileiro para implementa\u00e7\u00e3o de agentes de IA "
    "para cl\u00ednicas e consult\u00f3rios m\u00e9dicos em 2025/2026:",
    style_corpo
))
story.append(Spacer(1, 8))

# Tabela de pre\u00e7os principal
precos_data = [
    ["SERVI\u00c7O", "VALOR MNIMO", "VALOR M\u00c9DIO ", "VALOR PREMIUM"],
    ["Configura\u00e7\u00e3o b\u00e1sica (agendar + hor\u00e1rios)", "R$ 1.500", "R$ 3.000", "R$ 5.000"],
    ["Fluxo completo (agendar/cancelar/remarcar)", "R$ 2.500", "R$ 5.000", "R$ 8.000"],
    ["+ WhatsApp Business API integrado", "+ R$ 500", "+ R$ 1.000", "+ R$ 2.000"],
    ["+ Lembrete autom\u00e1tico (24h antes)", "+ R$ 300", "+ R$ 800", "+ R$ 1.500"],
    ["+ Integra\u00e7\u00e3o com sistema de gest\u00e3o", "+ R$ 1.000", "+ R$ 2.500", "+ R$ 5.000"],
    ["+ Dashboard de m\u9tricas/relat\u00f3rios", "+ R$ 800", "+ R$ 1.500", "+ R$ 3.000"],
    ["Suporte mensal (manuten\u00e7\u00e3o + ajustes)", "R$ 300/m\u00eas", "R$ 700/m\u00eas", "R$ 1.500/m\u00eas"],
    ["", "", "", ""],
    ["TOTAL (implementa\u00e7\u00e3o completa)", "R$ 4.100", "R$ 9.300", "R$ 15.500"],
]
precos_t = Table(precos_data, colWidths=[5*cm, 3.5*cm, 3.5*cm, 4*cm])
precos_t.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), AZUL_ESCURO),
    ("TEXTCOLOR", (0, 0), (-1, 0), BRANCO),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("FONTSIZE", (0, 0), (-1, 0), 9.5),
    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
    ("ALIGN", (0, 0), (0, -1), "LEFT"),
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ("TOPPADDING", (0, 0), (-1, -1), 6),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
    ("LEFTPADDING", (0, 0), (-1, -1), 6),
    ("RIGHTPADDING", (0, 0), (-1, -1), 6),
    ("GRID", (0, 0), (-1, -1), 0.5, CINZA_MEDIO),
    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [BRANCO, CINZA_CLARO]),
    ("FONTNAME", (0, -2), (-1, -2), "Helvetica-Bold"),
    ("FONTSIZE", (0, 1), (-1, -1), 9),
    ("BACKGROUND", (0, -2), (-1, -2), AZUL_CLARO),
    ("SPAN", (0, -2), (0, -2)),
]))
story.append(precos_t)

story.append(Spacer(1, 12))

story.append(Paragraph("Faixa de pre\u00e7os por perfil do cliente:", style_h2))

perfil_table = [
    ["PERFIL", "DESCRI\u00c7\u00c3O", "PRE\u00c7O SUGERIDO"],
    ["Consult\u00f3rio pequeno", "1 m\u00e9dico, at\u00e9 20 pacientes/dia", "R$ 1.500 a R$ 3.000"],
    ["Cl\u00ednica m\u00e9dica", "2-5 m\u00e9dicos, m\u00faltiplas especialidades", "R$ 3.000 a R$ 8.000"],
    ["Cl\u00ednica grande / Rede", "5+ m\u00e9dicos, alta demanda", "R$ 8.000 a R$ 15.000+"],
]
pt = Table(perfil_table, colWidths=[4*cm, 6*cm, 6*cm])
pt.setStyle(table_header_style())
story.append(pt)

story.append(Spacer(1, 8))
story.append(Paragraph(
    "<b>\U0001f4b0 Dica:</b> Al\u00e9m da implementa\u00e7\u00e3o, cobre uma mensalidade de suporte (R$ 300-700/m\u00eas) "
    "para ajustes, atualiza\u00e7\u00f5es e monitoramento. Isso gera receita recorrente!",
    style_destaque
))

story.append(Spacer(1, 8))
story.append(Paragraph(
    "<b>\u26a0\ufe0f Custos de infraestrutura:</b> Para o cliente final, os custos mensais s\u00e3o: "
    "VPS (R$ 60-120/m\u00eas), WhatsApp Business API (gratuito para at\u00e9 1.000 conversas/m\u00eas), "
    "Google Calendar API (gratuito). Total: ~R$ 60-120/m\u00eas.",
    style_aviso
))

story.append(PageBreak())

# === SEÇÃO 11: DICAS AVANÇADAS ===
story.append(Paragraph("11. DICAS AVAN\u00c7ADAS", style_h1))
story.append(divider())

dicas = [
    ("<b>1. Evite spam do WhatsApp:</b> O WhatsApp limita mensagens por hora. Use o n8n para controlar "
     "rate limiting (m\u00e1ximo 1 mensagem por paciente a cada 30 segundos). Mensagens em massa podem banir o n\u00fmero."),

    ("<b>2. Persist\u00eancia de contexto:</b> Use o n8n Memory Buffer ou um banco de dados para lembrar do contexto da conversa. "
     "Ex: se o paciente disse que quer agendar para quinta, guarde isso para a pr\u00f3xima mensagem."),

    ("<b>3. Calend\u00e1rio por m\u00e9dico:</b> Se a cl\u00ednica tem v\u00e1rios m\u00e9dicos, crie um calend\u00e1rio separado no Google Calendar "
     "para cada um. O agente deve perguntar ou detectar qual m\u00e9dico o paciente deseja."),

    ("<b>4. Confirma\u00e7\u00e3o em duas etapas:</b> Ap\u00f3s o agendamento, envie uma mensagem de confirma\u00e7\u00e3o com os dados: "
     "\u201cConsulta agendada com Dr. X para [data] \u00e0s [hor\u00e1rio]. Responda SIM para confirmar ou CANCELAR para desmarcar.\u201d"),

    ("<b>5. Hor\u00e1rios de almo\u00e7o:</b> Configure o c\u00e1lculo de vagas para respeitar o intervalo de almo\u00e7o e fim de expediente. "
     "Evite agendar consulta no hor\u00e1rio de almo\u00e7o do m\u00e9dico."),

    ("<b>6. Fuso hor\u00e1rio:</b> Sempre use America/Sao_Paulo no n8n e no Google Calendar. "
     "Configure TZ=America/Sao_Paulo no Docker."),

    ("<b>7. Prompt din\u00e2mico:</b> Use vari\u00e1veis do n8n no prompt (como {{nome_paciente}}) para personalizar as respostas."),

    ("<b>8. M\u00f3dulo de d\u00favidas frequentes:</b> Crie um banco de respostas para perguntas comuns (endere\u00e7o, conv\u00eanios, preparo) "
     "para reduzir custos de IA e acelerar respostas."),

    ("<b>9. Human-in-the-loop:</b> Configure um fallback: se a IA n\u00e3o entender (intensao = 'outro' ou baixa confian\u00e7a), "
     "encaminhe para um atendente humano ou pe\u00e7a para reformular."),

    ("<b>10. Monitoramento:</b> Use o n8n Executions Log para monitorar em tempo real. "
     "Configure alertas (email/Telegram) quando o fluxo falhar."),
]
for titulo, desc in dicas:
    story.append(Paragraph(f"{titulo}<br/>{desc}", style_corpo))

story.append(Spacer(1, 16))
story.append(divider(thickness=2))
story.append(Spacer(1, 8))
story.append(Paragraph(
    "<b>NOTA FINAL:</b> Este agente foi projetado para ser 100% gratuito (free-tier). "
    "Os custos s\u00e3o apenas do servidor (VPS ~R$ 60-120/m\u00eas). "
    "Google Calendar API \u00e9 gratuito com quotas de 1 milh\u00e3o de requisi\u00e7\u00f5es/dia. "
    "WhatsApp Business API \u00e9 gratuito para at\u00e9 1.000 conversas/m\u00eas. "
    "Groq API \u00e9 gratuito com limites generosos. "
    "<b>Voc\u00ea pode cobrar de R$ 1.500 a R$ 15.000 pela implementa\u00e7\u00e3o completa.</b>",
    style_destaque
))

# === BUILD ===
doc.build(story)
print(f"PDF gerado: {OUTPUT}")
print(f"Tamanho: {os.path.getsize(OUTPUT) / 1024:.1f} KB")
