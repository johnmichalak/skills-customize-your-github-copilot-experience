---
description: "Instructions to use whenever creating or editing assignment markdown files to ensure consistency and clarity for students."
applyTo: "assignments/**/*.md"
---

# Assignment Markdown Structure Guidelines

Create assignments that are learning-focused, appropriate for the intended skill level, and easy for students to follow.

## 1. Template Usage

- Assignment markdown files must follow the structure in [`templates/assignment-template.md`](../../../templates/assignment-template.md).
- Create each assignment as a `README.md` file in its own descriptive subfolder under `assignments/`.
- Do not remove or skip required sections from the template.
- Do not add extra sections unless explicitly requested.

## 2. Section Guidance

Use the template's section order and exact heading text, including its icons:

1. `# 📘 Assignment: [Assignment Title]`
2. `## 🎯 Objective`
3. `## 📝 Tasks`
4. `### 🛠️ [Task Title]`
5. `#### Description`
6. `#### Requirements`

- **Title**: Replace `[Assignment Title]` with a short, descriptive name (e.g., `Python Basics`, `Loops and Conditionals`, `Functions and Modules`).
- **Objective**: Write 1-2 sentences that state what the student will learn and build. Keep the scope appropriate for the assignment's difficulty level.
- **Tasks**: For each task:
   - Use a specific, action-oriented task name.
   - In **Description**, clearly explain what the student must do.
   - In **Requirements**, introduce the list with `Completed program should:` and use bullets for specific, measurable outcomes.
   - Include example input, output, or usage in fenced code blocks when it clarifies the expected behavior.

## 3. Writing Standards

- Use clear, concise, and encouraging language addressed directly to the student.
- Define unfamiliar technical terms when they first appear.
- Keep instructions focused on observable outcomes rather than implementation details unless a specific technique is part of the learning objective.
- Format filenames, function names, commands, and code with backticks.