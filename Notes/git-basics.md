# 🚀 Git Workflow Guide

This guide explains the basic workflow for working with Git in this project.

---

## 📌 1. Clone the Repository

```sh
git clone https://github.com/Saumya-Kanti-Sarma/pillai-college-fy-bca.git
cd pillai-college-fy-bca
```

---

## 📌 2. Check Current Branch

```sh
git branch
```

This shows all branches. The active one will have a `*`.

---

## 📌 3. Create a New Branch

```sh
git checkout -b new-branch-name
```

This **creates** and **switches** to `new-branch-name`.


## 📌 4. Make Changes & Push to GitHub

1. Stage your changes:

   ```sh
   git add .
   ```
2. Commit your changes:

   ```sh
   git commit -m "Your commit message"
   ```
3. Push to GitHub:

   ```sh
   git push origin new-branch-name
   ```

---

## 📌 5. Pull Latest Changes from `main`

Always make sure your branch is updated with `main` before pushing:

```sh
git checkout main
git pull origin main
```

Then switch back to your branch:

```sh
git checkout new-branch-name
git merge main
```

---

## 📌 6. Create Another Branch from Current Work

If you need a new branch for another feature:

```sh
git checkout -b another-branch
```

Then repeat **steps 4–5** to push code.

---

## 📌 7. Merge Branch into `main`

1. Switch to `main`:

   ```sh
   git checkout main
   ```
2. Update `main`:

   ```sh
   git pull origin main
   ```
3. Merge your branch:

   ```sh
   git merge new-branch-name
   ```
4. Push to GitHub:

   ```sh
   git push origin main
   ```

---

## 📌 8. Delete Merged Branch (Optional, for cleanup)

* Delete locally:

  ```sh
  git branch -d new-branch-name
  ```
* Delete on GitHub:

  ```sh
  git push origin --delete new-branch-name
  ```
