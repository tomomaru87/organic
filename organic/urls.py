from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.decorators import login_required
from account import views
from django.views.generic import TemplateView

# 実はページを表示するだけならこのように1行で書くことが出来ます。
index_view = TemplateView.as_view(template_name="registration/index.html")

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("account/", login_required(index_view), name="index"),
    path('',include('account.urls')),

   

]