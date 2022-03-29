from odoo import http, fields, models
from odoo.http import request
import json

class OrderCon(http.Controller):
    @http.route(['/order','/order/<int:idnya>'], auth='public', methods=['GET'], csrf=True)
    def getOrderCon(self, idnya=None, **kwargs):
        value = []
        if not idnya:
            order = request.env['toko.order'].search([])            
            for m in order:
                value.append({"id": m.id,
                            "nama" : m.name,
                            "paket_pesanan" : m.paket_ids[0].name})
            return json.dumps(value)
        else:
            orderid = request.env['toko.order'].search([('id','=',idnya)])
            for m in orderid:
                value.append({"id": m.id,
                            "nama" : m.name,
                            "paket_pesanan" : m.paket_ids.name})
            return json.dumps(value)