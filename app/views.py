from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
   return render(request, 'index.html')
def text(request):
   # Get the text
   data = request.POST.get('text','default')

   #check the checkbox value
   checkbox = request.POST.get('removepunc','off')
   capitalize = request.POST.get('capitalize','off')
   length = request.POST.get('charcount','off')
   lineremover =  request.POST.get('lineremover','off')
  
  #check which checkbox is on
   if checkbox =='on':
      punctuations    = '''!()-[];:'"\,<>./?@#$%^&*_~'''
      analyze = ''
      for char in data:
         if char not in punctuations:
            analyze = analyze + char
      param = {'type':'text analyzer','try':analyze}
      data = analyze   
   if(capitalize == 'on'):
      for char in data:
         analyze = ''
         analyze = analyze + data.upper()
      param = {'type':'text capitalizer','try':analyze}
      data = analyze
      # return render(request,'analyze.html',param)
   if(length=='on'):
      count = len(data)
      param = {'type':'length of your','try':count}
      
      # return render(request,'analyze.html',param)
   if(lineremover == 'on'):
      analyze = ''
      for char in data:
         if char != '\n' and char!= '\r':
            analyze = analyze + char
      param = {'type':'line removed','try':analyze}
      # return render(request,'analyze.html',param)
   if(checkbox !='on' and capitalize != 'on' and length !='on' and lineremover != 'on' ):
      return HttpResponse('Please select any operator')

   return render(request,'analyze.html',param)