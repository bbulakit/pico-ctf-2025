# write-up: 450_Verify

## Hidden Answer

<details>
  <summary><strong>Click to reveal the secret answer</strong></summary>

`picoCTF{trust_but_verify_2cdcb2de}`

</details>

<details>
<summary><strong>Click to reveal the steps</strong></summary>

```sh
for file in files/\*; do
./decrypt.sh "$file"
done
```

Or, filter out any error messages from the output:

```sh
for file in files/\*; do
./decrypt.sh "$file" 2>&1 | grep -v 'Error'
done
```

</details>
