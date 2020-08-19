from django.shortcuts import render 
from django.http import HttpResponse
from .models import tracking
from .models import day
from django.core.files.storage import FileSystemStorage
from .models import companytable
from .models import akash
from .models import vehicle
from .models import single
from .models import person
from .models import driver
import csv,os
from django.conf import settings

def index(request):
	if request.method == 'POST':
		obj=tracking()
		obj.usertype=request.POST.get("usertype");
		obj.email=request.POST.get("email");
		obj.password=request.POST.get("password");
		obj.contact=request.POST.get("contact");
		obj.save()
		context={'msg':"Record is saved"}
		return render(request,'gps/welcome.html',context)
	else:
		return render(request,'gps/index.html')
			
def welcome (request):
	return render(request,'gps/welcome.html')				
def showRecords(request):
	objs=tracking.objects.all();
	return render(request,'gps/showRecords.html',{'records':objs})
def Add_Vehicles(request):
	if request.method == 'POST'and request.FILES['vehiclephoto']:
		myfile = request.FILES['vehiclephoto']
		fs = FileSystemStorage()
		filename = fs.save(myfile.name, myfile)
		uploaded_file_url = fs.url(filename)
		obj=vehicle()
		obj.vehnumber=request.POST.get("vehnumber");
		obj.brand=request.POST.get("brand");
		obj.modnumber=request.POST.get("modnumber");
		obj.permitdate=request.POST.get("permitdate");
		obj.licensen=request.POST.get("licensen");
		obj.averg=request.POST.get("averg");
		obj.rc=request.POST.get("rc");
		obj.tank=request.POST.get("tank");
		obj.transp=request.POST.get("transp");
		obj.dnumber=request.POST.get("dnumber");
		obj.email=request.POST.get("email");
		obj.pword=request.POST.get("pword");
		obj.pic=uploaded_file_url
		obj.save()
		context={'msg':"Record is saved"}
		return render(request,'admin/msgpage.html',context)
	else:
		return render(request,'admin/Add_Vehicles.html')	






def about(request):
	return render(request,"gps/about.html")
def contact(request):
	return render(request,"gps/contact.html")
def services(request):
	return render(request,"gps/services.html")
def registratio(request):
	return render(request,"gps/registratio.html")	
def adminindex(request):
	return render(request,"admin/adminindex.html")
def login(request):
	if request.method =='POST':
		i=int(request.POST.get("id"))
		p=request.POST.get("pword")
		objs=single.objects.filter(id=i,pword=p)
		if objs:
			obj=single.objects.get(id=i)
			return render (request,'admin/adminindex.html',{'name':obj.name,'pic':obj.pic})
		else:
			return render (request,'gps/login.html',{'msg':'your id or password is wrong'})
	else:
		return render(request,"gps/login.html")

def Add_Person_for_Tracking(request):
	if request.method == 'POST' and request.FILES['myfile']:
		myfile = request.FILES['myfile']
		fs=FileSystemStorage()
		filename = fs.save(myfile.name,myfile)
		uploaded_file_url = fs.url(filename)
		obj=day()
		obj.name=request.POST.get("name");
		obj.fatherName=request.POST.get("fatherName");
		obj.email=request.POST.get("email");
		obj.birthDate=request.POST.get("birthDate");
		obj.mobilenumber=request.POST.get("mobilenumber");
		obj.gender=request.POST.get("gender");
		obj.email=request.POST.get("email");
		obj.address=request.POST.get("address");
		obj.idproof=request.POST.get("idproof");
		obj.idno=request.POST.get("idno");
		obj.pic=uploaded_file_url
		obj.save()
		context={'msg':"Record is saved"}
		return render(request,"admin/msgpage.html",context)
	else:
		return render(request,"admin/Add_Person_for_Tracking.html")
def showtable(request):
    
    objs=day.objects.all()
    return render(request,'admin/showtable.html',{'records':objs})

