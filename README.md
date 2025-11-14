![image](https://github.com/user-attachments/assets/4ec4f2c3-a461-46c8-8f1f-aaf9a3839644)

# AI Usage Documentation

This document describes how AI was used to complete the self-serve metrics system assignment.

| Prompt Goal | Example Prompt | AI Response Summary | How You Used or Modified It | What You Learned / Observed |
|-------------|----------------|---------------------|----------------------------|----------------------------|
| [Example] Draft YAML validation logic | "Write a Python function that checks if a YAML file includes keys: metric_name, description, schedule, sql." | Generated a working outline but used PyYAML incorrectly. | Took structure, fixed import errors, added exception handling. | AI was good at scaffolding but needed correction for YAML edge cases. |
| [Example] Debug SQL syntax in DuckDB | "Why does DuckDB fail on `DATE('2023-09-01')` in a WHERE clause?" | Explained DATE syntax differences and suggested using `DATE '2023-09-01'`. | Applied change directly to query. | AI was accurate; learned DuckDB's date literal format. |


## AI Collaboration Examples

| Task | Prompt or Question Used | Outcome / What You Learned |
|------|------------------------|---------------------------|
| Understanding YAML structure | "Giải thích cấu trúc của tệp YAML" | Learned the required fields for metric definition: metric_name, description, owner, schedule, and sql. Understood YAML syntax and formatting for multi-line SQL queries. |
| Schedule field functionality | "schedule trong yaml hoạt động như thế nào" | Learned that the schedule field in YAML is metadata-only in this prototype, storing cron expressions for future automation. Understood cron syntax and its potential integration with scheduling systems. |
| YAML validation implementation | "Viết hàm python kiểm tra xem tệp YAML có đầy đủ nội dung không (metric_name, description, owner, schedule, sql)" | Developed validation logic using PyYAML. Learned to check for required fields, handle empty values, and implement structured error reporting for YAML files. |
| Database visualization | "Có thể xem trực quan database ở duckDB được không" | Learned multiple methods to inspect DuckDB databases including CLI commands (.tables, DESCRIBE), Python scripts, and understanding DuckDB's system tables for metadata inspection. |
| Metric expansion | "Viết thêm 1 metric khác" | Created additional business metrics (active_customers, customer_geography) demonstrating diverse analytical use cases. Learned to design SQL queries for different business perspectives and data aggregations. |
| SQL optimization | "Làm thế nào để tối ưu hiệu suất SQL trong DuckDB" | Learned DuckDB-specific optimization techniques including proper JOIN order, filter pushdown, and efficient aggregation strategies for better query performance. |
| Cleanup utility | "Làm xóa để xóa dữ liệu trong duckdb database" | Implemented safe database cleanup with confirmation prompts. Learned about DROP TABLE operations and database maintenance practices. |

## Key Learnings from AI Collaboration

1. **Structured Development Approach**: Learned to break down complex projects into manageable components and implement them systematically.

2. **Error Handling Patterns**: Gained experience in comprehensive error handling for file I/O, database operations, and user input validation.

3. **DuckDB Proficiency**: Developed practical skills with DuckDB including database setup, query execution, table management, and system inspection.

4. **YAML Processing**: Mastered YAML file parsing, validation, and error reporting using Python's PyYAML library.

5. **Code Quality**: Learned to write clean, maintainable code with proper documentation and professional formatting.

## AI Usage Strategy

- Used AI as a collaborative partner for both high-level design and specific implementation details
- Asked targeted questions to solve specific problems while maintaining overall project understanding
- Verified all AI-generated code through testing and iterative refinement
- Used AI explanations to deepen understanding of new concepts and technologies

## Reflection

The AI collaboration enabled efficient development while ensuring code quality and personal learning. The most valuable aspects were:
- Rapid prototyping of complex components
- Practical learning of DuckDB through hands-on implementation
- Debugging assistance with specific error resolution
- Code structure guidance following software engineering best practices
- Business metric design thinking for analytical use cases
- Understanding of potential automation and scheduling implementations
