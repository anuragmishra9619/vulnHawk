from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

def generate_pdf_report(target, results):
    filename = f"reports/{target.replace('.', '_')}.pdf"
    os.makedirs("reports", exist_ok=True)

    c = canvas.Canvas(filename, pagesize=letter)
    c.setFont("Helvetica", 14)
    c.drawString(100, 750, f"SecureVajr Security Scan Report")
    c.drawString(100, 730, f"Target: {target}")
    y = 700

    for key, values in results.items():
        c.drawString(100, y, f"--- {key.upper()} ---")
        y -= 20
        for value in values:
            c.drawString(120, y, f"- {value}")
            y -= 20

    c.save()
