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

	def __response(self, httpstatus, message='', time_ms=0, found=0, data=[], error_dict=None):
		""" structure for body response """

		if not message:
			message = httpstatus.phrase

		ret = {'status' : {\
				'code' : httpstatus.value,\
				'message' : message,\
				'found' : found,\
				'time_ms' : time_ms}}

		if data:
			ret['data'] = data

			if found == 0:
				ret['data'] = len(data)

		if error_dict:
			ret['error'] = error_dict

		return ret

	# 2xx
	def ok(self, message='', time_ms=0, found=0, data=[]):
		""" response 200 OK """
		return self.__response(http.HTTPStatus.OK, message, time_ms, found, data)

	def created(self, message='', time_ms=0, found=0, data=[]):
		""" response 201 CREATED """
		return self.__response(http.HTTPStatus.CREATED, message, time_ms, found, data)

	def accepted(self, message='', time_ms=0, found=0, data=[]):
		""" response 202 ACCEPTED """
		return self.__response(http.HTTPStatus.ACCEPTED, message, time_ms, found, data)

	def no_content(self, message='', time_ms=0, found=0):
		""" response 204 NO CONTENT """
		return self.__response(http.HTTPStatus.NO_CONTENT, message, time_ms, found)

	# 3xx
	def moved_permanently(self, message='', time_ms=0):
		""" response 301 MOVED PERMANENTLY """
		return self.__response(http.HTTPStatus.MOVED_PERMANENTLY, message, time_ms)

	def found(self, message='', time_ms=0, error_dict=None):
		""" response 302 FOUND """
		return self.__response(http.HTTPStatus.FOUND, message, time_ms, error_dict=error_dict)

	def redirect(self, message='', time_ms=0):
		""" alias for found() """
		return self.found(message, time_ms)

	def not_modified(self, message='', time_ms=0):
		""" alias for not_modified() """
		return self.__response(http.HTTPStatus.NOT_MODIFIED, message, time_ms)

	# 4xx
	def bad_request(self, message='', time_ms=0, error_dict=None):
		""" response 400 Bad request """
		return self.__response(http.HTTPStatus.BAD_REQUEST, message, time_ms, error_dict=error_dict)

	def unauthorized(self, message='', time_ms=0):
		""" response 401 UNAUTHORIZED """
		return self.__response(http.HTTPStatus.UNAUTHORIZED, message, time_ms)

	def unauth(self, message='', time_ms=0):
		""" alias for unauthorized() """
		return self.unauthorized(message, time_ms)

	def bad_forbidden(self, message='', time_ms=0):
		""" response 403 FORBIDDEN """
		return self.__response(http.HTTPStatus.FORBIDDEN, message, time_ms)

	def not_found(self, message='', time_ms=0, error_dict=None):
		""" response 404 Not found """
		return self.__response(http.HTTPStatus.NOT_FOUND, message, time_ms, error_dict=error_dict)


	# 5xx
	def internal_server_error(self, message='', time_ms=0):
		""" response 500 INTERNAL SERVER ERROR """
		return self.__response(http.HTTPStatus.INTERNAL_SERVER_ERROR, message, time_ms)

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
	pprint.pprint(RESPONSE.bad_request(time_ms=30))
	pprint.pprint(RESPONSE.not_found(time_ms=30))
	pprint.pprint(RESPONSE.server_err(time_ms=30))
