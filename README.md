# Student Class Diagram to Code

This project maps a simple Student Class Diagram into Python code for the Software Engineering course.

## Student Class Diagram

```
+---------------------------+
|          Student          |
+---------------------------+
| - student_id : String     |
| - name : String           |
| - department : String     |
| - gpa : Float             |
| - courses : List          |
+---------------------------+
| + add_course(course_name) |
| + update_gpa(new_gpa)     |
| + get_info()              |
+---------------------------+
```
