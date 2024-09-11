from transformers import AutoTokenizer, AutoModelForSequenceClassification
from preprocessing import Preprocess


class ModelPredict():
    def __init__(self) -> None:
        # class labels
        self.idx2class = {0: 'negative', 1: 'neutral', 2: 'positive'}
        self.models_path = 'C:/Users/mahmo/Downloads/nlp_course/Sentiment project/model/BertTranformer_model-20240901T221905Z-001/BertTranformer_model'
        # Initialize preprocessor
        self.preprocessor = Preprocess()
        # Load tokenizer and model
        try:
            self.model = AutoModelForSequenceClassification.from_pretrained(self.models_path)
            self.model.eval()
            self.tokenizer = AutoTokenizer.from_pretrained(self.models_path)
            print('The Model has been loaded.....')
        except Exception as e:
            print(f"Error loading model: {e}")
            self.model = None

    def predict(self, text_list):
         
        results = []

        for text in text_list:
            
            text = self.preprocessor.preprocessing(text)

            inputs = self.tokenizer(text, padding=True, truncation=True, max_length=64, return_tensors="pt")

            # Get model output (logits)
            outputs = self.model(**inputs)

            # Calculate probabilities using softmax
            probs = outputs[0].softmax(1)

            # Get the index of the max probability
            pred_label_idx = probs.argmax()

            # Get the predicted label
            pred_label = self.idx2class[pred_label_idx.item()]

            # Store results
            results.append((probs, pred_label_idx, pred_label))

        return results


# # Example usage
# model_predict = ModelPredict()