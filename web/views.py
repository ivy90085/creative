from web.models import Message

def board(request):
        messages = Message.objects.all()
        response_string = "<a href='/post'>Post</a><hr/>"
        response_string += '<br/>'.join(["user: %s, subject: %s, time: %s" % (q.user, q.subject, q.publication_date) for q in messages])
        return HttpResponse(response_string)