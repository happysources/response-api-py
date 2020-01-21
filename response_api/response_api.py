#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Response API

HTTPStatus:
https://docs.python.org/3/library/http.html
"""

import http


def _response(httpstatus, message='', time_ms=0, found=0, data=[], error_dict={}):
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
def response_ok(message='', time_ms=0, found=0, data=[]):
	""" response 200 OK """
	return _response(http.HTTPStatus.OK, message, time_ms, found, data)

def response_created(message='', time_ms=0, found=0, data=[]):
	""" response 201 CREATED """
	return _response(http.HTTPStatus.CREATED, message, time_ms, found, data)

def response_accepted(message='', time_ms=0, found=0, data=[]):
	""" response 202 ACCEPTED """
	return _response(http.HTTPStatus.ACCEPTED, message, time_ms, found, data)

def response_no_content(message='', time_ms=0, found=0):
	""" response 204 NO CONTENT """
	return _response(http.HTTPStatus.NO_CONTENT, message, time_ms, found)

# 3xx
def response_moved_permanently(message='', time_ms=0):
	""" response 301 MOVED PERMANENTLY """
	return _response(http.HTTPStatus.MOVED_PERMANENTLY, message, time_ms)

def response_found(message='', time_ms=0):
	""" response 302 FOUND """
	return _response(http.HTTPStatus.FOUND, message, time_ms)

def response_redirect(message='', time_ms=0):
	""" alias for response_found() """
	return response_found(message, time_ms)

# 4xx
def response_bad_request(message='', time_ms=0, error_dict={}):
	""" response 400 Bad request """
	return _response(http.HTTPStatus.BAD_REQUEST, message, time_ms, error_dict=error_dict)

def response_unauthorized(message='', time_ms=0):
	""" response 401 UNAUTHORIZED """
	return _response(http.HTTPStatus.UNAUTHORIZED, message, time_ms)

def response_unauth(message='', time_ms=0):
	""" alias for response_unauthorized() """
	return response_unauthorized(message, time_ms)

def response_bad_forbidden(message='', time_ms=0):
	""" response 403 FORBIDDEN """
	return _response(http.HTTPStatus.FORBIDDEN, message, time_ms)

def response_not_found(message='', time_ms=0):
	""" response 404 Not found """
	return _response(http.HTTPStatus.NOT_FOUND, message, time_ms)


# 5xx
def response_internal_server_error(message='', time_ms=0):
	""" response 500 INTERNAL SERVER ERROR """
	return _response(http.HTTPStatus.INTERNAL_SERVER_ERROR, message, time_ms)

def response_server_error(message='', time_ms=0):
	""" alias for response_internal_server_error() """
	return response_internal_server_error(message, time_ms)

def response_server_err(message='', time_ms=0):
	""" alias for response_internal_server_error() """
	return response_internal_server_error(message, time_ms)


if __name__ == '__main__':

	import pprint

	pprint.pprint(response_ok(found=10, time_ms=20))
	pprint.pprint(response_redirect(time_ms=30))
	pprint.pprint(response_bad_request(time_ms=30))
	pprint.pprint(response_not_found(time_ms=30))
	pprint.pprint(response_server_err(time_ms=30))