def Add_Single_Client(request):
	if request.method == 'POST' and request.FILES['myfile']:
		myfile = request.FILES['myfile']
		fs=FileSystemStorage()
		filename = fs.save(myfile.name,myfile)
		uploaded_file_url = fs.url(filename)
		obj=single()
		obj.name=request.POST.get("name");
		obj.fatherName=request.POST.get("fatherName");
		obj.email=request.POST.get("email");
		obj.pword=request.POST.get("pword");
		obj.birthDate=request.POST.get("birthDate");
		obj.mobilenumber=request.POST.get("mobilenumber");
		obj.gender=request.POST.get("gender");
		obj.email=request.POST.get("email");
		obj.address=request.POST.get("address");
		obj.idproof=request.POST.get("idproof");
		obj.idno=request.POST.get("idno");
		obj.pic=uploaded_file_url
		obj.save()
		context={'msg':"Record is saved"}
		return render(request,"admin/msgpage.html",context)
	else:
		return render(request,"admin/Add_Single_Client.html")

def View_Single_Client(request):
	objs=single.objects.all();
	return render(request,"admin/View_Single_Client.html",{'records':objs})		
def Add_Transport_Company(request):
	if request.method == 'POST'and request.FILES['myfile']:
		myfile = request.FILES['myfile']
		fs = FileSystemStorage()
		filename = fs.save(myfile.name, myfile)
		uploaded_file_url = fs.url(filename)
		obj=akash()
		obj.comname=request.POST.get("comname");
		obj.drname=request.POST.get("drname");
		obj.Dateesbh=request.POST.get("Dateesbh");
		obj.email=request.POST.get("email");
		obj.mobilenumber=request.POST.get("mobilenumber");
		obj.address=request.POST.get("address");
		obj.regidno=request.POST.get("regidno");
		obj.gstnumber=request.POST.get("gstnumber");
		obj.licensenumber=request.POST.get("licensenumber");
		obj.vnumber=request.POST.get("vnumber");
		obj.pword=request.POST.get("pword");
		obj.pic=uploaded_file_url
		obj.save()
		context={'msg':"Record is saved"}
		return render(request,'admin/msgpage.html',context)
	else:
		return render(request,'admin/Add_Transport_Company.html')
def View_All_Transport_Company(request):
	objs=akash.objects.all();
	return render(request,"admin/View_All_Transport_Company.html",{'records':objs})
def View_All_Vehicles(request):
	objs=vehicle.objects.all();
	return render(request,"admin/View_All_Vehicles.html",{'records':objs})

def logout(request):
	return render(request,"admin/logout.html")
def msgpage(request):
	return render(request,"admin/msgpage.html")
def Add_Person_For_Tracking(request):
	if request.method == 'POST' and request.FILES['myfile']:
		myfile = request.FILES['myfile']
		fs=FileSystemStorage()
		filename = fs.save(myfile.name,myfile)
		uploaded_file_url = fs.url(filename)
		obj=person()
		obj.name=request.POST.get("name");
		obj.fatherName=request.POST.get("fatherName");
		obj.email=request.POST.get("email");
		obj.pword=request.POST.get("pword");
		obj.birthDate=request.POST.get("birthDate");
		obj.mobilenumber=request.POST.get("mobilenumber");
		obj.gender=request.POST.get("gender");
		obj.email=request.POST.get("email");
		obj.address=request.POST.get("address");
		obj.idproof=request.POST.get("idproof");
		obj.idno=request.POST.get("idno");
		obj.conone=request.POST.get("conone");
		obj.contwo=request.POST.get("contwo");
		obj.conthr=request.POST.get("conthr");
		obj.confour=request.POST.get("confour");
		obj.policenumber=request.POST.get("policenumber");
		obj.pic=uploaded_file_url
		obj.save()
		context={'msg':"Record is saved"}
		return render(request,"admin/msgpage.html",context)
	else:
		return render(request,"admin/Add_Person_For_Tracking.html")
	
def View_Person(request):
	objs=person.objects.all();
	return render(request,"admin/View_Person.html",{'records':objs})

def delcompanyrecord(request):

	if request.method == 'GET':
		s=int(request.GET.get('uid'))
		obj=akash.objects.get(id=s)
		obj.delete()
		obj=akash.objects.all()
		return render(request,"admin/View_All_Transport_Company",{'objs':obj})

def editcompany(request):
	if request.method == 'GET':
		s=int(request.GET.get('uid'))
		obj=akash.objects.get(id=s)
		return render(request,"admin/editcompany.html",{'obj':obj})

