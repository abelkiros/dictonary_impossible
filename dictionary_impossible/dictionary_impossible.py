"""
 file: dictionary_impossible.py
 language: python3
 author: amk7296@g.rit.edu abel m kiros
 description: This program the encodes and decodes files.
"""
def encode(file1, file2):
    """This function takes in two files and returns an encoded list and a dictionary.
    """
    with open(file1) as f:
        d = {}
        for line in f:
            split_line = line.split()
            key = split_line[0]
            value = split_line[1]
            d[key] = value

    with open(file2) as f:
        lst = []
        x = ""
        for line in f:
            line = line.strip().split()
            for word in line:
                x += d[word]+" "
            lst.append(x.strip())
            x = ""
        return lst, d


def decode(file1, lst):
    """This function takes in an encoded list and a file and decodes the file
    """
    with open(file1) as f:
        d = {}
        for line in f:
            split_line = line.split()
            key = split_line[1]
            value = split_line[0]
            d[key] = value
        print("The <encode_word, word> pairs are:\n", d)

        for line in lst:
            x = ""
            line = line.strip().split()
            for word in line:
                x += d[word] + " "
            print(x)


def simulation():
    """This function takes in user input
    """
    print("Welcome to the Encoder 2000!")
    s_file = input("Enter the name of the secret key file: ")
    p_file = input("Enter the name of the plain text file: ")
    print("Preparing to encode ", p_file, "using", s_file)
    lst,d = encode(s_file, p_file)
    print("The <word, encode_word> pairs are:\n", d)
    print(lst)
    print("Sending the encoded lines to the agent.")
    print("The encoded lines are: ")
    eclst,ed=encode(s_file, p_file)
    print(eclst)
    print("The agent is decoding the lines.")
    decode(s_file, eclst)
    print("Exiting the Encoder 2000!")

def main():
    """The main function"""
    simulation()

main()
