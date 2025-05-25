from django.shortcuts import render
from django.views import View

class IndexView(View):
    def get(self, request):
        message="ようこそ日記アプリへ！"
        return render(request, 'diary/index.html', {"message": message})
    
index = IndexView.as_view()

# Create your views here.
