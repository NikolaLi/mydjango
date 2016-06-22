from django.template import Template, Context
from django.http import HttpResponse
import datetime

def hello(request):
    return HttpResponse("Hello world")

# def current_datetime(request):
#     now = datetime.datetime.now()
#     html = "<html><body>It is now %s.</body></html>" % now
#     return HttpResponse(html)

# def current_datetime(request):
# 	now = datetime.datetime.now()
# 	fp = open("mytemplate.html")
# 	t = Template(fp.read())
# 	fp.close()
# 	html = t.render(Context({'current_date':now}))
# 	return HttpResponse(html)

def current_datetime(request):
	now = datetime.datetime.now()
	return render_to_response('current_datetime.html', {'current_date': now})