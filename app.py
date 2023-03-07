from flask import Flask, Response, render_template, request
import pdfkit

app = Flask(__name__,template_folder='templates')

@app.route('/card-to-pdf', methods=['POST'])
def convert_card_to_pdf():
    # Get the title and content from the request form data
    name = request.form.get('name')
    dob = request.form.get('dob')

    # Render the HTML template with the dynamic data using Flask's render_template function
    html = render_template('card.html', name=name, dob=dob)
    config = pdfkit.configuration()
    # Set up the PDF options
    options = {
        "page-size": "A5",
        "margin-top": "10mm",
        "margin-right": "10mm",
        "margin-bottom": "10mm",
        "margin-left": "10mm"
    }

    # Convert the HTML to a PDF using pdfkit
    pdf_data = pdfkit.from_string(html, False, options=options,configuration=config)

    # Set the response headers to indicate that this is a PDF
    headers = {"Content-Type": "application/pdf", "Content-Disposition": "attachment;filename=card.pdf"}

    # Return the PDF as a binary response
    return Response(pdf_data, headers=headers)
