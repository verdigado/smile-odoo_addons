# -*- coding: utf-8 -*-
# Copyright (C) 2022 Smile (<http://www.smile.fr>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    'name': 'Smile Blogs private',
    'category': 'Website',
    'website': 'https://www.smile.fr',
    'summary': 'Blogs and post private access',
    'version': '15.0.1.0.0',
    'author': 'OpenSur, Smile SA',
    'license': 'AGPL-3',
    'depends': ['website_blog'],
    'data': [
        'data/access_rules.xml',
        'views/website_blog_private_views.xml'
    ],
    'demo': [
    ],
    'test': [
    ],
    'qweb': [
    ],
    'installable': True,
    'application': True,
}
