# -*- coding: utf-8 -*-
from flask import url_for
#from unittest.TestCase import assertEquals
from utils.tests import BaseTestCase
from datetime import datetime
from application import db

class RoutesTest(BaseTestCase):

    def test_report_index_route(self):
        resp = self.client.get(url_for('report_app.index'))
        self.assertStatus(resp, 200)

class SquidLogModelsTest(BaseTestCase):

    def setUp(self):
        log = db.Log()
        log['timestamp']=0.0
        log['date']=datetime.fromtimestamp(0.0)
        log['ident']=u'john'
        log['host_ip']=u'127.0.0.1'
        log['elapsed']=u'250'
        log['action']=u'TCP_MISS'
        log['protocol']=u'http'
        log['uri']=u'http://localhost'
        log['domain']=u'localhost'
        log['http_status']=200
        log['bytes']=32
        log['method']=u'GET'
        log['type']=u'text/html'
        log['hierachi_code']=u'DIRECT'
        log['ip_server']=u'127.0.0.1'
        log.save()

    def test_get_data(self):
        assert1 = db.Log.find({'ident':'john'})[0]
        self.assertEquals(assert1['ident'], u'john')

    def tearDown(self):
        db.drop_collection('log')
