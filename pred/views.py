from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages 
import pandas as pd

# Create your views here.

def pred(request):

	if request.method == 'POST':

		gre_score = int(request.POST.get('gre_score'))
		university_rating = int(request.POST.get('university_rating'))
		cgpa = float(request.POST.get('cgpa'))
		research = int(request.POST.get('research'))

		# Unpickle model
		model = pd.read_pickle(r"model_pickle.pkl")

		# make prediction
		result = model.predict([[gre_score, university_rating, cgpa, research]])

    	# make prediction
		classification = result[0]

		if(classification<0.35):
			messages.warning(request, 'Student have less chances of admission.')

		elif(0.6>classification>=0.35):
			messages.success(request, 'Student have good chances to get admission.')

		elif(classification>=0.6):
			messages.success(request, 'Student have maximum chances to get admission.')


	return render(request,"predict.html")
