from django.shortcuts import render,redirect
from .models import FileModel
from .forms import FileForm

# Create your views here.
def home(request):
	data=FileModel.objects.all()
	print(data)
	return render(request,'home.html',{'data':data})

def create(request):
	if request.method=="POST":
		f=FileForm(request.POST,request.FILES)
		if f.is_valid():
			f.save()
			fm=FileForm()
			return render(request,'create.html',{'fm':fm,'msg':'record added'})
		else:
			return render(request,'create.html',{'fm':f,'msg':'check error'})
	else:
		fm=FileForm()
		return render(request,'create.html',{'fm':fm})

def delete(request,id):
	d=FileModel.objects.get(rno=id)
	d.delete()
	return redirect(home)
