import unittest

from application import create_app


class BaseTestCase(unittest.TestCase):

    def __call__(self, result=None):
        self._pre_setup()
        super(BaseTestCase, self).__call__(result)
        self._post_teardown()

    def _pre_setup(self):
        self.app = create_app('settings.TestingConfig')
        self.client = self.app.test_client()
        self.ctx = self.app.test_request_context()
        self.ctx.push()

    def _post_teardown(self):
        self.ctx.pop()

    def assertStatus(self, resp, status_code):
        self.assertEqual(resp.status_code, status_code)
