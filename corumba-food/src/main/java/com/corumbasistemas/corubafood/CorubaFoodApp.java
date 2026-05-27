package com.corumbasistemas.corubafood;

import com.corumbasistemas.corubafood.controller.AuthController;
import com.corumbasistemas.corubafood.model.Usuario;
import com.corumbasistemas.corubafood.util.JPAUtil;
import com.corumbasistemas.corubafood.util.SeedData;
import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class CorubaFoodApp extends Application {
    private static final Logger logger = LoggerFactory.getLogger(CorubaFoodApp.class);
    private static Stage primaryStage;
    private static AuthController authController;
    private static Usuario usuarioLogado;

    @Override
    public void start(Stage stage) throws Exception {
        primaryStage = stage;
        authController = new AuthController();
        JPAUtil.getEntityManagerFactory();
        logger.info("Coruba Food iniciado");
        try { SeedData.popular(); } catch (Exception e) { logger.warn("Seed ja executado ou erro: {}", e.getMessage()); }
        mostrarLogin();
    }

    public static void mostrarLogin() throws Exception {
        FXMLLoader loader = new FXMLLoader(CorubaFoodApp.class.getResource("/view/LoginView.fxml"));
        Parent root = loader.load();
        primaryStage.setTitle("Coruba Food - Login");
        primaryStage.setScene(new Scene(root));
        primaryStage.setResizable(false);
        primaryStage.show();
    }

    public static void mostrarPrincipal() throws Exception {
        FXMLLoader loader = new FXMLLoader(CorubaFoodApp.class.getResource("/view/PrincipalView.fxml"));
        Parent root = loader.load();
        primaryStage.setTitle("Coruba Food - MesaPronta v2.0 [" + usuarioLogado.getNome() + "]");
        primaryStage.setScene(new Scene(root, 1200, 800));
        primaryStage.setResizable(true);
        primaryStage.setMaximized(true);
    }

    public static Stage getPrimaryStage() { return primaryStage; }
    public static AuthController getAuthController() { return authController; }
    public static Usuario getUsuarioLogado() { return usuarioLogado; }
    public static void setUsuarioLogado(Usuario u) { usuarioLogado = u; }

    @Override
    public void stop() { JPAUtil.shutdown(); logger.info("Coruba Food encerrado"); }

    public static void main(String[] args) { launch(args); }
}
