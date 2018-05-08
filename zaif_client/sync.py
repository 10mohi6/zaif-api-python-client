# coding: utf-8
import hashlib
import requests
import time
import urllib
import hmac


class Client(object):

	def __init__(self, **kwargs):
		self.origin = kwargs.get('origin', 'https://api.zaif.jp')
		self.public_key = kwargs.get('public_key', None)
		if self.public_key is None:
			raise Exception('public key is absent.')
		self.private_key = kwargs.get('private_key', None)
		if self.private_key is None:
			raise Exception('private key is absent.')
		self.timeout = kwargs.get('timeout', None)

	def _request(self, path, method='GET', params=None):
		uri = '{0}{1}'.format(self.origin, path)
		params['nonce'] = time.time()
		headers = {
			'key': self.public_key,
			'sign': self._signature(params)
		}
		if method == 'GET':
			res = requests.get(uri, headers=headers, timeout=self.timeout, params=params)
		else: # method == 'POST'
			res = requests.post(uri, headers=headers, timeout=self.timeout, data=params)

		return res

	def _signature(self, params):
		sign = hmac.new(bytearray(self.private_key.encode('utf-8')), digestmod=hashlib.sha512)
		sign.update(urllib.parse.urlencode(params).encode('utf-8'))
		return sign.hexdigest()
