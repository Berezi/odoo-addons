# Copyright 2021 Alfredo de la Fuente - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from odoo import fields, models


class SlideQuestion(models.Model):
    _inherit = 'slide.question'
    answer_ids = fields.One2many(copy=True)


class SlideSlide(models.Model):
    _inherit = 'slide.slide'
    question_ids = fields.One2many(copy=True)


class SlideChannel(models.Model):
    _inherit = 'slide.channel'

    slide_content_ids = fields.One2many(copy=True)

    def insert_event_reponsible_in_slide_channel(self, event, responsible):
        slide_channel_partner_obj = self.env['slide.channel.partner']
        cond = [('channel_id', '=', self.id),
                ('partner_id', '=', responsible.partner_id.id)]
        slide_channel = slide_channel_partner_obj.search(cond, limit=1)
        if not slide_channel:
            self.create_responsible_in_slide_channel(
                event, responsible.partner_id)

    def create_responsible_in_slide_channel(self, event, partner):
        slide_channel_partner_obj = self.env['slide.channel.partner']
        vals = {
            'channel_id': self.id,
            'partner_id': partner.id,
            'partner_email': partner.email,
            'real_date_start': event.date_begin.date(),
            'real_date_end': event.date_end.date()
            }
        slide_channel_partner_obj.create(vals)