def updatecompanyrecord(request):
	if request.method == 'GET':
		s=int(request.GET.get('uid'))
		obj=akash.objects.get(id=s)
		obj.comname=request.GET.get("comname");
		obj.drname=request.GET.get("drname");
		obj.Dateesbh=request.GET.get("Dateesbh");
		obj.email=request.GET.get("email");
		obj.mobilenumber=request.GET.get("mobilenumber");
		obj.address=request.GET.get("address");
		obj.regidno=request.GET.get("regidno");
		obj.gstnumber=request.GET.get("gstnumber");
		obj.licensenumber=request.GET.get("licensenumber");
		obj.vnumber=request.GET.get("vnumber");
		obj.pword=request.GET.get("pword");
		obj.save()
		obj=akash.objects.all()
		return render(request,"admin/View_All_Transport_Company.html",{'objs':obj})			

def viewcomanyrecord(request):
	if request.method == 'GET':
		s=int(request.GET.get('uid'))
		obj=akash.objects.get(id=s)
		return render(request,"admin/viewcomanyrecord.html",{'obj':obj})

# Create your views here.
                  #  person view tracking------------------------------*/
def deletepersonrecord(request):
	if request.method == 'GET':
		s=int(request.GET.get('uid'))
		obj=person.objects.get(id=s)
		obj.delete()
		obj=person.objects.all()
		return render(request,"admin/View_Person.html",{'objs':obj})
def editpersonrecord(request):
	if request.method == 'GET':
		s=int(request.GET.get('uid'))
		obj=person.objects.get(id=s)
		return render(request,"admin/editpersonrecord.html",{'obj':obj})

def updatepersonrecord(request):
	if request.method == 'GET':
		s=int(request.GET.get('uid'));
		obj=person.objects.get(id=s)
		obj.name=request.GET.get("name");
		obj.fatherName=request.GET.get("fatherName");
		obj.email=request.GET.get("email");
		obj.pword=request.GET.get("pword");
		obj.birthDate=request.GET.get("birthDate");
		obj.mobilenumber=request.GET.get("mobilenumber");
		obj.gender=request.GET.get("gender");
		obj.email=request.GET.get("email");
		obj.address=request.GET.get("address");
		obj.idproof=request.GET.get("idproof");
		obj.idno=request.GET.get("idno");
		obj.conone=request.GET.get("conone");
		obj.contwo=request.GET.get("contwo");
		obj.conthr=request.GET.get("conthr");
		obj.confour=request.GET.get("confour");
		obj.policenumber=request.GET.get("policenumber");
		obj.save()
		obj=person.objects.all()
		return render(request,"admin/View_Person.html",{'objs':obj})

def viewpersonrecord(request):
	if request.method == 'GET':
		s=int(request.GET.get('uid'))
		obj=person.objects.get(id=s)
		return render(request,"admin/viewpersonrecord.html",{'obj':obj})		


#  client view tracking------------------------------*/		
def deleteclientrecord(request):
	if request.method == 'GET':
		s=int(request.GET.get('uid'))
		obj=single.objects.get(id=s)
		obj.delete()
		obj=single.objects.all()
		return render(request,"admin/View_Single_Client",{'objs':obj})
def editclientrecord(request):
	if request.method == 'GET':
		s=int(request.GET.get('uid'))
		obj=single.objects.get(id=s)
		return render(request,"admin/editclientrecord.html",{'obj':obj})
def updateclientrecord(request):
	if request.method == 'GET':
		s=int(request.GET.get('uid'));
		obj=single.objects.get(id=s)
		obj.name=request.GET.get("name");
		obj.fatherName=request.GET.get("fatherName");
		obj.email=request.GET.get("email");
		obj.pword=request.GET.get("pword");
		obj.birthDate=request.GET.get("birthDate");
		obj.mobilenumber=request.GET.get("mobilenumber");
		obj.gender=request.GET.get("gender");
		obj.email=request.GET.get("email");
		obj.address=request.GET.get("address");
		obj.idproof=request.GET.get("idproof");
		obj.idno=request.GET.get("idno");
		obj.save()
		obj=single.objects.all()
		return render(request,"admin/View_Single_Client.html",{'objs':obj})			

def viewclientrecord(request):
	if request.method == 'GET':
		s=int(request.GET.get('uid'))
		obj=single.objects.get(id=s)
		return render(request,"admin/viewclientrecord.html",{'obj':obj})

#  vehicle view tracking------------------------------*/
def deletevehiclerecord(request):
	if request.method == 'GET':
		s=int(request.GET.get('uid'))
		obj=vehicle.objects.get(id=s)
		obj.delete()
		obj=vehicle.objects.all()
		return render(request,"admin/View_All_Vehicles.html",{'objs':obj})

