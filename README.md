# Sentiment Analysis using AraBERT

This notebook focuses on sentiment analysis in Arabic text using AraBERT. It covers the full pipeline from data preprocessing, model fine-tuning, quantization for efficiency, and deployment via FastAPI.

## Model and Dataset
Model: AraBERT, a BERT-based transformer model pre-trained for Arabic natural language tasks.
Dataset: The dataset used is labeled Arabic text for sentiment classification (positive, negative, neutral).

## Task
The task is to classify Arabic text based on its sentiment using a fine-tuned transformer model. The pipeline includes model optimization (quantization) and a simple deployment solution.

## Pipeline Overview
1. Preprocessing Pipeline
  - Tokenization, normalization, and handling of Arabic text using NLP preprocessing techniques to prepare data for model training.
2. Fine-tuning AraBERT
  - Fine-tuning AraBERT on the Arabic sentiment analysis dataset. The model is trained to predict sentiment labels based on the input text.
3. Model Quantization with Quanto
  - After fine-tuning, the model is quantized using Quanto to reduce its size and improve inference efficiency without sacrificing accuracy.
4. Deploying with FastAPI
  - The quantized model is deployed using FastAPI, allowing for real-time sentiment analysis via an API. This step includes setting up the API endpoints for prediction.

## Usage

To use the notebook, follow these steps:
1. Clone the repository and set up the required dependencies.
2. Run the notebook to fine-tune and quantize the model.
3. Deploy the model using FastAPI to start serving sentiment analysis predictions.
