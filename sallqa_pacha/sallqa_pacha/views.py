from django.shortcuts import render
from django.views.generic import CreateView
from apps.objetivosonu.models import Comment
from apps.objetivosonu.forms import CommentForm
from django.urls import reverse_lazy

def Inicio(request):
	return render(request,'inicio.html')

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'

    def form_valid(self,form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)


    success_url = reverse_lazy('inicio')
   




