# Returns a list of prime numbers from 1 to n
def primes_less_than(n):
	all_primes=[]
	prime = [True for i in range(n + 1)]
	p = 2
	while (p * p <= n):
		if (prime[p] == True):
			for i in range(p ** 2, n + 1, p):
				prime[i] = False
		p += 1
	prime[0]= False
	prime[1]= False
	# Print all prime numbers
	for p in range(n + 1):
		if prime[p]:
			all_primes.append(p)
	return all_primes

##### These two functions will help determine if two numbers are coprimes ######
def gcd(p,q):
# Create the gcd of two positive integers.
    while q != 0:
        p, q = q, p%q
    return p
	 
def is_coprime(x, y):
    return gcd(x, y) == 1

def calculate_N(p, q):
	return p*q


def calculate_T(p, q):
	return (p-1)*(q-1)


def pick_e_d(p, q):
	N = calculate_N(p, q)
	T = calculate_T(p, q)

	e = 0
	for i in primes_less_than(T)[::-1]:
		if is_coprime(i, T) and is_coprime(i, N):
			e = i

	d = 0
	while ((e*d)%T!=1) or (e==d):
		d += 1
	return N, e, d
		
def encrypt(N, e, letter):
	v = ord(letter)
	# print("Letter:",letter,"V:",v)
	return (v**e)%N


def encrypt_message(N, e, message):
	encrypted_values = []
	for i in message:
		encrypted_values.append(encrypt(N, e, i))
	return encrypted_values


def decrypt(N, d, enc):
	idx = ((enc**d)%N)
	return chr(idx)


def decrypt_message(N, d, string):
	message = ""
	for i in string:
		message += decrypt(N, d, i)
	return message


print("\nPrime Numbers Less Than a 1,000:\n",primes_less_than(1000),"\n")
N, e, d = pick_e_d(19,23)
print("N:",N)
print("e:",e)
print("d:",d)

# N = 437
# e = 5
# d = 317
enc_Msg = encrypt_message(N,e, "Hello World!")
print(enc_Msg)

print(decrypt_message(N, d, enc_Msg))



N = 943
e = 53
d = 949
enc_Msg = encrypt_message(N,e, "Vortex Victor - 'Twisting reality, shaping destiny.'")
print("Encrypted Message:",enc_Msg)
print("Decrypted Message:",decrypt_message(N, d, enc_Msg))

