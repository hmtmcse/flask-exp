from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration

font_config = FontConfiguration()
html = HTML(string='<h1>The title</h1>')
css = CSS(string='''
    h1 {color: red;}''', font_config=font_config)
html.write_pdf(
    'example.pdf', stylesheets=[css],
    font_config=font_config)
