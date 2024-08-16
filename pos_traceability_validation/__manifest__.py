# -*- coding: utf-8 -*-
##############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2024-TODAY Cybrosys Technologies(<http://www.cybrosys.com>).
#    Author: Cybrosys Techno Solutions(<http://www.cybrosys.com>)
#    you can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    GENERAL PUBLIC LICENSE (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'POS Serial Number Validator',
    'version': '17.0.1.0.0',
    'category': 'Point of Sale',
    'summary': """Validate Serial number of a product by checking 
                  availability in stock""",
    'description': """This module validates the serial number of a product in
                        the Point of Sale (POS) by checking its availability 
                        in stock. If the serial number is not in stock or 
                        is a duplicate entry, it displays an error message.""",
    'author': 'Cybrosys Techno Solutions',
    'company': 'Cybrosys Techno Solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'website': "https://www.cybrosys.com",
    'depends': ['point_of_sale', 'stock', 'web'],
    'assets': {
        'point_of_sale._assets_pos': [
            'pos_traceability_validation/static/src/xml/pos_orderline.xml',
            'pos_traceability_validation/static/src/js/CustomPopup.js',
            'pos_traceability_validation/static/src/js/pos_traceability_validation.js',
            'pos_traceability_validation/static/src/js/pos_orderline.js',
        ]
    },
    'images': ['static/description/banner.png'],
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'application': True,
}