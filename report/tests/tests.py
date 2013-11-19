# -*- coding: utf-8 -*-
from flask import url_for
from utils.tests import BaseTestCase

class RoutesTest(BaseTestCase):

    def test_report_index_route(self):
        resp = self.client.get(url_for('report_app.index'))
        self.assertStatus(resp, 200)


