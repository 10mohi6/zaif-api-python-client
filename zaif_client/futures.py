# coding: utf-8
from sync import Client


class Futures(Client):

	def groups(self, **kwargs):
		params = kwargs
		path = '/fapi/1/groups/{0}'.format(params['group_id'])

		data = self._request(path, params=params)

		return data

	def last_price(self, **kwargs):
		params = kwargs
		path = '/fapi/1/last_price/{0}/{1}'.format(params['group_id'],params['currency_pair'])

		data = self._request(path, params=params)

		return data

	def ticker(self, **kwargs):
		params = kwargs
		path = '/fapi/1/ticker/{0}/{1}'.format(params['group_id'],params['currency_pair'])

		data = self._request(path, params=params)

		return data

	def trades(self, **kwargs):
		params = kwargs
		path = '/fapi/1/trades/{0}/{1}'.format(params['group_id'],params['currency_pair'])

		data = self._request(path, params=params)

		return data

	def depth(self, **kwargs):
		params = kwargs
		path = '/fapi/1/depth/{0}/{1}'.format(params['group_id'],params['currency_pair'])

		data = self._request(path, params=params)

		return data
