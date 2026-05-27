package com.corumbasistemas.corubafood.security;

import org.mindrot.jbcrypt.BCrypt;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

/**
 * Utilitário de hash de senha usando BCrypt.
 * - Gera hash com salt automático
 * - Verifica senha com proteção contra timing attack
 * - Compatível com migração de senhas plaintext
 */
public class PasswordHash {

    private static final Logger logger = LoggerFactory.getLogger(PasswordHash.class);
    private static final int WORKLOAD = 12;

    private PasswordHash() {}

    /**
     * Gera hash BCrypt da senha.
     */
    public static String hash(String senha) {
        if (senha == null || senha.isEmpty()) {
            throw new IllegalArgumentException("Senha não pode ser vazia");
        }
        String salt = BCrypt.gensalt(WORKLOAD);
        return BCrypt.hashpw(senha, salt);
    }

    /**
     * Verifica senha contra hash.
     * Se a senha armazenada NÃO for um hash BCrypt (plaintext legado),
     * compara diretamente e sinaliza para rehash.
     */
    public static boolean verify(String senha, String senhaArmazenada) {
        if (senha == null || senhaArmazenada == null) {
            return false;
        }

        if (isBCryptHash(senhaArmazenada)) {
            try {
                return BCrypt.checkpw(senha, senhaArmazenada);
            } catch (IllegalArgumentException e) {
                logger.warn("Hash BCrypt inválido: {}", e.getMessage());
                return false;
            }
        }

        // Compatibilidade com senhas plaintext (migração)
        logger.info("Senha em plaintext detectada - necessita migração para BCrypt");
        return senha.equals(senhaArmazenada);
    }

    /**
     * Verifica se o valor é um hash BCrypt válido.
     */
    public static boolean isBCryptHash(String valor) {
        return valor != null && valor.startsWith("$2a$") && valor.length() == 60;
    }

    /**
     * Verifica se a senha precisa ser rehashed (plaintext ou workload diferente).
     */
    public static boolean needsRehash(String senhaArmazenada) {
        if (!isBCryptHash(senhaArmazenada)) {
            return true;
        }
        return !senhaArmazenada.startsWith("$2a$" + WORKLOAD + "$");
    }
}
