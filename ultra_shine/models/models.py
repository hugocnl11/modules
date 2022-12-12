# -*- coding: utf-8 -*-

from odoo import models, fields, api
import random
import string
from odoo.exceptions import ValidationError
from datetime import datetime, timedelta
import math


class Cuenta(models.Model):

    _name = 'ultra_shine.cuenta'
    _description = 'Cuenta de Usuario'

    #type = fields.One2many('ultra_shine.personaje_unidad', ondelete="restrict", required=True)

    name = fields.Char(required=True)
    passwd = fields.Char()
    avatar = fields.Image(max_width = 250, max_heigth = 250)
    gemas = fields.Integer()
    personaje=fields.Many2many('ultra_shine.personaje_unidad')

class Batalla(models.Model):
    _name = 'ultra_shine.batalla'
    _description = 'Clase para las batallas'

    player1=fields.Many2one('ultra_shine.personaje_unidad')
    player2=fields.Many2one('ultra_shine.personaje')

    winner = fields.Char() 
    
    dateInicio = fields.Datetime() 
    dateFinal = fields.Datetime()
    
    def accionBatalla(self):  # ORM
        for b in self:
            nombre1 = b.player1.name
            nombre2 = b.player2.name 
            if b.player1.ataque > b.player2.ataque:
                b.winner = nombre1
            if b.player2.ataque > b.player1.ataque:
                b.winner = nombre2

         
                


class Personaje(models.Model):
    _name = 'ultra_shine.personaje'
    _description = 'Personaje Jugable con: nombre, sprite, spriteChibi, nivel, ataque, defensa, vida, velocidad, rol    , rareza (estrellas), elemento y habilidades (pasiva y activa) además de un slot para arma'
    #type = fields.One2many('ultra_shine.personaje_unidad', ondelete="restrict", required=True)

    name = fields.Char(required=True)
    sprite = fields.Image(max_width = 200, max_heigth = 200)
    icono = fields.Image(max_width = 200, max_heigth = 200)
    icono_tumb = fields.Image(related="icono", max_width = 80, max_heigth = 80)
    spriteAnimado = fields.Image(max_width = 200, max_heigth = 200)
    spriteAtaque= fields.Image(max_width = 200, max_heigth = 200)
    nivel = fields.Integer()
    ataque = fields.Integer()
    defensa = fields.Integer()
    vida =  fields.Integer()
    velocidad = fields.Integer()

    from odoo.exceptions import ValidationError

    @api.constrains('velocidad')
    def _check_velocidad(self):
        for Personaje in self:
            if Personaje.velocidad > 6:
                raise ValidationError("DEMASIADA VELOCIDAD" % Personaje.velocidad)

    rol = fields.Selection(([('1','DPS'),('2','SUBDPS'),('3','BUFFER'),('4','HEALER'),('5','TANK')]))
    rareza = fields.Selection(([('1','3'),('2','4'),('3','5'),('4','6')]))
    
    
    elemento = fields.Selection(([('1','Fuego'),('2','Agua'),('3','Planta'),('4','Rayo'),('5','Luz'),('6','Oscuridad')]))
    
    habilidadActiva = fields.Char(default='Por determinar')
    habilidadPasiva = fields.Char(default='Por determinar')
    
    slotArma = fields.Char(string="Slot Arma", compute="_slot_arma")
    def _slot_arma(self):          
      for r in self:                      
          if not r.slotArma:      
              r.slotArma = "Daga dentada" 
          else:
              r.slotArmat = "Nada"

class Personaje_unidad(models.Model):
    _name = 'ultra_shine.personaje_unidad'
    _description = 'Personaje Jugable con: nombre, sprite, spriteChibi, nivel, ataque, defensa, vida, velocidad, rol    , rareza (estrellas), elemento y habilidades (pasiva y activa) además de un slot para arma'
    type = fields.Many2one('ultra_shine.personaje', ondelete="restrict", required=True)
    

    name = fields.Char(related='type.name')
    sprite = fields.Image(related='type.sprite')
    icono = fields.Image(related='type.icono')
    icono_tumb = fields.Image(related='type.icono_tumb')
    spriteAnimado = fields.Image(related='type.spriteAnimado')
    spriteAtaque= fields.Image(related='type.spriteAtaque')
    nivel = fields.Integer(related='type.nivel')
    ataque = fields.Integer(related='type.ataque')
    defensa = fields.Integer(related='type.defensa')
    vida =  fields.Integer(related='type.vida')
    velocidad = fields.Integer(related='type.velocidad')
    rol = fields.Selection(related='type.rol')
    rareza = fields.Selection(related='type.rareza')
    elemento = fields.Selection(related='type.elemento')
    habilidadActiva = fields.Char(related='type.habilidadActiva')
    habilidadPasiva = fields.Char(related='type.habilidadPasiva')
    slotArma = fields.Char(related='type.slotArma')

