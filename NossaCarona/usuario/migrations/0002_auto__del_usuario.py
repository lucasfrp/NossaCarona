# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Usuario'
        db.delete_table(u'usuario_usuario')


    def backwards(self, orm):
        # Adding model 'Usuario'
        db.create_table(u'usuario_usuario', (
            ('nome', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('sexo', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('sobrenome', self.gf('django.db.models.fields.CharField')(max_length=50)),
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal(u'usuario', ['Usuario'])


    models = {
        
    }

    complete_apps = ['usuario']