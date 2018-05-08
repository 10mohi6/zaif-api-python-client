# coding: utf-8
from sync import Client


class Leverage(Client):

	def get_positions(self, **kwargs):
		params = kwargs
		params['method'] = 'get_positions'
		path = '/tlapi'
		
		data = self._request(path, method='POST', params=params)

		return data

	def position_history(self, **kwargs):
		params = kwargs
		params['method'] = 'position_history'
		path = '/tlapi'
		
		data = self._request(path, method='POST', params=params)

		return data

	def active_positions(self, **kwargs):
		params = kwargs
		params['method'] = 'active_positions'
		path = '/tlapi'
		
		data = self._request(path, method='POST', params=params)

		return data

	def create_position(self, **kwargs):
		params = kwargs
		params['method'] = 'create_position'
		path = '/tlapi'
		
		data = self._request(path, method='POST', params=params)

		return data

	def change_position(self, **kwargs):
		params = kwargs
		params['method'] = 'change_position'
		path = '/tlapi'
		
		data = self._request(path, method='POST', params=params)

		return data

	def cancel_position(self, **kwargs):
		params = kwargs
		params['method'] = 'cancel_position'
		path = '/tlapi'
		
		data = self._request(path, method='POST', params=params)

		return data
