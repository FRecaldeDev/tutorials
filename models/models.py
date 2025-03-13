# -*- coding: utf-8 -*-
from odoo import models, fields

class EstateProperty(models.Model):
  _name='estate.property'
  _description='Real Estate Property'

  name = fields.Char(string="Property Name", required=True)
  description = fields.Text(string="Description")
  postcode = fields.Char(string="Postcode")
  date_availability = fields.Date(string="Avaiability Date")
  expected_price= fields.Float(string="Expected Price", required=True)
  selling_price= fields.Float(string="Selling Price")
  bedrooms= fields.Integer(string="Bedrooms")
  living_area = fields.Integer(string="Living Area")
  facades = fields.Integer(string="Number of Facades")
  garage = fields.Boolean(String="Garage")
  garden = fields.Boolean(string="Garden")
  garden_area = fields.Integer(string="Garden Area")
  garden_orientation = fields.Char(string="Garden Orientation")

  create_uid = fields.Many2one('res.users', string="Created by", readonly=True)
  create_date = fields.Datetime(string="Creation Date", readonly=True)
  write_uid = fields.Many2one('res.users', string="Last updated by", readonly=True)
  write_date = fields.Datetime(string="last Updated Date", readonly=True)


