# -*- coding: utf-8 -*-
{
    'name': "Se7 Ventas Mantenimiento",

    'summary': """
        Modificaciones específicas para Roselló Solar en ventas.
    """,

    'description': """
        Añadir un campo a las ventas que indique si es: Reparación o Mantenimiento.
        Crear menú específico para mantenimiento reparaciones (filtrando las ventas que correspondan a Reparaciones/Mantenimiento)
        Añadir Smart button en cliente para que enseñe las reparaciones y los mantenimientos.
    """,

    'author': "SE7 Consulting Balears",
    'website': "https://www.se7bal.com",
    'version': '12.0.2.0',
    'depends': ['base', 'hr', 'se7_gestion_instaladoras', 'contract', 'se7_mf_diarios_tecnicos'],
    'data': [
        'views/sale_order_views.xml',
        'views/new_sale_order_views.xml',
        'views/res_partner_views.xml',
        'views/res_config_settings_views.xml',
    ],
}
