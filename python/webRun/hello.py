
def application(environ, start_response):
	d = start_response('200 ok', [('Content-Type', 'text/html')])
	print(d)
	print('---------------------')
	print(environ)
	print('=====================================')
	print(start_response)
	
	body = '<h1>hello, %s</h1>' % (environ['PATH_INFO'][1:]or 'web')

	return [body.encode('utf-8')]


