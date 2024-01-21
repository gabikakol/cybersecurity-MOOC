from django.shortcuts import render, redirect

from .models import questions

def find_topic(tid):
	for q in questions:
		if q['id'] == tid:
			return q
	return None


def quizView(request, tid):
	topic = find_topic(tid)

	request.session['level'] = 0
	return render(request, 'pages/question.html', {'topic' : topic, 'question' : topic['questions'][0]})



def answerView(request, tid, aid):
	if (request.session['tid'] != tid or request.session['over']):
		return redirect('/cheater')
			
	topic = find_topic(tid)

	level = request.session['level']

	if topic['questions'][level]['correct'] == aid:
		level += 1
		request.session['level'] = level

		if level == len(topic['questions']):
			request.session['over'] = True
			return redirect('/finish/')

		return render(request, 'pages/question.html', {'topic' : topic, 'question' : topic['questions'][level]})
	else:
		return redirect('/incorrect/')


def incorrectView(request):
	request.session['over'] = True
	return render(request, 'pages/incorrect.html')


def finishView(request):
	try:
		if (request.session['over']):
			return render(request, 'pages/finish.html')
		else:
			return redirect('/cheater')
	except:
		return redirect('/cheater')


def cheaterView(request):
	return render(request, 'pages/cheater.html')


def thanksView(request):
	# Like we were going to pay anyone
	return render(request, 'pages/thanks.html')



def topicView(request, tid):
	request.session['tid'] = tid
	topic = find_topic(tid)
	return render(request, 'pages/topic.html', {'topic' : topic})


def topicsView(request):
	request.session['over'] = False
	return render(request, 'pages/topics.html', {'questions' : questions})