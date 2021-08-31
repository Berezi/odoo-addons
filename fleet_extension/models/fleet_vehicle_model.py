# Copyright 2021 Berezi - Iker - AvanzOSC
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).
from odoo import models, fields


class FleetVehicleModel(models.Model):
    _inherit = 'fleet.vehicle.model'

    collection_id = fields.Many2one(
        string='Collection', comodel_name='fleet.vehicle.model.collection')
    type_id = fields.Many2one(
        string='Vehicle type', comodel_name='fleet.vehicle.model.type')