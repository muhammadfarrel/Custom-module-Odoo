from odoo import api, fields, models


class Served(models.Model):
    _name = 'toko.served'
    _description = 'Served'

    name = fields.Char(compute='_compute_name_cust', string='Customer')
    order_id = fields.Many2one(comodel_name='toko.order', string='Kode Order')
    
    @api.depends('order_id')
    def _compute_name_cust(self):
        for record in self:
            record.name = self.env['toko.order'].search([('id', '=', record.order_id.id)]).mapped('customer_id').name

    tgl_sajikan = fields.Date(compute='_compute_tgl_sajikan', string='Tanggal sajikan')
    
    @api.depends('order_id')
    def _compute_tgl_sajikan(self):
        for record in self:
            record.tgl_sajikan = record.order_id.tanggal_sajikan

    tagihan = fields.Integer(compute='_compute_tagihan', string='Tagihan')
    
    @api.depends('order_id')
    def _compute_tagihan(self):
        for record in self:
            record.tagihan = record.order_id.total 


    @api.model
    def create(self,vals):
        record = super(Served, self).create(vals) 
        if record.tgl_sajikan:
            self.env['toko.order'].search([('id','=',record.order_id.id)]).write({'sajikan':True})  
            self.env['toko.akunting'].create({'kredit' : record.tagihan, 'name':record.name})       
            return record
    
    def unlink(self):
        for data in self:
            self.env['toko.order'].search([('id','=',data.order_id.id)]).write({'sajikan':False})
        record = super(Served, self).unlink()