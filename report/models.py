# -*- coding: utf-8 -*-

from flask.ext.mongokit import Document
from flask.ext.babel import gettext as _

import datetime

from application import db

@db.register
class Log(Document):
    __collection__ = 'log'

    structure = {
            'timestamp': float,
            'date': datetime.datetime,
            'ident':  unicode,
            'host_ip':  unicode,
            'elapsed':  unicode,
            'action':  unicode,
            'protocol':  unicode,
            'uri':  unicode,
            'domain': unicode,
            'http_status': int,
            'bytes': int,
            'method':  unicode,
            'type':  unicode,
            'hierachi_code':  unicode,
            'ip_server':  unicode,
    }

    def __repr__(self):
        return "<DB Log: %s" % (self.structure['ident'])
