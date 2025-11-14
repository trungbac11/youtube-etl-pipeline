![image](https://github.com/user-attachments/assets/4ec4f2c3-a461-46c8-8f1f-aaf9a3839644)

# AI Usage Documentation

This document describes how AI was used to complete the self-serve metrics system assignment.

## AI Collaboration Examples

| Task | Prompt or Question Used | Outcome / What You Learned |
|------|------------------------|---------------------------|
| Understanding YAML structure | "Giải thích cấu trúc của tệp YAML" | Learned the required fields for metric definition: metric_name, description, owner, schedule, and sql. Understood YAML syntax and formatting for multi-line SQL queries. |
| YAML validation implementation | "Viết hàm python kiểm tra xem tệp YAML có đầy đủ nội dung không (metric_name, description, owner, schedule, sql)" | Developed validation logic using PyYAML. Learned to check for required fields, handle empty values, and implement structured error reporting for YAML files. |
| Database visualization | "Có thể xem trực quan database ở duckDB được không" | Learned multiple methods to inspect DuckDB databases including CLI commands (.tables, DESCRIBE), Python scripts, and understanding DuckDB's system tables for metadata inspection. |
| Metric expansion | "Viết thêm 2 metric khác" | Created additional business metrics (active_customers, customer_geography) demonstrating diverse analytical use cases. Learned to design SQL queries for different business perspectives and data aggregations. |
| SQL optimization | "Làm thế nào để tối ưu hiệu suất SQL trong DuckDB" | Learned DuckDB-specific optimization techniques including proper JOIN order, filter pushdown, and efficient aggregation strategies for better query performance. |
| Project requirements analysis | "tôi cần hiểu đề bài yêu cầu gì" | Broke down complex requirements into clear components. Learned to identify key deliverables: validation script, execution script, and metric examples. |
| Database setup | "oke hãy bắt đầu với setup DuckDB" | Implemented DuckDB database initialization with CSV loading. Learned DuckDB's read_csv_auto function and database connection management. |
| Execution script development | "trong yêu cầu có kêu viết mã Python để: Đọc tất cả các file YAML từ thư mục /metrics, Thực thi mỗi câu lệnh SQL trên cơ sở dữ liệu DuckDB, Tạo hoặc thay thế một bảng có tên theo số liệu (metric_name)" | Built the core execution engine with file handling, SQL execution, and dynamic table creation. Learned about DuckDB's CREATE OR REPLACE TABLE syntax and error handling in database operations. |
| Debugging assistance | Error with "Binder Error: Referenced column 'row_count' not found" | Discovered DuckDB version compatibility issues with system tables. Learned to use alternative approaches like SHOW TABLES and manual COUNT queries. |
| Code optimization | "tinh gọn setup_database.py (đừng dùng quá nhiều icon)" | Refined code to professional standards by removing unnecessary icons and simplifying output messages while maintaining functionality. |
| Cleanup utility | "làm xóa để xóa dữ liệu trong duckdb database" | Implemented safe database cleanup with confirmation prompts. Learned about DROP TABLE operations and database maintenance practices. |
| Automation scheduling | "Làm thế nào để thêm tính năng tự động hóa việc chạy metrics theo lịch schedule trong YAML?" | Learned about cron job scheduling, Python scheduling libraries (APScheduler), and how to parse cron expressions from YAML for potential future automation features. |

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
