# coding: utf-8
from sync import Client


class Trade(Client):

	def get_info(self, **kwargs):
		params = kwargs
		params['method'] = 'get_info'
		path = '/tapi'
		
		data = self._request(path, method='POST', params=params)

		return data

	def get_info2(self, **kwargs):
		params = kwargs
		params['method'] = 'get_info2'
		path = '/tapi'
		
		data = self._request(path, method='POST', params=params)

		return data

	def get_personal_info(self, **kwargs):
		params = kwargs
		params['method'] = 'get_personal_info'
		path = '/tapi'
		
		data = self._request(path, method='POST', params=params)

		return data

	def get_id_info(self, **kwargs):
		params = kwargs
		params['method'] = 'get_id_info'
		path = '/tapi'
		
		data = self._request(path, method='POST', params=params)

		return data

	def trade_history(self, **kwargs):
		params = kwargs
		params['method'] = 'trade_history'
		path = '/tapi'
		
		data = self._request(path, method='POST', params=params)

		return data

	def active_orders(self, **kwargs):
		params = kwargs
		params['method'] = 'active_orders'
		path = '/tapi'
		
		data = self._request(path, method='POST', params=params)

		return data

	def trade(self, **kwargs):
		params = kwargs
		params['method'] = 'trade'
		path = '/tapi'
		
		data = self._request(path, method='POST', params=params)

		return data

	def cancel_order(self, **kwargs):
		params = kwargs
		params['method'] = 'cancel_order'
		path = '/tapi'
		
		data = self._request(path, method='POST', params=params)

		return data

	def withdraw(self, **kwargs):
		params = kwargs
		params['method'] = 'withdraw'
		path = '/tapi'
		
		data = self._request(path, method='POST', params=params)

		return data

	def deposit_history(self, **kwargs):
		params = kwargs
		params['method'] = 'deposit_history'
		path = '/tapi'
		
		data = self._request(path, method='POST', params=params)

		return data

	def withdraw_history(self, **kwargs):
		params = kwargs
		params['method'] = 'withdraw_history'
		path = '/tapi'
		
		data = self._request(path, method='POST', params=params)

		return data
