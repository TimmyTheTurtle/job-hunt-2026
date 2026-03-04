# How to Add a Folder to Your Job Hunt Repository

This guide explains how to add new folders for tracking job applications in your job hunt repository.

## Quick Start: Adding a New Job Application

### Step 1: Create the Folder

Navigate to the `applications/` directory and create a new folder following the naming convention:

```bash
cd applications/
mkdir YYYY-MM_company_role_keywords
```

**Naming Convention:**
- `YYYY-MM`: Year and month of application (e.g., `2026-03`)
- `company`: Company name in lowercase (e.g., `iridium`)
- `role_keywords`: Key words from the role (e.g., `modeling_simulation`)

**Example:**
```bash
mkdir 2026-03_spacex_simulation_engineer
```

### Step 2: Create Required Files

Inside your new application folder, create these standard files:

```bash
cd 2026-03_spacex_simulation_engineer/
touch job_description.md
touch notes.md
touch submission_snnapshot.md
touch interview_prep.md
```

### Step 3: Fill in the Templates

#### `job_description.md`
Copy the job posting URL and details:
```markdown
job posting[URL]
company profile[URL]

Job Details
[Paste job requirements and description here]
```

#### `notes.md`
Use this template to organize your thoughts:
```markdown
# Application Notes

Company:
Role:
Date Applied:
Branch (A/B/C):

## Why This Role

## Narrative Angle Used

## Skills Emphasized

## Requirements I Fully Meet

## Requirements I Stretch On

## Likely Interview Probes

## Gaps Identified

## Energy Reaction (1-10)

## Would I Accept If Offered? (Y/N/Conditional)
```

#### `submission_snnapshot.md`
Document what you submitted:
```markdown
# Submission Snapshot

Date:
Resume Version:
Cover Letter:

## Resume Used
[Copy or link to the exact resume version submitted]

## Cover Letter Used
[Copy or link to the exact cover letter submitted]

## Application Responses
[Record your responses to application questions]
```

#### `interview_prep.md`
Prepare for potential interviews:
```markdown
# Interview Prep

## Company Research
- Mission:
- Recent News:
- Key Products:

## Role-Specific Prep
- Technical skills to highlight:
- Projects to discuss:

## Questions to Ask Them
1.
2.
3.

## STAR Stories Ready
1.
2.
3.
```

### Step 4: Update Master Tracker

Add a new row to `master_tracker.md`:

```markdown
| 2026-03-15 | SpaceX | Simulation Engineer | B | 9 | 5 | sim_v1 | Applied | Excited | 2026-03-29 |
```

**Columns:**
- **Date**: Application date
- **Company**: Company name
- **Role**: Job title
- **Branch (A/B/C)**: 
  - A = Space Systems Modeling
  - B = Computational Physics
  - C = Distributed Simulation
- **Alignment (1-10)**: How well it matches your goals
- **Stretch (1-10)**: How much you're stretching for requirements
- **Resume Version**: Which resume you used (e.g., `sim_v1`, `backend_v1`)
- **Status**: Current status (Drafting, Applied, Screening, Interviewing, Rejected, Offer, Withdrew)
- **Energy Reaction**: How you feel about this opportunity
- **Follow-Up**: Date to follow up (typically 2 weeks after application)

## Other Folders You Can Add

### Adding Resume Versions

Create new resume files in the `resumes/` folder:

```bash
cd resumes/
touch resume_newversion_v2.md
```

### Adding Cover Letters

Create new cover letter templates or specific letters in the `cover_letters/` folder:

```bash
cd cover_letters/
touch companyname_2026-03.md
# or
touch template_newtype.md
```

## Tips

1. **Consistency**: Always follow the naming conventions to keep your repository organized
2. **Immediate Documentation**: Fill in the templates right after applying to capture fresh insights
3. **Review Cadence**: As noted in README, review patterns every 10 applications
4. **Branch Focus**: Use the branch system (A/B/C) to track your strategic focus
5. **Gaps Tracking**: Update `gaps.md` when you identify new skills to develop

## Example Workflow

```bash
# 1. Create the folder
cd /path/to/job-hunt-2026/applications
mkdir 2026-04_nasa_physics_modeling

# 2. Create files
cd 2026-04_nasa_physics_modeling
touch job_description.md notes.md submission_snnapshot.md interview_prep.md

# 3. Copy job description into job_description.md
# 4. Fill out notes.md during application prep
# 5. Document what you submitted in submission_snnapshot.md
# 6. Update master_tracker.md with new entry
# 7. If you identify gaps, update gaps.md
```

## Automation Option

If you want to automate folder creation, you can create a script:

```bash
#!/bin/bash
# save as: create_application.sh

if [ $# -ne 1 ]; then
    echo "Usage: ./create_application.sh YYYY-MM_company_role"
    exit 1
fi

FOLDER_NAME=$1
mkdir -p "applications/$FOLDER_NAME"
cd "applications/$FOLDER_NAME"

cat > job_description.md << 'EOF'
job posting[URL]
company profile[URL]

Job Details
EOF

cat > notes.md << 'EOF'
# Application Notes

Company:
Role:
Date Applied:
Branch (A/B/C):

## Why This Role

## Narrative Angle Used

## Skills Emphasized

## Requirements I Fully Meet

## Requirements I Stretch On

## Likely Interview Probes

## Gaps Identified

## Energy Reaction (1-10)

## Would I Accept If Offered? (Y/N/Conditional)
EOF

cat > submission_snnapshot.md << 'EOF'
# Submission Snapshot

Date:
Resume Version:
Cover Letter:

## Resume Used

## Cover Letter Used

## Application Responses
EOF

cat > interview_prep.md << 'EOF'
# Interview Prep

## Company Research
- Mission:
- Recent News:
- Key Products:

## Role-Specific Prep

## Questions to Ask Them

## STAR Stories Ready
EOF

echo "✅ Created application folder: $FOLDER_NAME"
echo "📝 Don't forget to update master_tracker.md!"
```

Make it executable and use it:
```bash
chmod +x create_application.sh
./create_application.sh 2026-04_lockheed_distributed_systems
```

---

**Remember:** The goal of this structure is to make it easy to:
- Track all applications systematically
- Review patterns and learn from each application
- Prepare thoroughly for interviews
- Maintain different resume/cover letter versions
- Identify and address skill gaps

Good luck with your job hunt! 🚀
