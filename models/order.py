from odoo import api, fields, models
from odoo.exceptions import ValidationError


class Order(models.Model):
    _name = 'toko.order'
    _description = 'Order pesanan'

    name = fields.Char(string='Kode Order', required=True)

    paket_ids = fields.One2many('toko.orderpaketdetail', 'orderpa_id', string='Order Paket')
    makanan_ids = fields.One2many('toko.ordermakanandetail', 'orderma_id', string='Order Makanan')
    minuman_ids = fields.One2many('toko.orderminumandetail', 'ordermi_id', string='Order Minuman')

    tanggal_order = fields.Date(string='Tanggal pesan', default=fields.Datetime.now())
    tanggal_sajikan = fields.Date(string='Tanggal sajikan', default=fields.Datetime.now())
    
    customer_id = fields.Many2one(
        comodel_name='res.partner', 
        string='Customer', 
        domain=[('is_customernya', '=', True)],store=True)

    total = fields.Char(compute='_compute_total', string='Total', store=True)
    
    @api.depends('paket_ids','makanan_ids','minuman_ids')
    def _compute_total(self):
        for record in self:
            a = sum(self.env['toko.orderpaketdetail'].search([('orderpa_id', '=', record.id)]).mapped('harga'))
            b = sum(self.env['toko.ordermakanandetail'].search([('orderma_id', '=', record.id)]).mapped('harga'))
            c = sum(self.env['toko.orderminumandetail'].search([('ordermi_id', '=', record.id)]).mapped('harga'))
            record.total = a + b + c
    
    sajikan = fields.Boolean(string='Already Served', default=False)
    

class OrderPaketDetail(models.Model):
    _name = 'toko.orderpaketdetail'
    _description = 'New Description'

    name = fields.Char(string='Name')

    orderpa_id = fields.Many2one('toko.order', string='Order Paket')
    paket_id = fields.Many2one('toko.paket', string='Paket')

    qty = fields.Integer(string='Quantity')

    harga_satuan = fields.Integer(compute='_compute_harga_satuan', string='harga_satuan')
    
    @api.depends('paket_id')
    def _compute_harga_satuan(self):
        for record in self:
            record.harga_satuan = record.paket_id.harga

    harga = fields.Integer(compute='_compute_harga', string='harga')
    
    @api.depends('qty', 'harga_satuan')
    def _compute_harga(self):
        for record in self:
           record.harga = record.harga_satuan * record.qty

    @api.constrains('qty')
    def _check_stok(self):
        for record in self:
            bahan = self.env['toko.paket'].search([('stok', '<', record.qty),('id', '=',record.id)])
            if bahan:
                raise ValidationError("Stok Tidak Cukup")

    @api.model
    def create(self,vals):
        record = super(OrderPaketDetail, self).create(vals) 
        if record.qty:
            self.env['toko.paket'].search([('id','=',record.paket_id.id)]).write({'stok':record.paket_id.stok-record.qty})
            return record


class OrderMakananDetail(models.Model):
    _name = 'toko.ordermakanandetail'
    _description = 'New Description'

    name = fields.Char(string='Name')

    orderma_id = fields.Many2one('toko.order', string='Order Makanan')
    makanan_id = fields.Many2one('toko.makanan', string='Makanan')

    qty = fields.Integer(string='Quantity')

    harga_satuan = fields.Integer(compute='_compute_harga_satuan', string='harga_satuan')
    
    @api.depends('makanan_id')
    def _compute_harga_satuan(self):
        for record in self:
            record.harga_satuan = record.makanan_id.harga

    harga = fields.Integer(compute='_compute_harga', string='harga')
    
    @api.depends('qty','harga_satuan')
    def _compute_harga(self):
        for record in self:
           record.harga = record.harga_satuan * record.qty 
    

class OrderMinumanDetail(models.Model):
    _name = 'toko.orderminumandetail'
    _description = 'New Description'

    name = fields.Char(string='Name')

    ordermi_id = fields.Many2one('toko.order', string='Order Minuman')
    minuman_id = fields.Many2one('toko.minuman', string='Minuman')

    qty = fields.Integer(string='Quantity')

    harga_satuan = fields.Integer(compute='_compute_harga_satuan', string='harga_satuan')
    
    @api.depends('minuman_id')
    def _compute_harga_satuan(self):
        for record in self:
            record.harga_satuan = record.minuman_id.harga

    harga = fields.Integer(compute='_compute_harga', string='harga')
    
    @api.depends('qty','harga_satuan')
    def _compute_harga(self):
        for record in self:
           record.harga = record.harga_satuan * record.qty
