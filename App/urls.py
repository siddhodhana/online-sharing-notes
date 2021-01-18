from django.urls import path
from App import views
from django.contrib.auth import views as v

urlpatterns = [
	path("",views.home,name="hm"),
	path("reg/",views.registration,name="rg"),
	path("ds/",views.dashboard,name="dsh"),
	path("prfl/",views.profile,name="pf"),
	path("upfl/",views.updateprf,name="upf"),
	path("login/",v.LoginView.as_view(template_name="html/login.html"),name="lg"),
	path("logout/",v.LogoutView.as_view(template_name="html/logout.html"),name="lgo"),
	path("creat/",views.creatnt,name="cn"),
	path("vwn/",views.viewnote,name="vw"),
	path("updnt/<int:pk>/",views.updnt,name="updn"),
	path("delt/<int:dr>/",views.delnt,name="del"),
	]


