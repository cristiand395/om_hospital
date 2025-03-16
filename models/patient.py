from odoo import fields, models


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Hospital Patient"

    name = fields.Char(string="Name", tracking=True)
    last_name = fields.Char(string="Last Name", tracking=True)
    age = fields.Integer(string="Age", tracking=True)
    gender = fields.Selection(
        [("male", "Male"), ("female", "Female")],
        string="Gender",
        tracking=True,
    )
    active = fields.Boolean(string="Active", default=True, tracking=True)
