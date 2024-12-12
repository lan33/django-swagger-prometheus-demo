#import pandas as pd
from django.shortcuts import render, redirect
from .forms import DataFileForm
from prometheus_client import Gauge, Counter
#import autokeras as ak
#from sklearn.model_selection import train_test_split
#from django_prometheus.middleware import metrics
from rest_framework.decorators import api_view

# Création du métrique pour le modèle d'IA
# ACCURACY = Gauge('accuracy', 'Accuracy of the model')

from django.http import HttpResponse
@api_view(['GET'])
def hello_world(request):
    return HttpResponse('Hello, World!')

@api_view(['GET', 'POST'])
#@metrics
def upload_file(request):
    if request.method == 'POST':
        form = DataFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = DataFileForm()
    return render(request, 'upload.html', {'form': form})

# @metrics
# def train_model(request):
#     REQUEST_COUNT.inc()
#     with REQUEST_LATENCY.time():
#         data_file = DataFile.objects.latest('id')
#         data = pd.read_csv(data_file.file.path)
#         X = data.drop(columns=['target_column'])
#         y = data['target_column']
#         X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#         # Entraînement du modèle avec Auto-Keras
#         clf = ak.StructuredDataClassifier(max_trials=10)
#         clf.fit(X_train, y_train, epochs=10)

#         # Évaluation du modèle
#         accuracy = clf.evaluate(X_test, y_test)[1]
#         ACCURACY.set(accuracy)

#         return render(request, 'result.html', {'accuracy': accuracy})