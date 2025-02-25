# write-up: 121 keygenme-py

## Hidden Answer

<details>
  <summary><strong>Click to reveal the secret answer</strong></summary>

`picoCTF{1n_7h3_|<3y_of_f911a486}`

</details>

<details>
<summary><strong>Click to reveal the steps</strong></summary>

1. Examine the `keygenme-trial.py`
2. Notice that we have to find the second part of key (`key_part_dynamic1_trial`)
3. Notice that we have to check the `check_key()` function
4. Notice that the script using `hashlib.sha256().hexdigest()` to hash the key
5. the username_trial parameter is receive from `enter_license()` function which passing `bUsername_trial` that is `b"GOUGH"`
6. Write the code to decrypt then combine the three key parts and save as `.\decode_script.py`
7. Execute the `python .\decode_script.py`
8. Get the flag!

</details>
