from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["produto_list"] = Produto.objects.all().order_by("-id")
        return context


class TodosProdutoView(TemplateView):
    template_name = "todosprodutos.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["todocategorias"] = Categoria.objects.all()
        return context


class ProdutoDetalheView(TemplateView):
    template_name = "produtodetalhe.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        url_slug = self.kwargs["slug"]
        produto = Produto.objects.get(slug=url_slug)
        produto.visualizacao += 1
        produto.save()
        context["produto"] = produto
        return context


class AddCarroView(TemplateView):
    template_name = "addprocarro.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        produto_id = self.kwargs["pro_id"]
        produto_obj = Produto.objects.get(id=produto_id)
        carro_id = self.request.session.get("carro_id", None)
        if carro_id:
            carro_obj = Carro.objects.get(id=carro_id)
            produto_no_carro = carro_obj.carroproduto_set.filter(produto=produto_obj)

            if produto_no_carro.exists():
                carroproduto = produto_no_carro.last()
                carroproduto.quantidade += 1
                carroproduto.subtotal += produto_obj.venda
                carroproduto.save()
                carro_obj.total += produto_obj.venda
                carro_obj.save()
            else:
                carroproduto = CarroProduto.objects.create(
                    carro=carro_obj,
                    produto=produto_obj,
                    avaliacao=produto_obj.venda,
                    quantidade=1,
                    subtotal=produto_obj.venda,
                )
                carro_obj.total += produto_obj.venda
                carro_obj.save()

        else:
            carro_obj = Carro.objects.create(total=0)
            self.request.session["carro_id"] = carro_obj.id
            carroproduto = CarroProduto.objects.create(
                carro=carro_obj,
                produto=produto_obj,
                avaliacao=produto_obj.venda,
                quantidade=1,
                subtotal=produto_obj.venda,
            )
            carro_obj.total += produto_obj.venda
            carro_obj.save()
        return context


class MeuCarroView(TemplateView):
    template_name = "meucarro.html"


class SobreView(TemplateView):
    template_name = "sobre.html"


class ContatoView(TemplateView):
    template_name = "contato.html"
