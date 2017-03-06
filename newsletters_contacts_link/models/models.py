# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class newsletters_contacts_link(models.Model):
#     _name = 'newsletters_contacts_link.newsletters_contacts_link'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100


class Partner(models.Model):
    _inherit = "res.partner"
    newsletter_id=fields.Many2many('mail.mass_mailing.list',string="Newsletters")


    @api.one
    def write(self, values, context=None):
        newsletters_before=set(self.newsletter_id)
        if "email" in values:
            email_before=self.email
            email_after=values["email"]

            if not email_after and newsletters_before and (
                (not "newsletter_id" in values) or ("newsletter_id" in values and not values["newsletter_id"])
            ):
                raise Warning("Attention, veuillez supprimer les newsletters associées au contact")

            if email_after:
                for ml in newsletters_before:
                    ml.changePartnerAddress(email_before,email_after)
            else:
                values["newsletter_id"]=[[6,False,[]]]
                email_after=email_before
        else:
            email_after=self.email

        if "newsletter_id" in values:
            if not values["newsletter_id"]:
                newsletters_after=set()
            else:
                if values["newsletter_id"][0][0]==4: # c'est un appel depuis sync pour ajouter un element
                    versionApres=values["newsletter_id"][0][1]
                    newsletters_after=set(self.env["mail.mass_mailing.list"].browse(versionApres)).union(set(self.newsletter_id))
                elif values["newsletter_id"][0][0]==6:
                    versionApres=values["newsletter_id"][0][2]
                    newsletters_after=set(self.env["mail.mass_mailing.list"].browse(versionApres))
                else:
                    res_id = super(Partner, self).write(values)
                    return res_id
            supprimes=newsletters_before.difference(newsletters_after)
            for ml in supprimes:
                ml.deletePartnerAddress(email_after)
            nouveaux=newsletters_after.difference(newsletters_before)
            for ml in nouveaux:
                ml.addPartnerAddress(self,email_after)

        res_id = super(Partner, self).write(values)
        return res_id


class MassMailingList(models.Model):
    _inherit = 'mail.mass_mailing.list'
    partner_id = fields.Many2many("res.partner",string="Contacts Internes")

    def changePartnerAddress(self,old,new):
        if not new:
            return
        cts=self.env['mail.mass_mailing.contact'].search([('list_id','=',self.id),('email','=',old)])
        for c in cts:
            c.write({"email":new})

    def deletePartnerAddress(self,email):
        cts=self.env['mail.mass_mailing.contact'].search([('list_id','=',self.id),('email','=',email)])
        partners=self.env['res.partner'].search([['email','=',email]])
        for p in partners:
            p.write({"newsletter_id":[(3,self.id,0)]})
        cts.unlink()

    def addPartnerAddress(self,partner,email):
        if not email:
            raise Warning("Attention, un contact n'a pas d'email associé, vous devez renseigner ce champ pour l'inscription à une newsletter")
        existant=self.env['mail.mass_mailing.contact'].search([['email','=',email],['list_id','=',self.id]])
        if not existant:
            self.env['mail.mass_mailing.contact'].create({
                "name":partner.display_name,
                "email": email,
                "list_id":self.id
            })

    @api.multi
    def write(self, values, context=None):
        partner_before=set(self.partner_id)
        if "partner_id" in values:
            if not values["partner_id"]:
                partner_after=set()
            else:
                versionApres=values["partner_id"][0][2]
                partner_after=set(self.env["res.partner"].browse(versionApres))
            supprimes=partner_before.difference(partner_after)
            for c in supprimes:
                self.deletePartnerAddress(c.email)
            nouveaux=partner_after.difference(partner_before)
            for c in nouveaux:
                self.addPartnerAddress(c,c.email)

        res_id = super(MassMailingList, self).write(values)
        return res_id
