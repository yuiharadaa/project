from django.shortcuts import render, redirect
from django.views import View
from .forms import PageForm

class IndexView(View):
    def get(self, request):
        message="ようこそ日記アプリへ！"
        return render(request, 'diary/index.html', {"message": message})

class PageCreateView(View):
    def get(self, request):
        form = PageForm()
        return render(request, 'diary/page_form.html', {'form': form})
       
    def post(self, request):
        form = PageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("diary:index")
        return render(request, 'diary/page_form.html', {'form': form})

index = IndexView.as_view()
page_create = PageCreateView.as_view()

# Create your views here.
