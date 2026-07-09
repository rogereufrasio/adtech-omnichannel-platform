# Taxonomia de Eventos

## Objetivo

Definir a classificação padronizada dos eventos utilizados pela plataforma AdTech da ShopSphere.

A taxonomia estabelece uma linguagem comum para produtores e consumidores de eventos, facilitando governança, rastreabilidade e reutilização.

---

# Domínio de Navegação

Eventos relacionados à interação dos clientes nos canais digitais.

| Evento | Descrição |
|----------|-------------|
| page_view | Visualização de página |
| session_start | Início de sessão |
| search | Realização de busca |

---

# Domínio Comercial

Eventos relacionados à jornada de compra.

| Evento | Descrição |
|----------|-------------|
| product_view | Visualização de produto |
| add_to_cart | Inclusão no carrinho |
| remove_from_cart | Remoção do carrinho |
| checkout_start | Início do checkout |
| purchase | Compra concluída |

---

# Domínio de Marketing

Eventos relacionados a campanhas e comunicação.

| Evento | Descrição |
|----------|-------------|
| campaign_impression | Impressão de campanha |
| campaign_click | Clique em campanha |
| email_open | Abertura de e-mail |
| email_click | Clique em e-mail |
| push_open | Abertura de push notification |

---

# Domínio de Cliente

Eventos relacionados ao perfil e relacionamento do cliente.

| Evento | Descrição |
|----------|-------------|
| login | Autenticação |
| logout | Encerramento de sessão |
| profile_update | Atualização cadastral |
| loyalty_registration | Adesão ao programa de fidelidade |

---

## Convenções

- Eventos devem utilizar nomenclatura em inglês;
- Eventos devem representar fatos de negócio;
- Eventos devem possuir schema versionado;
- Eventos não devem conter dados pessoais desnecessários.