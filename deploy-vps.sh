#!/bin/bash
# ============================================================
# deploy-vps.sh - Script de Deploy na VPS Dedicada
# ============================================================
# Uso: bash deploy-vps.sh
# ============================================================

set -e

echo "============================================"
echo "🚀 Deploy Corumbá Sistemas - VPS Dedicada"
echo "============================================"

# --- Configurações ---
VPS_USER="root"
VPS_IP="${1:-SEU_IP_AQUI}"
PROJECTS_DIR="/opt/projects"
NODE_VERSION="20"

# --- Cores ---
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

log() { echo -e "${GREEN}✅ $1${NC}"; }
warn() { echo -e "${YELLOW}⚠️  $1${NC}"; }
err() { echo -e "${RED}❌ $1${NC}"; exit 1; }

# ============================================================
# 1. ATUALIZAR SISTEMA
# ============================================================
echo ""
echo "📦 [1/7] Atualizando sistema..."
apt-get update -qq && apt-get upgrade -y -qq
log "Sistema atualizado"

# ============================================================
# 2. INSTALAR DEPENDÊNCIAS
# ============================================================
echo ""
echo "📦 [2/7] Instalando dependências..."

# Python 3.12+
apt-get install -y -qq python3 python3-pip python3-venv

# Node.js 20
if ! command -v node &> /dev/null; then
    curl -fsSL https://deb.nodesource.com/setup_${NODE_VERSION}.x | bash -
    apt-get install -y -qq nodejs
    log "Node.js $(node --version) instalado"
else
    log "Node.js $(node --version) já instalado"
fi

# PostgreSQL 16
if ! command -v psql &> /dev/null; then
    apt-get install -y -qq postgresql postgresql-contrib
    log "PostgreSQL instalado"
else
    log "PostgreSQL já instalado"
fi

# Java 17 (MesaPronta)
if ! command -v java &> /dev/null; then
    apt-get install -y -qq openjdk-17-jdk
    log "Java 17 instalado"
else
    log "Java $(java -version 2>&1 | head -1) já instalado"
fi

# Docker (Evolution API)
if ! command -v docker &> /dev/null; then
    curl -fsSL https://get.docker.com | sh
    systemctl enable docker && systemctl start docker
    log "Docker instalado"
else
    log "Docker já instalado"
fi

# ============================================================
# 3. CONFIGURAR POSTGRESQL
# ============================================================
echo ""
echo "🗄️  [3/7] Configurando PostgreSQL..."

systemctl start postgresql

# Criar banco e usuário
su - postgres -c "
psql -c \"CREATE USER corumba WITH PASSWORD 'corumba2025' CREATEDB;\" 2>/dev/null || true
psql -c \"CREATE DATABASE corumba OWNER corumba;\" 2>/dev/null || true
psql -c \"GRANT ALL PRIVILEGES ON DATABASE corumba TO corumba;\" 2>/dev/null || true
"

# Aceitar conexões externas
PG_HBA=$(su - postgres -c "psql -t -c 'SHOW hba_file;'" | tr -d ' ')
if ! grep -q "corumba" "$PG_HBA" 2>/dev/null; then
    echo "host    corumba    corumba    0.0.0.0/0    md5" >> "$PG_HBA"
    systemctl restart postgresql
fi

log "PostgreSQL configurado (porta 5432)"

# ============================================================
# 4. CLONAR/ATUALIZAR PROJETOS
# ============================================================
echo ""
echo "📁 [4/7] Configurando projetos..."

mkdir -p "$PROJECTS_DIR"

# Clonar repositórios (se ainda não existirem)
for repo in SaltoGestao coruba-food consultaagenda; do
    if [ ! -d "$PROJECTS_DIR/$repo" ]; then
        warn "Repositório $repo não encontrado em $PROJECTS_DIR/"
        warn "Execute manualmente: git clone https://github.com/wandersonjosee/$repo.git"
    else
        cd "$PROJECTS_DIR/$repo" && git pull 2>/dev/null || true
        log "$repo atualizado"
    fi
done

# ============================================================
# 5. CONFIGURAR AMBIENTE PYTHON
# ============================================================
echo ""
echo "🐍 [5/7] Configurando ambiente Python..."

