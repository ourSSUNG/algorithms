#include <stdio.h>

unsigned int A, B, C, D, E;
int count = 0;
unsigned char message[64];
unsigned int Warray[80];

unsigned int k1 = 0x5a827999;
unsigned int k2 = 0x6ed9eba1;
unsigned int k3 = 0x8f1bbcdc;
unsigned int k4 = 0xca62c1d6;


int BitPrinter(unsigned int k) {
	int mask = 0;
	for (int i = 31; i >= 0; i--) {
		mask = 1 << i;
		printf("%d", k & mask ? 1 : 0);
		if (i % 8 == 0) printf(" ");
	}
	
	printf("\n");

	return 0;
}

unsigned int ShitfLeft(unsigned int k) {
	unsigned int n = k;
	
	if (n >= 0x80000000) {		
		n = n << 1;
		n = n + 1;
	}
	else {
		n = n << 1;		
	}
	
	
	return n;
}

int Cycle() {
	unsigned int newA, newB, newC, newD, newE;
	newE = D;
	newD = C;
	newB = A;

	unsigned int m = B;
	for (int i = 0; i < 30; i++) {		
		m = ShitfLeft(m);
	}
	newC = m;

	unsigned int F;
	unsigned int K;
	if (count < 20) {
		F = (B&C) | ((~B)&D);
		K = k1;
	}
	else if (count < 40) {
		F = B ^ C ^ D;
		K = k2;
	}
	else if (count < 60) {
		F = (B&C) | (B&D) | (C&D);
		K = k3;
	}
	else {
		F = B ^ C ^ D;
		K = k4;
	}

	unsigned int tmp;	

	m = A;
	for (int i = 0; i < 5; i++) {
		m = ShitfLeft(m);
	}
	
	tmp = m + F + E + K + Warray[count];
	
	newA = tmp;

	A = newA;
	B = newB;
	C = newC;
	D = newD;
	E = newE;

	count++;
	
	return 0;
}

int main() {	
	A = 0x67452301;
	B = 0xefcdab89;
	C = 0x98badcfe;
	D = 0x10325476;
	E = 0xc3d2e1f0;

	printf("input your message:");
	scanf_s("%[^\n]", message);
	
	int i = 0;
	while (message[i] != '\0') {
		i++;
	}
	
	message[63] = (unsigned char)i*8;
	message[i] = (unsigned char)0x80;

	for (int j = i + 1; j < 63; j++) {
		message[j] = 0;
	}

	for (int j = 0; j < 16; j++) {
		Warray[j] = 0;
		Warray[j] += (unsigned int)message[j * 4 + 3];
		Warray[j] += (unsigned int)message[j * 4 + 2] * 256;
		Warray[j] += (unsigned int)message[j * 4 + 1] * 256 * 256;
		Warray[j] += (unsigned int)message[j * 4] * 256 * 256 * 256;
		
	}
	


	for (int j = 16; j < 80; j++) {
		unsigned int tmp = Warray[j - 16] ^ Warray[j - 14] ^ Warray[j - 8] ^ Warray[j - 3];
		tmp = ShitfLeft(tmp);
		Warray[j] = tmp;
		
	}

	for (int j = 0; j < 80; j++) {
		
		Cycle();
		
	}
	
	unsigned int A2, B2, C2, D2, E2;
	A2 = 0x67452301;
	B2 = 0xefcdab89;
	C2 = 0x98badcfe;
	D2 = 0x10325476;
	E2 = 0xc3d2e1f0;

	
	A = A + A2;
	B = B + B2;
	C = C + C2;
	D = D + D2;
	E = E + E2;

	
	printf("%08X%08X%08X%08X%08X\n", A,B,C,D,E);

	return 0;
}
