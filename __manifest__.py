{
    'name': 'Soporte Técnico',
    'version': '1.0',
    'depends': ['base'],
    'author': 'Mauro Dordoni',
    'category': 'Herramientas',
    'summary': 'Gestión de tickets de soporte técnico',
    'description': 'Módulo para crear, asignar y resolver tickets de soporte técnico.',
    'data': [
        'security/ir.model.access.csv',
        'views/ticket_views.xml',
    ],
    'installable': True,
    'application': True,
}
