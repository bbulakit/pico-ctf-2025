# write-up: 288 Power Cookie

## Hidden Answer

<details>
  <summary><strong>Click to reveal the secret answer</strong></summary>

`picoCTF{gr4d3_A_c00k13_65fd1e1a}`

</details>

<details>
<summary><strong>Click to reveal the steps</strong></summary>

1. Open Inspect tool and look into storage area for cookie
2. Click the `Continue as guest` button in the home page
3. Monitor the change
4. Find out that there is `isAdmin` parameter on the cookie
5. Modify the value from 0 to 1
6. Refresh the web page
7. Get the flag!
<br>
</details>
