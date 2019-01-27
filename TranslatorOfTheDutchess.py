import boto3
import json
import sys
import re
from string import punctuation

def dutchess(input):
    dutchess_tongue = {
        'you': 'thou',
        'your': 'thy',
        'yours' : 'thine',
        'are' : 'art',
        'monitor' : 'portal of light',
        'bug' : 'Satans Dirty Trick',
        'code' : 'lightspeak',
        'computer' : 'light calculator',
        'science' : 'alchemy',
        'digital' : 'realm of light',
        'syntax error' : 'lapse in judgement',
        'programmer' : 'light alchemist',
        'cloud' : 'heavens',
        'cloud storage' : 'heavens vault',
        'data' : 'knowledge',
        'data security' : 'knowledges fortress',
        'big data' : 'Herculean Knowledge',
        'debug' : 'exorcise',
        'programming language' : 'language of light',
        'compiler' : 'light translator',
        'bandwidth' : 'light capacity',
        'binary' : 'language of the saints',
        'bit' : 'light information',
        'byte' : 'light information',
        'program' : 'light device',
        'database' : 'library of knowledge',
        'i/o port' : 'light connector',
        'pixel' : 'portrait of light',
        'psuedocode' : 'psuedo-lightspeak',
        'source code' : 'holy lightspeak',
        'spaghetti code' : 'dirty lightspeak',
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
        'in truth' : 'forsooth',
        'i think' : 'methinks',
        'i know' : 'methinks',
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
        '' : '',
        '' : '',
        '' : '',
        '' : '',
        
    }
    if input in dutchess_tongue:
        return dutchess_tongue[input]

    return input

if __name__ == '__main__':
    file = sys.argv[1]

    # comprehend = boto3.client(service_name='comprehend', region_name='region')

    with open(sys.argv[1], 'r') as file:
        #text = file.read().replace('\n', ' ')
        #pattern = re.compile(r'(\s+|[{}])'.format(re.escape(punctuation)))
        for line in file:
            for word in line.split():
                #pattern.split(word)
                in1 = dutchess(word)
                print(in1)

    #print('Calling DetectKeyPhrases')
    #print(json.dumps(comprehend.detect_key_phrases(Text=text, LanguageCode='en'), sort_keys=True, indent=4))
    #print('End of DetectKeyPhrases\n')
