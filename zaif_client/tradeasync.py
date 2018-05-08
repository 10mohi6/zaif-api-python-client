# coding: utf-8
import grequests
import time
from trade import Trade


class TradeAsync(Trade):

	def _request(self, path, method='GET', params=None):
		uri = '{0}{1}'.format(self.origin, path)
		params['nonce'] = time.time()
		headers = {
			'key': self.public_key,
			'sign': self._signature(params)
		}
		if method == 'GET':
			res = grequests.get(uri, headers=headers, timeout=self.timeout, params=params)
		else: # method == 'POST'
			res = grequests.post(uri, headers=headers, timeout=self.timeout, data=params)

		return res
