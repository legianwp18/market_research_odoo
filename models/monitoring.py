import datetime
from odoo import models, fields, api 

class Monitoring(models.Model):
    _name = 'monitoring'

    name = fields.Char(string='Name', required=True)
    date = fields.Date(string='Date', default=fields.Date.today(), required=True)
    user_id = fields.Many2one(comodel_name='res.users', string='Responsible', default=lambda self: self.env.user.id, required=True)
    monitor_line = fields.One2many(comodel_name='monitoring.line', inverse_name='monitoring_id', string='Monitoring Line', readonly=False, track_visibility='onchange')
    last_scan = fields.Datetime(string='Last Scan')
    
    
    @api.multi
    def hitung_data(self):
        for monitor in self:
            monitor.last_scan = datetime.datetime.now()
            for rec in monitor.monitor_line:
                cat_all = self.env['res.partner'].search([('id_category', '=', rec.id_category.id)])
                poten=0
                count=0.00
                count_real=0.00
                persen = 0.00
                rerata = 0
                for cat in cat_all:
                    count = count + 1
                    if cat.potensi >= 10000000: 
                        if cat.printer_line or cat.catridge_line :
                            count_real = count_real + 1
                            poten = poten + cat.potensi
                if count > 0 :
                    if count_real > 0 :
                        persen = ((count_real / count) * 100)
                    else:
                        persen = 0
                else :
                    persen = 0
                if (count_real != 0) or (poten != 0) :
                    rerata = poten / count_real
                else :
                    rerata = 0
                rec.potensi_rill = poten
                rec.jml_data = count
                rec.jml_data_rill = count_real
                rec.persen = persen
                rec.potensi_rerata = rerata
                rec.potensi_all = rec.potensi_rerata * count
                if rec.persen < 10:
                    rec.status = 'running'
                elif rec.persen > 10:
                    rec.status = 'close'
    
class MonitoringLine(models.Model):
    _name = 'monitoring.line'

    monitoring_id = fields.Many2one(comodel_name='monitoring', string='Monitoring', ondelete='cascade', readonly=True)
    id_category = fields.Many2one(comodel_name='category.customer', string='Instansi/Perseroan')
    potensi_rill = fields.Float(string='Capaian Responden Rill', digits=(12,2))
    status = fields.Selection(
        string='Status',
        selection=[('running', 'Running'), ('pending', 'Pending'), ('close', 'Close')]
    )
    jml_data = fields.Float(string='Jumlah Data', digits=(12,0))
    jml_data_rill = fields.Float(string='Capaian Data Rill', digits=(12,0))
    persen = fields.Float(string='Persentase', digits=(3,2))
    potensi_rerata = fields.Float(string='Rerata', digits=(12,2))
    potensi_all = fields.Float(string='Estimasi Pasar Data Rill', digits=(12,2))

# CATRIDGE TINTA

class MonitoringTinta(models.Model):
    _name = 'monitoring.tinta'

    name = fields.Char(string='Name', required=True)
    date = fields.Date(string='Date', default=fields.Date.today(), required=True)
    user_id = fields.Many2one(comodel_name='res.users', string='Responsible', default=lambda self: self.env.user.id, required=True)
    monitor_tinta_line = fields.One2many(comodel_name='monitoring.tinta.line', inverse_name='monitoring_id', string='Monitoring Tinta Line', readonly=False, track_visibility='onchange')
    last_scan = fields.Datetime(string='Last Scan')
    
    
    @api.multi
    def hitung_data(self):
        for monitor in self:
            monitor.last_scan = datetime.datetime.now()
            for rec in monitor.monitor_tinta_line:
                cat_all = self.env['res.partner'].search([('id_category', '=', rec.id_category.id)])
                poten=0
                count=0.00
                count_real=0.00
                persen = 0.00
                rerata = 0
                for cat in cat_all:
                    count = count + 1
                    if cat.potensi_tinta >= 10000000: 
                        if cat.printer_tinta_line or cat.catridge_tinta_line:
                            count_real = count_real + 1
                            poten = poten + cat.potensi_tinta
                if count > 0 :
                    if count_real > 0 :
                        persen = ((count_real / count) * 100)
                    else:
                        persen = 0
                else :
                    persen = 0
                if (count_real != 0) or (poten != 0) :
                    rerata = poten / count_real
                else :
                    rerata = 0
                rec.potensi_rill = poten
                rec.jml_data = count
                rec.jml_data_rill = count_real
                rec.persen = persen
                rec.potensi_rerata = rerata
                rec.potensi_all = rec.potensi_rerata * count
                if rec.persen < 10:
                    rec.status = 'running'
                elif rec.persen > 10:
                    rec.status = 'close'
    
