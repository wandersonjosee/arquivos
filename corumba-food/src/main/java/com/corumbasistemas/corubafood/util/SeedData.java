package com.corumbasistemas.corubafood.util;

import com.corumbasistemas.corubafood.model.*;
import com.corumbasistemas.corubafood.security.PasswordHash;
import jakarta.persistence.EntityManager;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import java.math.BigDecimal;

public class SeedData {
    private static final Logger logger = LoggerFactory.getLogger(SeedData.class);

    public static void popular() {
        EntityManager em = JPAUtil.getEntityManager();
        try {
            em.getTransaction().begin();
            Long count = em.createQuery("SELECT COUNT(e) FROM Empresa e", Long.class).getSingleResult();
            if (count > 0) { logger.info("Banco ja populado"); em.getTransaction().commit(); return; }

            Empresa empresa = new Empresa();
            empresa.setNome("Restaurante Demo");
            empresa.setDocumento("12.345.678/0001-90");
            empresa.setTelefone("(11) 99999-0000");
            empresa.setEndereco("Rua da Comida, 100");
            empresa.setCidade("Corumba");
            empresa.setEstado("MS");
            em.persist(empresa);
            em.flush();

            Categoria cat1 = new Categoria(); cat1.setNome("Pratos Principais"); cat1.setOrdem(1); cat1.setEmpresa(empresa); em.persist(cat1);
            Categoria cat2 = new Categoria(); cat2.setNome("Bebidas"); cat2.setOrdem(2); cat2.setEmpresa(empresa); em.persist(cat2);
            Categoria cat3 = new Categoria(); cat3.setNome("Sobremesas"); cat3.setOrdem(3); cat3.setEmpresa(empresa); em.persist(cat3);

            Produto p1 = new Produto(); p1.setCodigo("PRATO-001"); p1.setNome("File a Parmegiana"); p1.setDescricao("File mignon empanado com molho tomate e queijo"); p1.setPreco(new BigDecimal("45.90")); p1.setCategoria(cat1); p1.setEmpresa(empresa); em.persist(p1);
            Produto p2 = new Produto(); p2.setCodigo("PRATO-002"); p2.setNome("Espaguete ao Molho"); p2.setDescricao("Espaguete artesanal com molho bolonhesa"); p2.setPreco(new BigDecimal("32.90")); p2.setCategoria(cat1); p2.setEmpresa(empresa); em.persist(p2);
            Produto p3 = new Produto(); p3.setCodigo("BEB-001"); p3.setNome("Suco Natural"); p3.setDescricao("Suco de laranja natural (500ml)"); p3.setPreco(new BigDecimal("8.90")); p3.setCategoria(cat2); p3.setEmpresa(empresa); em.persist(p3);
            Produto p4 = new Produto(); p4.setCodigo("BEB-002"); p4.setNome("Refrigerante Lata"); p4.setDescricao("Coca-Cola, Guarana ou Fanta (350ml)"); p4.setPreco(new BigDecimal("6.50")); p4.setCategoria(cat2); p4.setEmpresa(empresa); em.persist(p4);
            Produto p5 = new Produto(); p5.setCodigo("SOB-001"); p5.setNome("Petit Gateau"); p5.setDescricao("Bolo de chocolate com centro cremoso e sorvete"); p5.setPreco(new BigDecimal("22.90")); p5.setCategoria(cat3); p5.setEmpresa(empresa); em.persist(p5);

            for (int i = 1; i <= 10; i++) {
                Mesa mesa = new Mesa(); mesa.setNumero(i); mesa.setCapacidade(i <= 4 ? 2 : i <= 7 ? 4 : 6); mesa.setStatus(Mesa.Status.LIVRE); mesa.setEmpresa(empresa); em.persist(mesa);
            }

            Usuario admin = new Usuario(); admin.setNome("Administrador"); admin.setUsername("admin"); admin.setSenha(PasswordHash.hash("admin123")); admin.setPapel(Usuario.Papel.ADMIN); admin.setEmpresa(empresa); em.persist(admin);
            Usuario garcom = new Usuario(); garcom.setNome("Garcom Joao"); garcom.setUsername("garcom"); garcom.setSenha(PasswordHash.hash("garcom123")); garcom.setPapel(Usuario.Papel.GARCOM); garcom.setEmpresa(empresa); em.persist(garcom);

            em.getTransaction().commit();
            logger.info("Seed executado: empresa, 5 produtos, 10 mesas, 2 usuarios");
        } catch (Exception e) {
            if (em.getTransaction().isActive()) em.getTransaction().rollback();
            logger.error("Erro no seed: {}", e.getMessage(), e);
            throw new RuntimeException("Falha no seed", e);
        } finally { em.close(); }
    }
}
