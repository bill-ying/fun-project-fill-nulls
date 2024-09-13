# fun-project-fill-null

This is a fun project to demo the power of Python Pandas package.  It was originally from a SQL question.  

Say I have a table called scores containing following data:

| tester | test_sequence | test_score |
|--------|---------------|-----------|
| Alice  | 1             | 10        |
| Alice  | 2             | 10        |
| Alice  | 3             | Null      |
| Alice  | 4             | 20        |
| Alice  | 5             | 15        |
| Alice  | 6             | Null      |
| Bob    | 1             | 21        |
| Bob    | 2             | Null      |
| Bob    | 3             | 23        |
| Bob    | 4             | Null      |
| Bob    | 5             | 15        |
| Bob    | 6             | 9         |
| Dave   | 1             | 22        |
| Dave   | 2             | 23        |
| Dave   | 3             | 24        |
| Dave   | 4             | Null      |
| Dave   | 5             | 31        |
| Dave   | 6             | Null      |
| Rick   | 1             | 32        |
| Rick   | 2             | Null      |
| Rick   | 3             | 36        |
| Rick   | 4             | Null      |
| Rick   | 5             | 25        |
| Rick   | 6             | 27        |


Please write a SQL to fill Null with previous non Null score of the same tester.  

The anticipated output would be:

| tester | test_sequence | test_score |
|--------|---------------|------------|
| Alice  | 1             | 10         |
| Alice  | 2             | 10         |
| Alice  | 3             | 10         |
| Alice  | 4             | 20         |
| Alice  | 5             | 15         |
| Alice  | 6             | 15         |
| Bob    | 1             | 21         |
| Bob    | 2             | 21         |
| Bob    | 3             | 23         |
| Bob    | 4             | 23         |
| Bob    | 5             | 15         |
| Bob    | 6             | 9          |
| Dave   | 1             | 22         |
| Dave   | 2             | 23         |
| Dave   | 3             | 24         |
| Dave   | 4             | 24         |
| Dave   | 5             | 31         |
| Dave   | 6             | 31         |
| Rick   | 1             | 32         |
| Rick   | 2             | 32         |
| Rick   | 3             | 36         |
| Rick   | 4             | 36         |
| Rick   | 5             | 25         |
| Rick   | 6             | 27         |

	
Although this could be accomplished using a stored procedure, achieving the same result with a single SQL statement can be challenging due to the need for two rarely used built-in functions. However, the same outcome can be easily achieved using the Pandas forward fill function, as demonstrated in the code.

For the reference, the SQL solution of the above question is:

```sql
SELECT
    tester,
    test_sequence,
    COALESCE(test_score, LAG(test_score) OVER (PARTITION BY tester ORDER BY test_sequence)) AS test_score
FROM
    scores;

