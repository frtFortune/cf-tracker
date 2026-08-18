# V1 Data Model

This document defines the data model for CF Tracker Version 1.

The model is designed around Codeforces users, problems, tags, and submissions while keeping API communication separate from persistence and business logic.

## Entities

### User

Represents a Codeforces user tracked by CF Tracker.

| Field | Type | Description |
|---|---|---|
| id | INTEGER | Internal primary key |
| handle | TEXT | Codeforces username |

Constraints:

- `id` is the primary key.
- `handle` must be unique.
- `handle` must not be null.

---

### Problem

Represents a Codeforces problem.

| Field | Type | Description |
|---|---|---|
| contest_id | INTEGER | Codeforces contest identifier |
| index | TEXT | Problem index within the contest |
| name | TEXT | Problem name |
| type | TEXT | Problem type |
| rating | INTEGER | Codeforces difficulty rating |

Constraints:

- `(contest_id, index)` uniquely identifies a problem.
- `name` must not be null.
- `type` must not be null.
- `rating` may be null because not every Codeforces problem has a rating.

The problem's identity is based on its Codeforces contest ID and problem index rather than its name.

For example:

```text
contest_id = 2179
index = C
identifies problem 2179C.

Tag

Represents a Codeforces problem tag.

Field

Type

Description

id

INTEGER

Internal primary key

name

TEXT

Tag name

Constraints:

id is the primary key.

name must be unique.

name must not be null.

ProblemTag

Represents the many-to-many relationship between problems and tags.

Field

Type

Description

problem_id

INTEGER

Referenced problem

tag_id

INTEGER

Referenced tag

Constraints:

(problem_id, tag_id) is the primary key.

problem_id references Problem.

tag_id references Tag.

A problem can have multiple tags, and a tag can belong to multiple problems.

Submission

Represents a Codeforces submission made by a user.

Field

Type

Description

id

INTEGER

Codeforces submission ID

user_id

INTEGER

User who made the submission

problem_id

INTEGER

Problem submitted

creation_time

INTEGER

Unix timestamp of submission

verdict

TEXT

Codeforces submission verdict

language

TEXT

Programming language used

participant_type

TEXT

Codeforces participation type

Constraints:

id is the Codeforces submission ID and primary key.

user_id references User.

problem_id references Problem.

creation_time must not be null.

verdict must not be null.

Relationships

The relationships between the entities are:

User
 │
 │ 1
 │
 │ many
 ▼
Submission
 │
 │ many
 │
 │ 1
 ▼
Problem
 │
 │ many
 │
 ▼
ProblemTag
 │
 │ many
 ▼
Tag

More precisely:

One User can have many Submission records.

One Problem can have many Submission records.

One Problem can have many Tag records.

One Tag can belong to many Problem records.

ProblemTag implements the many-to-many relationship between Problem and Tag.

Solved Problems

CF Tracker will not store a separate solved boolean on Problem.

A problem is considered solved for a particular user when that user has at least one submission for the problem with:

verdict = OK

For example:

User: FortuneIji
Problem: 2179C

Submissions:
WA
TLE
OK

The problem is considered solved by FortuneIji.

This keeps solved status derived from submission data rather than storing duplicate state that could become inconsistent.

Separation of Responsibilities

The data layer will be independent from the Codeforces API client.

Codeforces API
      │
      ▼
CodeforcesClient
      │
      ▼
Persistence Layer
      │
      ▼
SQLite Database
      │
      ▼
Business / Analytics Logic

The CodeforcesClient is responsible only for communicating with the Codeforces API.

The persistence layer is responsible only for storing and retrieving application data.

Business and analytics logic will operate on persisted data rather than making API requests directly.

V1 Scope

The V1 data model intentionally stores only information needed for the tracker.

The following submission fields from the Codeforces API are not currently persisted:

relativeTimeSeconds

testset

passedTestCount

timeConsumedMillis

memoryConsumedBytes

detailed author metadata

These can be added later if a future feature requires them.

The model may evolve as V1 development reveals additional requirements.
