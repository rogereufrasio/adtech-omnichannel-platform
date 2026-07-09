# Arquitetura Alvo (Target State)

## Visão Geral

A arquitetura alvo da ShopSphere tem como objetivo substituir o modelo atual baseado em integrações batch e plataformas isoladas por uma plataforma moderna, orientada a eventos e centrada no cliente.

A nova arquitetura permitirá a captura, processamento e ativação de dados em tempo quase real, suportando iniciativas de Customer 360, personalização, analytics avançado e futuras aplicações de Inteligência Artificial.

---

## Capacidades Estratégicas

A arquitetura alvo deverá habilitar as seguintes capacidades:

- Customer 360
- Segmentação dinâmica de audiências
- Ativação omnichannel
- Governança de dados
- Observabilidade ponta a ponta
- Analytics avançado
- Integração orientada a eventos
- Compliance com LGPD

---

## Arquitetura Alvo

```text
Canais Digitais
       │
       ▼
Coleta de Eventos
       │
       ▼
Apache Kafka
       │
 ┌─────┼─────┐
 ▼     ▼     ▼
CDP Analytics Data Platform
 │             │
 ▼             ▼
Customer 360  Data Products
 │
 ▼
Audience Activation
 │
 ├── Google Ads
 ├── Meta Ads
 ├── CRM
 └── Canais Proprietários
```

---

## Mudanças Arquiteturais Principais

| Situação Atual | Arquitetura Alvo |
|----------------|------------------|
| Integrações Batch | Streaming de Eventos |
| Dados Fragmentados | Customer 360 |
| Audiências Estáticas | Segmentação Dinâmica |
| Integrações Ponto a Ponto | Arquitetura Desacoplada |
| Baixa Observabilidade | Monitoramento Centralizado |

---

## Benefícios Esperados

- Redução do tempo de ativação de campanhas;
- Melhoria da qualidade dos dados;
- Menor acoplamento entre plataformas;
- Escalabilidade para novos canais;
- Base tecnológica preparada para IA e Analytics Avançado;
- Evolução contínua da estratégia de Customer 360.