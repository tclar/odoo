# -*- coding: utf-8 -*-
{
    'name': "Se7 Historico Estados Sale Order",

    'summary': """
        Guardar un registro del cambio de estados en Sale Order.
        """,

    'author': "SE7 Consulting Balears",
    'website': "https://www.se7bal.com",
    'version': '12.0.3.0',
    'depends': ['base', 'sale', 'hr', 'se7_gestion_instaladoras'],
    'data': [
        'security/ir.model.access.csv',
        'views/sale_views.xml',
        'views/historico_estado_sale_order_view.xml',
    ],
}