def editvehiclerecord(request):
	if request.method == 'GET':
		s=int(request.GET.get('uid'))
		obj=vehicle.objects.get(id=s)
		return render(request,"admin/editvehiclerecord.html",{'obj':obj})								
def updatevehiclerecord(request):
	if request.method == 'GET':
		s=int(request.GET.get('uid'));
		obj=vehicle.objects.get(id=s)
		obj.vehnumber=request.GET.get("vehnumber");
		obj.brand=request.GET.get("brand");
		obj.modnumber=request.GET.get("modnumber");
		obj.permitdate=request.GET.get("permitdate");
		obj.licensen=request.GET.get("licensen");
		obj.averg=request.GET.get("averg");
		obj.rc=request.GET.get("rc");
		obj.tank=request.GET.get("tank");
		obj.transp=request.GET.get("transp");
		obj.dnumber=request.GET.get("dnumber");
		obj.email=request.GET.get("email");
		obj.pword=request.GET.get("pword");
		obj.save()
		obj=vehicle.objects.all()
		return render(request,"admin/View_All_Vehicles.html",{'objs':obj})

def viewvehiclerecord(request):
	if request.method == 'GET':
		s=int(request.GET.get('uid'))
		obj=vehicle.objects.get(id=s)
		return render(request,"admin/viewvehiclerecord.html",{'obj':obj})

#  gps tracking------------------------------*/

def readcsvfile(request):
	k=[]
	with open(os.path.join(settings.BASE_DIR,'petrol.csv'))as f:
		data = csv.reader(f)
		for row in data:
			k.append(row)
	return render(request,"admin/readcsvfile.html",{'records':k})	
#  Next SIngle login-----------------------------*/		
def singleindex (request):
	return render(request,'single/singleindex.html')
def Add_One_Client (request):
	if request.method == 'POST' and request.FILES['myfile']:
		myfile = request.FILES['myfile']
		fs=FileSystemStorage()
		filename = fs.save(myfile.name,myfile)
		uploaded_file_url = fs.url(filename)
		obj=single()
		obj.name=request.POST.get("name");
		obj.fatherName=request.POST.get("fatherName");
		obj.email=request.POST.get("email");
		obj.pword=request.POST.get("pword");
		obj.birthDate=request.POST.get("birthDate");
		obj.mobilenumber=request.POST.get("mobilenumber");
		obj.gender=request.POST.get("gender");
		obj.email=request.POST.get("email");
		obj.address=request.POST.get("address");
		obj.idproof=request.POST.get("idproof");
		obj.idno=request.POST.get("idno");
		obj.pic=uploaded_file_url
		obj.save()
		context={'msg':"Record is saved"}
		return render(request,"admin/msgpage.html",context)
	else:
		return render(request,'single/Add_One_Client.html')

def View_Client(request):
	objs=single.objects.all();
	return render(request,"single/View_Client.html",{'records':objs})

def deleteclientreco(request):
	if request.method == 'GET':
		s=int(request.GET.get('uid'))
		obj=single.objects.get(id=s)
		obj.delete()
		obj=single.objects.all()
		return render(request,"single/View_Client",{'objs':obj})
def editclientreco(request):
	if request.method == 'GET':
		s=int(request.GET.get('uid'))
		obj=single.objects.get(id=s)
		return render(request,"single/editclientreco.html",{'obj':obj})
def updateclientreco(request):
	if request.method == 'GET':
		s=int(request.GET.get('uid'));
		obj=single.objects.get(id=s)
		obj.name=request.GET.get("name");
		obj.fatherName=request.GET.get("fatherName");
		obj.email=request.GET.get("email");
		obj.pword=request.GET.get("pword");
		obj.birthDate=request.GET.get("birthDate");
		obj.mobilenumber=request.GET.get("mobilenumber");
		obj.gender=request.GET.get("gender");
		obj.email=request.GET.get("email");
		obj.address=request.GET.get("address");
		obj.idproof=request.GET.get("idproof");
		obj.idno=request.GET.get("idno");
		obj.save()
		obj=single.objects.all()
		return render(request,"single/View_Client.html",{'objs':obj})			

def viewclientreco(request):
	if request.method == 'GET':
		s=int(request.GET.get('uid'))
		obj=single.objects.get(id=s)
		return render(request,"single/viewclientreco.html",{'obj':obj})





