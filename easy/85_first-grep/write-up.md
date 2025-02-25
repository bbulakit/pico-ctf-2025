# write-up: 85 First Grep

## Hidden Answer

<details>
  <summary><strong>Click to reveal the secret answer</strong></summary>

`picoCTF{grep_is_good_to_find_things_5af9d829}`

</details>

<details>
<summary><strong>Click to reveal the steps</strong></summary>

1. Check out what the `file` look like by `cat file`, so we got unreadable text.
2. We know that the flag prefix is `picoCTF`
3. Execute this shell: `cat file | grep "picoCTF{.*"`
4. Get the Flag!

</details>
