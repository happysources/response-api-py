#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Response API

HTTPStatus:
https://docs.python.org/3/library/http.html
"""

import http

class ResponseAPI(object):
	""" ResponseAPI object """

	_pylint_fixed = 0

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

		if param.get('data'):
			ret['data'] = param.get('data')

			if found == 0:
				ret['data'] = len(param.get('data'))

		if param.get('error_dict'):
			ret['error'] = param.get('error_dict')

		return ret


	# 2xx
	def ok(self, message='', time_ms=0, found=0, data=()):
		""" 200 OK """

		return self.__response(http.HTTPStatus.OK,\
			{'message':message, 'time_ms':time_ms, 'found':found, 'data':data})


	def created(self, message='', time_ms=0, found=0, data=()):
		""" 201 CREATED """

		return self.__response(http.HTTPStatus.CREATED,\
			{'message':message, 'time_ms':time_ms, 'found':found, 'data':data})


	def accepted(self, message='', time_ms=0, found=0, data=()):
		""" 202 ACCEPTED """

		return self.__response(http.HTTPStatus.ACCEPTED,\
			{'message':message, 'time_ms':time_ms, 'found':found, 'data':data})


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



if __name__ == '__main__':

	import pprint

	RESPONSE = ResponseAPI()
	pprint.pprint(RESPONSE.ok(found=10, time_ms=20))
	pprint.pprint(RESPONSE.redirect(time_ms=30))
	pprint.pprint(RESPONSE.bad_request(time_ms=40))
	pprint.pprint(RESPONSE.not_found(time_ms=50))

	pprint.pprint(RESPONSE.server_err(time_ms=60))
	pprint.pprint(RESPONSE.server_error(time_ms=60))
