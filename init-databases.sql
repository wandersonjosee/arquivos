-- ============================================================
-- init-databases.sql
-- Cria os bancos de dados para cada sistema
-- Executado automaticamente na primeira vez que o PostgreSQL sobe
-- ============================================================

-- Banco principal (SaltoGestão + ConsultaAgenda compartilham)
CREATE DATABASE corumba;
\c corumba;

-- Schema para SaltoGestão (opcional - organização)
-- Tables serão criadas pelo SQLAlchemy na primeira execução

-- Banco MesaPronta (se quiser separado, ou usa o mesmo corumba)
-- CREATE DATABASE mesapronta;

-- Usuário dedicado para a aplicação
CREATE USER corumba_app WITH PASSWORD 'corumba2025' CREATEDB;
GRANT ALL PRIVILEGES ON DATABASE corumba TO corumba_app;
ALTER DATABASE corumba OWNER TO corumba_app;
