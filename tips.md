# Handy Sqlite3 tips

## Parse SQL query to Sqlite3

```bash
$ database.db < SQL_query.sql
```

```bash
$ cat SQL_query.sql | sqlite3 database.db
```

## Redirect output from query to a text file
```bash
$ cat SQL_query.sql | sqlite3 database.db > output.txt
```