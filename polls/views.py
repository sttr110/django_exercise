#from django.shortcuts import render
#from django.template import Context, loader
#from django.http import HttpResponse
from polls.models import Poll
from django.shortcuts import render_to_response, get_object_or_404

def index(request):
  polls = Poll.objects.all()
  return render_to_response('polls/index.html', {'polls': polls})

def detail(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    return render_to_response('polls/detail.html', {'poll': p})


  #try:
  #  p = Poll.objects.get(pk=poll_id)
  #except Poll.DoesNotExist:
  #  raise Http404


  #t = loader.get_template('polls/index.html')
  #c = Context({
  #  'polls': polls, 
  #})
  #return HttpResponse(t.render(c))

