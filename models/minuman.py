from odoo import api, fields, models


class Minuman(models.Model):
    _name = 'toko.minuman'
    _description = 'Minuman'

    name = fields.Char(string='Name')
    tipe = fields.Selection(string='Tipe Minuman', selection=[('hot','Hot'), ('cold','Cold')])
    deskripsi = fields.Char(string='Deskripsi')
    harga = fields.Integer(string='Harga')
