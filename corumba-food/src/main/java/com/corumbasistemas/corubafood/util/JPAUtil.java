package com.corumbasistemas.corubafood.util;

import jakarta.persistence.EntityManager;
import jakarta.persistence.EntityManagerFactory;
import jakarta.persistence.Persistence;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import java.util.HashMap;
import java.util.Map;

public class JPAUtil {
    private static final Logger logger = LoggerFactory.getLogger(JPAUtil.class);
    private static final String PU_NAME = "coruba-food-pu";
    private static volatile EntityManagerFactory emf;
    private static final Object lock = new Object();

    private JPAUtil() {}

    public static EntityManagerFactory getEntityManagerFactory() {
        if (emf == null) {
            synchronized (lock) {
                if (emf == null) {
                    try {
                        Map<String, String> props = new HashMap<>();
                        String dbPath = System.getenv("DB_PATH");
                        if (dbPath != null && !dbPath.isEmpty()) props.put("jakarta.persistence.jdbc.url", "jdbc:sqlite:" + dbPath);
                        String hbm2ddl = System.getenv("HBM2DDL_AUTO");
                        if (hbm2ddl != null) props.put("hibernate.hbm2ddl.auto", hbm2ddl);
                        String showSql = System.getenv("SHOW_SQL");
                        if (showSql != null) props.put("hibernate.show_sql", showSql);
                        emf = Persistence.createEntityManagerFactory(PU_NAME, props);
                        logger.info("EntityManagerFactory criado");
                        Runtime.getRuntime().addShutdownHook(new Thread(() -> {
                            if (emf != null && emf.isOpen()) { emf.close(); logger.info("EMF fechado (shutdown)"); }
                        }));
                    } catch (Exception e) {
                        logger.error("Erro ao criar EMF: {}", e.getMessage(), e);
                        throw new RuntimeException("Falha ao inicializar JPA", e);
                    }
                }
            }
        }
        return emf;
    }

    public static EntityManager getEntityManager() { return getEntityManagerFactory().createEntityManager(); }

    public static void shutdown() {
        synchronized (lock) {
            if (emf != null && emf.isOpen()) { emf.close(); logger.info("EMF fechado"); emf = null; }
        }
    }
}
