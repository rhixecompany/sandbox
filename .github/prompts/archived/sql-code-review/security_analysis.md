# 🔒 Security Analysis

> Extracted from `sql-code-review.prompt.md`.

## 🔒 Security Analysis

### SQL Injection Prevention

```sql
-- ❌ CRITICAL: SQL Injection vulnerability
query = "SELECT * FROM users WHERE id = " + userInput;
query = f"DELETE FROM orders WHERE user_id = {user_id}";

-- ✅ SECURE: Parameterized queries
-- PostgreSQL/MySQL
PREPARE stmt FROM 'SELECT * FROM users WHERE id = ?';
EXECUTE stmt USING @user_id;

-- SQL Server
EXEC sp_executesql N'SELECT * FROM users WHERE id = @id', N'@id INT', @id = @user_id;
```

### Access Control & Permissions

- **Principle of Least Privilege**: Grant minimum required permissions
- **Role-Based Access**: Use database roles instead of direct user permissions
- **Schema Security**: Proper schema ownership and access controls
- **Function/Procedure Security**: Review DEFINER vs INVOKER rights

### Data Protection

- **Sensitive Data Exposure**: Avoid SELECT \* on tables with sensitive columns
- **Audit Logging**: Ensure sensitive operations are logged
- **Data Masking**: Use views or functions to mask sensitive data
- **Encryption**: Verify encrypted storage for sensitive data
