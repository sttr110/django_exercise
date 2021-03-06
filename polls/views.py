#from django.shortcuts import render
#from django.template import Context, loader
#from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from polls.models import Choice, Poll
from django.template import RequestContext

def index(request):
  polls = Poll.objects.all()
  return render_to_response('polls/index.html', {'polls': polls})

def detail(request, poll_id):
  p = get_object_or_404(Poll, pk=poll_id)
  return render_to_response('polls/detail.html', {'poll': p}, context_instance=RequestContext(request))

def vote(request, poll_id):
  p = get_object_or_404(Poll, pk=poll_id)
  try:
    selected_choice=p.choice_set.get(pk=request.POST['choice'])
  except (KeyError, Choice.DoesNotExist):
    return render_to_response('polls/detail.html', {
        'poll': p,
        'error_message': "you not selected",
    }, context_instance=RequestContext(request))
  else:
    selected_choice.votes += 1
    selected_choice.save()
    return HttpResponseRedirect(reverse('polls.views.results', args=(p.id,)))

def results(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    return render_to_response('polls/results.html', {'poll': p})
