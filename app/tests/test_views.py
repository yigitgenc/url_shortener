"""Application test views module."""

import json
import unittest

from app import create_app
from app.models import db


class TestAppViewsModule(unittest.TestCase):
    def setUp(self):
        self.app = create_app({
            'TESTING': True,
            'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:',
            'SQLALCHEMY_TRACK_MODIFICATIONS': False,
        })
        self.client = self.app.test_client()

    def tearDown(self):
        with self.app.app_context():
            db.drop_all()

    def test_redirect_view_not_found(self):
        response = self.client.get('/cannotFindMe')
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 404)
        self.assertIn('error', data)

    def test_redirect_view_ok(self):
        response = self.client.post('/shorten', data={'url': 'http://example.com'})
        data = json.loads(response.data)

        response = self.client.get('/{}'.format(data['code']))
        self.assertEqual(response.status_code, 302)

    def test_shorten_view_bad_request(self):
        response = self.client.post('/shorten', data={'url': 'this-is-not-url'})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 400)
        self.assertIn('error', data)

    def test_shorten_view_created(self):
        response = self.client.post('/shorten', data={'url': 'http://example.com'})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 201)
        self.assertIn('url', data)
        self.assertIn('code', data)

        self.assertEqual(data['url'], 'http://example.com')
        self.assertEqual(data['code'], 'YTliOWYw')

    def test_shorten_view_ok(self):
        self.client.post('/shorten', data={'url': 'http://example.com'})
        response = self.client.post('/shorten', data={'url': 'http://example.com'})
        data = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertIn('url', data)
        self.assertIn('code', data)

        self.assertEqual(data['url'], 'http://example.com')
        self.assertEqual(data['code'], 'YTliOWYw')
