from typing import Any
from django.views.generic import View, DetailView, UpdateView
from django.shortcuts import get_object_or_404, render, redirect
from .models import Feed
from django.urls import reverse_lazy
from .forms import *

class Index(View):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name)

class TagStudy(View):
    template_name = 'tag_study.html'

    def get(self, request):
        feeds = Feed.objects.all().order_by('id')
        return render(
            request, 
            self.template_name,
            {'feed_list':feeds}
            )

class NewContent(View):
    template_name = 'upload_form.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        
        param = request.POST.get('content', '')
        print("전달받은 내용:" + param)
        param2 = request.FILES.get('up_photo', False)

        feed = Feed(content=param, photo =param2)
        feed.save()
        return redirect('edu:tag_study')
    
class FeedDetail(DetailView):
    template_name = "feed/detail.html"
    model = Feed

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        feed = get_object_or_404(Feed, pk = self.kwargs['pk'])
        context['feed'] = feed
        return context
    
class FeedUpdate(UpdateView):
    model = Feed
    template_name = "feed/update.html"
    form_class = FeedForm

    def get_object(self):
        return get_object_or_404(Feed, pk = self.kwargs['pk'])
    
    def get_success_url(self):
        return reverse_lazy('edu:feed_detail', args = (self.object.id,))