def Add_Person (request):
	if request.method == 'POST' and request.FILES['myfile']:
		myfile = request.FILES['myfile']
		fs=FileSystemStorage()
		filename = fs.save(myfile.name,myfile)
		uploaded_file_url = fs.url(filename)
		obj=person()
		obj.name=request.POST.get("name");
		obj.fatherName=request.POST.get("fatherName");
		obj.email=request.POST.get("email");
		obj.pword=request.POST.get("pword");
		obj.birthDate=request.POST.get("birthDate");
		obj.mobilenumber=request.POST.get("mobilenumber");
		obj.gender=request.POST.get("gender");
		obj.email=request.POST.get("email");
		obj.address=request.POST.get("address");
		obj.idproof=request.POST.get("idproof");
		obj.idno=request.POST.get("idno");
		obj.conone=request.POST.get("conone");
		obj.contwo=request.POST.get("contwo");
		obj.conthr=request.POST.get("conthr");
		obj.confour=request.POST.get("confour");
		obj.policenumber=request.POST.get("policenumber");
		obj.pic=uploaded_file_url
		obj.save()
		context={'msg':"Record is saved"}
		return render(request,"admin/msgpage.html",context)
	else:
		return render(request,'single/Add_Person.html')
def View__Person(request):
	objs=person.objects.all();
	return render(request,"single/View__Person.html",{'records':objs})


def deletepersonreco(request):
	if request.method == 'GET':
		s=int(request.GET.get('uid'))
		obj=person.objects.get(id=s)
		obj.delete()
		obj=person.objects.all()
		return render(request,"single/View__Person.html",{'objs':obj})
def editpersonreco(request):
	if request.method == 'GET':
		s=int(request.GET.get('uid'))
		obj=person.objects.get(id=s)
		return render(request,"single/editpersonreco.html",{'obj':obj})

def updatepersonreco(request):
	if request.method == 'GET':
		s=int(request.GET.get('uid'));
		obj=person.objects.get(id=s)
		obj.name=request.GET.get("name");
		obj.fatherName=request.GET.get("fatherName");
		obj.email=request.GET.get("email");
		obj.pword=request.GET.get("pword");
		obj.birthDate=request.GET.get("birthDate");
		obj.mobilenumber=request.GET.get("mobilenumber");
		obj.gender=request.GET.get("gender");
		obj.email=request.GET.get("email");
		obj.address=request.GET.get("address");
		obj.idproof=request.GET.get("idproof");
		obj.idno=request.GET.get("idno");
		obj.conone=request.GET.get("conone");
		obj.contwo=request.GET.get("contwo");
		obj.conthr=request.GET.get("conthr");
		obj.confour=request.GET.get("confour");
		obj.policenumber=request.GET.get("policenumber");
		obj.save()
		obj=person.objects.all()
		return render(request,"single/View__Person.html",{'objs':obj})

def viewpersonreco(request):
	if request.method == 'GET':
		s=int(request.GET.get('uid'))
		obj=person.objects.get(id=s)
		return render(request,"single/viewpersonreco.html",{'obj':obj})

		













	
def Add_Vehicle (request):
	if request.method == 'POST'and request.FILES['vehiclephoto']:
		myfile = request.FILES['vehiclephoto']
		fs = FileSystemStorage()
		filename = fs.save(myfile.name, myfile)
		uploaded_file_url = fs.url(filename)
		obj=vehicle()
		obj.vehnumber=request.POST.get("vehnumber");
		obj.brand=request.POST.get("brand");
		obj.modnumber=request.POST.get("modnumber");
		obj.permitdate=request.POST.get("permitdate");
		obj.licensen=request.POST.get("licensen");
		obj.averg=request.POST.get("averg");
		obj.rc=request.POST.get("rc");
		obj.tank=request.POST.get("tank");
		obj.transp=request.POST.get("transp");
		obj.dnumber=request.POST.get("dnumber");
		obj.email=request.POST.get("email");
		obj.pword=request.POST.get("pword");
		obj.pic=uploaded_file_url
		obj.save()
		context={'msg':"Record is saved"}
		return render(request,'admin/msgpage.html',context)
	else:
		return render(request,'single/Add_Vehicle.html')

def View__Vehicle(request):
	objs=vehicle.objects.all();
	return render(request,"single/View__Vehicle.html",{'records':objs})

