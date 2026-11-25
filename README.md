# One Line, One Laugh: Roast Your Fridge

[![Competition](https://make.fun/badge/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521.svg)](https://make.fun/bounty/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521)
[![Rank](https://make.fun/badge/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521/kazamisao/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521/rank.svg)](https://make.fun/bounty/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521)
[![Reward](https://make.fun/badge/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521/kazamisao/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521/reward.svg)](https://make.fun/bounty/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521)

Entry for the make.fun bounty [One Line, One Laugh: Roast Your Fridge](https://make.fun/bounty/u-suzy-one-line-one-laugh-roast-your-fridge-f1063521).

`main.py` (Python 3.13, standard library only) writes one line to
`/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` when that
variable is set): a roast of a phone that keeps begging its owner to
delete their own photos so System Data can stretch out — the buyer
paid for the phone, yet somehow is the tenant and System Data is the
landlord.

Run the contract test with:

```
python3 test_entry.py
```

The test runs `main.py` into a temporary output directory and asserts
exactly one line of 1 to 200 characters that roasts the phone on the
specific detail "System Data", with the landlord/tenant twist landing
in the last few words.
