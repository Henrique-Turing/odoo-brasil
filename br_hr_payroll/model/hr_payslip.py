# -*- coding: utf-8 -*-
# © 2016 Alessandro Fernandes Martini, Trustcode
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from math import ceil
from odoo import api, fields, models


class HrPayslip(models.Model):
    _inherit = 'hr.payslip'

    def week_of_month(self, dt):
        """ Returns the week of the month for the specified date.
        """

        first_day = dt.replace(day=1)

        dom = dt.day
        adjusted_dom = dom + first_day.weekday()

        return int(ceil(adjusted_dom/7.0))

    @api.model
    def get_worked_day_lines(self, contract_ids, date_from, date_to):
        res = super(HrPayslip, self).get_worked_day_lines(
            contract_ids, date_from, date_to)
        employee = self.employee_id
        if self.get_contract(employee, date_from, date_to):
            leaves = self.env['hr.holidays'].search(
                [('employee_id', '=', self.employee_id.id),
                 ('date_from', '>=', date_from),
                 ('date_to', '<=', date_to),
                 ('state', '=', 'validate'),
                 ('type', '=', 'remove')])
            dsr = {}
            for leave in leaves:
                # BUG: Fazer validação da falta
                if leave.holiday_status_id.name == 'Unpaid':
                    leave_start = fields.Datetime.from_string(leave.date_from)
                    dsr[self.week_of_month(leave_start)] = leave_start
            dsr_dict = {
             'name': "Descanso Semanal Remunerado",
             'sequence': 8,
             'code': 'DSR',
             'number_of_days': len(dsr),
             'contract_id': self.contract_id,
             }
            if dsr_dict['number_of_days'] != 0:
                res += [dsr_dict, {
                 'name': "Provisão de #13",
                 'sequence': 13,
                 'code': 'P13',
                 'number_of_days': 30,
                 'contract_id': self.contract_id,
                }]
            else:
                res += [{
                 'name': "Provisão de #13",
                 'sequence': 13,
                 'code': 'P13',
                 'number_of_days': 30,
                 'contract_id': self.contract_id,
                }]

            return res
