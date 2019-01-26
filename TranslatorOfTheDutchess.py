def dutchess(input):
    dutchess_tongue = {
        'you': 'thee',
        'your': 'thou'
    }

    output = dutchess_tongue[input]

    return output

if __name__ == '__main__':
    in1 = "you"
    output = dutchess(in1)
    print(output)
