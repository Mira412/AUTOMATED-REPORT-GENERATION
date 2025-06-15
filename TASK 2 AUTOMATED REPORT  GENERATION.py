import pandas as pd
from fpdf import FPDF

data = pd.read_csv('D:/codetech CODES python/data.csv')# Replace with your actual dataset
summary = data.describe()

pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', 'B', 16)
pdf.cell(200, 10, 'Automated Report', ln=True, align='C')

pdf.set_font('Arial', '', 12)
for col in summary.columns:
    pdf.cell(200, 10, f"{col}: {summary[col]['mean']}", ln=True)

pdf.output('report.pdf')
