from django.views.generic import View
from django.shortcuts import get_object_or_404, render

class Index(View):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name)