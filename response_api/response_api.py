#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Response API

HTTPStatus:
https://docs.python.org/3/library/http.html
"""

import http
from logni import log

class ResponseAPI(object):
	""" ResponseAPI object """

	def __init__(self, server_name='API'):

		self.server_name = server_name
		self._pylint_fixed = 0


	def __response(self, httpstatus, param):
		""" structure for body response """

		self._pylint_fixed = 0

		message = param.get('message')
		time_ms = param.get('time_ms')
		found = param.get('found', 0)

		if not message:
			message = httpstatus.phrase

		ret = {'status' : {\
				'code' : httpstatus.value,\
				'message' : message,\
				'found' : found,\
				'time_ms' : time_ms}}

		if param.get('payload'):
			ret['payload'] = param.get('payload')

			if found == 0:
				ret['payload'] = len(param.get('payload'))

		if param.get('error_dict'):
			ret['error'] = param.get('error_dict')

		# todo
		uri = ''

		# response ok (code: ok, no_content, redirect, ... )
		if ret['status']['code'] < 400:
			log.info('response %s%s: code=%s, ret=%s',\
				(self.server_name, uri, httpstatus.value, ret), 3)

		# response error (code: bad_request, not found, ... )
		elif ret['status']['code'] >= 400 and ret['status']['code'] < 500:
			log.error('response %s%s: code=%s, ret=%s',\
				(self.server_name, uri, httpstatus.value, ret), 3)

		# response fatal/critical (code: server_error, ... )
		else:
			log.critical('response %s%s: code=%s, ret=%s',\
				(self.server_name, uri, httpstatus.value, ret), 3)

		return ret


	# 2xx
	def ok(self, message='', time_ms=0, found=0, payload=()):
		""" 200 OK """

		return self.__response(http.HTTPStatus.OK,\
			{'message':message, 'time_ms':time_ms, 'found':found, 'payload':payload})


	def created(self, message='', time_ms=0, found=0, payload=()):
		""" 201 CREATED """

		return self.__response(http.HTTPStatus.CREATED,\
			{'message':message, 'time_ms':time_ms, 'found':found, 'payload':payload})


	def accepted(self, message='', time_ms=0, found=0, payload=()):
		""" 202 ACCEPTED """

		return self.__response(http.HTTPStatus.ACCEPTED,\
			{'message':message, 'time_ms':time_ms, 'found':found, 'payload':payload})


	def no_content(self, message='', time_ms=0, found=0):
		""" 204 NO CONTENT """

		return self.__response(http.HTTPStatus.NO_CONTENT,\
			{'message':message, 'time_ms':time_ms, 'found':found})


	# 3xx
	def moved_permanently(self, message='', time_ms=0):
		""" 301 MOVED PERMANENTLY """

		return self.__response(http.HTTPStatus.MOVED_PERMANENTLY,\
			{'message':message, 'time_ms':time_ms})


	def found(self, message='', time_ms=0, error_dict=None):
		""" 302 FOUND """

		return self.__response(http.HTTPStatus.FOUND,\
			{'message':message, 'time_ms':time_ms, 'error_dict':error_dict})

	def redirect(self, message='', time_ms=0, error_dict=None):
		""" alias for found() """
		return self.found(message, time_ms, error_dict=error_dict)


	def not_modified(self, message='', time_ms=0):
		""" alias for not_modified() """

		return self.__response(http.HTTPStatus.NOT_MODIFIED,\
			{'message':message, 'time_ms':time_ms})


	# 4xx
	def bad_request(self, message='', time_ms=0, error_dict=None):
		""" 400 Bad request """

		return self.__response(http.HTTPStatus.BAD_REQUEST,\
			{'message':message, 'time_ms':time_ms, 'error_dict':error_dict})

	def unauthorized(self, message='', time_ms=0, error_dict=None):
		""" 401 UNAUTHORIZED """

		return self.__response(http.HTTPStatus.UNAUTHORIZED,\
			{'message':message, 'time_ms':time_ms, 'error_dict':error_dict})

	def unauth(self, message='', time_ms=0, error_dict=None):
		""" alias for unauthorized() """
		return self.unauthorized(message, time_ms, error_dict=error_dict)


	def bad_forbidden(self, message='', time_ms=0, error_dict=None):
		""" 403 FORBIDDEN """

		return self.__response(http.HTTPStatus.FORBIDDEN,\
			{'message':message, 'time_ms':time_ms, 'error_dict':error_dict})


	def not_found(self, message='', time_ms=0, error_dict=None):
		""" 404 Not found """

		return self.__response(http.HTTPStatus.NOT_FOUND,\
			{'message':message, 'time_ms':time_ms, 'error_dict':error_dict})


	# 5xx
	def internal_server_error(self, message='', time_ms=0):
		""" 500 INTERNAL SERVER ERROR """

		return self.__response(http.HTTPStatus.INTERNAL_SERVER_ERROR,\
			{'message':message, 'time_ms':time_ms})

	def server_error(self, message='', time_ms=0):
		""" alias for internal_server_error() """
		return self.internal_server_error(message, time_ms)

	def server_err(self, message='', time_ms=0):
		""" alias for internal_server_error() """
		return self.internal_server_error(message, time_ms)


	# swagger
	def swagger(self, response):
		""" swagger response """

		ret = {}
		if not response:
			return ret

		for status in response:

			payload = None
			error = None
			if response[status]:
				payload = response[status].get('payload')
				error = response[status].get('error')

			if status == 'bad_request' and not error:
				error = {'message': 'param_name: expected str, string must be input',\
					'type': 'type_error'}

			(code, response_data) = self.__swagger(status, payload, error)
			ret[code] = response_data

		return ret


	def __swagger(self, status='OK', payload=None, error=None):
		""" swagger response status """

		self._pylint_fixed = 1

		# alias
		alias = {'UNAUTH': 'UNAUTHORIZED',\
			'SERVER_ERR': 'INTERNAL_SERVER_ERROR',\
			'SERVER_ERROR': 'INTERNAL_SERVER_ERROR'}

		# status enum name
		status_upper = status.upper()
		status_upper = alias.get(status_upper, status_upper)
		httpstatus = http.HTTPStatus[status_upper]
		found = 0

		if status_upper == 'OK':
			found = 1

		# http response
		ret = {'status' : {\
			'code' : httpstatus.value,\
			'message' : httpstatus.phrase,\
			'found' : found,\
			'time_ms' : 1}}

		if payload:
			ret['payload'] = payload

		if error:
			ret['error'] = error

		# swagger response
		responses = {'description': httpstatus.name,\
			'examples': {'application/json': ret}}

		return str(httpstatus.value), responses


if __name__ == '__main__':

	import pprint

	RESPONSE = ResponseAPI()
	pprint.pprint(RESPONSE.ok(found=10, time_ms=20))
	pprint.pprint(RESPONSE.redirect(time_ms=30))
	pprint.pprint(RESPONSE.bad_request(time_ms=40))
	pprint.pprint(RESPONSE.not_found(time_ms=50))

	pprint.pprint(RESPONSE.server_err(time_ms=60))
	pprint.pprint(RESPONSE.server_error(time_ms=60))

	print()
	print('response')
	pprint.pprint(RESPONSE.swagger({\
		'ok': {'payload':{'id':1}},\
		'bad_request': None,\
		'NOT_FOUND': '',\
		'SERVER_ERR': {},\
	}))
