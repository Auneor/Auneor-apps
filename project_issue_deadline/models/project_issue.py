# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime


class project_issue(models.Model):
    _inherit = "project.issue"

    deadline = fields.Date("Deadline")
    is_open = fields.Boolean("Is open", compute="_is_open", store=True)
    is_late = fields.Boolean("Is late", compute="_is_open", store=True)
    is_next = fields.Boolean("Is next", compute="_is_open", store=True)

    @api.model
    def recompute_all(self):
        issues = self.search([('is_open', '=', False)])
        issues._is_open()
        return True

    @api.depends("stage_id","deadline")
    def _is_open(self):
        for record in self:
            if record.stage_id and record.stage_id.fold:
                record.is_open = False
            else:
                record.is_open = True
            if record.is_open and record.deadline and fields.Date.from_string(record.deadline) < datetime.date.today():
                record.is_late = True
            else:
                record.is_late = False

            if record.is_open and record.deadline and not record.is_late and fields.Date.from_string(
                    record.deadline) < datetime.date.today() + datetime.timedelta(5):
                record.is_next = True
            else:
                record.is_next = False

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
