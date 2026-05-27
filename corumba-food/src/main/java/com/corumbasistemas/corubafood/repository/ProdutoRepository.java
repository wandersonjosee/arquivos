package com.corumbasistemas.corubafood.repository;

import com.corumbasistemas.corubafood.model.Categoria;
import com.corumbasistemas.corubafood.model.Produto;
import com.corumbasistemas.corubafood.util.JPAUtil;
import jakarta.persistence.EntityManager;
import jakarta.persistence.NoResultException;
import jakarta.persistence.TypedQuery;
import java.util.List;

public class ProdutoRepository {

    public List<Produto> buscarTodos(Long empresaId) {
        EntityManager em = JPAUtil.getEM();
        try {
            return em.createQuery(
                "SELECT p FROM Produto p WHERE p.empresa.id = :eid AND p.ativo = true ORDER BY p.categoria.nome, p.nome",
                Produto.class).setParameter("eid", empresaId).getResultList();
        } finally { em.close(); }
    }

    public List<Produto> buscarPorCategoria(Long empresaId, Long categoriaId) {
        EntityManager em = JPAUtil.getEM();
        try {
            return em.createQuery(
                "SELECT p FROM Produto p WHERE p.empresa.id = :eid AND p.categoria.id = :cid AND p.ativo = true ORDER BY p.nome",
                Produto.class).setParameter("eid", empresaId).setParameter("cid", categoriaId).getResultList();
        } finally { em.close(); }
    }

    public Produto salvar(Produto produto) {
        EntityManager em = JPAUtil.getEM();
        try {
            em.getTransaction().begin();
            if (produto.getId() == null) em.persist(produto);
            else produto = em.merge(produto);
            em.getTransaction().commit();
            return produto;
        } catch (Exception e) {
            if (em.getTransaction().isActive()) em.getTransaction().rollback();
            throw e;
        } finally { em.close(); }
    }

    public List<Categoria> buscarCategorias(Long empresaId) {
        EntityManager em = JPAUtil.getEM();
        try {
            return em.createQuery(
                "SELECT c FROM Categoria c WHERE c.empresa.id = :eid AND c.ativo = true ORDER BY c.ordem, c.nome",
                Categoria.class).setParameter("eid", empresaId).getResultList();
        } finally { em.close(); }
    }
}
