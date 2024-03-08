# from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.conf import settings
from xhtml2pdf import pisa

def generate_pdf(request):
    template_path = 'report/report_template.html'
    context = {'myvar': 'Hello, this is a PDF file!'}
    # Create a Django template
    template = get_template(template_path)
    # Render the template with the context
    html = template.render(context)
    # Create a PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'
    # Generate PDF using xhtml2pdf
    pisa_status = pisa.CreatePDF(html, dest=response)
    # Return PDF file
    return response