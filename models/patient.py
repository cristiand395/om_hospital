from odoo import fields, models


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Hospital Patient"

    name = fields.Char(string="Name")
    last_name = fields.Char(string="Last Name")
    age = fields.Integer(string="Age")
    gender = fields.Selection(
        [("male", "Male"), ("female", "Female")], string="Gender"
    )
    active = fields.Boolean(string="Active", default=True)
