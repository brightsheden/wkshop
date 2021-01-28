from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib import messages

# Create your views here.

def home(request):
	return render(request, "age/Dob.html", {"result" : age})
	#else:
			#return redirect("/")

def age(request):
  if request.method=='POST' :
	  mtn5 = int(request.POST['mtn_500']) * 550
	  #c_y = 2020
	  mtn2 = int(request.POST['mtn_200']) * 220
	  mtn1 = int(request.POST['mtn_100']) * 110
	  #mtn summ
	  age = mtn5 + mtn2 + mtn1
	  #glo calc
	  gl_5 = int(request.POST['glo_500']) * 500
	  gl_2 = int(request.POST['glo_200']) * 210
	  gl_1 = int(request.POST['glo_100']) * 110
	  #glo sum
	  gl_total = gl_1 + gl_2 + gl_5
	
	  #Airtcard
	  Airt_5 = int(request.POST['airtel_500']) * 550
	  Airt_2 = int(request.POST['airtel_200']) * 210
	  Airt_1 = int(request.POST['airtel_100']) * 110
	  Airt = Airt_5 + Airt_2 + Airt_1 
	  T_B = age + gl_total + Airt
	  context = {
	  'result' : age,
	  'res' : gl_total,
	  'Airt' : Airt,
	  'total_balance' : T_B,
	  }
	
  return render(request, 'age/result.html',context)
  	 

	
	
def age2(request):
	if request.method=='POST':
		mtnr5 = int(request.POST['mtn_500r']) * 550
		#c_y = 2020
		mtnr2 = int(request.POST['mtn_200r']) * 220
		mtnr1 = int(request.POST['mtn_100r']) * 110
		#mtn summ
		ager = mtnr5 + mtnr2 + mtnr1
		#glo calc
		gl_5r = int(request.POST['glo_500r']) * 500
		gl_2r = int(request.POST['glo_200r']) * 210
		gl_1r = int(request.POST['glo_100r']) * 110
		#glo sum
		gl_totalr = gl_1r + gl_2r + gl_5r
		
		#Airtcard
		Airt_5r = int(request.POST['airtel_500r']) * 550
		Airt_2r = int(request.POST['airtel_200r']) * 210
		Airt_1r = int(request.POST['airtel_100r']) * 110
		Airtr = Aisrt_5r + Airt_2r + Airt_1r 
		T_Br = ager + gl_totalr + Airtr
		contextr = {
			'mtn' : ager,
			'glo' : gl_totalr,
			'Airtel' : Airtr,
			'total_balance2' : T_Br,
			}
	return render(request, 'age/result.html',contextr)


    
	    
#import datetime
#DOb = input('Enter Year:- ')
#Currentyear #=datetime.datetime.now#().year
#Age = Currentyear - int(DOb)
#print('Your Age is #{}'.format(Age))