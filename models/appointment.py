# -*- coding: utf-8 -*-

from odoo import models, fields


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _description = "HospitalAppointment"

    patient_id = fields.Many2one(
        comodel_name="hospital.patient", string="Patient"
    )
    appointment_time = fields.Datetime(
        string="Appointment Time", default=fields.Datetime.now
    )
