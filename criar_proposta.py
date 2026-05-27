#!/usr/bin/env python3
"""PDF - Proposta Comercial - Site para Barbearia"""
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm, cm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, HRFlowable)
import os

output_path = "/opt/projects/Proposta_Comercial_Barbearia.pdf"
doc = SimpleDocTemplate(output_path, pagesize=A4, rightMargin=2*cm, leftMargin=2*cm, topMargin=2*cm, bottomMargin=2*cm)

CP = colors.HexColor("#0b1a30")
CD = colors.HexColor("#c9a84c")
CF = colors.HexColor("#f8fafc")
CB = colors.HexColor("#e2e8f0")
CW = colors.white

styles = getSampleStyleSheet()

def add_style(name, **kw):
    styles.add(ParagraphStyle(name=name, **kw))
    return styles[name]

ST = add_style("T", fontSize=20, leading=26, textColor=CP, spaceBefore=4*mm, spaceAfter=3*mm, fontName="Helvetica-Bold")
SS = add_style("S", fontSize=14, leading=20, textColor=CP, spaceBefore=4*mm, spaceAfter=2*mm, fontName="Helvetica-Bold")
SB = add_style("SB", fontSize=10.5, leading=15, textColor=CP, spaceBefore=2*mm, spaceAfter=1.5*mm, fontName="Helvetica-Bold")
SC = add_style("SC", fontSize=9.5, leading=14.5, textColor=colors.HexColor("#334155"), spaceAfter=2*mm, fontName="Helvetica")
SI = add_style("SI", fontSize=9.5, leading=14, textColor=colors.HexColor("#334155"), fontName="Helvetica", leftIndent=5*mm, spaceAfter=1.5*mm)
SCenter = add_style("SCenter", fontSize=9, leading=13, textColor=colors.HexColor("#64748b"), alignment=TA_CENTER, fontName="Helvetica")

def hr():
    return HRFlowable(width="100%", thickness=1, color=CB, spaceAfter=2*mm, spaceBefore=1*mm)

def sp(h=3*mm):
    return Spacer(1, h)

def tmake(data, cols):
    t = Table(data, colWidths=cols)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), CP),
        ("TEXTCOLOR", (0,0), (-1,0), CW),
        ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
        ("FONTSIZE", (0,0), (-1,-1), 9),
        ("ALIGN", (0,0), (-1,0), "CENTER"),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("GRID", (0,0), (-1,-1), 0.5, CB),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [CW, CF]),
        ("TOPPADDING", (0,0), (-1,-1), 7),
        ("BOTTOMPADDING", (0,0), (-1,-1), 7),
        ("LEFTPADDING", (0,0), (-1,-1), 8),
        ("RIGHTPADDING", (0,0), (-1,-1), 8),
    ]))
    return t

story = []

# CAPA
story.append(sp(2*cm))
story.append(Paragraph("PROPOSTA COMERCIAL", add_style("capa", fontSize=32, leading=38, alignment=TA_CENTER, textColor=CP, spaceAfter=8*mm, fontName="Helvetica-Bold")))
story.append(Paragraph("Desenvolvimento de Website - Barbearia", add_style("sub", fontSize=16, leading=22, alignment=TA_CENTER, textColor=CD, fontName="Helvetica-Bold")))
story.append(sp(6*mm))
story.append(hr())
story.append(sp(4*mm))
story.append(Paragraph("Data: Maio/2025", SCenter))
story.append(Paragraph("Validade: 15 dias", SCenter))
story.append(PageBreak())

# 1. ESCOPO
story.append(Paragraph("1. ESCOPO DO PROJETO", ST))
story.append(hr())
story.append(Paragraph("Desenvolvimento de website profissional para barbearia, com visual moderno em tema escuro, totalmente responsivo (funciona em celular, tablet e computador).", SC))
story.append(sp(2*mm))
story.append(tmake([
    ["Aspecto", "Descricao"],
    ["Tipo", "Website pagina unica (One Page)"],
    ["Estilo", "Moderno, tema escuro, profissional"],
    ["Responsivo", "Sim - adaptado para celular e desktop"],
    ["Modelos", "3 opcoes de design para escolher"],
    ["Integracao", "WhatsApp para agendamento online"],
    ["Prazo", "Ate 5 dias uteis apos aprovacao"],
], [3.5*cm, 12*cm]))

# 2. MODELOS
story.append(PageBreak())
story.append(Paragraph("2. MODELOS DISPONIVEIS", ST))
story.append(hr())
story.append(Paragraph("Voce podera escolher entre 3 modelos profissionais, todos com tema escuro e totalmente personalizaveis:", SC))
story.append(sp(2*mm))
story.append(tmake([
    ["Modelo", "Estilo", "Caracteristicas", "Ideal Para"],
    ["Barber Classic", "Elegante e minimalista", "Dourado + Preto, tipografia classica", "Barbearias tradicionais"],
    ["Barber Street", "Urbano e jovem", "Vermelho + Preto, bold, animacoes", "Barbearias modernas"],
    ["Barber Premium", "Luxo e sofisticado", "Dourado suave, espacamento generoso", "Barbearias premium"],
], [2.8*cm, 3*cm, 4.5*cm, 5*cm]))

