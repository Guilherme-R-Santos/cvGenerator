# 📄 Gerador de Currículo em PDF

![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)
![ReportLab](https://img.shields.io/badge/reportlab-4.0+-green.svg)

Script em Python que gera um currículo profissional em formato PDF de forma automatizada, utilizando a biblioteca **ReportLab**. Ideal para quem deseja manter uma versão sempre atualizada do currículo sem precisar abrir editores gráficos.

## 🚀 Funcionalidades

- Geração de PDF **pronto para impressão** em tamanho A4.
- Estrutura organizada com:
  - Cabeçalho com nome, cargo e contatos.
  - Seções separadas por linhas horizontais.
  - Blocos de texto com formatação limpa e espaçamento adequado.
- Fácil personalização: altere as informações diretamente no código.
- Utiliza apenas **fontes padrão** (Helvetica) – não requer fontes externas.

## 🖥️ Como funciona

O script constrói o PDF passo a passo:

1. Define o arquivo de saída (`Curriculo_Guilherme_Ribeiro_dos_Santos.pdf`) e o tamanho da página (A4).
2. Configura margens e posição inicial do texto.
3. Define funções auxiliares:
   - `draw_line()`: desenha uma linha horizontal separadora.
   - `section(title)`: adiciona um título de seção em negrito, maiúsculo, com linha abaixo.
   - `text_block(text)`: escreve um bloco de texto com quebras de linha automáticas.
4. Escreve o cabeçalho e cada seção com seu conteúdo.
5. Salva o arquivo PDF.

## 🛠️ Pré-requisitos

- **Python 3.x** instalado.
- Biblioteca **ReportLab** (instalável via pip).

## 📦 Instalação

1. Clone ou baixe este repositório:
   ```bash
   git clone https://github.com/seu-usuario/gerador-curriculo.git
   cd gerador-curriculo
Instale a dependência necessária:

bash
pip install reportlab
Execute o script:

bash
python generator.py
🎨 Personalização
Edite o arquivo generator.py para ajustar as informações conforme seu currículo.

1. Dados pessoais e contato
Altere as linhas do cabeçalho:

python
c.drawString(x_margin, y, "SEU NOME COMPLETO")
c.drawString(x_margin, y, "Seu cargo ou área")
c.drawString(x_margin, y, "linkedin.com/in/seu-perfil | github.com/seu-usuario | seu-email@exemplo.com")
2. Seções e conteúdos
Cada seção é definida por uma chamada a section() seguida de text_block() com o conteúdo:

python
section("Experiência Profissional")
text_block(
"""Cargo | Empresa | período
Principais atividades e realizações.

Próxima experiência..."""
)
Adicione ou remova seções conforme necessário. O script já inclui:

Experiência Profissional

Formação Acadêmica

Certificações

Competências Técnicas

Você pode alterar os textos, criar novas seções ou remover as existentes.

3. Ajustes de layout
Margens: altere x_margin e y inicial para modificar o espaçamento das bordas.

Espaçamento: os valores em cm (ex: 0.8 * cm) controlam os espaços entre elementos. Ajuste conforme sua preferência.

Fontes: por padrão usa Helvetica e Helvetica-Bold. Caso queira outras, instale e registre as fontes no ReportLab (consulte a documentação).
