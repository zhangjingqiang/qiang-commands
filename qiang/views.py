from django.shortcuts import render

from qiang.models import Command

def index(request):
	latest_command_list = Command.objects.all()
	context = {'latest_command_list': latest_command_list}
	return render(request, 'qiang/index.html', context)