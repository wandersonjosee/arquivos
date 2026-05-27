# 🚀 Guia de Deploy - VPS Dedicada Corumbá Sistemas

## Arquitetura

```
┌─────────────────────────────────────────────────────────┐
│                    VPS DEDICADA                         │
│                                                         │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐     │
│  │ SaltoGestão │  │ MesaPronta  │  │ConsultaAgenda│    │
│  │  :8080      │  │  (Desktop)  │  │  :8085      │     │
│  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘     │
│         │                │                │             │
│         └────────────────┼────────────────┘             │
│                          │                              │
│                  ┌───────▼───────┐                      │
│                  │  PostgreSQL   │                      │
│                  │  :5432        │                      │
│                  └───────────────┘                      │
│                                                         │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐     │
│  │ SaltoGestão │  │  pgAdmin    │  │ Evolution   │     │
│  │ Frontend    │  │  :5050      │  │ API :8081   │     │
│  │  :3000      │  │             │  │ (WhatsApp)  │     │
│  └─────────────┘  └─────────────┘  └─────────────┘     │
└─────────────────────────────────────────────────────────┘
         │
         │  Internet
         │
    ┌────┴────┐
    │ Cliente │  (qualquer navegador)
    │  PDV 1  │
    │  PDV 2  │
    └─────────┘
```

## Ambientes

| Ambiente | Máquina | Banco | Como rodar |
|---|---|---|---|
| **Development** | Seu PC | SQLite local | `python dev.py` |
| **Production** | VPS Dedicada | PostgreSQL | `systemctl start salto-backend` |

## Quick Start (VPS)

### Primeira vez (setup completo)

```bash
# 1. Copiar arquivos para a VPS
scp -r /opt/projects/* root@IP_DA_VPS:/opt/projects/

# 2. Na VPS, rodar o deploy automático
ssh root@IP_DA_VPS
cd /opt/projects
chmod +x deploy-vps.sh
bash deploy-vps.sh

# 3. Iniciar todos os serviços
systemctl start salto-backend
systemctl start salto-frontend
systemctl start consultaagenda-backend
```

### Atualizações (após mudanças)

```bash
# Na VPS
cd /opt/projects/SaltoGestao && git pull
cd /opt/projects/consultaagenda && git pull
cd /opt/projects/coruba-food && git pull

# Reiniciar serviços se necessário
systemctl restart salto-backend
systemctl restart consultaagenda-backend
```

## Portas

| Serviço | Porta | Acesso |
|---|---|---|
| SaltoGestão Backend | 8080 | http://IP_VPS:8080/docs |
| SaltoGestão Frontend | 3000 | http://IP_VPS:3000 |
| ConsultaAgenda Backend | 8085 | http://IP_VPS:8085/docs |
| pgAdmin | 5050 | http://IP_VPS:5050 |
| PostgreSQL | 5432 | IP_VPS:5432 |
| Evolution API | 8081 | http://IP_VPS:8081 |

## Contas Padrão

### SaltoGestão (Admin)
- **URL:** http://IP_VPS:3000/admin
- **Email:** admin@corumbasistemas.com.br
- **Senha:** corumba2026

### ConsultaAgenda (Admin)
- **URL:** http://IP_VPS:8085/admin
- **Email:** admin@consulta.com
- **Senha:** admin123

### pgAdmin
- **URL:** http://IP_VPS:5050
- **Email:** admin@corumbasistemas.com.br
- **Senha:** admin123

### PostgreSQL
- **Host:** IP_VPS
- **Porta:** 5432
- **Banco:** corumba
- **Usuário:** corumba
- **Senha:** corumba2025

## Troubleshooting

```bash
# Ver logs em tempo real
journalctl -u salto-backend -f
journalctl -u consultaagenda-backend -f

# Verificar se PostgreSQL está rodando
systemctl status postgresql
psql -U corumba -d corumba -c "SELECT 1"

# Verificar portas em uso
ss -tlnp | grep -E '3000|8080|8085|5432'

# Reiniciar tudo
systemctl restart postgresql
systemctl restart salto-backend
systemctl restart salto-frontend
systemctl restart consultaagenda-backend
```
