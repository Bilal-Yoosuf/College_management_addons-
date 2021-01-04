{
    'name': "College",
    'version': '13.1',
    'depends': ['base'],
    'author': "Socius Trainee",
    # 'category': 'Category',
    # 'description': "Library management module",
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/front_end/webpages/college_page.xml',
        'views/college_details.xml',
        'views/front_end/webpages/college_list.xml'

    ],
    # data files containing optionally loaded demonstration data
    'demo': [
        # 'demo/demo_data.xml',
    ],
    'installable': True
}
