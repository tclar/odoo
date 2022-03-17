# -*- coding: utf-8 -*-
{
    'name': "Se7 Resumen entregas por producto",

    'summary': """
        Crea un informe de los movimientos de los productos.
    """,

    'author': "SE7 Consulting Balears",
    'website': "https://www.se7bal.com",
    'version': '12.0.1.0',
    'depends': ['base', 'stock'],
    'data': [
        'views/report.xml',
        'views/modal_view.xml',
    ],
}
