"""Superfeedr callback handlers.

Not really sure what this will be yet. Background:
https://github.com/snarfed/bridgy-fed/issues/18#issuecomment-430731476
https://documentation.superfeedr.com/publishers.html
"""
import logging

import webapp2

import common


class SuperfeedrHandler(common.Handler):
    """Superfeedr subscription callback handler.

    https://documentation.superfeedr.com/publishers.html#subscription-callback
    """

    def post(self):
        logging.info('Got:\n%s', self.request.body)
        self.response.status_int = 204

    get = post


ROUTES = [
    (r'/superfeedr/.*', SuperfeedrHandler),
]
