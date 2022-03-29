from odoo import http, fields, models
from odoo.http import request
import json

class MakananCon(http.Controller):
    @http.route(['/makanan','/makanan/<int:idnya>'], auth='public', methods=['GET'], csrf=True)
    def getMakanan(self, idnya=None, **kwargs):
        value = []
        if not idnya:
            makanan = request.env['toko.makanan'].search([])            
            for m in makanan:
                value.append({"id": m.id,
                            "nama_makanan" : m.name,
                            "tipe_makanan" : m.tipe,
                            "deskripsi" : m.deskripsi,
                            "harga" : m.harga})
            return json.dumps(value)
        else:
            makananid = request.env['toko.makanan'].search([('id','=',idnya)])
            for m in makananid:
                value.append({"id": m.id,
                            "nama_makanan" : m.name,
                            "tipe_makanan" : m.tipe,
                            "deskripsi" : m.deskripsi,
                            "harga" : m.harga})
            return json.dumps(value)

    @http.route('/createmakanan',auth='user', type='json', methods=['POST'])
    def createMakanan(self, **kw):    
        if request.jsonrequest:    
            if kw['name']:
                vals={
                    'name': kw['name'], 
                    'tipe' : kw['tipe'],
                    'deskripsi' : kw['deskripsi'],
                    'harga' : kw['harga'],
                }
                makanan = request.env['toko.makanan'].create(vals)
                args = {'success': True, 'ID':makanan.id}
                return args