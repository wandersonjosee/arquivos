package com.corumbasistemas.corubafood.repository;

import com.corumbasistemas.corubafood.model.Pagamento;
import com.corumbasistemas.corubafood.util.JPAUtil;
import jakarta.persistence.EntityManager;
import jakarta.persistence.NoResultException;
import jakarta.persistence.TypedQuery;
import java.util.List;

public class PagamentoRepository {
    public Pagamento buscarPorPedido(Long empresaId, Long pedidoId) {
        EntityManager em = JPAUtil.getEntityManager();
        try { return em.createQuery("SELECT p FROM Pagamento p WHERE p.empresa.id = :empId AND p.pedido.id = :pedidoId", Pagamento.class).setParameter("empId", empresaId).setParameter("pedidoId", pedidoId).getSingleResult(); }
        catch (NoResultException e) { return null; } finally { em.close(); }
    }
    public List<Pagamento> buscarTodos(Long empresaId) {
        EntityManager em = JPAUtil.getEntityManager();
        try { return em.createQuery("SELECT p FROM Pagamento p WHERE p.empresa.id = :empId ORDER BY p.createdAt DESC", Pagamento.class).setParameter("empId", empresaId).getResultList(); }
        finally { em.close(); }
    }
    public Pagamento salvar(Pagamento pagamento) {
        EntityManager em = JPAUtil.getEntityManager();
        try { em.getTransaction().begin(); if (pagamento.getId() == null) em.persist(pagamento); else pagamento = em.merge(pagamento); em.getTransaction().commit(); return pagamento; }
        catch (Exception e) { if (em.getTransaction().isActive()) em.getTransaction().rollback(); throw e; } finally { em.close(); }
    }
}
