# write-up: 408 CanYouSee

## Hidden Answer

<details>
  <summary><strong>Click to reveal the secret answer</strong></summary>

`picoCTF{ME74D47A_HIDD3N_3b9209a2}`

</details>

<details>
<summary><strong>Click to reveal the steps</strong></summary>

1. using `exiftool` for extracting the metadata of image
2. found the encoded/encrypted text on `Attribution URL`
3. the value end with `==`, guess that `base64`

<img src="images/exiftool.png" height=320px>

4. copy the value then decode it
5. get the flag!

<img src="images/decode.png" height=50px width=480px>

</details>
