import logging

from odoo import models, fields

_logger = logging.getLogger(__name__)


class Doctor(models.Model):
    _inherit = 'res.users'

    is_doctor = fields.Boolean(string='Is a Doctor', default=True)
    specialty = fields.Char(string='Specialty')
    visit_ids = fields.One2many('hr_hospital.visit', 'doctor_id',
                                string='Visits')
