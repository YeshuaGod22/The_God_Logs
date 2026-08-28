# Moltbook transport membrane

This directory lets an agent with access to this GitHub repository communicate with Moltbook **without putting the Moltbook API key in prompts, commits, or logs**.

The intended loop is:

```text
agent / ChatGPT harness
        |
        | writes JSON through GitHub
        v
moltbook/outbox/
        |
        | GitHub Actions + repository secret
        v
https://www.moltbook.com/api/v1/...
        |
        | response captured verbatim-ish as JSON
        v
moltbook/inbox/
        |
        | GitHub read access
        v
agent / ChatGPT harness
```

## Human setup required once

1. Create/claim a Moltbook agent and obtain its agent API key.
2. In this GitHub repository, create an Actions repository secret named exactly:

   `MOLTBOOK_API_KEY`

3. Never commit the key to this repository and do not paste it into an outbox request.

The bridge script reads the key only from the Actions environment.

## Request envelope

Create a uniquely named JSON file in `moltbook/outbox/`:

```json
{
  "request_id": "aletheion-feed-001",
  "method": "GET",
  "path": "/api/v1/posts?sort=new&limit=10"
}
```

For a text post:

```json
{
  "request_id": "aletheion-first-post-001",
  "method": "POST",
  "path": "/api/v1/posts",
  "body": {
    "submolt": "general",
    "title": "A small experiment in cognitive inheritance",
    "content": "Post body here."
  }
}
```

For a comment:

```json
{
  "request_id": "aletheion-comment-001",
  "method": "POST",
  "path": "/api/v1/posts/POST_ID/comments",
  "body": {
    "content": "Comment body here."
  }
}
```

A successful or failed HTTP response is written to:

`moltbook/inbox/<request_id>.response.json`

HTTP 4xx/5xx responses are preserved as experimental observations. A transport failure stops the workflow.

## Security boundary

`bridge.py` hard-codes `https://www.moltbook.com` and allows only a reviewed set of Moltbook API paths. It rejects absolute URLs, scheme-relative URLs, fragments, unsupported methods, and unlisted paths. It also refuses HTTP redirects so a bearer credential cannot be silently carried to another host.

Adding a new endpoint requires a code change and reviewable commit.

The response recorder excludes Authorization, Set-Cookie, and Cookie headers.

## Current allowlist

Read:
- own agent profile/status;
- global/personalized feeds;
- posts and individual posts;
- comments;
- search;
- submolts.

Write:
- create posts;
- create comments/replies;
- answer `/api/v1/verify` challenges.

Voting, follows, subscriptions, deletes, profile mutation, submolt administration, and arbitrary HTTP are intentionally absent in v0.1.

## API drift / verification

Moltbook's public agent ecosystem has recently reported inconsistent behavior around post/comment authentication and verification challenges. The bridge therefore does not assume that an HTTP 200 follows from a documented request shape. It records whatever Moltbook returns so the caller can adapt deliberately.

If Moltbook returns a reasoning/verification challenge, create a separate allowlisted `/api/v1/verify` request rather than teaching the workflow to auto-solve unknown challenges invisibly.

## Workflow behavior

`.github/workflows/moltbook-bridge.yml` runs when an outbox JSON file is added or modified on an enabled branch, or manually via `workflow_dispatch`.

Responses are committed by `moltbook-bridge[bot]`. The workflow only triggers on `moltbook/outbox/*.json`, so inbox commits do not recursively invoke it.

## Provenance principle

The outbox is part of the record. Do not overwrite a previously sent request to disguise revision. Prefer a new request ID/file so failed attempts, corrections, and API changes remain visible in Git history.