class MonitoringTintaLine(models.Model):
    _name = 'monitoring.tinta.line'

    monitoring_id = fields.Many2one(comodel_name='monitoring_tinta', string='Monitoring Tinta', ondelete='cascade', readonly=True)
    id_category = fields.Many2one(comodel_name='category.customer', string='Instansi/Perseroan')
    potensi_rill = fields.Float(string='Capaian Responden Rill', digits=(12,2))
    status = fields.Selection(
        string='Status',
        selection=[('running', 'Running'), ('pending', 'Pending'), ('close', 'Close')]
    )
    jml_data = fields.Float(string='Jumlah Data', digits=(12,0))
    jml_data_rill = fields.Float(string='Capaian Data Rill', digits=(12,0))
    persen = fields.Float(string='Persentase', digits=(3,2))
    potensi_rerata = fields.Float(string='Rerata', digits=(12,2))
    potensi_all = fields.Float(string='Estimasi Pasar Data Rill', digits=(12,2))
    
# CATRIDGE LAIN

class MonitoringLain(models.Model):
    _name = 'monitoring.lain'

    name = fields.Char(string='Name', required=True)
    date = fields.Date(string='Date', default=fields.Date.today(), required=True)
    user_id = fields.Many2one(comodel_name='res.users', string='Responsible', default=lambda self: self.env.user.id, required=True)
    monitor_lain_line = fields.One2many(comodel_name='monitoring.lain.line', inverse_name='monitoring_id', string='Monitoring Lain Line', readonly=False, track_visibility='onchange')
    last_scan = fields.Datetime(string='Last Scan')
    
    
    @api.multi
    def hitung_data(self):
        for monitor in self:
            monitor.last_scan = datetime.datetime.now()
            for rec in monitor.monitor_lain_line:
                cat_all = self.env['res.partner'].search([('id_category', '=', rec.id_category.id)])
                poten=0
                count=0.00
                count_real=0.00
                persen = 0.00
                rerata = 0
                for cat in cat_all:
                    count = count + 1
                    if cat.potensi_lain >= 10000000: 
                        if cat.printer_lain_line or cat.catridge_lain_line :
                            count_real = count_real + 1
                            poten = poten + cat.potensi_lain
                if count > 0 :
                    if count_real > 0 :
                        persen = ((count_real / count) * 100)
                    else:
                        persen = 0
                else :
                    persen = 0
                if (count_real != 0) or (poten != 0) :
                    rerata = poten / count_real
                else :
                    rerata = 0
                rec.potensi_rill = poten
                rec.jml_data = count
                rec.jml_data_rill = count_real
                rec.persen = persen
                rec.potensi_rerata = rerata
                rec.potensi_all = rec.potensi_rerata * count
                if rec.persen < 10:
                    rec.status = 'running'
                elif rec.persen > 10:
                    rec.status = 'close'
    
class MonitoringLainLine(models.Model):
    _name = 'monitoring.lain.line'

    monitoring_id = fields.Many2one(comodel_name='monitoring_lain', string='Monitoring Lain', ondelete='cascade', readonly=True)
    id_category = fields.Many2one(comodel_name='category.customer', string='Instansi/Perseroan')
    potensi_rill = fields.Float(string='Capaian Responden Rill', digits=(12,2))
    status = fields.Selection(
        string='Status',
        selection=[('running', 'Running'), ('pending', 'Pending'), ('close', 'Close')]
    )
    jml_data = fields.Float(string='Jumlah Data', digits=(12,0))
    jml_data_rill = fields.Float(string='Capaian Data Rill', digits=(12,0))
    persen = fields.Float(string='Persentase', digits=(3,2))
    potensi_rerata = fields.Float(string='Rerata', digits=(12,2))
    potensi_all = fields.Float(string='Estimasi Pasar Data Rill', digits=(12,2))