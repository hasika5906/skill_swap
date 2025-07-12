from odoo import models, fields


class Skill(models.Model):

    _name = 'skill.swap.skill'

    _description = 'Skill'


    name = fields.Char(string='Skill Name', required=True)

    category = fields.Selection([

        ('tech', 'Technical'),

        ('lang', 'Language'),

        ('art', 'Arts'),

        ('other', 'Other'),

    ], string='Category', required=True)