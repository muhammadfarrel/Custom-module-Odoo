from odoo import api, fields, models


class Paket(models.Model):
    _name = 'toko.paket'
    _description = 'Paket Makanan & Minuman'

    name = fields.Char(string='Name')

    makanan_id = fields.Many2one(comodel_name='toko.makanan', 
                                string='Makanan')
    minuman_id = fields.Many2one(comodel_name='toko.minuman', 
                                string='Minuman')
    channel_id = fields.Many2one('ir.model.fields', 
                                string='Channel',
                                domain=[('relation','=', '')])
    
    stok = fields.Integer(string='Stok Paket')
    deskripsi = fields.Char(string='Deskripsi')

    harga = fields.Char(compute='_compute_harga', string='Harga', store=True)
    
    @api.depends('makanan_id','minuman_id')
    def _compute_harga(self):
        for record in self:
            record.harga = record.makanan_id.harga + record.minuman_id.harga - 2000

    des_makanan = fields.Char(compute='_compute_des_makanan', string='Deskripsi Makanan')
    
    @api.depends('makanan_id')
    def _compute_des_makanan(self):
        for record in self:
            record.des_makanan = record.makanan_id.deskripsi

    des_minuman = fields.Char(compute='_compute_des_minuman', string='Deskripsi Minuman')
    
    @api.depends('minuman_id')
    def _compute_des_minuman(self):
        for record in self:
            record.des_minuman = record.minuman_id.deskripsi