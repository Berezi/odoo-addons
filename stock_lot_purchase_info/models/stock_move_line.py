# Copyright 2022 Alfredo de la Fuente - AvanzOSC
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
from odoo import fields, models


class StockMoveLine(models.Model):
    _inherit = "stock.move.line"

    supplier_id = fields.Many2one(
        string="Supplier", comodel_name="res.partner", copy=False, store=True,
        related="lot_id.supplier_id")
    purchase_price = fields.Float(
        string="Purchase Price Unit", digits="Product Price", copy=False,
        store=True, related="lot_id.purchase_price")