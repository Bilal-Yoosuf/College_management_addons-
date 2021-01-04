from odoo import http
from odoo.http import request


class FirstPage(http.Controller):

    @http.route('/first/page/', type='http', website=True,  auth='public')
    def first_page(self):
        return request.render('library_management.first_page')