def deletevehiclere(request):
	if request.method == 'GET':
		s=int(request.GET.get('uid'))
		obj=vehicle.objects.get(id=s)
		obj.delete()
		obj=vehicle.objects.all()
		return render(request,"single/View__Vehicle.html",{'objs':obj})

def editvehiclere(request):
	if request.method == 'GET':
		s=int(request.GET.get('uid'))
		obj=vehicle.objects.get(id=s)
		return render(request,"single/editvehiclere.html",{'obj':obj})								
def updatevehiclere(request):
	if request.method == 'GET':
		s=int(request.GET.get('uid'));
		obj=vehicle.objects.get(id=s)
		obj.vehnumber=request.GET.get("vehnumber");
		obj.brand=request.GET.get("brand");
		obj.modnumber=request.GET.get("modnumber");
		obj.permitdate=request.GET.get("permitdate");
		obj.licensen=request.GET.get("licensen");
		obj.averg=request.GET.get("averg");
		obj.rc=request.GET.get("rc");
		obj.tank=request.GET.get("tank");
		obj.transp=request.GET.get("transp");
		obj.dnumber=request.GET.get("dnumber");
		obj.email=request.GET.get("email");
		obj.pword=request.GET.get("pword");
		obj.save()
		obj=vehicle.objects.all()
		return render(request,"single/View__Vehicle.html",{'objs':obj})

def viewvehiclere(request):
	if request.method == 'GET':
		s=int(request.GET.get('uid'))
		obj=vehicle.objects.get(id=s)
		return render(request,"single/viewvehiclere.html",{'obj':obj})









#  Next SIngle login-----------------------------*/
def transportindex(request):
	return render(request,'transport Company/transportindex.html')
def singlelogin(request):
	if request.method =='POST':
		i=int(request.POST.get("id"))
		p=request.POST.get("pword")
		objs=person.objects.filter(id=i,pword=p)
		if objs:
			obj=person.objects.get(id=i)
			return render (request,'single/singleindex.html',{'name':obj.name,'pic':obj.pic})
		else:
			return render (request,'gps/singlelogin.html',{'msg':'your id or password is wrong'})
	else:
		return render(request,"gps/singlelogin.html")




	return render(request,"gps/singlelogin.html")	
def Track_Vehicles(request):
	return render(request,'transport Company/Track_Vehicles.html')		

def Track_Path_Vehicles(request):
	return render(request,'transport Company/Track_Path_Vehicles.html')
def Search_Vehicles(request):
	return render(request,'transport Company/Search_Vehicles.html')
def Upload_Driver(request):
	if request.method == 'POST' and request.FILES['myfile']:
		myfile = request.FILES['myfile']
		fs=FileSystemStorage()
		filename = fs.save(myfile.name,myfile)
		uploaded_file_url = fs.url(filename)
		obj=driver()
		obj.driverid=request.POST.get("driverid");
		obj.name=request.POST.get("name");
		obj.address=request.POST.get("address");
		obj.email=request.POST.get("email");
		obj.birthDate=request.POST.get("birthDate");
		obj.mobilenumber=request.POST.get("mobilenumber");
		obj.gender=request.POST.get("gender");
		obj.experience=request.POST.get("experience");
		obj.idproof=request.POST.get("idproof");
		obj.idno=request.POST.get("idno");
		obj.pic=uploaded_file_url
		obj.save()
		context={'msg':"Record is saved"}
		return render(request,"admin/msgpage.html",context)
	else:
		return render(request,'transport Company/Upload_Driver.html')




#/end for driver
	
def View_Driver(request):
	objs=driver.objects.all();
	return render(request,"transport Company/View_Driver.html",{'records':objs})

def deletedriverrecord(request):
	if request.method == 'GET':
		s=int(request.GET.get('uid'))
		obj=driver.objects.get(id=s)
		obj.delete()
		obj=driver.objects.all()
		return render(request,"transport Company/View_Driver.html",{'objs':obj})
def editdriverrecord(request):
	if request.method == 'GET':
		s=int(request.GET.get('uid'))
		obj=driver.objects.get(id=s)
		return render(request,"transport Company/editdriverrecord.html",{'obj':obj})
