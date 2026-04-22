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