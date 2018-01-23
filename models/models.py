# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

class PosOrderReport(models.Model):
	_inherit = 'report.pos.order'
	
	category_list = {}
	products_ids = self.pool.get('product_product').search(cr, uid, [])
	for line in products:
		products_ids[line.product_id].categ_id.name
		if category_list.get(products_ids[line.product_id].categ_id.name) == None:
			category_list.update[products_ids[line.product_id].categ_id.name] = 1
		else:
			category_list[products_ids[line.product_id].categ_id.name] = category_list[products_ids[line.product_id].categ_id.name]+1