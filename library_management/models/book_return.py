# -*- coding: utf-8 -*-


from odoo import fields, models


class BookReturn(models.Model):
    _name = 'book.return'

    sname = fields.Many2one('students.students',string="Student Name", required=True)
    name = fields.Many2one("book.registration", string="Title", required=True)
    code = fields.Char(string="ISBN", required=True)
    email = fields.Char(string="Email", copy=False, default="abc@gmail.com")
    phone = fields.Char("Phone", copy=False)
    genere = fields.Char(string="Genere")
    Author = fields.Char(string="Author")
    pickup = fields.Datetime("Pickup Date")
    ret = fields.Datetime("Return Date")
    taken_type = fields.Selection([('pickup', 'Pickup '),
                                   ('return', 'Return ')],
                                  string="Type of Action",
                                  )