story.append(Paragraph("Todos os modelos incluem:", SB))
for x in [
    "Pagina unica com todas as informacoes",
    "Secao de servicos com precos",
    "Secao de barbeiros com fotos e bio",
    "Botao de agendamento via WhatsApp em cada servico",
    "Localizacao e horarios de funcionamento",
    "Links para redes sociais",
    "Design responsivo (celular + desktop)",
    "Codigo comentado para facil personalizacao",
]:
    story.append(Paragraph("  " + x, SI))

# 3. PACOTES
story.append(PageBreak())
story.append(Paragraph("3. PACOTES E PRECOS", ST))
story.append(hr())

story.append(Paragraph("PACOTE BASICO", SS))
story.append(Paragraph("Ideal para quem quer um site profissional rapido e economico.", SC))
story.append(tmake([
    ["Item", "Descricao", "Valor"],
    ["Escolha do modelo", "3 opcoes para escolher o estilo ideal", "Incluso"],
    ["Personalizacao", "Nome, textos, cores, fotos, precos, barbeiros", "Incluso"],
    ["WhatsApp", "Links de agendamento em cada servico", "Incluso"],
    ["Responsivo", "Adaptado para celular e desktop", "Incluso"],
    ["Hospedagem", "Dominio .com.br + hospedagem (1 ano)", "R$ 149"],
    ["", "TOTAL PACOTE BASICO", "R$ 497"],
], [4*cm, 8*cm, 4*cm]))

story.append(sp(4*mm))
story.append(Paragraph("PACOTE COMPLETO (RECOMENDADO)", SS))
story.append(Paragraph("Para quem quer tudo pronto para comecar a atrair clientes online.", SC))
story.append(tmake([
    ["Item", "Descricao", "Valor"],
    ["Tudo do Basico", "Modelo + personalizacao + WhatsApp + responsivo", "Incluso"],
    ["SEO Basico", "Otimizacao para Google (Google Meu Negocio)", "R$ 199"],
    ["Fotos profissionais", "Tratamento de ate 10 fotos (Photoshop)", "R$ 200"],
    ["Manutencao", "Suporte e alteracoes por 2 meses", "Cortesia"],
    ["Hospedagem", "Dominio .com.br + hospedagem (1 ano)", "Cortesia"],
    ["", "TOTAL PACOTE COMPLETO", "R$ 897"],
], [4*cm, 8*cm, 4*cm]))

story.append(sp(4*mm))
story.append(Paragraph("Adicionais opcionais:", SB))
for x in [
    "Foto adicional (tratamento Photoshop): R$ 20/cada",
    "Manutencao mensal (apos 2 meses): R$ 80/mes",
    "Criacao de logo: R$ 150",
    "Sistema de agendamento online avancado: R$ 500",
    "Pagina extra adicional: R$ 100/pagina",
]:
    story.append(Paragraph("  " + x, SI))

# 4. DIFERENCIAIS
story.append(PageBreak())
story.append(Paragraph("4. DIFERENCIAIS", ST))
story.append(hr())
story.append(tmake([
    ["Diferencial", "Beneficio para o cliente"],
    ["3 modelos profissional", "Escolha o estilo que mais combina com sua barbearia"],
    ["Tema escuro moderno", "Visual sofisticado que diferencia da concorrencia"],
    ["Agendamento via WhatsApp", "Cliente agenda direto pelo site, sem ligacao"],
    ["100% responsivo", "Funciona perfeitamente em qualquer celular"],
    ["Codigo comentado", "Facil de atualizar ou passar para outro desenvolvedor"],
    ["Opcao de SEO", "Aparece no Google quando alguem procurar barbearia"],
    ["Manutencao inclusa", "2 meses de suporte sem custo no Pacote Completo"],
], [5*cm, 11*cm]))

# 5. PRAZO E PAGAMENTO
story.append(Paragraph("5. PRAZO E PAGAMENTO", ST))
story.append(hr())
story.append(tmake([
    ["Item", "Condicao"],
    ["Prazo de entrega", "Basico: 3 dias uteis | Completo: 5 dias uteis"],
    ["Forma de pagamento", "Pix, transferencia ou boleto"],
    ["Parcelamento", "Em ate 2x sem juros"],
    ["Sinal para iniciar", "50% no inicio + 50% na entrega"],
    ["Validade da proposta", "15 dias da data de emissao"],
], [5*cm, 11*cm]))

# 6. PROXIMOS PASSOS
story.append(Paragraph("6. PROXIMOS PASSOS", ST))
story.append(hr())
story.append(Paragraph("Para iniciar o projeto, preciso que voce me envie:", SC))
story.append(sp(2*mm))
for i, x in enumerate([
    "Escolha do modelo (1, 2 ou 3) - posso enviar link para visualizar",
    "Logo da barbearia (se tiver)",
    "Fotos da barbearia e dos barbeiros",
    "Lista de servicos e precos atuais",
    "Endereco e telefone/WhatsApp",
    "Link do Instagram (se tiver)",
    "Textos ou informacoes que quer destacar",
], 1):
    story.append(Paragraph(str(i) + ". " + x, SI))

story.append(sp(5*mm))
story.append(Paragraph("=" * 50, SCenter))
story.append(Paragraph("Proposta gerada por OWL - Hermes Agent", SCenter))

doc.build(story)
print("PDF criado: " + output_path + " (" + str(os.path.getsize(output_path) // 1024) + " KB)")
