from django.shortcuts import render
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

# list of default notes
myNotes=[
    {'title':"Title",
    'content':'Content',
    'id':1,},
    ]
    # return all notes
def notes(request):
    return JsonResponse({
        'status':200,
        'data':myNotes,
    } , content_type='application/json')


# add new note
@csrf_exempt
def addNote(request):
        if myNotes.__len__()==0:
            noteID=1
        else :
            noteID=myNotes[-1]['id']+1
        if(request.method=='POST'):
            body=json.loads(request.body)
            newNote={
            'title':body['title'],
            'content':body['content'],
            'id':noteID
            }
            myNotes.append(newNote)
            return JsonResponse({'status':200,
            'data':newNote
            })
        else :
            return JsonResponse({'status':405}
        )
@csrf_exempt
def deleteNote(request):
    idnum=json.loads(request.body)['id']
    for note in myNotes:
        if note['id']==idnum:
            myNotes.remove(note)
            break
    return JsonResponse({
        'status':200,
        'data':'note has been deleted',
    })
def e(request):
    pass 