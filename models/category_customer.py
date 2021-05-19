from odoo import api, fields, models


class CategoryCutomer(models.Model):
    _name = 'category.customer'
    _description = 'Category Customer'
    _parent_name = 'parent_category'
    _parent_store = True
    _parent_order = 'name'
    _rec_name = 'name'

    name = fields.Char(string='Category', required=True)
    complete_name = fields.Char(string='Full Category', compute='_compute_complete_name', store=True)
    parent_category = fields.Many2one(comodel_name='category.customer', string='Parent Category', index=True, ondelete='cascade')
    child_category = fields.One2many(comodel_name='category.customer', inverse_name='parent_category', string='Contains')
    desc = fields.Text(string='Description')
    parent_left = fields.Integer('Left Parent', index=True)
    parent_right = fields.Integer('Right Parent', index=True)
    
    @api.one
    @api.depends('name', 'parent_category.complete_name')
    def _compute_complete_name(self):
        """ Forms complete name of category from parent category to child category. """
        if self.parent_category.complete_name:
            self.complete_name = '%s/%s' % (self.parent_category.complete_name, self.name)
        else:
            self.complete_name = self.name

class MetodePembelian(models.Model):
    _name = 'metode.pembelian'
    _description = 'Metode Pembelian'
    
    name = fields.Char(string='Name', required=True)
    ket = fields.Text(string='Keterangan')
    
