# write-up: 115 Wireshark doo dooo do doo...

## Hidden Answer

<details>
  <summary><strong>Click to reveal the secret answer</strong></summary>

`picoCTF{p33kab00_1_s33_u_deadbeef}`

</details>

<details>
<summary><strong>Click to reveal the steps</strong></summary>

0. After digging through a bunch of encrypted packets...
1. Filter protocol to HTTP
2. Notice a suspicious packet that smelled like a clue...

<details>
<summary><strong>Reveal the image</strong></summary>
<img src="images/filter_http.png" height=300px>
</details>

3. Used `Follow -> HTTP Stream` on the packet
4. We got the source of that smell!

<details>
<summary><strong>Reveal the image</strong></summary>
<img src="images/http_stream.png" height=300px>
</details>

5. Recognized the **`____{ ... }`** pattern – **_classic flag format_**
6. Guess that in might be encrypted with Caesar Cipher
7. Brute-forced the decryption using `https://www.dcode.fr/caesar-cipher`

<details>
<summary><strong>Reveal the image</strong></summary>
<img src="images/decoded_flag.png" height=300px>
</details>

8. We got the flag!

</details>
