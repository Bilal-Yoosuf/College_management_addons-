# -*- coding: utf-8 -*-

from odoo import models, fields, api


class BookRegistration(models.Model):
    _name = "book.registration"
    _description = "Book registration module"

    name = fields.Char(string="Book Name", required=True)
    number = fields.Integer(string="Book Number", required=True)
    author_id = fields.Many2one('res.partner', string="Author", domain="[('author','=','True')]")
    image = fields.Binary(string="Image")
    registration_date = fields.Date(string="Registration Date")
    category_id = fields.Many2one('book.category', string="Category")
    published_year = fields.Integer(string="Published Year")
    shelf_id = fields.Many2one('book.shelf', string="Book Shelf")
    student_ids = fields.One2many('book.status', 'book_id', string="Book orders", compute='_automate_books_list')

    @api.depends('name')
    def _automate_books_list(self):
        print("inside depends")
        for record in self:
            # self.name = "Book1"
            student_rec = self.env['book.return'].search([('name', '=', self.id)])
            print("student records", student_rec)
            for student in student_rec:
                line = {
                    'book_id': self.id,
                    'student_name': student.sname.name,
                    'student_taken_type': student.taken_type,
                    'book_title': student.name.name
                }
                print("line", line)
                record.student_ids.create(line)


# @api.model
# def default_get(self, fields):
#     res = super(BookRegistration, self).default_get(fields)
#     student_lines = [(5, 0, 0)]
#     student_rec = self.env['book.return'].search([])
#     # print(student_rec)
#     for student in student_rec:
#             print(self.name)
#             # print(student.sname.name)
#             line = (0, 0, {
#                 'student_name': student.sname.name,
#                 'student_taken_type': student.taken_type,
#                 'book_title': student.name.name
#             })
#             student_lines.append(line)
#     res.update({
#         'student_ids': student_lines,
#
#     })
#     return res


class BookCategory(models.Model):
    _name = "book.category"
    _description = "Categories of book"
    name = fields.Char(string="Book Category")


class BookAuthor(models.Model):
    _inherit = 'res.partner'
    author = fields.Boolean(string="Book Author")


class BookShelf(models.Model):
    _name = "book.shelf"
    name = fields.Char(string="Shelf ID")
    book_ids = fields.One2many('book.registration', 'shelf_id', string="Book")


class BookStatus(models.Model):
    _name = 'book.status'
    student_name = fields.Char(string='Student')
    book_title = fields.Char(string='Book')
    student_taken_type = fields.Char(string="Taken Type")
    book_id = fields.Many2one('book.registration', string="Book Name")