def updatedriverrecord(request):
	if request.method == 'GET':
		s=int(request.GET.get('uid'));
		obj=driver.objects.get(id=s)
		obj.name=request.GET.get("name");
		obj.driverid=request.GET.get("driverid");
		obj.email=request.GET.get("email");
		obj.experience=request.GET.get("experience");
		obj.birthDate=request.GET.get("birthDate");
		obj.mobilenumber=request.GET.get("mobilenumber");
		obj.gender=request.GET.get("gender");
		obj.address=request.GET.get("address");
		obj.idproof=request.GET.get("idproof");
		obj.idno=request.GET.get("idno");
		obj.save()
		obj=driver.objects.all()
		return render(request,"transport Company/View_Driver.html",{'objs':obj})			

def viewdriverrecord(request):
	if request.method == 'GET':
		s=int(request.GET.get('uid'))
		obj=driver.objects.get(id=s)
		return render(request,"transport Company/viewdriverrecord.html",{'obj':obj})







#/end for driver


	
def Upload_Subscription(request):
	return render(request,'transport Company/Upload_Subscription.html')
def Update_Profile(request):
	return render(request,'transport Company/Update_Profile.html')
def companylogin(request):
	if request.method =='POST':
		i=int(request.POST.get("id"))
		p=request.POST.get("pword")
		objs=akash.objects.filter(id=i,pword=p)
		if objs:
			obj=akash.objects.get(id=i)
			return render (request,'transport Company/transportindex.html',{'name':obj.comname,'pic':obj.pic})
		else:
			return render (request,'gps/companylogin.html',{'msg':'your id or password is wrong'})
	else:
		return render(request,"gps/companylogin.html")
def AddVehicles(request):
	if request.method == 'POST'and request.FILES['vehiclephoto']:
		myfile = request.FILES['vehiclephoto']
		fs = FileSystemStorage()
		filename = fs.save(myfile.name, myfile)
		uploaded_file_url = fs.url(filename)
		obj=vehicle()
		obj.vehnumber=request.POST.get("vehnumber");
		obj.brand=request.POST.get("brand");
		obj.modnumber=request.POST.get("modnumber");
		obj.permitdate=request.POST.get("permitdate");
		obj.licensen=request.POST.get("licensen");
		obj.averg=request.POST.get("averg");
		obj.rc=request.POST.get("rc");
		obj.tank=request.POST.get("tank");
		obj.transp=request.POST.get("transp");
		obj.dnumber=request.POST.get("dnumber");
		obj.email=request.POST.get("email");
		obj.pword=request.POST.get("pword");
		obj.pic=uploaded_file_url
		obj.save()
		context={'msg':"Record is saved"}
		return render(request,'admin/msgpage.html',context)
	else:
		return render(request,'transport Company/AddVehicles.html')





def ViewVehicles(request):
	objs=vehicle.objects.all();
	return render(request,"transport Company/ViewVehicles.html",{'records':objs})
def editvehiclerec(request):
	if request.method == 'GET':
		s=int(request.GET.get('uid'))
		obj=vehicle.objects.get(id=s)
		return render(request,"transport Company/editvehiclerec.html",{'obj':obj})
def updatevehiclereco(request):
	if request.method == 'GET':
		s=int(request.GET.get('uid'));
		obj=vehicle.objects.get(id=s)
		obj.vehnumber=request.GET.get("vehnumber");
		obj.brand=request.GET.get("brand");
		obj.modnumber=request.GET.get("modnumber");
		obj.permitdate=request.GET.get("permitdate");
		obj.licensen=request.GET.get("licensen");
		obj.averg=request.GET.get("averg");
		obj.rc=request.GET.get("rc");
		obj.tank=request.GET.get("tank");
		obj.transp=request.GET.get("transp");
		obj.dnumber=request.GET.get("dnumber");
		obj.email=request.GET.get("email");
		obj.pword=request.GET.get("pword");
		obj.save()
		obj=vehicle.objects.all()
		return render(request,"transport Company/ViewVehicles.html",{'objs':obj})										

def deletevehiclereco(request):
	if request.method == 'GET':
		s=int(request.GET.get('uid'))
		obj=vehicle.objects.get(id=s)
		obj.delete()
		obj=vehicle.objects.all()
		return render(request,"transport Company/ViewVehicles",{'objs':obj})
def viewvehiclereco(request):
	if request.method == 'GET':
		s=int(request.GET.get('uid'))
		obj=vehicle.objects.get(id=s)
		return render(request,"transport Company/viewvehiclereco.html",{'obj':obj})

