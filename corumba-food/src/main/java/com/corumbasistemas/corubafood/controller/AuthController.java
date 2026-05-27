package com.corumbasistemas.corubafood.controller;

import com.corumbasistemas.corubafood.model.Empresa;
import com.corumbasistemas.corubafood.model.Usuario;
import com.corumbasistemas.corubafood.repository.UsuarioRepository;
import com.corumbasistemas.corubafood.security.PasswordHash;
import com.corumbasistemas.corubafood.util.JPAUtil;
import jakarta.persistence.EntityManager;
import jakarta.persistence.NoResultException;
import jakarta.persistence.TypedQuery;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class AuthController {
    private static final Logger logger = LoggerFactory.getLogger(AuthController.class);
    private final UsuarioRepository usuarioRepo = new UsuarioRepository();

    public Usuario autenticar(Long empresaId, String username, String senha) {
        try {
            Usuario usuario = usuarioRepo.buscarPorUsername(empresaId, username);
            if (usuario == null) {
                PasswordHash.hash("dummy_password_timing_protection");
                logger.warn("Login usuario inexistente: {} (empresa: {})", username, empresaId);
                return null;
            }
            if (!PasswordHash.verify(senha, usuario.getSenha())) {
                logger.warn("Senha invalida para: {} (empresa: {})", username, empresaId);
                return null;
            }
            if (PasswordHash.needsRehash(usuario.getSenha())) {
                logger.info("Migrando senha de {} para BCrypt...", username);
                usuario.setSenha(PasswordHash.hash(senha));
                usuarioRepo.salvar(usuario);
            }
            logger.info("Login OK: {} (empresa: {}, papel: {})", username, empresaId, usuario.getPapel());
            return usuario;
        } catch (Exception e) { logger.error("Erro autenticacao: {}", e.getMessage(), e); return null; }
    }

    public Empresa buscarEmpresaPorDocumento(String documento) {
        EntityManager em = JPAUtil.getEntityManager();
        try { return em.createQuery("SELECT e FROM Empresa e WHERE e.documento = :doc AND e.ativo = true", Empresa.class).setParameter("doc", documento).getSingleResult(); }
        catch (NoResultException e) { return null; } finally { em.close(); }
    }

    public boolean isAdmin(Usuario usuario) { return usuario != null && usuario.getPapel() == Usuario.Papel.ADMIN; }
}
