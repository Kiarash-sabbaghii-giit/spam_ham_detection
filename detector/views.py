# detector/views.py

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import joblib
import os
import re
import string
from datetime import datetime
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import nltk

try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('stopwords')


# ========== Text Preprocessing ==========
def preprocess_text(text):
    text = text.lower()

    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"
                               u"\U0001F300-\U0001F5FF"
                               u"\U0001F680-\U0001F6FF"
                               u"\U0001F1E0-\U0001F1FF"
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               "]+", flags=re.UNICODE)
    text = emoji_pattern.sub(r'', text)

    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    text = re.sub(r'@\w+', '', text)
    text = re.sub(r'#\w+', '', text)
    text = re.sub(r'\d+', '', text)
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = re.sub(r'\s+', ' ', text).strip()

    stop_words = set(stopwords.words('english'))
    stemmer = PorterStemmer()
    words = text.split()
    words = [stemmer.stem(word) for word in words if word not in stop_words]
    text = ' '.join(words)
    text = ' '.join([word for word in text.split() if len(word) > 2])

    return text


# ========== Load Models ==========
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, 'models', 'spam_model.pkl')
VECTORIZER_PATH = os.path.join(BASE_DIR, 'models', 'vectorizer.pkl')

model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

# ========== History ==========
history = []


# ========== Views ==========
def index(request):
    return render(request, 'detector/index.html')


def about(request):
    return render(request, 'detector/about.html')


def history_view(request):
    return render(request, 'detector/history.html', {'history': history})


@csrf_exempt
@require_http_methods(["POST"])
def predict(request):
    comment = request.POST.get('comment', '').strip()

    if not comment:
        return JsonResponse({'error': 'Please enter a comment!'}, status=400)

    processed = preprocess_text(comment)
    comment_vec = vectorizer.transform([processed])

    prediction = model.predict(comment_vec)[0]
    probability = model.predict_proba(comment_vec)[0]

    if model.classes_[0] == 'ham':
        spam_prob = float(probability[1])
        ham_prob = float(probability[0])
    else:
        spam_prob = float(probability[0])
        ham_prob = float(probability[1])

    result = {
        'comment': comment,
        'processed': processed,
        'prediction': prediction,
        'spam_probability': round(spam_prob * 100, 2),
        'ham_probability': round(ham_prob * 100, 2),
        'is_spam': prediction == 'spam',
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }

    history.insert(0, result)
    if len(history) > 50:
        history.pop()

    return JsonResponse(result)


@csrf_exempt
@require_http_methods(["POST"])
def clear_history(request):
    history.clear()
    return JsonResponse({'success': True})