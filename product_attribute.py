# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
import openerp.addons.decimal_precision as dp
from openerp.osv import osv
from openerp.osv import fields
from openerp.tools.translate import _
import time

class product_product(osv.osv):
    """ 扩展产品"""
    _name = "product.product"
    _inherit = ['product.product']
   # _description = u"扩展产品属性"
    _columns = {
        'type': fields.char('型号', size=64, required=True),
        'length': fields.char('长度', size=64, required=True),
        'standard': fields.char('规格', size=64, required=True),
        'meter': fields.char('仪表', size=64, required=True),
        'sensor': fields.char('传感器', size=64, required=True),
    }
    _sql_constraints = [

    ]
class purchase_order(osv.osv):
    """ 扩展内部询价单"""
    _name = "purchase.order"
    _inherit = ['purchase.order']
    _columns = {
        'zhibaojin': fields.float('质保金', digits_compute=dp.get_precision('zhibaojin'),required=True),
        'zhibao_end_date': fields.datetime('质保到期时间', required=True),
        'advance_payment': fields.float('预付款', digits_compute=dp.get_precision('advance_payment'),required=True),
        'add_invoice_price': fields.float('增开发票金额', digits_compute=dp.get_precision('add_invoice_price'),required=True),
        'add_fee_price': fields.float('增开税款', digits_compute=dp.get_precision('add_fee_price'),required=True),
        'custom_fee': fields.many2one('product.fee', string='税'),
    }



class sale_order(osv.osv):
    """ 扩展报价单，订单"""
   # _name = "sale.order"
    _inherit = 'sale.order'
    _columns = {
        'zhibaojin': fields.float('质保金', digits_compute=dp.get_precision('zhibaojin'),required=True),
        'zhibao_end_date': fields.datetime('质保到期时间', required=True),
        'advance_payment': fields.float('预付款', digits_compute=dp.get_precision('advance_payment'),required=True),
        'add_invoice_price': fields.float('增开发票金额', digits_compute=dp.get_precision('add_invoice_price'),required=True),
        'add_fee_price': fields.float('增开税款', digits_compute=dp.get_precision('add_fee_price'),required=True),
        'custom_fee': fields.many2one('product.fee', string='税'),
    }

    def _inv_get(self, cr, uid, order, context=None):
        vals = ({
            'zhibaojin':order.zhibaojin,
            'zhibao_end_date':order.zhibao_end_date,
            'advance_payment':order.advance_payment,
            'add_invoice_price':order.add_invoice_price,
            'add_fee_price':order.add_fee_price
        })
        return vals

class account_invoice(osv.osv):
    """ 扩展发票管理"""
    _name = "account.invoice"
    _inherit = ['account.invoice']
    _columns = {
        'zhibaojin': fields.float('质保金', digits_compute=dp.get_precision('zhibaojin'),required=True),
        'zhibao_end_date': fields.datetime('质保到期时间', required=True),
        'advance_payment': fields.float('预付款', digits_compute=dp.get_precision('advance_payment'),required=True),
        'add_invoice_price': fields.float('增开发票金额', digits_compute=dp.get_precision('add_invoice_price'),required=True),
        'add_fee_price': fields.float('增开税款', digits_compute=dp.get_precision('add_fee_price'),required=True),
        'custom_fee': fields.many2one('product.fee', string='税'),
    }

    _defaults = {
    }
class product_fee(osv.osv):
    """ 扩展产品"""
    _name = "product.fee"
    _inherit = ['mail.thread']
  #  _description = u"税率管理"
    _columns = {
        'fee': fields.float('税率[小数形式]', size=64, required=True),
        'note': fields.text('备注', required=True),

    }
    _sql_constraints = [

    ]


