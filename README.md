# Pipeline Automatizado para Monitoramento de Logística Portuária (SC)

Este projeto implementa um fluxo completo de engenharia e análise de dados para o monitoramento de manobras de navios nas zonas de praticagem ZP-21 (Complexo Portuário de Itajaí e Navegantes) e ZP-18 (São Francisco do Sul e Itapoá).

## Arquitetura da Solução
A solução foi desenhada para operar de forma autônoma, garantindo a integridade e a atualização constante das informações:

* **Ingestão de Dados (Python):** Scripts customizados para extração (web scraping) e normalização de dados brutos provenientes dos portais de praticagem.
* **Orquestração e CI/CD (GitHub Actions):** Automação do ciclo de vida dos dados, com execuções agendadas via cron job, garantindo o versionamento e a persistência histórica em arquivo .csv.
* **Business Intelligence (Power BI Service):** Dashboard executivo integrado via nuvem, permitindo monitoramento remoto em tempo real sem dependência de infraestrutura local (Gateway).

##  Escopo Analítico
* **Produtividade por Berço:** Monitoramento do fluxo de manobras e ocupação.
* **Perfil de Frota:** Análise técnica de dimensões (Boca e Calado) para compreensão do perfil de navios que operam no complexo.
* **Histórico Operacional:** Consolidação de base de dados para análise de tendências e sazonalidade portuária.

##  Tecnologias Utilizadas
* **Linguagem:** Python 3.10 (Pandas, Selenium, WebDriver Manager)
* **Automação:** GitHub Actions
* **Visualização:** Microsoft Power BI (DAX / Power Query)
