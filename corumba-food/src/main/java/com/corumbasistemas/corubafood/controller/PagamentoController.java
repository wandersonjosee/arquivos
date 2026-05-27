package com.corumbasistemas.corubafood.controller;

import com.corumbasistemas.corubafood.model.Pagamento;
import com.corumbasistemas.corubafood.model.Usuario;
import com.corumbasistemas.corubafood.repository.PagamentoRepository;
import com.corumbasistemas.corubafood.security.PasswordHash;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import java.math.BigDecimal;

public class PagamentoController {
    private static final Logger logger = LoggerFactory.getLogger(PagamentoController.class);
    private final PagamentoRepository pagamentoRepo = new PagamentoRepository();
    private final AuthController authController;

    public PagamentoController(AuthController authController) { this.authController = authController; }

    public boolean aplicarDesconto(Long pedidoId, Long empresaId, BigDecimal valorDesconto, String adminUsername, String adminSenha) {
        Usuario admin = authController.autenticar(empresaId, adminUsername, adminSenha);
        if (admin == null || !authController.isAdmin(admin)) {
            logger.warn("Desconto nao autorizado por: {}", adminUsername); return false;
        }
        try {
            Pagamento pag = pagamentoRepo.buscarPorPedido(empresaId, pedidoId);
            if (pag != null) {
                pag.setDesconto(valorDesconto);
                pag.setDescontoAutorizadoPor(PasswordHash.hash(adminUsername));
                pagamentoRepo.salvar(pag);
                logger.info("Desconto {} aplicado no pedido {} por {}", valorDesconto, pedidoId, adminUsername);
                return true;
            }
            return false;
        } catch (Exception e) { logger.error("Erro aplicar desconto: {}", e.getMessage(), e); return false; }
    }

    public void registrarPagamento(Pagamento pagamento) {
        pagamentoRepo.salvar(pagamento);
        logger.info("Pagamento registrado: pedido {} - {} ({})", pagamento.getPedido().getId(), pagamento.getValor(), pagamento.getFormaPagamento());
    }
}
