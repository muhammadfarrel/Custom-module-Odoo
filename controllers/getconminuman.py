from odoo import http, fields, models
from odoo.http import request
import json

class MakananCon(http.Controller):
    @http.route(['/minuman','/minuman/<int:idnya>'], auth='public', methods=['GET'], csrf=True)
    def getMinuman(self, idnya=None, **kwargs):
        value = []
        if not idnya:
            makanan = request.env['toko.minuman'].search([])            
            for m in makanan:
                value.append({"id": m.id,
                            "nama_minuman" : m.name,
                            "tipe_minuman" : m.tipe,
                            "deskripsi" : m.deskripsi,
                            "harga" : m.harga})
            return json.dumps(value)
        else:
            makananid = request.env['toko.minuman'].search([('id','=',idnya)])
            for m in makananid:
                value.append({"id": m.id,
                            "nama_minuman" : m.name,
                            "tipe_minuman" : m.tipe,
                            "deskripsi" : m.deskripsi,
                            "harga" : m.harga})
            return json.dumps(value)

    @http.route('/createminuman',auth='user', type='json', methods=['POST'])
    def createMinuman(self, **kw):    
        if request.jsonrequest:    
            if kw['name']:
                vals={
                    'name': kw['name'], 
                    'tipe' : kw['tipe'],
                    'deskripsi' : kw['deskripsi'],
                    'harga' : kw['harga'],
                }
                minuman = request.env['toko.minuman'].create(vals)
                args = {'success': True, 'ID':minuman.id}
                return args