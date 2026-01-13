from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm

file_path = "Curriculo_Guilherme_Ribeiro_dos_Santos.pdf"

c = canvas.Canvas(file_path, pagesize=A4)
width, height = A4

x_margin = 2 * cm
y = height - 2 * cm

def draw_line():
    global y
    c.line(x_margin, y, width - x_margin, y)
    y -= 0.8 * cm

def section(title):
    global y
    y -= 0.6 * cm
    c.setFont("Helvetica-Bold", 10)
    c.drawString(x_margin, y, title.upper())
    y -= 0.8 * cm
    draw_line()
    c.setFont("Helvetica", 9)

def text_block(text):
    global y
    for line in text.split("\n"):
        c.drawString(x_margin, y, line)
        y -= 0.5 * cm

# Cabeçalho
c.setFont("Helvetica-Bold", 14)
c.drawString(x_margin, y, "GUILHERME RIBEIRO DOS SANTOS")
y -= 0.9 * cm

c.setFont("Helvetica", 9)
c.drawString(
    x_margin, y,
    "Desenvolvedor Back-end | Analista de Sistemas"
)
y -= 0.4 * cm

c.drawString(
    x_margin, y,
    "linkedin.com/in/guilherme-r-santos9 | "
    "github.com/Guilherme-R-Santos | "
    "guilhermersantos99@outlook.com"
)
y -= 0.8 * cm
draw_line()

section("Experiência Profissional")
text_block(
"""Desenvolvedor Back-end Jr. | Abra Casa e Abra Cadabra Oficial | mar/2025 – atual
JavaScript, Node.js, PHP, APIs REST, ERP, PostgreSQL, MongoDB, atendimento N3, Scrum.

Estagiário de Desenvolvimento de Software | ago/2024 – mar/2025
Back-end com JavaScript, Node.js, APIs, DevOps, PostgreSQL, MongoDB, Scrum.

Assistente de Sistemas | Instituto Dara | mar/2024 – ago/2024
Análise de sistemas, requisitos, SQL, Azure, Windows Server, .NET, Scrum e Kanban.

Estagiário em Análise de Sistemas | jul/2023 – mar/2024
Processos, suporte, SQL, dashboards, Azure, .NET.

Analista de Backoffice | MEDGRUPO | fev/2022 – fev/2023
Atendimento consultivo e suporte multicanal."""
)

section("Formação Acadêmica")
text_block(
"""Bacharelado em Tecnologia da Informação | IBMR | 2023 – 2026
Bacharelado em Publicidade | Estácio | 2018 – 2022"""
)

section("Certificações")
text_block(
""".NET Developer | JavaScript Developer | SQL e MongoDB
Data Analytics e Power BI | AWS, Azure e DevOps
Metodologias Ágeis (Scrum, Kanban, XP)"""
)

section("Competências Técnicas")
text_block(
"""JavaScript, Node.js, PHP, C#, .NET
PostgreSQL, MongoDB, SQL Server
Azure, AWS, Docker, Linux
APIs REST, Git, GitHub, Scrum, Kanban"""
)

c.save()
print("Currículo PDF gerado com sucesso!")
