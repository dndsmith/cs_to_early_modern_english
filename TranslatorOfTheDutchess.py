import boto3
import json
import sys
from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
import subprocess
import codecs
from tempfile import gettempdir
import os
import re

def dutchess(input):
    dutchess_tongue = {
        'you': 'thou',
        'your': 'thy',
        'yours' : 'thine',
        'are' : 'art',
        'monitor' : 'portal of light',
        'bug' : 'Dirty Trick',
        'anomoly' : 'Dirty Trick',
        'defect' : 'Dirty Trick',
        'error' : 'Dirty Trick',
        'exception' : 'Dirty Trick',
        'code' : 'lightspeak',
        'computer' : 'light calculator',
        'science' : 'alchemy',
        'digital' : 'realm of light',
        'software' : 'lightware',
        'hardware' : 'mortalware',
        'syntax error' : 'lapse in judgement',
        'programmer' : 'light alchemist',
        'developer' :'light alchemist',
        'coder' :'light alchemist',
        'scientist' : 'alchemist',
        'cloud' : 'heavens',
        'storage' : 'vault',
        'data' : 'knowledge',
        'security' : 'fortress',
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
        'databases' : 'libraries of knowledge',
        #'i/o port' : 'light connector',
        'pixel' : 'portrait of light',
        'psuedocode' : 'psuedo-lightspeak',
        'source code' : 'holy lightspeak',
        #'spaghetti code' : 'dirty lightspeak',
        'spaghetti' : 'dirty',
        'string' : 'light sequence',
        'syntax' : 'light structure',
        'with' : 'wi\'',
        #'In' : 'I\'',
        'of' : 'o\'',
        #'to' : 't\''
        #'it' : '\'t',
        'it\'s' : '\'tis',
        'was' : '\'twas',
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
        'oh' : 'gods',
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
        'network' : 'interconnected arrangement',
        'system' : 'alchemists theatre',
        'parameter' : 'light argument',
        'password' : 'evidence of thy knowledge',
        'pixel' : 'image of light',
        'circuit' : 'light pathway',
        'board' : 'plate',
        'internet' : 'yonder thither',
        'cyber' : 'yonder',
        'cybersecurity' : 'yonder fortress',
        'array' : 'light sequence',
        'pseudocode' : 'pseudolight speak',
        'ram' : 'knaves memory',
        'rom' : 'noblemans memory',
        'terminal' : 'ambassador of light',
        'brother' : 'bretheren',
        'and' : 'as well as',
        'learning' : 'acquisition',
        'ai' : 'witchcraft',
        'coding' : 'lightspeaking',
        '!' : ', Indeed thy saucy fellow!',
        'has' : 'hast',
        'have' : 'hath',
        'will' : 'shall',
        'fight' : 'square',
        'them' : 'those folk',
        'hello' : 'holla',
        'notebook' : 'table',
        'my' : 'mine',
        'pretty' : 'quaint',
        'do' : 'dost',
        'see' : 'seeth',
        'they' : 'those gents',
        'need' : 'needeth',
        'anything' : 'aught',
        'why' : 'wherefore',
        'aws' : 'yonder thither services',
        'server' : 'that which provideth',
        'google' : 'boundless wisdom',
        'math' : 'maths',
        'hack' : 'heavy blow',
        'hacker' : 'filthy trojan',
        'hackers' : 'filthy trojans',
        'cuhackit' : 'assembly of inquisitive trojans',
        'artificial' : 'feigned'
    }
    if input.lower() in dutchess_tongue:
        return dutchess_tongue[input.lower()]

    return input

if __name__ == '__main__':
    outfile = open("output.txt", 'w')
    storeString = ''
    rendered = ''
    cnt = 0
    file_names = ''
    s3 = boto3.client('s3')
    response = dict()
    result = dict()
    comprehend = boto3.client(service_name='comprehend', region_name='us-east-2')
    translate = boto3.client(service_name='translate', region_name='us-east-2', use_ssl=True)


    with open(sys.argv[1], 'r') as f:
        for line in f:
            response = boto3.client(service_name='comprehend', region_name='us-east-2').detect_dominant_language(Text=line)
            print(response["Languages"][0]["LanguageCode"])

            if response["Languages"][0]["LanguageCode"] != 'en':
                result = translate.translate_text(Text=line,
                                                  SourceLanguageCode=response["Languages"][0]["LanguageCode"], TargetLanguageCode='en')
                line = result['TranslatedText']
            rendered = ''
            storeString = ''
            line = line.replace('"', '\\"')
            command = 'aws polly synthesize-speech --text-type ssml --output-format "mp3" --voice-id "Brian" --text "{0}" {1}'
            if '\r\n' == line:
                #A pause after a paragraph
                rendered = '<speak><break time= "2s"/></speak>'
            else:
                in1 = re.findall(r"[\w']+|[.,!?;]", line)

                for i in in1:
                    storeString += dutchess(i) + ' '
                    outfile.write(dutchess(i) + ' ')

                #A pause after a sentence
                rendered = '<speak><amazon:effect name=\\"drc\\">' + storeString.strip() + '<break time=\\"1s\\"/></amazon:effect></speak>'
    
            file_name = ' polly_out{0}.mp3'.format(u''.join(str(cnt)).encode('utf-8'))
            cnt += 1
            command = command.format(rendered.encode('utf-8'), file_name)
            file_names += file_name
            print command
            subprocess.call(command, shell=True)

    print file_names
    execute_command = 'cat ' + file_names + '>result.mp3'
    subprocess.call(execute_command, shell=True)

    # upload result.mp3 file to s3
    filename = 'result.mp3'
    bucketname = 'cstoeme'
    s3.upload_file(filename, bucketname, filename)

    execute_command = 'rm ' + file_names
    print 'Removing temporary files: ' + execute_command
    subprocess.call(execute_command, shell=True)


    # THE BELOW CODE IS NO LONGER RELEVANT

    #print('Calling DetectKeyPhrases')
    #print(json.dumps(comprehend.detect_key_phrases(Text=text, LanguageCode='en'), sort_keys=True, indent=4))
    #print('End of DetectKeyPhrases\n')

    # Create a client using the credentials and region defined in the [adminuser]
    # section of the AWS credentials file (~/.aws/credentials).
    """
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
        subprocess.call([opener, output])"""
