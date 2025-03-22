# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _description = "HospitalAppointment"
    _rec_name = "patient_id"

    patient_id = fields.Many2one(
        comodel_name="hospital.patient", string="Patient"
    )
    gender = fields.Selection(
        string="Patient Gender", related="patient_id.gender"
    )
    appointment_time = fields.Datetime(
        string="Appointment Time", default=fields.Datetime.now
    )
    patient_reference = fields.Char(string="Patient Reference")
    prescription = fields.Html(string="Prescription")
    priority = fields.Selection(
        [
            ("normal", "Normal"),
            ("medium", "Medium"),
            ("high", "High"),
            ("very_high", "Very High"),
        ],
        string="Priority",
        default="normal",
    )

    @api.onchange("patient_id")
    def onchange_patient_id(self):
        for record in self:
            if record.patient_id:
                record.patient_reference = record.patient_id.reference
