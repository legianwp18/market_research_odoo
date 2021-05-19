# -*- coding: utf-8 -*-

from odoo import models, fields, api

########################### Printer
class CustomerPrinter(models.Model):
    _name = 'customer.printer.laser'

    id_brand = fields.Many2one(comodel_name='customer.brand', string='Brand/Merk', required=True)
    name = fields.Char(string='Nama Printer Laser', required=True)
    model = fields.Char(string='Model Printer Laser')
    note = fields.Char(string='Note')

class CustomerPrinterTinta(models.Model):
    _name = 'customer.printer.tinta'

    id_brand = fields.Many2one(comodel_name='customer.brand', string='Brand/Merk', required=True)
    name = fields.Char(string='Nama Printer Tinta', required=True)
    model = fields.Char(string='Model Printer Tinta')
    note = fields.Char(string='Note')

class CustomerPrinterLain(models.Model):
    _name = 'customer.printer.lain'

    id_brand = fields.Many2one(comodel_name='customer.brand', string='Brand/Merk', required=True)
    name = fields.Char(string='Nama Printer Lainya', required=True)
    model = fields.Char(string='Model Printer Lainya')
    note = fields.Char(string='Note')

#################################### Catridge
class CustomerCatridge(models.Model):
    _name = 'customer.catridge.laser'

    id_brand = fields.Many2one(comodel_name='customer.brand', string='Brand/Merk', required=True)
    name = fields.Char(string="Type Catridge Laser", required=True)
    moncol = fields.Selection(string='Mono/Color', selection=[('Mono', 'Mono'), ('Color', 'Color'),])
    note = fields.Char(string='Note')

class CustomerCatridgeTinta(models.Model):
    _name = 'customer.catridge.tinta'

    id_brand = fields.Many2one(comodel_name='customer.brand', string='Brand/Merk', required=True)
    name = fields.Char(string="Type Catridge Tinta", required=True)
    moncol = fields.Selection(string='Mono/Color', selection=[('Mono', 'Mono'), ('Color', 'Color'),])
    note = fields.Char(string='Note')

class CustomerCatridgeLain(models.Model):
    _name = 'customer.catridge.lain'

    id_brand = fields.Many2one(comodel_name='customer.brand', string='Brand/Merk', required=True)
    name = fields.Char(string="Type Catridge Lainya", required=True)
    moncol = fields.Selection(string='Mono/Color', selection=[('Mono', 'Mono'), ('Color', 'Color'),])
    note = fields.Char(string='Note')

class CustomerBrand(models.Model):
    _name = 'customer.brand'

    name = fields.Char(string="Brand/Merk", required=True)
    ket = fields.Char(string="Keterangan")