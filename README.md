# Dan's Ballot — A Workshop for Better Thinking v1.1

A one-file web page. Dan opens a link on his phone, taps through **18 screens**,
and one button emails his decisions to Michael.

## Why this exists

Dan has no computer. The printed proof (`../v1.1/..._MARKED_PROOF.pdf`) is still the
primary object — this is the same 18 decisions for a phone, for whichever he'll
actually use. **Neither requires an account, a login, or an app store.**

## How it works

- **`index.html` is the whole thing.** No build, no server, no dependencies.
  Fonts come from Google Fonts; everything else is inline.
- Answers save to the phone's `localStorage` as he taps. He can close it, come back
  in three days, and pick up where he left off.
- **Send to Michael** opens his mail app with the answers pre-filled as plain text.
  He taps send. **Copy answers instead** is the fallback if mail isn't set up —
  he pastes it into a text message.
- Nothing is transmitted anywhere until he presses a button.

## Hosting

Any static host. GitHub Pages matches the existing setup:

```
feldtdesign-ship-it/keck-ballot  →  https://feldtdesign-ship-it.github.io/keck-ballot/
```

Push `index.html` to the repo root, enable Pages on `main`, text Dan the link.

## When his answers come back

```bash
python3 parse_reply.py dans-email.txt
```

Writes `decisions.json` — every AQ with its decision and note, plus a list of
anything left blank. That file drives v1.2.

## Rules that are built in

- **Blank is never a yes.** Unanswered questions are reported as `NOT ANSWERED`
  and listed at the bottom of the email. The finish screen says so plainly.
- **Nothing is rewritten in his voice.** Every proposed line is a sentence already
  in that tool, moved up. The one exception is flagged on the screen where it appears.

## Verified

Walked all 18 screens end to end on iPhone 12, iPhone SE and iPad: no JS errors,
no horizontal scroll, no tap targets under the fixed footer, answers persist across
reload. Email body is ~2.9 KB — inside every mail client's URL limit.
