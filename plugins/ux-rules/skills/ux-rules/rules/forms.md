# Forms

The text size of fields (16px) is in typography (`typography.md`), the submit button in buttons and actions (`buttons-and-actions.md`) and border contrast in accessibility (`accessibility.md`).

**How to review (applies to every rule):**
1. Fill in the form the way people would: with mistakes, in a hurry, pasting text, going back a step.
2. For each field, ask: is it really needed? Can the app find it out on its own?
3. Make mistakes on purpose and see where the message appears, what it says and whether what was typed is still there.

## Label always visible

**Rule:** every field has a label above it that stays visible while people type. Text inside the field, which disappears on typing, doesn’t do that job; if the field needs an example or a format, it goes below the label, visible the whole time. In the code, the label is tied to the field.

**Why:** the text inside the field disappears when people start typing; they forget what the field asked for and can’t check it before submitting. And a screen reader announces a field with no label as just “text field”.

**Wrong:** fields with only “Name”, “Email” and “Phone” written inside, disappearing on typing.

**Right:** “Email” above the field and, right below, “e.g. name@example.com”.

**Sources:** Nielsen Norman Group, “Placeholders in Form Fields Are Harmful” (https://www.nngroup.com/articles/form-design-placeholders/).

## Ask only for what’s needed

**Rule:**
- every field has to justify itself;
- what the app already knows or can work out isn’t asked (with the date of birth, the age comes on its own);
- what has already been given isn’t asked again;
- optional fields carry “(optional)” in the label, and required ones carry no asterisk;
- sign-up comes after people have seen the app’s value, not when it opens.

**Why:** every extra field is a reason to give up. And the asterisk is a code people have to decipher; “(optional)” says it in words.

**Wrong:** asking for the date of birth and, right after, the age; asking for the email twice; requiring an account before showing anything.

**Right:** only the date of birth; “Nickname (optional)”.

**Sources:** GOV.UK Design System, Question pages — ask only for what you need and mark what’s optional (https://design-system.service.gov.uk/patterns/question-pages/); WCAG 3.3.7, don’t ask twice, level A (https://www.w3.org/WAI/WCAG22/Understanding/redundant-entry.html).

## The right keyboard and autofill

**Rule:** each field opens the keyboard for what it asks — email, number, phone — and tells the device what it is — name, email, ZIP code, address —, so the phone and the password manager can fill it in. Pasting is always allowed, including in the password, and the password has an option to show it.

**Why:** typing on a phone is slow and error-prone. Autofill saves all of that, and blocking paste breaks the password manager.

**Wrong:** a letter keyboard on the phone number field; a password that doesn’t accept pasting; a sign-up where the phone suggests nothing.

**Right:** a number pad for the phone number and the ZIP code; the phone suggests the email; “Show password”.

**Sources:** WCAG 1.3.5, the field says what it is, level AA (https://www.w3.org/WAI/WCAG22/Understanding/identify-input-purpose.html); WCAG 3.3.8, pasting and password managers, level AA (https://www.w3.org/WAI/WCAG22/Understanding/accessible-authentication-minimum.html).

## Accept the way people type

**Rule:** the field accepts the common variations and tidies them up on its own: phone numbers, ZIP codes and other codes with or without dashes, parentheses and spaces; email with capitals or a trailing space. When a format is required, show an example in the label or right below it.

**Why:** people type their own way. Rejecting “(555) 123-4567” because the system wanted digits only is the app’s mistake, not theirs.

**Wrong:** “Invalid phone number” for a correct number, just because it came with dashes; a date field that doesn’t say the format.

**Right:** the phone number accepted any way and shown formatted; “Date of birth (e.g. 12/25/1990)”.

**Sources:** Postel’s law — be tolerant of what people type (https://lawsofux.com/postels-law/); Nielsen Norman Group, explain the required format (https://www.nngroup.com/articles/web-form-design/).

## Errors next to the field, saying how to fix them

**Rule:**
- when: after people finish the field — on moving to the next one or on submitting —, never in the middle of typing or before they start;
- where: right below the field, with an icon and text — color alone isn’t enough (see “Never color alone”, in accessibility);
- what: what’s wrong and how to fix it;
- with several errors on submit, a summary at the top and focus on the first one;
- never erase what was typed.

**Why:** an error far from the field forces people to search. An error that only says “invalid” forces them to guess. And an error that erases everything makes them give up.

**Exception:** when creating a password, the requirements appear and get checked off as people type — there, instant feedback helps.

**Wrong:** “Form error” at the top, without saying where; a red border with no text; complaining about the email at the first character; the page coming back with everything blank.

**Right:** below the phone number, with an icon: “A phone number has 10 digits. This one has 8.”; and the rest of what was typed is still there.

**Sources:** Nielsen Norman Group, errors shown when people finish the field, and the password exception (https://www.nngroup.com/articles/errors-forms-design-guidelines/) and premature errors (https://www.nngroup.com/articles/hostile-error-messages/); WCAG 3.3.3, suggest how to fix it, level AA (https://www.w3.org/WAI/WCAG22/Understanding/error-suggestion.html).

## One column, in the order people think

**Rule:**
- the fields go one below the other, in one column;
- fields that belong together are grouped (address, contact);
- the width of the field suggests the length of the answer: short ZIP code, long address;
- the order is the order of a conversation: name before email, address before delivery time;
- a long form becomes steps, with “Step 2 of 3”.

**Why:** in one column, the eye goes straight down and doesn’t skip a field. In two, people don’t know whether to read across or down.

**Exception:** pairs people read as one — city and state, date and time — can sit side by side.

**Wrong:** name and phone side by side and email below the name; a ZIP code field as wide as the address field; twenty fields on a single screen.

**Right:** one column, the address grouped, a short ZIP code field, the form in short steps.

**Sources:** Nielsen Norman Group, “Website Forms Usability: Top 10 Recommendations” — one column, grouped fields and field width by answer (https://www.nngroup.com/articles/web-form-design/).

## The right control for each question

**Rule:**
- two to five options: all visible, to tap;
- many options: a list with search;
- an on/off switch only for what takes effect immediately, like a setting;
- when there is a sensible default, it comes already selected;
- consent never comes pre-checked.

**Why:** options hidden in a two-tap menu hide the decision. And an “I want to receive offers” box that comes checked decides for the person.

**Wrong:** a menu that opens to choose between “Yes” and “No”; a list of 200 countries with no search; “Send me offers” already checked.

**Right:** “Yes” and “No” in view; country with search and the device’s country already selected; offers unchecked.
