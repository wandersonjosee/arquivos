package com.corumbasistemas.corubafood.controller;

import com.corumbasistemas.corubafood.CorubaFoodApp;
import com.corumbasistemas.corubafood.model.Empresa;
import com.corumbasistemas.corubafood.model.Usuario;
import javafx.fxml.FXML;
import javafx.scene.control.*;
import javafx.scene.paint.Color;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class LoginController {
    private static final Logger logger = LoggerFactory.getLogger(LoginController.class);
    @FXML private TextField txtDocumento;
    @FXML private TextField txtUsername;
    @FXML private PasswordField txtSenha;
    @FXML private Label lblMensagem;
    @FXML private Button btnEntrar;
    @FXML private ProgressIndicator progress;

    @FXML public void initialize() { lblMensagem.setText(""); progress.setVisible(false); }

    @FXML
    private void handleEntrar() {
        String documento = txtDocumento.getText().trim();
        String username = txtUsername.getText().trim();
        String senha = txtSenha.getText();
        if (documento.isEmpty() || username.isEmpty() || senha.isEmpty()) {
            lblMensagem.setTextFill(Color.RED); lblMensagem.setText("Preencha todos os campos!"); return;
        }
        progress.setVisible(true); btnEntrar.setDisable(true);
        Empresa empresa = CorubaFoodApp.getAuthController().buscarEmpresaPorDocumento(documento);
        if (empresa == null) { lblMensagem.setTextFill(Color.RED); lblMensagem.setText("Empresa nao encontrada!"); progress.setVisible(false); btnEntrar.setDisable(false); return; }
        Usuario usuario = CorubaFoodApp.getAuthController().autenticar(empresa.getId(), username, senha);
        if (usuario == null) { lblMensagem.setTextFill(Color.RED); lblMensagem.setText("Usuario ou senha invalidos!"); progress.setVisible(false); btnEntrar.setDisable(false); return; }
        CorubaFoodApp.setUsuarioLogado(usuario);
        logger.info("Login: {} ({})", username, empresa.getNome());
        try { CorubaFoodApp.mostrarPrincipal(); } catch (Exception e) { logger.error("Erro carregar principal: {}", e.getMessage(), e); lblMensagem.setTextFill(Color.RED); lblMensagem.setText("Erro ao carregar sistema."); }
    }
}
