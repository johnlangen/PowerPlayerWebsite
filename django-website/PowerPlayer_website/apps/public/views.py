from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist

def summarize(text: str, num_sentences: int = 1) -> str:
    # Tokenize the text into sentences
    sentences = sent_tokenize(text)

    # Check if there are enough sentences to generate a summary
    if len(sentences) < num_sentences:
        return f"Error: Text has only {len(sentences)} sentence(s). Please choose a smaller number of sentences."

    # Tokenize the text into words
    words = word_tokenize(text)

    # Remove stop words from the words list
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word.casefold() not in stop_words]

    # Calculate the frequency distribution of the words
    freq_dist = FreqDist(words)

    # Sort the sentences by the sum of their word frequencies
    sentence_scores = {}
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in freq_dist:
                if sentence not in sentence_scores:
                    sentence_scores[sentence] = freq_dist[word]
                else:
                    sentence_scores[sentence] += freq_dist[word]

    sorted_sentences = sorted(sentence_scores.items(), key=lambda item: item[1], reverse=True)

    # Get the top `num_sentences` sentences as the summary
    summary_sentences = []
    for i in range(num_sentences):
        summary_sentences.append(sorted_sentences[i][0])

    summary = ' '.join(summary_sentences)

    return summary


def summarize_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        text = request.POST['text']
        num_sentences = int(request.POST.get('num_sentences', 1))
        summary = summarize(text, num_sentences=num_sentences)
        context = {'text': text, 'num_sentences': num_sentences, 'summary': summary}
        return render(request, 'summarize.html', context)
    else:
        return render(request, 'summarize.html')


def index(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        text = request.POST['text']
        num_sentences = int(request.POST.get('num_sentences', 1))
        summary = summarize(text, num_sentences=num_sentences)
        context = {'summary': summary, 'text': text, 'num_sentences': num_sentences}
        return render(request, 'index.html', context)
    else:
        return render(request, 'index.html')



def leaderboards(request: HttpRequest) -> HttpResponse:
    return render(request, 'leaderboards.html')

def contact(request: HttpRequest) -> HttpResponse:
    return render(request, 'contact.html')
