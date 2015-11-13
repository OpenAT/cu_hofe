# -*- coding: utf-8 -*-

from openerp.fields import Char
from openerp.osv import osv



class calendar_event(osv.osv):
    _inherit = 'res.partner'

    email_a = Char(string='Alternative E-Mail A')
    email_b = Char(string='Alternative E-Mail B')