class Banner_Personaje(models.Model):
    _name= 'ultra_shine.banner_personaje'
    _description= 'Seleccionador de personajes para agruparlos y preparar los banners'
    
    name = fields.Char(required=True)
    iconoBanner = fields.Image()
    tirar = fields.Char()
    player = fields.Many2one('ultra_shine.cuenta')

    unidad1 = fields.Many2one('ultra_shine.personaje', ondelete="restrict", required=True)
    rareza1 = fields.Selection(related='unidad1.rareza')
    sprite1 = fields.Image(related='unidad1.spriteAnimado')

    unidad2 = fields.Many2one('ultra_shine.personaje', ondelete="restrict", required=True)
    rareza2 = fields.Selection(related='unidad2.rareza')
    sprite2 = fields.Image(related='unidad2.spriteAnimado')

    unidad3 = fields.Many2one('ultra_shine.personaje', ondelete="restrict", required=True)
    rareza3 = fields.Selection(related='unidad3.rareza')
    sprite3 = fields.Image(related='unidad3.spriteAnimado')

    unidad4 = fields.Many2one('ultra_shine.personaje', ondelete="restrict", required=True)
    rareza4 = fields.Selection(related='unidad4.rareza')
    sprite4 = fields.Image(related='unidad4.spriteAnimado')

    unidad5 = fields.Many2one('ultra_shine.personaje', ondelete="restrict", required=True)
    rareza5 = fields.Selection(related='unidad5.rareza')
    sprite5 = fields.Image(related='unidad5.spriteAnimado')

    unidad6 = fields.Many2one('ultra_shine.personaje', ondelete="restrict", required=True)
    rareza6 = fields.Selection(related='unidad6.rareza')
    sprite6 = fields.Image(related='unidad6.spriteAnimado')
    
    unidadGanada = fields.Many2one('ultra_shine.personaje', ondelete="restrict")
    rarezaGanada = fields.Selection(related='unidadGanada.rareza')
    spriteGanada = fields.Image(related='unidadGanada.spriteAnimado') 
    
    def accionar_banner(self):  # ORM
        for b in self:
            
            r = random.randint(1, 6)
            
            if r==1:
                b.unidadGanada = b.unidad1
                self.env['ultra_shine.personaje_unidad'].create({
                    "type": b.unidad1.id
                })
            if r==2:
                b.unidadGanada = b.unidad2
                b.unidadGanada = b.unidad2
                self.env['ultra_shine.personaje_unidad'].create({
                    "type": b.unidad2.id
                })
            if r==3:
                b.unidadGanada = b.unidad3
                b.unidadGanada = b.unidad3
                self.env['ultra_shine.personaje_unidad'].create({
                    "type": b.unidad3.id
                })
            if r==4:
                b.unidadGanada = b.unidad4
                b.unidadGanada = b.unidad4
                self.env['ultra_shine.personaje_unidad'].create({
                    "type": b.unidad4.id
                })
            if r==5:
                b.unidadGanada = b.unidad5
                b.unidadGanada = b.unidad5
                self.env['ultra_shine.personaje_unidad'].create({
                    "type": b.unidad5.id
                })
            if r==6:
                b.unidadGanada = b.unidad6
                b.unidadGanada = b.unidad6
                self.env['ultra_shine.personaje_unidad'].create({
                    "type": b.unidad6.id
                })
            


class Comp_Builder(models.Model):
     _name = 'ultra_comp_builder'
     _description = 'Clase para montar los equipos'




class Enemigo(models.Model):
     _name = 'ultra_shine.enemigo'
     _description = 'Clase para los enemigos del PVE que deberán tener:  nombre, sprite, spriteChibi, nivel, ataque, defensa, vida, velocidad, rol, rareza (estrellas), elemento y habilidades'

     name = fields.Char(required=True)
     sprite = fields.Image(max_width = 200, max_heigth = 200)
     spriteChibi = fields.Image(max_width = 200, max_heigth = 200)
     nivel = fields.Integer()
     ataque = fields.Integer()
     defensa = fields.Integer()
     vida =  fields.Integer()
     velocidad = fields.Integer()
     rol = fields.Selection(([('1','Slime'),('2','Guerrero'),('3','NoMuerto'),('4','Bestia'),('5','Mítico')]))
     rareza = fields.Selection(([('1','Esbirro'),('2','Comandante'),('3','Jefe'),('4','666')]))
     elemento = fields.Selection(([('1','Fuego'),('2','Agua'),('3','Planta'),('4','Rayo'),('5','Luz'),('6','Oscuridad')]))
     habilidadActiva = fields.Char()




#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
