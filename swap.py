from odoo import models, fields


class SwapRequest(models.Model):

    _name = 'skill.swap.request'

    _description = 'Skill Swap Request'


    from_user = fields.Char(string='From User', required=True)

    to_user = fields.Char(string='To User', required=True)

    skill_requested = fields.Many2one('skill.swap.skill', string='Requested Skill')

    status = fields.Selection([

        ('pending', 'Pending'),

        ('accepted', 'Accepted'),

        ('rejected', 'Rejected'),

    ], string='Status', default='pending')