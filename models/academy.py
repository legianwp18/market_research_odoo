from datetime import datetime, timedelta
from dateutil import relativedelta
import time
from odoo import models, fields, api 

class Academy(models.Model):
    _name = 'academy'

    name = fields.Char(string='Name', required=True)
    date_from = fields.Datetime(string='Date From', default=time.strftime('%Y-%m-01'), required=True)
    date_to = fields.Datetime(string='Date To', default=str(datetime.now() + relativedelta.relativedelta(months=+1, day=1, days=-1))[:10], required=True)
    user_id = fields.Many2one(comodel_name='res.users', string='Responsible', default=lambda self: self.env.user.id, required=True)
    academy_line = fields.One2many(comodel_name='academy.line', inverse_name='academy_id', string='Academy Line', readonly=False, track_visibility='onchange')
    last_scan = fields.Datetime(string='Last Scan')
    insentif12 = fields.Float(string='Insentif Point 12 (Rp)', digits=(12,2))
    insentif6 = fields.Float(string='Insentif Point 6 (Rp)', digits=(12,2))
    insentif2 = fields.Float(string='Insentif Point 2 (Rp)', digits=(12,2))
    
    @api.multi
    def hitung_data_academy(self):
        for academy in self:
            academy.last_scan = datetime.now()
            for rec in academy.academy_line:
                cat_all = self.env['res.partner'].search([
                    ('market_id', '=', rec.market_id.id), 
                    ('market', '=', True),
                    ('date_market', '>=', academy.date_from),
                    ('date_market', '<=', academy.date_to)
                ])
                point12 = 0
                point6 = 0
                point2 = 0
                count=0
                for cat in cat_all:
                    count = count + 1 
                    if cat.potensi_all >= 20000000:
                        if cat.printer_line or cat.printer_tinta_line or cat.printer_lain_line or cat.catridge_line or cat.catridge_tinta_line or cat.catridge_lain_line :
                            point12 = point12 + 1
                    elif cat.potensi_all >= 10000000 and cat.potensi_all < 20000000:
                        if cat.printer_line or cat.printer_tinta_line or cat.printer_lain_line or cat.catridge_line or cat.catridge_tinta_line or cat.catridge_lain_line :
                            point6 = point6 + 1
                    elif cat.potensi_all >= 1 and cat.potensi_all < 10000000:
                        if cat.printer_line or cat.printer_tinta_line or cat.printer_lain_line or cat.catridge_line or cat.catridge_tinta_line or cat.catridge_lain_line :
                            point2 = point2 + 1
                rec.total = point2 + point6 + point12
                rec.point12 = point12
                rec.point6 = point6
                rec.point2 = point2
                rec.insentif = (point12 * academy.insentif12) + (point6 * academy.insentif6) + (point2 * academy.insentif2)
    
class AcademyLine(models.Model):
    _name = 'academy.line'

    academy_id = fields.Many2one(comodel_name='academy', string='Academy', ondelete='cascade', readonly=True)
    market_id = fields.Many2one(comodel_name='res.users', string='Market Person')
    point12 = fields.Float(string='Point 12')
    point6 = fields.Float(string='Point 6')
    point2 = fields.Float(string='Point 2')
    total = fields.Float(string='Total')
    insentif = fields.Float(string='Insentif')
    