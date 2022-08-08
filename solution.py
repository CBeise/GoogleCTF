from mt19937predictor import MT19937Predictor
# https://github.com/kmyk/mersenne-twister-predictor/blob/master/mt19937predictor.py

predictor = MT19937Predictor()

# Open the phone number list to retrieve the randomly generated numbers
roboNums = []
with open("robo_numbers_list.txt") as infile:
    for file in infile:
        roboNums.append(int(file.replace("-","").strip("\n")) - (1 << 31))

# Feed "random" phone numbers into the predictor
for num in roboNums:
    predictor.setrandbits(num, 32)

# Retrieve the encoded secret message
with open("secret.enc", "rb") as secret:
    letters = list(secret.readline())

# Decrypt each letter in the message by XOR-ing it with the "randomly"
# generated value used to encrypt it
answer = ""
for i in range(len(letters)):
    answer = answer + chr(letters[i] ^ predictor.getrandbits(8))

print(answer)
