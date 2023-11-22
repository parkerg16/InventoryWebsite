from django.http import HttpResponse
from fpdf import FPDF
from .models import WorkOrder
import os


def workorder_pdf(request, workorder_id):
	work_order = WorkOrder.objects.get(pk=workorder_id)

	pdf = FPDF()
	pdf.add_page()

	# Header
	pdf.set_font("Arial", 'B', 16)
	pdf.cell(200, 10, "Work Order", 0, 1, 'C')

	# Subheader
	pdf.set_font("Arial", 'I', 12)
	pdf.cell(200, 10, f"Work Order ID: {work_order.work_order_id}", 0, 1, 'L')
	pdf.ln(10)  # Add a line break

	# Work Order Description
	pdf.set_font("Arial", size=12)
	pdf.multi_cell(0, 10, f"Description: {work_order.description}")

	# Footer
	pdf.set_y(-15)
	pdf.set_font("Arial", 'I', 8)
	pdf.cell(0, 10, 'Page ' + str(pdf.page_no()), 0, 0, 'C')

	# Generate PDF content as a byte array
	pdf_content = pdf.output(dest='S')

	# Determine file path
	filename = f"work_order_{workorder_id}.pdf"
	file_path = os.path.join('path/to/save', filename)  # Specify the directory to save PDF

	# Save PDF content to a file
	with open(file_path, 'wb') as f:
		f.write(pdf_content)

	# Return a message indicating the PDF was saved successfully
	return HttpResponse(f"PDF saved to file: {file_path}")
