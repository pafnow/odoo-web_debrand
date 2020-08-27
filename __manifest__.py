# Copyright 2020 Pafnow
{
    'name': "Web Debrand",
    'version': "13.0.1.0.0",
    'description': 'Web Debrand',
    'author': "MRM, Pafnow",
    'company': "MRM",
    'category': 'Tools',
    'depends': ['web'],
    'data': [
        'views/webclient_templates.xml',
    ],
    'qweb': [
        "static/src/xml/base.xml",
    ],
    'installable': True,
    'application': False
}
