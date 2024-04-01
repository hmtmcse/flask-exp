from pdf.pweb_pdf import PWebPDF

# PWebPDF.generate(url="https://www.hmtmcse.com", pdf_store_path="pdf-from-url.pdf")
# PWebPDF.generate(html_file_path="html-css/ticket.html", pdf_store_path="pdf-from-html-css.pdf", embed_css=True)
PWebPDF.generate(
    html_content='''
    <h1>PWeb PDF</h1>
    <p>Content goes here</p>
''',
    css='@page { size: A3; margin: 1cm } h1{color: red;}',
    pdf_store_path="pdf-from-html-css-str.pdf",
    embed_css=True
)
