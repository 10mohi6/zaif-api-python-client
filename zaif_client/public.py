# coding: utf-8
from sync import Client


class Public(Client):

	def currencies(self, **kwargs):
		params = kwargs
		path = '/api/1/currencies/{0}'.format(params['currency'])

		data = self._request(path, params=params)

		return data

	def currency_pairs(self, **kwargs):
		params = kwargs
		path = '/api/1/currency_pairs/{0}'.format(params['currency_pair'])

		data = self._request(path, params=params)

		return data

	def last_price(self, **kwargs):
		params = kwargs
		path = '/api/1/last_price/{0}'.format(params['currency_pair'])

		data = self._request(path, params=params)

		return data

	def ticker(self, **kwargs):
		params = kwargs
		path = '/api/1/ticker/{0}'.format(params['currency_pair'])

		data = self._request(path, params=params)

		return data

	def trades(self, **kwargs):
		params = kwargs
		path = '/api/1/trades/{0}'.format(params['currency_pair'])

		data = self._request(path, params=params)

		return data

	def depth(self, **kwargs):
		params = kwargs
		path = '/api/1/depth/{0}'.format(params['currency_pair'])

		data = self._request(path, params=params)

		return data
