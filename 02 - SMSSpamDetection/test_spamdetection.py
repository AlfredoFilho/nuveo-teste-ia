import spamdetection as sp
import unittest

class Test_SpamDetection(unittest.TestCase):

    def test_is_spam(self):

        SpamDetect = sp.SpamDetector()
        self.assertFalse(SpamDetect.is_spam("Hello whats your name"))
        self.assertFalse(SpamDetect.is_spam("Love you aathi..love u lot.."))
        self.assertFalse(SpamDetect.is_spam("Argh why the fuck is nobody in town ;_;"))
        self.assertFalse(SpamDetect.is_spam("Yep then is fine 7.30 or 8.30 for ice age."))
        self.assertTrue(SpamDetect.is_spam("Camera - You are awarded a SiPix Digital Camera! call 09061221066 fromm landline. Delivery within 28 days."))
        self.assertTrue(SpamDetect.is_spam("tells u 2 call 09066358152 to claim £5000 prize. U have 2 enter all ur mobile & personal details @ the prompts. Careful!"))
        self.assertTrue(SpamDetect.is_spam("If you don't, your prize will go to another customer. T&C at www.t-c.biz 18+ 150p/min Polo Ltd Suite 373 London W1J 6HL Please call back if busy"))
        self.assertTrue(SpamDetect.is_spam("18 days to Euro2004 kickoff! U will be kept informed of all the latest news and results daily. Unsubscribe send GET EURO STOP to 83222."))
    
    def test_prob_spam(self):
        
        SpamDetect = sp.SpamDetector()
        self.assertEqual(SpamDetect.prob_spam("Hello whats your name"), "0.00000014743922349680")
        self.assertEqual(SpamDetect.prob_spam("Love you aathi..love u lot.."), "0.00000000000000000139")
        self.assertEqual(SpamDetect.prob_spam("Argh why the fuck is nobody in town ;_;"), "0.00000000000002059443")
        self.assertEqual(SpamDetect.prob_spam("Yep then is fine 7.30 or 8.30 for ice age."), "0.00000000001092170885")
        self.assertEqual(SpamDetect.prob_spam("Camera - You are awarded a SiPix Digital Camera! call 09061221066 fromm landline. Delivery within 28 days."), "1")
        self.assertEqual(SpamDetect.prob_spam("tells u 2 call 09066358152 to claim £5000 prize. U have 2 enter all ur mobile & personal details @ the prompts. Careful!"), "1")
        self.assertEqual(SpamDetect.prob_spam("If you don't, your prize will go to another customer. T&C at www.t-c.biz 18+ 150p/min Polo Ltd Suite 373 London W1J 6HL Please call back if busy"), "1")
        self.assertEqual(SpamDetect.prob_spam("18 days to Euro2004 kickoff! U will be kept informed of all the latest news and results daily. Unsubscribe send GET EURO STOP to 83222."), "1")

if __name__ == "__main__":
    unittest.main()