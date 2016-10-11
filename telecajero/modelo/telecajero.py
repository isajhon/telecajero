# -*- coding: utf-8 -*-

from openerp.osv import fields, osv


class telecajero(osv.osv):
    _name = 'telecajero.telecajero'
    _rec_name = 'cedula'
     
    _columns={
        'cedula':fields.integer('cedula',size=10,required=True,help='ingrese su cedula'),
        'cuenta':fields.integer('cuenta',size=20,required=True,help='ingrese su cuenta'),
        'fecha':fields.date('Fecha',size=20,help='fecha de consulta'),
        'nombre':fields.char('Nombre',size=100,help='Nombre del Titular'),
        'active':fields.boolean('Activo',help='Si esta activo el motor lo incluira en la vista...')
        }
        
    _defaults={
        'active':True,
        }