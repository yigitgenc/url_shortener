"""Application views module."""

from typing import Union

from flask import request, redirect, jsonify
from flask.views import View
from validators import url as url_validator

from app.models import db, Url, Visit
from app.utils import generate_code


class RedirectView(View):
    """
    Base redirect endpoint. [/<string:code> (GET)]
    """
    methods = ['GET']

    def dispatch_request(self, code) -> Union[jsonify, redirect]:
        obj = db.session.query(Url).filter_by(code=code).first()

        if not obj:
            return jsonify({'error': 'Not found'}), 404

        visit = Visit(url=obj, ip_address=request.remote_addr, user_agent=str(request.user_agent))
        db.session.add(visit)
        db.session.commit()

        return redirect(obj.url, code=302)


class ShortenView(View):
    """
    Shorten URL endpoint. [/shorten (POST)]
    Form data: ['url']
    """
    methods = ['POST']

    def dispatch_request(self) -> jsonify:
        url = request.values.get('url')

        if not url_validator(url):
            return jsonify({'error': 'Not a valid URL.'}), 400  # Bad request.

        status = 200  # OK.
        start = 0

        while True:
            code = generate_code(url, start)
            obj = db.session.query(Url).filter_by(code=code).first()
            data = {'url': url, 'code': code}

            if not obj:
                obj = Url(**data)
                db.session.add(obj)
                db.session.commit()
                status = 201  # Created.

            if obj and obj.url != url:
                # Edge case scenario;
                # In order to avoid conflicts, increment starting index and try again.
                start += 1
                continue

            break

        return jsonify(data), status
