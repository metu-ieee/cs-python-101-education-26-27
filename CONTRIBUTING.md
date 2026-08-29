# Contributing to METU IEEE Education Materials

First off, thank you for volunteering to improve the curriculum! Whether you are fixing a typo in a lecture, adding a new assignment, or updating the cloud environment, your work helps future students learn faster.

## Who is this for?
This guide is for **Instructors, Coordinators, and Teaching Assistants**. Students taking the course will interact with this repository through GitHub Classroom and do not need to submit Pull Requests here unless they are fixing a bug in the syllabus.

---

## 🛠️ How to Update the Curriculum

### 1. Updating Lectures
* All lecture materials must go into the `/lectures` directory, organized by week (e.g., `/lectures/week-01`).
* Prefer **Markdown (`.md`)** files or **Jupyter Notebooks (`.ipynb`)** over heavy PDFs so they render natively in the browser and on GitHub.

### 2. Updating Assignments
* All homework goes into the `/assignments` directory.
* **Do not push solution files** directly into the student-facing folders. Keep solutions in a separate private repository or an instructor-only branch.

### 3. Modifying the Cloud Environment (Codespaces)
* If the course requires a new VS Code extension or a new software package, do **not** ask students to install it manually. 
* Add it to the `.devcontainer/devcontainer.json` file. Test the container locally before merging to ensure it doesn't break the boot time for students.

---

## 🔄 The Pull Request Workflow
Even as instructors, we do not push directly to `main`. We treat our educational materials with the same discipline as our software.

1. **Branch Out:** Create a branch for your update (e.g., `docs/update-week-3-slides`).
2. **Commit:** Use Conventional Commits (e.g., `docs: add week 3 pointers tutorial`).
3. **Review:** Open a Pull Request and have the lead instructor or Education Coordinator approve it before merging.
