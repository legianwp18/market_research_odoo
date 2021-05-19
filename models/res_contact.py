import datetime
from odoo import tools
from odoo import api, fields, models


class ResContact(models.Model):
    _inherit = 'res.partner'

    @api.model
    def _get_default_requested_by(self):
        return self.env['res.users'].browse(self.env.uid)

    printer_line = fields.One2many(comodel_name='printer.line', inverse_name='id_partner', string='Printer Line')
    printer_tinta_line = fields.One2many(comodel_name='printer.tinta.line', inverse_name='id_partner', string='Printer Tinta Line')
    printer_lain_line = fields.One2many(comodel_name='printer.lain.line', inverse_name='id_partner', string='Printer Lainya Line')
    catridge_line = fields.One2many(comodel_name='catridge.line', inverse_name='id_partner', string='Catridge Line')
    catridge_tinta_line = fields.One2many(comodel_name='catridge.tinta.line', inverse_name='id_partner', string='Catridge Tinta Line')
    catridge_lain_line = fields.One2many(comodel_name='catridge.lain.line', inverse_name='id_partner', string='Catridge Lainya Line')
    id_category = fields.Many2one(comodel_name='category.customer', string='Instansi/Perseroan')
    id_metode = fields.Many2one(comodel_name='metode.pembelian', string='Metode Pembelian')
    freq = fields.Integer(string='Frek Pembelian (1Thn)')
    potensi = fields.Integer(string='Potensi Laser (Rp)')
    potensi_tinta = fields.Integer(string='Potensi Tinta (Rp)')
    potensi_lain = fields.Integer(string='Potensi Lainya (Rp)')
    potensi_all = fields.Integer(compute='_compute_potensi_all', string='Potensi All (Rp)', store=False)
    market_id = fields.Many2one(comodel_name='res.users', string='Market Person', track_visibility='onchange', default=_get_default_requested_by)
    market = fields.Boolean(string='Market', default=False)
    date_market = fields.Datetime(string='Date Market')
    point = fields.Selection(string='Point', selection=[('point12', 'Point 12'), ('point6', 'Point 6'), ('point2', 'Point 2')])

    @api.depends('potensi_all')
    def _compute_potensi_all(self):
        for rec in self:
            rec.potensi_all = rec.potensi + rec.potensi_tinta + rec.potensi_lain
    
    @api.onchange('potensi')
    def onchange_potensi(self):
        if self.potensi_all >= 20000000:
            if self.printer_line or self.printer_tinta_line or self.printer_lain_line or self.catridge_line or self.catridge_tinta_line or self.catridge_lain_line :
                self.point = 'point12'
        elif self.potensi_all >= 10000000 and self.potensi_all < 20000000:
            if self.printer_line or self.printer_tinta_line or self.printer_lain_line or self.catridge_line or self.catridge_tinta_line or self.catridge_lain_line :
                self.point = 'point6'
        elif self.potensi_all >= 1 and self.potensi_all < 10000000:
            if self.printer_line or self.printer_tinta_line or self.printer_lain_line or self.catridge_line or self.catridge_tinta_line or self.catridge_lain_line :
                self.point = 'point2'
        else:
            self.point = ''

    @api.onchange('potensi_tinta')
    def onchange_potensi_tinta(self):
        if self.potensi_all >= 20000000:
            if self.printer_line or self.printer_tinta_line or self.printer_lain_line or self.catridge_line or self.catridge_tinta_line or self.catridge_lain_line :
                self.point = 'point12'
        elif self.potensi_all >= 10000000 and self.potensi_all < 20000000:
            if self.printer_line or self.printer_tinta_line or self.printer_lain_line or self.catridge_line or self.catridge_tinta_line or self.catridge_lain_line :
                self.point = 'point6'
        elif self.potensi_all >= 1 and self.potensi_all < 10000000:
            if self.printer_line or self.printer_tinta_line or self.printer_lain_line or self.catridge_line or self.catridge_tinta_line or self.catridge_lain_line :
                self.point = 'point2'
        else:
            self.point = ''
    
    @api.onchange('potensi_lain')
    def onchange_potensi_lain(self):
        if self.potensi_all >= 20000000:
            if self.printer_line or self.printer_tinta_line or self.printer_lain_line or self.catridge_line or self.catridge_tinta_line or self.catridge_lain_line :
                self.point = 'point12'
        elif self.potensi_all >= 10000000 and self.potensi_all < 20000000:
            if self.printer_line or self.printer_tinta_line or self.printer_lain_line or self.catridge_line or self.catridge_tinta_line or self.catridge_lain_line :
                self.point = 'point6'
        elif self.potensi_all >= 1 and self.potensi_all < 10000000:
            if self.printer_line or self.printer_tinta_line or self.printer_lain_line or self.catridge_line or self.catridge_tinta_line or self.catridge_lain_line :
                self.point = 'point2'
        else:
            self.point = ''

    @api.onchange('market')
    def onchange_market(self):
        if self.market :
            self.date_market = datetime.datetime.now()
    
    @api.onchange('market_id')
    def onchange_market_id(self):
        if self.market_id :
            self.date_market = datetime.datetime.now()

class CatridgeLine(models.Model): 
    _name = 'catridge.line'
    _description = 'Catridge Line'
    
    name = fields.Many2one(comodel_name='customer.catridge.laser', string='Catridge', required=True)
    qty = fields.Integer(string='Jumlah', required=True)
    id_partner = fields.Many2one(comodel_name='res.partner', string='Customer')
    note = fields.Char(string='Notes')

class CatridgeTintaLine(models.Model): 
    _name = 'catridge.tinta.line'
    _description = 'Catridge Tinta Line'
    
    name = fields.Many2one(comodel_name='customer.catridge.tinta', string='Catridge Tinta', required=True)
    qty = fields.Integer(string='Jumlah', required=True)
    id_partner = fields.Many2one(comodel_name='res.partner', string='Customer')
    note = fields.Char(string='Notes')

class CatridgeLainLine(models.Model): 
    _name = 'catridge.lain.line'
    _description = 'Catridge Lain Line'
    
    name = fields.Many2one(comodel_name='customer.catridge.lain', string='Catridge Lainya', required=True)
    qty = fields.Integer(string='Jumlah', required=True)
    id_partner = fields.Many2one(comodel_name='res.partner', string='Customer')
    note = fields.Char(string='Notes')

class PrinterLine(models.Model):
    _name = 'printer.line'
    _description = 'Printer Line'

    name = fields.Many2one(comodel_name='customer.printer.laser', string='Printer', required=True)
    qty = fields.Integer(string='Jumlah', required=True)
    id_partner = fields.Many2one(comodel_name='res.partner', string='Customer')
    note = fields.Char(string='Notes')

class PrinterTintaLine(models.Model):
    _name = 'printer.tinta.line'
    _description = 'Printer Tinta Line'

    name = fields.Many2one(comodel_name='customer.printer.tinta', string='Printer Tinta', required=True)
    qty = fields.Integer(string='Jumlah', required=True)
    id_partner = fields.Many2one(comodel_name='res.partner', string='Customer')
    note = fields.Char(string='Notes')

class PrinterLainyaLine(models.Model):
    _name = 'printer.lain.line'
    _description = 'Printer Lain Line'

    name = fields.Many2one(comodel_name='customer.printer.lain', string='Printer Lainya', required=True)
    qty = fields.Integer(string='Jumlah', required=True)
    id_partner = fields.Many2one(comodel_name='res.partner', string='Customer')
    note = fields.Char(string='Notes')
    