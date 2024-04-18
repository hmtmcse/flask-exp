from weasyprint import HTML, CSS
from weasyprint.text.fonts import FontConfiguration


class PWebPDF:

    @staticmethod
    def generate(
            html_content: str = None,
            html_file_path: str = None,
            pdf_store_path: str = None,
            url: str = None,
            css: str = None,
            css_file_path: str = None,
            css_url: str = None,
            resource_root_path: str = None,
            encoding=None,
            content_zoom: float = 1,
            font_config=FontConfiguration(),
            embed_css=False,
            media_type='print'):

        # Started Main Coding
        if not html_content and not html_file_path and not url:
            print("Throw exception")

        # Configuring HTML Content
        html_object = HTML(
            base_url=resource_root_path,
            string=html_content,
            filename=html_file_path,
            url=url,
            media_type=media_type,
            encoding=encoding
        )

        # Configuring CSS
        stylesheets = None
        css_font_conf = None
        if css_url or css or css_file_path:
            css_font_conf = font_config
            stylesheets = [CSS(
                base_url=resource_root_path,
                string=css,
                filename=css_file_path,
                url=css_url,
                font_config=css_font_conf,
                media_type=media_type,
                encoding=encoding
            )]
        elif embed_css:
            css_font_conf = font_config

        # Generation PDF
        response = html_object.write_pdf(
            target=pdf_store_path,
            stylesheets=stylesheets,
            font_config=css_font_conf,
            zoom=content_zoom
        )
        return response
