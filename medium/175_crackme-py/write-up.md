# write-up: 175 crackme-py

## Hidden Answer

<details>
  <summary><strong>Click to reveal the secret answer</strong></summary>

`picoCTF{1|\/|_4_p34|\|ut_dd2c4616}`

</details>

<details>
<summary><strong>Click to reveal the steps</strong></summary>

1. Open the crackme.py with text editor
2. Found that there is secret and uninvoked function

<details><summary>Reveal the image</summary>
<img src="images/code_inside.png" height=560px>
</details>

3. Comment the invoked function
4. Call the uninvoked function in 2. and passed the secret as an argument

<details><summary>Reveal the image</summary>
<img src="images/replaced_code.png" height=80px>
</details>

5. Execute crackme.py
6. Get the flag!

</details>
