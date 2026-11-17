# States

**How to review (applies to every rule):**
1. For each screen, list the possible states: empty the first time, empty because of a filter, loading, with an error, offline, half-full and too full.
2. See whether each state was designed on purpose or left the way the code made it.
3. In the code, force each state: empty list, slow response, server down, internet off.

## Every screen has every state

**Rule:** each screen is designed in every state it can have, not just “full and working”: empty, loading, with an error, offline, half-full and with too much data.

**Why:** the first screen people see is almost always the empty one, and the worst memory tends to be the error. They are the least designed states and the ones that weigh the most.

**Wrong:** a list that, when empty, shows only its header; an error that shows the server’s raw message.

**Right:** each state with text, image or action thought through.

## Empty states show the way

**Rule:** the empty screen says which state it is, has a sentence that reassures and offers the way forward. And it changes with the reason:
- first time: what will appear there and how to start;
- search or filter with no results: which filter is on, and a button to clear it;
- all done: confirmation that it’s finished.

**Why:** a blank screen looks like a defect. A well-made empty state teaches the app and leads to the first action.

**Wrong:** “No items.” and nothing else; “No results” without saying the “Netflix only” filter is on.

**Right:** “Your map is still empty. Add your first movie and watch its country light up.” with the “Add movie” button; “Nothing with the Netflix only filter.” with “Clear filter”.

**Sources:** Nielsen Norman Group, “Designing Empty States in Complex Applications: 3 Guidelines” (https://www.nngroup.com/articles/empty-state-interface-design/).

## The wait fits the time

**Rule:**
- up to 1 second: no indicator;
- from 1 to 10 seconds: a skeleton — the outline of the page that’s coming — for the whole screen, or a spinner in the place of what’s loading;
- more than 10 seconds: real progress, with named steps and real numbers going up. Never an anonymous bar or a frozen “Loading…”.

And the content arrives in the skeleton’s place, without pushing the screen around.

**Why:** up to 1 second, people don’t lose their train of thought. Up to 10, they wait if they see something is happening. Past 10, they need to know how much is left — otherwise they give up or think it froze.

**Wrong:** the whole screen spinning for 20 seconds; text that jumps down when the image loads.

**Right:** the list’s skeleton while it loads; “Finding your movies: 120 of 253” in a long import.

**Sources:** Jakob Nielsen, “Response Times: The 3 Important Limits” (https://www.nngroup.com/articles/response-times-3-important-limits/); Nielsen Norman Group, “Progress Indicators Make a Slow System Less Insufferable” (https://www.nngroup.com/articles/progress-indicators/) and “Skeleton Screens 101” (https://www.nngroup.com/articles/skeleton-screens/).

## Errors say what happened and what to do

**Rule:** in plain words, with no bare code (“Error 500”) and without blaming the person, the message says what happened and what still works, and offers two ways forward: try again and an alternative path. And it doesn’t lose what the person had already done.

**Why:** “Something went wrong” doesn’t help decide the next step. And blaming people for a system failure breaks trust.

**Wrong:** “Error 500”; “You did something invalid”; an error screen with no button at all.

**Right:** “We couldn’t find the movie right now. Your map is still saved.” with “Try again” and “Add without searching”.

**Sources:** Nielsen Norman Group, “Error-Message Guidelines” (https://www.nngroup.com/articles/error-message-guidelines/).

## Offline, the app stays useful

**Rule:** when the internet drops, the app says the problem is the connection, shows what it already has stored and holds actions to send later, saying so. When the internet comes back, it tries again on its own.

**Why:** on a phone, the connection drops in the subway, in the elevator, on the road. An app that only shows an error looks broken; an app that holds the action looks reliable.

**Wrong:** a white screen with “Network failure”; what the person typed is lost.

**Right:** “You’re offline. Your movies are here, and the new one will be saved when the connection is back.”

## Success only when it happened

**Rule:** the app only says it worked after it worked. The success message says what changed, with numbers. If it was partial, it says what went in and what didn’t. And if the app showed the result before confirming and the action failed, it undoes it and says so.

**Why:** false success is worse than an error: people only find out later, when there’s no way to fix it anymore.

**Wrong:** “Imported successfully!” when 7 items were left out; a movie that shows up in the list and disappears when the app is reopened.

**Right:** “93 of 100 movies imported. 7 were left out: see which.”

## Missing data is not zero

**Rule:** what doesn’t exist or hasn’t arrived shows as “—”, not as “0”. A missing image has a placeholder in the same proportion, honest about there being no photo. And no made-up examples in the real app — no filler text, no fake numbers.

**Why:** “0” is information; “—” is the lack of it. Swapping one for the other tells a lie, and whoever reads it makes decisions based on it.

**Wrong:** “0 goals” for a game that hasn’t happened yet; “Lorem ipsum” in the live app; a stock photo in place of the missing one.

**Right:** “—” in the score of a future game; a gray poster with the movie’s title in place of the poster that didn’t arrive.
