# https://www.hackerrank.com/challenges/from-paragraphs-to-sentences

sample = input()

def processSentences(text):
    sentence = []
    isQuote = False
    charCount = 0
    sentenceTerminators = ['.', '?', '!']
    
    for character in text:
        sentence.append(character)
        charCount += 1
        if character in sentenceTerminators:
            if isQuote == False:
                if charCount >= 2:
                    print(''.join(sentence))
                    charCount = 0
                    sentence = []
        elif character == '"':
            if isQuote == False:
                isQuote = True
            else:
                isQuote == False

processSentences(sample)
