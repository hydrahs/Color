import azure.cognitiveservices.speech as speechsdk

# Creates an instance of a speech config with specified subscription key and service region.
# Replace with your own subscription key and service region (e.g., "westus").
#speech_key, service_region = "c17c3d44c951410f81389cba1bbfd1b3", "eastus"
#speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region)

# Creates a recognizer with the given settings
#speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)


# Starts speech recognition, and returns after a single utterance is recognized. The end of a
# single utterance is determined by listening for silence at the end or until a maximum of 15
# seconds of audio is processed.  The task returns the recognition text as result.
# Note: Since recognize_once() returns only a single utterance, it is suitable only for single
# shot recognition like command or query.
# For long-running multi-utterance recognition, use start_continuous_recognition() instead.

speech_key = "891ff7e726e24f71a64b54f2870df829"
service_region = "eastasia"
speech_config = speechsdk.SpeechConfig(
    subscription=speech_key, region=service_region)
# Creates a recognizer with the given settings
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)


class Listener:
    def __init__(self):
        # Creates an instance of a speech config with specified subscription key and service region.
        # Replace with your own subscription key and service region (e.g., "westus").

        self.red = 0
        self.green = 0
        self.blue = 0
        self.ifrun = 0
        self.apply = 0
        self.up = 0
        self.down = 0
        self.night = 0

    def run(self):
        # while True:
        print('speaking please:')
        self.result = speech_recognizer.recognize_once()
        print("{}".format(self.result.text))
        if self.result.text.lower().find("into") != -1 or self.result.text.lower().find("start") != -1:
            self.ifrun = 1
        elif self.ifrun == 1:
            if (self.red == 1 or self.green == 1 or self.blue == 1) and self.result.text.lower().find("apply") != -1:
                self.apply = 1
            elif self.result.text.lower().find("green") != -1:
                self.green = 1
                self.red = 0
                self.blue = 0
            elif self.result.text.lower().find("red") != -1:
                self.red = 1
                self.green = 0
                self.blue = 0
            elif self.result.text.lower().find("blue") != -1:
                self.blue = 1
                self.red = 0
                self.green = 0
            elif (self.red == 1 or self.green == 1 or self.blue == 1) and self.result.text.lower().find("apply") == -1:
                if self.result.text.lower().find('up') != -1:
                    self.up = 1
                    self.down = 0
                elif self.result.text.lower().find('down') != -1:
                    self.up = 0
                    self.down = 1
            elif self.result.text.lower().find('night mode') != -1:
                self.night = 1
            