# Instalar dependências SaltoGestão
if [ -f "$PROJECTS_DIR/SaltoGestao/backendPy/dev.py" ]; then
    cd "$PROJECTS_DIR/SaltoGestao/backendPy"
    pip3 install -q -r requirements.txt 2>/dev/null || \
    pip3 install -q fastapi uvicorn sqlalchemy python-jose passlib python-dotenv psycopg2-binary pydantic
    log "SaltoGestão backend configurado"
fi

# Instalar dependências ConsultaAgenda
if [ -f "$PROJECTS_DIR/consultaagenda/backendPy/main.py" ]; then
    cd "$PROJECTS_DIR/consultaagenda/backendPy"
    pip3 install -q -r requirements.txt 2>/dev/null || \
    pip3 install -q fastapi uvicorn sqlmodel python-jose python-dotenv psycopg2-binary pydantic
    log "ConsultaAgenda backend configurado"
fi

# ============================================================
# 6. CONFIGURAR FRONTEND
# ============================================================
echo ""
echo "🌐 [6/7] Configurando frontend..."

if [ -d "$PROJECTS_DIR/SaltoGestao/frontend-web" ]; then
    cd "$PROJECTS_DIR/SaltoGestao/frontend-web"
    npm install --silent 2>/dev/null || npm install
    log "SaltoGestão frontend configurado"
fi

# ============================================================
# 7. CRIAR SYSTEMD SERVICES
# ============================================================
echo ""
echo "⚙️  [7/7] Criando serviços automáticos..."

# SaltoGestão Backend
cat > /etc/systemd/system/salto-backend.service << 'EOF'
[Unit]
Description=SaltoGestão Backend (FastAPI)
After=network.target postgresql.service

[Service]
Type=simple
User=root
WorkingDirectory=/opt/projects/SaltoGestao/backendPy
Environment=APP_ENV=production
Environment=DATABASE_URL=postgresql+psycopg2://corumba:corumba2025@localhost:5432/corumba
ExecStart=/usr/bin/python3 dev.py
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
EOF

# SaltoGestão Frontend
cat > /etc/systemd/system/salto-frontend.service << 'EOF'
[Unit]
Description=SaltoGestão Frontend (Next.js)
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/opt/projects/SaltoGestao/frontend-web
ExecStart=/usr/bin/npm run start
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
EOF

# ConsultaAgenda Backend
cat > /etc/systemd/system/consultaagenda-backend.service << 'EOF'
[Unit]
Description=ConsultaAgenda Backend (FastAPI)
After=network.target postgresql.service

[Service]
Type=simple
User=root
WorkingDirectory=/opt/projects/consultaagenda/backendPy
Environment=APP_ENV=production
Environment=DATABASE_URL=postgresql+psycopg2://corumba:corumba2025@localhost:5432/corumba
ExecStart=/usr/bin/python3 dev.py
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
EOF

# Recarregar systemd
systemctl daemon-reload

# Habilitar serviços
systemctl enable salto-backend 2>/dev/null || true
systemctl enable salto-frontend 2>/dev/null || true
systemctl enable consultaagenda-backend 2>/dev/null || true

log "Serviços criados e habilitados"

# ============================================================
# RESUMO
# ============================================================
echo ""
echo "============================================"
echo "✅ Deploy concluído!"
echo "============================================"
echo ""
echo "📋 Serviços:"
echo "  SaltoGestão Backend:  systemctl start salto-backend"
echo "  SaltoGestão Frontend: systemctl start salto-frontend"
echo "  ConsultaAgenda:       systemctl start consultaagenda-backend"
echo ""
echo "📋 Portas:"
echo "  SaltoGestão:          http://$(hostname -I | awk '{print $1}'):8080"
echo "  SaltoGestão Frontend: http://$(hostname -I | awk '{print $1}'):3000"
echo "  ConsultaAgenda:       http://$(hostname -I | awk '{print $1}'):8085"
echo "  pgAdmin:              http://$(hostname -I | awk '{print $1}'):5050"
echo "  PostgreSQL:           $(hostname -I | awk '{print $1}'):5432"
echo ""
echo "📋 Comandos úteis:"
echo "  Ver logs:     journalctl -u salto-backend -f"
echo "  Reiniciar:    systemctl restart salto-backend"
echo "  Status:       systemctl status salto-backend"
echo ""
