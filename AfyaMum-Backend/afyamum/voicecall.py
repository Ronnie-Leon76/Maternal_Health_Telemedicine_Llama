import africastalking, os
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

# africastalking voice API
class VOICE:
    def __init__(self):
		# Set app credentials
        self.username = os.environ['AT_USERNAME']
        self.api_key = os.environ['AT_API_KEY']

		# Initialize SDK
        africastalking.initialize(self.username, self.api_key)

		# Get voice service
        self.voice = africastalking.Voice

    def call(self, userPhoneNumber):
        # Set Africa's Talking phone number in international format
        callFrom = os.environ['CallFromNumber']

        # Set numbers you want to call to in a comma-separated list
        callTo   = [userPhoneNumber]

        try:
			# Make the call
            result = self.voice.call(callFrom, callTo)
            print (result)
        except Exception as e:
            print ("Encountered an error while making the call:%s" %str(e))

if __name__ == '__main__':
    VOICE().call() # -> TODO: Add Test Number