# -*- coding: utf-8 -*-
from flask import url_for
from utils.tests import BaseTestCase

class RouteTest(BaseTestCase):

    def test_index_redirect_to_report(self):
        resp = self.client.get('/')
        self.assertStatus(resp, 302)
