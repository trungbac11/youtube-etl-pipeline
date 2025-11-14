![image](https://github.com/user-attachments/assets/4ec4f2c3-a461-46c8-8f1f-aaf9a3839644)

# AI Usage Documentation

This document describes how AI was used to complete the self-serve metrics system assignment.

## AI Collaboration Examples

| Task | Prompt or Question Used | Outcome / What You Learned |
|------|------------------------|---------------------------|
| Understanding requirements | "tôi cần hiểu đề bài yêu cầu gì" | AI helped break down the complex requirements into clear components: YAML definition, validation script, execution script, and metrics demonstration. Learned to systematically analyze project specifications. |
| Database setup | "oke hãy bắt đầu với setup DuckDB" | AI provided complete DuckDB setup code with proper error handling. Learned how to use DuckDB's read_csv_auto function and database connection management. |
| YAML schema design | "viết thêm 2 metric khác" | Collaborated with AI to design 4 diverse metrics covering different business aspects. Learned YAML structure design and SQL query optimization for analytics. |
| Execution script development | "trong yêu cầu có kêu viết mã Python để: Đọc tất cả các file YAML từ thư mục /metrics, Thực thi mỗi câu lệnh SQL trên cơ sở dữ liệu DuckDB, Tạo hoặc thay thế một bảng có tên theo số liệu (metric_name)" | AI built the core execution engine with proper file handling, SQL execution, and table management. Learned about dynamic SQL execution and database operations. |
| Validation script creation | "yêu cầu để bài có 2 file py một là run_metrics như bạn làm ở trên, hai là Xác thực YAML và SQL" | AI created a comprehensive validation system with YAML structure checks, SQL syntax validation, and execution testing. Learned about input validation patterns and error reporting. |
| Debugging assistance | "làm sao để xem các bảng trong duckdb" and error troubleshooting | AI helped resolve DuckDB version compatibility issues and provided multiple ways to inspect database contents. Learned about DuckDB system tables and debugging techniques. |
| Code optimization | "tinh gọn setup_database.py (đừng dùng quá nhiều icon)" | AI refined code to be more professional and minimalistic while maintaining functionality. Learned about code style preferences and clean code principles. |

## Key Learnings from AI Collaboration

1. **Structured Problem Solving**: AI helped break down complex problems into manageable steps, following a logical development workflow.

2. **Error Handling Patterns**: Learned comprehensive error handling strategies for file I/O, database operations, and user input validation.

3. **DuckDB Specific Knowledge**: Gained understanding of DuckDB's unique features like read_csv_auto, system tables, and in-memory database management.

4. **Code Organization**: Learned to structure Python projects with separate modules for validation, execution, and utilities.

5. **Documentation Practices**: Understood the importance of clear documentation for both technical implementation and AI usage tracking.

## AI Usage Strategy

- Used AI as a collaborative coding partner rather than a code generator
- Asked specific, focused questions to get targeted solutions
- Verified all AI-generated code through testing and understanding
- Used iterative refinement to improve initial AI suggestions
- Maintained ownership of the overall architecture and design decisions

## Reflection

The AI collaboration significantly accelerated development while maintaining code quality. The most valuable aspects were:
- Quick prototyping of complex components
- Debugging assistance with specific error messages
- Learning new technologies (DuckDB) through practical examples
- Code structure suggestions that followed best practices

This approach allowed for efficient development while ensuring deep understanding of the implemented solution.
