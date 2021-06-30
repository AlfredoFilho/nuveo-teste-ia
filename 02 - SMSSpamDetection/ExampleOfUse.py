import spamdetection as sp


SpamDetect = sp.SpamDetector()
stringSms = "Hello whats your name"

prob = SpamDetect.prob_spam(stringSms)
is_spam = SpamDetect.is_spam(stringSms)

print("Sms: " + stringSms)
print("Probabilidade: " + prob)
print("É spam: " + str(is_spam))
