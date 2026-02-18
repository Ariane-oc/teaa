
from transformers import pipeline

class Classifier:
    def loadModel(self):
         self.classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")

    def classify(self, text):
       return self.classifier(text)[0]
       
        
