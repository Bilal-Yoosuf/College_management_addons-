
{
    'name': "Library Management",
    'version': '13.1',
    'depends': ['base', 'website'],
    'author': "Socius Trainee",
    # 'category': 'Category',
    # 'description': "Library management module",
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/book_view.xml',
        'views/book_registration.xml',
        'views/book_category.xml',
        'views/res_partner_inherit_form.xml',
        'views/book_shelf.xml',
        'views/front_end/webpages/first_page.xml',
        'reports/report.xml',
        'reports/book_report.xml',
    ],
    # data files containing optionally loaded demonstration data
    'demo': [
        # 'demo/demo_data.xml',
    ],
    'installable': True

}
