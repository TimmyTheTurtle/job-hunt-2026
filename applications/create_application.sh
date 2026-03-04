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
