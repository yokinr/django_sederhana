from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from .models import ModelName
from .forms import *
# from rest_framework.pagination import PageNumberPagination


class ModelNameListView(ListView):
    model = ModelName
    template_name = 'model_name_list.html'
    queryset = ModelName.objects.all()
    context_object_name = "items"
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Daftar Artikel'
        return context


class ModelNameDetailView(DetailView):
    model = ModelName
    template_name = "model_name_detail.html"
    context_object_name = "item"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Detail Artikel'
        return context


class ModelNameCreateView(CreateView):
    model = ModelName
    form_class = MyModelForm
    template_name = 'model_name_create.html'
    success_url = '.'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Artikel Baru'
        return context


class ModelNameUpdateView(UpdateView):
    model = ModelName
    form_class = MyModelForm
    template_name = 'model_name_update.html'
    success_url = '..'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update Artikel'
        return context


class ModelNameDeleteView(DeleteView):
    model = ModelName
    template_name = 'model_name_delete.html'
    success_url = '..'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Hapus Artikel'
        return context
