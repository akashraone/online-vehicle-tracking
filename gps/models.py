from django.db import models




class tracking(models.Model):
   usertype = models.CharField(max_length=200)
   email = models.CharField(max_length=200)
   password = models.CharField(max_length=200)
   contact = models.CharField(max_length=200)
class day(models.Model):
	name = models.CharField(max_length=200)
	fatherName = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	birthDate = models.CharField(max_length=200)
	mobilenumber = models.CharField(max_length=200)
	gender = models.CharField(max_length=200)
	address = models.CharField(max_length=200)
	idproof = models.CharField(max_length=200)
	idno = models.CharField(max_length=200)
	pic=models.CharField(max_length=200)

class companytable(models.Model):
   comname = models.CharField(max_length=200)
   drname = models.CharField(max_length=200)
   email = models.CharField(max_length=200)
   Dateesbh = models.CharField(max_length=200)
   mobilenumber = models.CharField(max_length=200)
   address= models.CharField(max_length=200) 
   regidno= models.CharField(max_length=200)
   pic=models.CharField(max_length=200)
   licensenumber = models.CharField(max_length=200)
   gstnumber = models.CharField(max_length=200)
   pword= models.CharField(max_length=200)
   vnumber=models.CharField(max_length=200)

class akash(models.Model):
   comname = models.CharField(max_length=200)
   drname = models.CharField(max_length=200)
   email = models.CharField(max_length=200)
   Dateesbh = models.CharField(max_length=200)
   mobilenumber = models.CharField(max_length=200)
   address= models.CharField(max_length=200) 
   regidno= models.CharField(max_length=200)
   pic=models.CharField(max_length=200)
   licensenumber = models.CharField(max_length=200)
   gstnumber = models.CharField(max_length=200)
   pword= models.CharField(max_length=200)
   vnumber=models.CharField(max_length=200)   
class vehicle(models.Model):
   vehnumber = models.CharField(max_length=200)
   brand = models.CharField(max_length=200)
   email = models.CharField(max_length=200)
   pword = models.CharField(max_length=200,default="")
   modnumber = models.CharField(max_length=200)
   permitdate = models.CharField(max_length=200)
   licensen= models.CharField(max_length=200) 
   averg= models.CharField(max_length=200)
   rc=models.CharField(max_length=200)
   tank = models.CharField(max_length=200)
   transp = models.CharField(max_length=200)
   dnumber= models.CharField(max_length=200)
   pic=models.CharField(max_length=200)


class single(models.Model):
   name = models.CharField(max_length=200)
   fatherName = models.CharField(max_length=200)
   email = models.CharField(max_length=200)
   birthDate = models.CharField(max_length=200)
   mobilenumber = models.CharField(max_length=200)
   gender = models.CharField(max_length=200)
   address = models.CharField(max_length=200)
   idproof = models.CharField(max_length=200)
   pword = models.CharField(max_length=200,default="")
   idno = models.CharField(max_length=200)
   pic=models.CharField(max_length=200)


class person(models.Model):
   name = models.CharField(max_length=200)
   fatherName = models.CharField(max_length=200)
   email = models.CharField(max_length=200)
   pword = models.CharField(max_length=200,default="")
   birthDate = models.CharField(max_length=200)
   mobilenumber = models.CharField(max_length=200)
   gender = models.CharField(max_length=200)
   address = models.CharField(max_length=200)
   idproof = models.CharField(max_length=200)
   idno = models.CharField(max_length=200)
   pic=models.CharField(max_length=200)
   policenumber =models.CharField(max_length=200)
   conone=models.CharField(max_length=200)
   contwo=models.CharField(max_length=200)
   conthr=models.CharField(max_length=200)
   confour=models.CharField(max_length=200)

class driver(models.Model):
   name = models.CharField(max_length=200)
   driverid = models.CharField(max_length=200)
   address = models.CharField(max_length=200)
   email = models.CharField(max_length=200)
   birthDate = models.CharField(max_length=200)
   mobilenumber = models.CharField(max_length=200)
   gender = models.CharField(max_length=200)
   experience = models.CharField(max_length=200)
   idproof = models.CharField(max_length=200)
   idno = models.CharField(max_length=200)
   pic=models.CharField(max_length=200)


