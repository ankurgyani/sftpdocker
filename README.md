# File Shuffle Homework

## Goal

The goal of this homework is to assess your ability to create well written and easy to maintain production code for a simplified version of a task you would likely see here.  There's no whiteboard coding tricks, we want to know that when we look at your code in six months that anyone can quickly get up to speed with it, update it, and have confidence they didn't break anything in the process.

We encourage you to output logs, write tests, code defensively, and leave a NOTES.md file with info on how to setup and run your solution, and any thoughts or feedback you have.  Please use whatever language you feel most comfortable using to complete this assignment and only spend a few hours on this assignment, ideally no more than an afternoon.  Return your solution using the same method as it was given to you (generally, email).

## The task

Our customer "Williams-Williams" has just contracted us to perform special data insight analysis on _their_ series of events.  If this works out, we may start offering this service as a product to _all_ our customers.

Using two input files, `our_insights.json` and `events_today.json`, render a new file, `customer_insights_today.json`, that contains a list of only the customer's event id's that have been enriched with the insight description we found for the event.

The new file must then be sent to the customer using SFTP.  We don't have the upload URL or credentials yet, so use the given docker-compose setup as the SFTP destination for now.  Connect to `foo@localhost` on port `2222` using a the password `pass` and upload files into a `upload/YYYY-MM-DD-insights` directory, which you may need to create.  `YYYY-MM-DD` is the ISO-8601 date spec for the current date in UTC.

The customer expects this to occur daily.  The daily data generation process will put updated source files into and kick off your script thereafter.  There's no current need to check the source files for freshness, you only need to process and upload them.

## File Format Examples

### our_insights.json

```json
{
    "said_hello": "They said hello to me",
    "on_world": "They are part of this world",
    "bob_sally": "Bob knows Sally",
    "business_stuff": "This Business really knows their stuff"
}
```

### events_today.json

```json
[
    [ 1, "customer foo", "said_hello", "88377378meep", ... ],
    [ 8877738, "Customer McBaz", "on_world", "733313ec-f7d8-463f-a3f0-7b3d9ff13713", ... ],
    [ 8877892, "customer foo", "bob_sally", "733313ec-f7d8-463f-a3f0-7b3d9ff13713", ... ],
    [ 8888140, "Spacely Space Sprockets", "business_stuff", "733313ec-f7d8-463f-a3f0-7b3d9ff13713", ... ],
    [ 8888999, "Barney Rubble", "business_stuff", "733313ec-f7d8-463f-a3f0-7b3d9ff13713", ... ],
    [ 8890000, "Zoinks Inc", "said_hello", "733313ec-f7d8-463f-a3f0-7b3d9ff13713", ... ]
]
```

### customer_insights_today.json

The file for `customer foo` would look like like:

```json
[
    { "id" : 1, "insight": "They said hello to me" },
    { "id" : 8877892, "insight" : "Bob knows Sally" }
]
```
