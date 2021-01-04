from odoo import models, fields, api


class CollegeDetails(models.Model):
    _name = 'college.details'
    college_specialisation = fields.Selection([('engineering', 'Engineering '),
                                               ('arts', 'Arts ')],
                                              string="College Specialisation",
                                              )
    college_name = fields.Char(string='College Name', required=True)
    college_id = fields.Integer(string='college ID', required=True)
    college_type = fields.Selection([('public', 'Public'),
                                     ('private', 'Private ')],
                                    string="Type of College",
                                    )
    college_town = fields.Char(string='Town')
    college_district = fields.Char(string='District')
    college_pin = fields.Integer(string='Pin Code')
