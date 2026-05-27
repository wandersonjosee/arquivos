package com.corumbasistemas.corubafood.repository;

import com.corumbasistemas.corubafood.model.Usuario;
import com.corumbasistemas.corubafood.util.JPAUtil;
import jakarta.persistence.EntityManager;
import jakarta.persistence.NoResultException;
import jakarta.persistence.TypedQuery;
import java.util.List;

public class UsuarioRepository {
    public Usuario buscarPorUsername(Long empresaId, String username) {
        EntityManager em = JPAUtil.getEntityManager();
        try {
            TypedQuery<Usuario> q = em.createQuery("SELECT u FROM Usuario u WHERE u.empresa.id = :empId AND u.username = :username AND u.ativo = true", Usuario.class);
            q.setParameter("empId", empresaId); q.setParameter("username", username);
            return q.getSingleResult();
        } catch (NoResultException e) { return null; } finally { em.close(); }
    }
    public List<Usuario> buscarTodos(Long empresaId) {
        EntityManager em = JPAUtil.getEntityManager();
        try {
            return em.createQuery("SELECT u FROM Usuario u WHERE u.empresa.id = :empId AND u.ativo = true ORDER BY u.nome", Usuario.class).setParameter("empId", empresaId).getResultList();
        } finally { em.close(); }
    }
    public Usuario salvar(Usuario usuario) {
        EntityManager em = JPAUtil.getEntityManager();
        try {
            em.getTransaction().begin();
            if (usuario.getId() == null) em.persist(usuario); else usuario = em.merge(usuario);
            em.getTransaction().commit(); return usuario;
        } catch (Exception e) { if (em.getTransaction().isActive()) em.getTransaction().rollback(); throw e; }
        finally { em.close(); }
    }
}
