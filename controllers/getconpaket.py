from odoo import http, fields, models
from odoo.http import request
import json

class PaketCon(http.Controller):
    @http.route(['/paket','/paket/<int:idnya>'], auth='public', methods=['GET'], csrf=True)
    def getPaket(self, idnya=None, **kwargs):
        value = []
        if not idnya:
            paket = request.env['toko.paket'].search([])            
            for m in paket:
                value.append({"id": m.id,
                            "name": m.name,
                            "makanan" : m.makanan_id.name,
                            "minuman" : m.minuman_id.name,
                            "stok" : m.stok,
                            "deskripsi": m.deskripsi,
                            "harga" : m.harga})
            return json.dumps(value)
        else:
            paketid = request.env['toko.paket'].search([('id','=',idnya)])
            for m in paketid:
                value.append({"id": m.id,
                            "name": m.name,
                            "makanan" : m.makanan_id.name,
                            "minuman" : m.minuman_id.name,
                            "stok" : m.stok,
                            "deskripsi": m.deskripsi,
                            "harga" : m.harga})
            return json.dumps(value)