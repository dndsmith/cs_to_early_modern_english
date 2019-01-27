import boto3
import json
import sys
from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
import subprocess
from tempfile import gettempdir
import os

def dutchess(input):
    dutchess_tongue = {
        'you': 'thou',
        'your': 'thy',
        'yours' : 'thine',
        'are' : 'art',
        'monitor' : 'portal of light',
        'bug' : 'Satans Dirty Trick',
        'anomoly' : 'Satans Dirty Trick',
        'defect' : 'Satans Dirty Trick',
        'error' : 'Satans Dirty Trick',
        'exception' : 'Satans Dirty Trick',
        'code' : 'lightspeak',
        'computer' : 'light calculator',
        'science' : 'alchemy',
        'digital' : 'realm of light',
        'software' : 'lightware',
        'hardware' : 'mortalware',
        'syntax error' : 'lapse in judgement',
        'programmer' : 'light alchemist',
        'developer' :'light alchemist',
        'scientist' : 'alchemist',
        'cloud' : 'heavens',
        'cloud storage' : 'heavens vault',
        'data' : 'knowledge',
        'data security' : 'knowledges fortress',
        #'big data' : 'Herculean Knowledge',
        'debug' : 'exorcise',
        #'programming language' : 'language of light',
        'compiler' : 'light translator',
        'bandwidth' : 'light capacity',
        'binary' : 'language of the saints',
        'bit' : 'light information',
        'byte' : 'light information',
        'program' : 'light device',
        'database' : 'library of knowledge',
        #'i/o port' : 'light connector',
        'pixel' : 'portrait of light',
        'psuedocode' : 'psuedo-lightspeak',
        'source code' : 'holy lightspeak',
        #'spaghetti code' : 'dirty lightspeak',
        'spaghetti' : 'dirty',
        'string' : 'light sequence',
        'syntax' : 'light structure',
        'with' : 'wi\'',
        'In' : 'I\'',
        'of' : 'o\'',
        'to' : 't\'',
        'it' : '\'t',
        'it is' : '\'tis',
        'it was' : '\'twas',
        'even' : 'e\'en',
        'ever' : 'e\'er',
        'never' : 'ne\'er',
        'never' : 'ne\'er',
        'no' : 'nay',
        'yes' : 'aye',
        'truth' : 'sooth',
        #'in truth' : 'forsooth',
        #'i think' : 'methinks',
        #'i know' : 'methinks',
        'maybe' : 'perchance',
        'really' : 'forsooth or insooth',
        'oh no' : 'gods me',
        'please' : 'prithee',
        #'thank you' : '',
        'big' : 'herculean',
        'here' : 'hither',
        'there' : 'thither',
        'happen' : 'befall',
        'happened' : 'befallen',
        'API' : 'sacred transmission',
        'boot' : 'sanctify',
        'reboot' : 'sanctify',
        'program' : 'sacred instructions',
        'emulation' : 'cheap imitation',
        'interface' : 'alchemists theatre',
        'network' : 'alchemists theatre',
        'system' : 'alchemists theatre',
        'parameter' : 'light argument',
        'password' : 'evidence of your knowledge',
        'pixel' : 'image of light',
        'circuit board' : 'light block',
        'array' : 'light sequence',
        'pseudocode' : 'pseudolight speak',
        'ram' : 'knaves memory',
        'rom' : 'noblemans memory',
        'terminal' : 'ambassador of light',
        'brother' : 'bretheren',
        'and' : 'as well as',
        'AI' : 'witchcraft',
        'coding' : 'lightspeaking'
    }
    if input.lower() in dutchess_tongue:
        return dutchess_tongue[input.lower()]

    return input

if __name__ == '__main__':
    file = sys.argv[1]
    outfile = open("output.txt", 'w')
    storeString = ''

    # comprehend = boto3.client(service_name='comprehend', region_name='region')

    with open(sys.argv[1], 'r') as file:
        #text = file.read().replace('\n', ' ')
        #pattern = re.compile(r'(\s+|[{}])'.format(re.escape(punctuation)))
        for line in file:
            in1 = re.findall(r"[\w']+|[.,!?;]", line)

            for i in in1:
                storeString = dutchess(i)
                storeString = storeString + ' '
                outfile.write(storeString)

    #print('Calling DetectKeyPhrases')
    #print(json.dumps(comprehend.detect_key_phrases(Text=text, LanguageCode='en'), sort_keys=True, indent=4))
    #print('End of DetectKeyPhrases\n')

    # Create a client using the credentials and region defined in the [adminuser]
    # section of the AWS credentials file (~/.aws/credentials).
    session = Session(profile_name="default")
    polly = session.client("polly")

    try:
        # Request speech synthesis
        response = polly.synthesize_speech(Text=storeString, OutputFormat="mp3", VoiceId="Joanna")
    except (BotoCoreError, ClientError) as error:
        # The service returned an error, exit gracefully
        print(error)
        sys.exit(-1)

    # Access the audio stream from the response
    if "AudioStream" in response:
        # Note: Closing the stream is important as the service throttles on the
        # number of parallel connections. Here we are using contextlib.closing to
        # ensure the close method of the stream object will be called automatically
        # at the end of the with statement's scope.
        with closing(response["AudioStream"]) as stream:
            output = os.path.join(gettempdir(), "elegantSpeech.mp3")

            try:
                # Open a file for writing the output as a binary stream
                with open(output, "wb") as file:
                    file.write(stream.read())
            except IOError as error:
                # Could not write to file, exit gracefully
                print(error)
                sys.exit(-1)

    else:
        # The response didn't contain audio data, exit gracefully
        print("Could not stream audio")
        sys.exit(-1)

    # Play the audio using the platform's default player
    if sys.platform == "win32":
        os.startfile(output)
    else:
        # the following works on Mac and Linux. (Darwin = mac, xdg-open = linux).
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, output])
