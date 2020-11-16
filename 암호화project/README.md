Information System Security HW#1 (fall 2020)
due date: 10/6(화)

JAVA cryptography architecture에서 제공하는 AES 알고리즘 라이브러리를 이용해서 임의의 파일을 암호화하고 복호화 하는 JAVA 프로그램을 작성하시오. 프로그램은 다음 사항을 지원해야 합니다 (Python, C 등 원하는 언어 사용 가능).

1-1. 암호화 기능을 제공할 수 있어야 한다. 암호화 프로그램은 사용자로부터 평문 파일명을 입력 받고 암호에 사용할 비밀키 값을 입력 받을 수 있어야 한다. 반드시 PKCS5 패딩을 사용해야 한다. AES는 IV를 포함한 CBC모드로 구현되어야 한다. 암호화된 파일이 생성될 수 있어야 한다.

1-2. 1-1에서 생성된 파일에 대해서 복호화 기능을 제공할 수 있어야 한다. 복호화 프로그램은 사용자로부터 암호문 파일명을 입력 받고 복호에 사용할 비밀키 값을 입력 받을 수 있어야 한다. 복호화된 파일이 생성될 수 있어야 한다.

2. SHA256을 이용해서 생성된 결과값(256비트) 중, 처음 16비트가 모두 0인 결과값을 생성하는 임의의 입력값 스트링을 하나 이상 찾으시오.

숙제 파일을 가상강의실에 제출하며, 1) 소스코드 파일 (자세한 주석 포함), 2) 프로그램 시연 화면 캡쳐 파일(평문 -> 암호문, 암호문 -> 평문 변환 화면 등), 3) 소감 파일로 구성함.

아래는 참고용이며, 더 좋은 방식을 발견하면 그 방식대로 구현하기 바랍니다.

참고자료
	 http://docs.oracle.com/javase/7/docs/technotes/guides/security/crypto/CryptoSpec.html

Generate an AES key
		KeyGenerator keygen = KeyGenerator.getInstance("AES");		SecretKey aesKey = keygen.generateKey();
Create a cipher object for AES in ECB mode and PKCS5 padding
		Cipher aesCipher;		aesCipher = Cipher.getInstance("AES/ECB/PKCS5Padding");
Encrypt
		aesCipher.init(Cipher.ENCRYPT_MODE, aesKey);		byte[] plaintext = "My secret message".getBytes();		byte[] ciphertext = aesCipher.doFinal(plaintext);
Decrypt
		aesCipher.init(Cipher.DECRYPT_MODE, aesKey);		byte[] plaintext1 = aesCipher.doFinal(ciphertext);