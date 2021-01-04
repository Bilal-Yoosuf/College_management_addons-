from odoo import http
from odoo.http import request


class CollegePage(http.Controller):

    @http.route('/college/page/', type='http', website=True, auth='public')
    def first_page(self):
        return request.render('college.college_page')


class CollegeList(http.Controller):

    @http.route('/college-list', type='http', website=True, auth='public')
    def school_list(self):
        college_obj = request.env["college.details"].sudo().search([])
        return request.render('college.college_list', {'college': college_obj})
