#from osv import orm, osv, fields
#from tools.translate import _
import time
from openerp.osv import fields,osv
from openerp.tools.translate import _


class sale_order_inherit(osv.osv):
    _inherit = 'sale.order'
    def onchange_partner_id(self, cr, uid, ids, part, context=None):
        res = super(sale_order_inherit, self).onchange_partner_id(cr, uid,ids, part, context=context)
        if not part:
            return res
        part = self.pool.get('res.partner').browse(cr, uid, part, context=context)
        sect = part.section_id.id
        res['value']['section_id']=sect
        return res
