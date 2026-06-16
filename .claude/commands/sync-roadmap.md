# sync-roadmap

Reconcile `articles/ROADMAP.md` checked items with `articles/roadmap-dashboard.html`.

## Steps

1. Read `articles/ROADMAP.md`. Find every line matching `- [x]` (case-insensitive on the x).

2. For each checked line, extract the ID at the start of the item text:
   - Article IDs match the pattern `S\d-A\d+` (e.g. S1-A1, S2-A2, S4-A10)
   - Build IDs match the pattern `B\d+` (e.g. B1, B10)

3. Read `articles/roadmap-dashboard.html`.

4. For each checked **article ID**: find the matching object in the `ARTICLES` JavaScript array
   (search for `id:'<ID>'`) and set its `status` field to `'done'`.

5. For each checked **build ID**: find the matching object in the `BUILD` JavaScript array
   (search for `id:'<ID>'`) and set its `done` field to `true`.

6. Write the updated `articles/roadmap-dashboard.html`.

7. Report a concise summary: which IDs were newly marked done, which were already done,
   and how many remain incomplete in each category (articles / build items).

8. Do NOT commit. Leave that to the user.

## Notes

- If an ID appears in ROADMAP.md but not in the HTML arrays, report it as a warning rather
  than failing.
- Do not modify any other fields in the arrays.
- The status `'done'` triggers a strikethrough style and a ✓ badge in the dashboard.
