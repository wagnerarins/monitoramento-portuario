# Monitoramento Automático de Movimentação Portuária (SC)

Este projeto automatiza a coleta, processamento e visualização de dados das zonas portuárias ZP-21 (Itajaí/NVT) e ZP-18 (SFS/Itapoá).

##  Funcionamento
1. **Coleta (Python):** Um script realiza o web scraping dos dados de embarque e desembarque de práticos.
2. **Automação (GitHub Actions):** O robô acorda diariamente às 06:00 (BRT), executa a coleta e atualiza um arquivo CSV no repositório.
3. **Visualização (Power BI):** O dashboard consome o CSV direto do GitHub e atualiza automaticamente às 08:00 (BRT), garantindo dados sempre frescos sem intervenção humana.

## Tecnologias
- **Linguagem:** Python (Pandas/BeautifulSoup)
- **CI/CD:** GitHub Actions
- **BI:** Power BI Service (Cloud)

## Insights do Dashboard
- Volume de manobras por berço e origem.
- Monitoramento de KPIs de saídas totais por zona.
