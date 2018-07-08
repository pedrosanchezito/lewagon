# `git` conflicts

When using a source control software like `git`, conflicts **always** arise at some point. It's just a matter of time. Let's use this exercise to understand the scenarios which always lead to conflict. Knowing that will help prevent the conflicts! Of course, we will also cover how to deal with a conflict.

## `master` changes

Imagine the following scenario:

1. 2 developers are working on the same git repository
1. On Monday, at 9am, the two developers `pull` master.
1. From the same commit (`HEAD`), they create a branch:
  1. Developer A creates the `feature-a` branch
  1. Developer B creates the `feature-b` branch
1. They spend the morning working on their own feature. They commit several times on their branches and push their work to GitHub to save it (in case of a computer crash, developers would be able to retrieve their WIP from the pushed branch on GitHub)
1. Developer A is done at 11am, Developer B is not. Developer A heads to GitHub to create a Pull Request for `feature-a`.
1. Developer C reviews the code at 11:05am and find it good enough (perfect?). Anyway, Developer C **merges** `feature-a` to `master` on the GitHub Pull Request interface.

Let's pause for a minute. Can you draw a picture of the scenario `git`-wise? ✏️ Take a pencil and a sheet of paper.

<details><summary>View solution</summary><p>

![](../../img/merge-a.png)

</p></details>
