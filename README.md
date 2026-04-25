# Student-Data-Organiser.py
A Python-based Student Data Organizer that analyzes performance using NumPy, identifies improvement areas, and motivates users with daily quotes. Built collaboratively with a focus on efficient data management and insights.

## Member 1 Contribution (Data Management)

**Name:** Tharun Dev M C  
**UID:** 25LBCS3324

This module handles all student data operations using JSON storage.

### Files Added
- `student.py` → Defines Student class for data structure
- `data_manager.py` → Handles CRUD operations on student data
- `data.json` → Stores student records

### Features Implemented
- Add student record
- Get student by roll number
- Update student details
- Delete student record
- Add marks history
- JSON-based persistent storage

### Data Format

Each student is stored in the following format:

```json
{
  "roll_no": "101",
  "name": "Arjun",
  "subjects": ["Maths", "Physics", "Chemistry"],
  "marks_history": [
    {
      "date": "2026-04-22",
      "scores": [78, 65, 70]
    }
  ]
}
```

## Member 2 Contribution (NumPy Analysis)

**Name:** Samriddhi Singh  
**UID:** 25LBCS3214 

This module handles all mark analysis using NumPy arrays.

### Files Added
- `analysis.py` → NumPy-based performance analysis engine

### Features Implemented
- Calculate overall average of student marks
- Calculate per-subject average across multiple tests
- Identify weak subjects (score < 65)
- Identify strong subjects (score >= 80)
- Find highest and lowest scoring subject
- Returns a complete report dictionary for Member 4 to use

### Input Received From Member 4
subjects = ["Maths", "Physics", "Chemistry"]
scores = [82, 68, 74]

### Output Returned To Member 4
{
  "average": 74.67:
  "highest_subject": "Maths":
  "lowest_subject": "Physics":
  "weak_subjects": []:
  "strong_subjects": ["Maths"]
}
