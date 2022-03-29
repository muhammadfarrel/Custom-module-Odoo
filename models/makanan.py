from odoo import api, fields, models


class Makanan(models.Model):
    _name = 'toko.makanan'
    _description = 'Makanan'

    name = fields.Char(string='Name')
    tipe = fields.Selection(string='Tipe Makanan', selection=[('main','Main'), ('side','Side'),  ('dessert','Dessert')])
    deskripsi = fields.Char(string='Deskripsi')
    harga = fields.Integer(string='Harga')
    
    
