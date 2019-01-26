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
        
        '.' : '. Indeed thou saucy fellow!' 
    }

    return dutchess_tongue[input]

if __name__ == '__main__':
    in1 = "you"
    output = dutchess(in1)
    print(output)
