from django.shortcuts import render,redirect
from . forms import Usreg,Uppfle,NeFld,Cn,Un
import random
from . models import Creatnote

# Create your views here.

def home(request):
	return render(request,'html/home.html')

def registration(request):
	if request.method == "POST":
		t = Usreg(request.POST)
		if t.is_valid():
			t.save()
			return redirect('/login')
	t = Usreg() 
	return render(request,'html/register.html',{'y':t})

def dashboard(request):
	return render(request,'html/dashboard.html')

def profile(request):
	return render(request,'html/profile.html')

def updateprf(request):
	if request.method == "POST":
		u = Uppfle(request.POST,instance=request.user)
		d = NeFld(request.POST,request.FILES,instance=request.user.updext)
		if u.is_valid() and d.is_valid():
			u.save()
			d.save()
			return redirect('/prfl')
	u = Uppfle(instance=request.user)
	d = NeFld(instance=request.user.updext)
	return render(request,'html/updpfle.html',{'m':u,'t':d})


def creatnt(request):
	if request.method =="POST":
		t=Cn(request.POST,request.FILES)
		if t.is_valid():
			m = t.save(commit=False)
			m.created_by = request.user.username
			m.generatekey = random.randrange(1,9999999999)
			m.s_id = request.user.id			
			# print(m.generatekey,m.title,m.s_id,m.created_by)
			m.save()
			return redirect('/vwn')
	t=Cn()
	return render(request,'html/creatnote.html',{'a':t})

def viewnote(request):
	z = Creatnote.objects.filter(s_id=request.user.id)
	return render(request,'html/viewnotedata.html',{'r':z})

def updnt(request,pk):
	sa = Creatnote.objects.get(id=pk)
	if request.method == "POST":
		q = Un(request.POST,request.FILES,instance=sa)
		if q.is_valid():
			q.save()
			return redirect("/vwn")
	q = Un(instance=sa)
	return render(request,'html/updatenote.html',{'p':q})
	
def delnt(request,dr):
	b = Creatnote.objects.get(id=dr)
	if request.method == "POST":
		b.delete()
		return redirect('/vwn')
	return render(request,"html/deletenotes.html",{'t':b})
	