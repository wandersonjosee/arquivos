package com.corumbasistemas.corubafood.security;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class PasswordHashTest {
    @Test void testHashECriar() {
        String hash = PasswordHash.hash("senha123");
        assertNotNull(hash);
        assertTrue(hash.startsWith("$2a$"));
        assertEquals(60, hash.length());
    }
    @Test void testVerifySenhaCorreta() {
        String hash = PasswordHash.hash("minha_senha");
        assertTrue(PasswordHash.verify("minha_senha", hash));
    }
    @Test void testVerifySenhaIncorreta() {
        String hash = PasswordHash.hash("minha_senha");
        assertFalse(PasswordHash.verify("senha_errada", hash));
    }
    @Test void testVerifyPlaintextLegado() {
        assertTrue(PasswordHash.verify("senha_antiga", "senha_antiga"));
    }
    @Test void testNeedsRehash() {
        assertTrue(PasswordHash.needsRehash("senha_plaintext"));
        assertFalse(PasswordHash.needsRehash(PasswordHash.hash("teste")));
    }
    @Test void testIsBCryptHash() {
        assertTrue(PasswordHash.isBCryptHash(PasswordHash.hash("teste")));
        assertFalse(PasswordHash.isBCryptHash("plaintext"));
        assertFalse(PasswordHash.isBCryptHash(null));
    }
    @Test void testNullSafety() {
        assertFalse(PasswordHash.verify(null, "hash"));
        assertFalse(PasswordHash.verify("senha", null));
    }
    @Test void testSenhaVazia() {
        assertThrows(IllegalArgumentException.class, () -> PasswordHash.hash(""));
    }
}
