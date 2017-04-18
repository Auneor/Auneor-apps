# -*- coding: utf-8 -*-

from openerp import models, fields, api


class category(models.Model):
    _name = 'product.category'
    _inherit = 'product.category'

    profondeur = fields.Integer(compute="_profondeur", store=True)
    categorie=fields.Many2one('product.category',compute='_profondeur',store=True)
    sous_categorie=fields.Many2one('product.category',compute='_profondeur',store=True)

    @api.depends('parent_id')
    def _profondeur(self):
        for record in self:
            parent = record.parent_id
            prof = 0
            while parent:
                if not parent.parent_id:
                    record.categorie=parent.id
                    if not record.sous_categorie:
                        record.sous_categorie=parent.id
                else:
                    record.sous_categorie=parent.id
                parent = parent.parent_id
                prof += 1
            if prof==0:
                record.categorie=record.id
                record.sous_categorie=record.id
            if prof==1:
                record.categorie=record.parent_id
                record.sous_categorie=record.id
            record.profondeur = prof
