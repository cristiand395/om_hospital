from odoo import fields, models, api


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "Hospital Patient"

    name = fields.Char(string="Name", tracking=True)
    last_name = fields.Char(string="Last Name", tracking=True)
    age = fields.Integer(string="Age", compute="_compute_age", tracking=True)
    gender = fields.Selection(
        [("male", "Male"), ("female", "Female")],
        string="Gender",
        tracking=True,
    )
    active = fields.Boolean(string="Active", default=True, tracking=True)
    birth_date = fields.Date(string="Birthday")
    reference = fields.Char(string="Reference")

    @api.depends("birth_date")
    def _compute_age(self):
        for record in self:
            if record.birth_date:
                today = fields.Date.today()
                record.age = (
                    today.year
                    - record.birth_date.year
                    - (
                        (today.month, today.day)
                        < (record.birth_date.month, record.birth_date.day)
                    )
                )
            else:
                record.age = 0
